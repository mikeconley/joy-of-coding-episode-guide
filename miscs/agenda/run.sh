#!/bin/bash
# Read Password

source config.sh

ssh-add $SITE_USER_SSH_FILE

clear

trap ctrl_c INT

function ctrl_c() {
  echo "** Clearing rsync key"
  ssh-add -d $SITE_USER_SSH_FILE
  deactivate
  exit 0
}

echo "Activating venv..."
. venv/bin/activate

while :
do
  echo "Watching $NOTES_DIR for .md file changes...\n"
  python3 gen_and_sync.py --notesdir $NOTES_DIR --output $OUTPUT_DIR --watch --episodeguidedir "$EPISODE_GUIDE_DIR"
  if [ $? -ne 0 ]
  then
    exit 1
  fi

  echo "Saw changes - syncing\n"
  rsync --delete -a $NOTES_IMAGES_DIR $IMAGES_OUTPUT_DIR
  rsync -a assets/ $OUTPUT_DIR
  rsync --delete -a -e "ssh -p ${SSH_PORT}" $OUTPUT_DIR/ $RSYNC_TO
  echo "Press [CTRL+C] to stop.."
done

