# Development

No bundler, no test framework. The extension is plain JS that runs unchanged on Firefox and Chrome.

A single codebase targets both browsers. The only per-browser difference is the manifest:

- `manifest.json` — Firefox (Manifest V3 event page: `background.scripts`, `browser_specific_settings.gecko`).
- `manifest.chrome.json` — Chrome (Manifest V3 service worker: `background.service_worker`).

`background.js` and `popup.js` use the promise-based `browser.*` API. A small shim at the top of
each (`if (typeof browser === "undefined") globalThis.browser = chrome;`) aliases Chrome's `chrome.*`
namespace, whose Manifest V3 APIs already return promises. No polyfill or build transform is needed.

## Loading for testing

**Firefox**

1. Open `about:debugging` → **This Firefox** → **Load Temporary Add-on**.
2. Select `manifest.json` from the repo root.

Temporary add-ons are removed when Firefox restarts.

**Chrome**

Chrome's service-worker background requires `manifest.chrome.json`, so load a built folder rather
than the repo root:

1. Run `./build.sh`.
2. Open `chrome://extensions` → enable **Developer mode** → **Load unpacked**.
3. Select `dist/chrome/`.

## Building for distribution

```bash
./build.sh
```

Produces, under `dist/` (git-ignored):

- `dist/firefox/` + `dist/tabbit-firefox-<ver>.zip` — submit to [addons.mozilla.org](https://addons.mozilla.org).
- `dist/chrome/` + `dist/tabbit-chrome-<ver>.zip` — submit to the [Chrome Web Store](https://chrome.google.com/webstore/devconsole).

Each zip has `manifest.json` at the archive root, as both stores expect. The version is read from
`manifest.json` — keep it in sync with `manifest.chrome.json` when bumping.

For Firefox self-distribution (no public listing), upload the zip to AMO, choose "On your own", and
download the signed `.xpi`.

## Architecture

- `background.js` — core logic. Listens to `tabs.onCreated` (grouping), `tabs.onRemoved` (lonely tab
  cleanup), and `tabs.onActivated` (auto-collapse). Reads settings from `browser.storage.local`.
- `popup.html` / `popup.js` — toolbar popup with all settings UI. Auto-saves on change.
- `icons/` — extension icons at 16, 32, 48, 96, 128px.

Requires the `tabs`, `tabGroups`, and `storage` permissions. Tab groups require Firefox 139+ or
Chrome 89+.
