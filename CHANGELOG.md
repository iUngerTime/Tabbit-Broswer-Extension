# Changelog

## v1.1.0

### Added

- Chrome support — the extension now builds for both Chrome (Manifest V3 service worker) and Firefox
  from a single shared codebase, via a `chrome`/`browser` namespace shim and a per-browser manifest
- `build.sh` produces store-ready zips for both the Chrome Web Store and addons.mozilla.org

### Fixed

- Links opened from another application — a mail client, a chat app, a terminal — no longer group
  with whatever tab happened to be active. The browser hands those tabs an opener even though no
  page opened them, so Tabbit now ignores a tab created while the browser is unfocused or in the
  moment right after it was raised
- Tabs sitting on the browser's own new tab page are never grouped, even when something set an
  opener on them
- Group names for hosts under a multi-part suffix like `gov.br` use the registrable domain instead
  of the suffix

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
