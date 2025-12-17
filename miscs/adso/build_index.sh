#!/bin/bash

# Build Pagefind search index for Joy of Coding transcripts
# This should be run AFTER Jekyll builds the site

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/../.."
SITE_DIR="$REPO_ROOT/_site"

echo "Building Jekyll site first..."
cd "$REPO_ROOT"
bundle exec jekyll build

echo "Building Pagefind index..."
echo "Indexing: $SITE_DIR"

# Install pagefind if not available
if ! command -v pagefind &> /dev/null; then
    echo "Pagefind not found. Install it with:"
    echo "  npm install -g pagefind"
    echo "  or"
    echo "  brew install pagefind"
    exit 1
fi

# Run pagefind to index the built site
# It will automatically create _site/pagefind/ directory
npx pagefind --site "$SITE_DIR" --glob "**/transcript.html"

echo "Index built successfully at $SITE_DIR/pagefind/"
