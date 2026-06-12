# Changelog

## Unreleased

- Chrome support — the extension now builds for both Chrome (Manifest V3 service worker) and Firefox
  from a single shared codebase, via a `chrome`/`browser` namespace shim and a per-browser manifest
- `build.sh` produces store-ready zips for both the Chrome Web Store and addons.mozilla.org

## v1.0.0

Initial release.

- Group tabs automatically with the tab that opened them
- Two grouping modes: by opening tab or by matching domain
- Group naming by domain, subdomain, full hostname, page title, or nameless
- Pretty names option for capitalized, clean group titles
- Max tabs per group limit
- Auto-ungroup lonely tabs when a group shrinks to one
- Auto-collapse inactive groups on tab switch
- Custom rules with domain suffix matching, configurable alias and color, ordered first-match-wins
- Blacklist to exclude specific domains from grouping
- All settings in the toolbar popup with instant save
- Reset to defaults
