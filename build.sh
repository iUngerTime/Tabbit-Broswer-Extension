#!/usr/bin/env bash
#
# Build store-ready packages for Firefox and Chrome from the shared source.
#
#   ./build.sh
#
# Produces:
#   dist/firefox/                 unpacked Firefox build (manifest.json = Firefox)
#   dist/chrome/                  unpacked Chrome build (manifest.json = Chrome)
#   dist/tabbit-firefox-<ver>.zip submit to addons.mozilla.org
#   dist/tabbit-chrome-<ver>.zip  submit to the Chrome Web Store
#
set -euo pipefail
cd "$(dirname "$0")"

# Files shared by both builds. Each browser gets its own manifest.json.
SHARED=(background.js popup.html popup.js tabbit-name-small.png icons)

VERSION=$(grep -m1 '"version"' manifest.json \
  | sed -E 's/.*"version"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/')

rm -rf dist
mkdir -p dist/firefox dist/chrome

# Firefox: manifest.json is already the Firefox manifest.
cp manifest.json dist/firefox/manifest.json
cp -R "${SHARED[@]}" dist/firefox/

# Chrome: swap in the Chrome manifest under the canonical name.
cp manifest.chrome.json dist/chrome/manifest.json
cp -R "${SHARED[@]}" dist/chrome/

# Zip the *contents* (store uploads expect manifest.json at the archive root).
(cd dist/firefox && zip -qr "../tabbit-firefox-${VERSION}.zip" . -x '*.DS_Store')
(cd dist/chrome  && zip -qr "../tabbit-chrome-${VERSION}.zip"  . -x '*.DS_Store')

echo "Built v${VERSION}:"
echo "  dist/tabbit-firefox-${VERSION}.zip"
echo "  dist/tabbit-chrome-${VERSION}.zip"
