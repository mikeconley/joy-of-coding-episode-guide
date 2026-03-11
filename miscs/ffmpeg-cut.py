#!/usr/bin/env python3

# Usage example:
# ./ffmpeg-cut.py input.mkv output.mkv --cut 01:10:25-01:10:28 --cut 01:10:25-01:10:28

import argparse
import re
import subprocess
from dataclasses import dataclass
from typing import List, Tuple

TIME_RE = re.compile(r"^\s*(?:(\d+):)?(\d{1,2}):(\d{2})(?:\.(\d+))?\s*$")

def parse_time(s: str) -> float:
    s = s.strip()
    # Allow plain seconds (int/float)
    try:
        return float(s)
    except ValueError:
        pass

    m = TIME_RE.match(s)
    if not m:
        raise ValueError(f"Invalid time format: {s!r} (use HH:MM:SS[.ms], MM:SS[.ms], or seconds)")
    hh, mm, ss, frac = m.groups()
    hh = int(hh) if hh is not None else 0
    mm = int(mm)
    ss = int(ss)
    out = hh * 3600 + mm * 60 + ss
    if frac:
        out += float("0." + frac)
    return out

def parse_cut(spec: str) -> Tuple[float, float]:
    if "-" not in spec:
        raise ValueError(f"Invalid cut spec: {spec!r} (use START-END)")
    a, b = spec.split("-", 1)
    start = parse_time(a)
    end = parse_time(b)
    if end <= start:
        raise ValueError(f"Cut end must be > start: {spec!r}")
    return start, end

def merge_cuts(cuts: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    if not cuts:
        return []
    cuts = sorted(cuts)
    merged = [list(cuts[0])]
    for s, e in cuts[1:]:
        if s <= merged[-1][1]:  # overlap/adjacent
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return [(float(s), float(e)) for s, e in merged]

def build_filter(cuts: List[Tuple[float, float]]) -> str:
    # Build kept segments: [0, cut1_start), (cut1_end, cut2_start), ..., (last_end, inf)
    keeps = []
    cur = 0.0
    for s, e in cuts:
        if s > cur:
            keeps.append((cur, s))
        cur = e
    keeps.append((cur, None))  # tail to end

    v_parts = []
    a_parts = []
    for i, (s, e) in enumerate(keeps):
        if e is None:
            v_parts.append(f"[0:v]trim=start={s},setpts=PTS-STARTPTS[v{i}]")
            a_parts.append(f"[0:a]atrim=start={s},asetpts=PTS-STARTPTS[a{i}]")
        else:
            v_parts.append(f"[0:v]trim=start={s}:end={e},setpts=PTS-STARTPTS[v{i}]")
            a_parts.append(f"[0:a]atrim=start={s}:end={e},asetpts=PTS-STARTPTS[a{i}]")

    concat_inputs = "".join([f"[v{i}][a{i}]" for i in range(len(keeps))])
    concat = f"{concat_inputs}concat=n={len(keeps)}:v=1:a=1[v][a]"
    return "; ".join(v_parts + a_parts + [concat])

def main():
    ap = argparse.ArgumentParser(description="Snip out one or more time ranges from a video using ffmpeg concat filters.")
    ap.add_argument("input", help="Input video file (e.g., input.mkv)")
    ap.add_argument("output", help="Output video file (e.g., output.mkv)")
    ap.add_argument("--cut", action="append", default=[], required=True,
                    help="Time range to remove: START-END (e.g., 01:10:25-01:10:28). Repeat for multiple cuts.")
    ap.add_argument("--dry-run", action="store_true", help="Print ffmpeg command without running it.")
    ap.add_argument("--ffmpeg", default="ffmpeg", help="ffmpeg binary (default: ffmpeg)")
    args = ap.parse_args()

    cuts = merge_cuts([parse_cut(c) for c in args.cut])

    # Sanity check: no negative times
    for s, e in cuts:
        if s < 0 or e < 0:
            raise SystemExit("Cut times must be >= 0")

    filt = build_filter(cuts)

    cmd = [
        args.ffmpeg,
        "-hide_banner", "-y",
        "-i", args.input,
        "-filter_complex", filt,
        "-map", "[v]", "-map", "[a]",
        args.output,
    ]

    if args.dry_run:
        print(" ".join(subprocess.list2cmdline([c]) if " " in c else c for c in cmd))
        return

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
