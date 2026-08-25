# Tabbit - Automatic Tab Grouping

![Tabbit](branding/marketing-image.png)

Automatic tab grouping for Firefox and Chrome. When you open a link in a new tab, Tabbit groups it
with the tab that opened it.

Requires **Firefox 139+** or **Chrome 89+**.

## Features

- **Group by opening tab or domain** — group every tab from the same opener, or only when domains
  match
- **Configurable group naming** — name groups by domain, subdomain, full hostname, page title, or
  leave nameless
- **Pretty names** — capitalize and clean up group names automatically
- **Max tabs per group** — cap how many tabs a group can hold
- **Auto-ungroup lonely tabs** — dissolve a group when it shrinks to one tab
- **Auto-collapse inactive groups** — keep only the active group expanded
- **Custom rules** — override group name and color for specific domains, with ordered
  first-match-wins evaluation
- **Blacklist** — prevent specific domains from being grouped

All settings are accessible from the toolbar popup — click the Tabbit icon in your toolbar.

## Screenshots

| Settings                                                        | Custom Rules                                                  | Blacklist                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| ![Settings](branding/screenshots/tabbit-settings-configure.png) | ![Custom Rules](branding/screenshots/tabbit-custom-rules.png) | ![Blacklist](branding/screenshots/tabbit-blacklist.png) |

| Group Naming                                             | Custom Rules in Action                                     |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| ![Naming](branding/screenshots/tabbit-settings-name.png) | ![Demo](branding/screenshots/tabbit-custom-rules-demo.png) |

## Install

Coming soon to [addons.mozilla.org](https://addons.mozilla.org) and the
[Chrome Web Store](https://chromewebstore.google.com).

To build both packages from source, run `./build.sh` — see [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

## Privacy

Tabbit sends nothing anywhere — no server, no network requests, no analytics. It reads tab URLs in
the moment to name a group, and stores only your settings, on your own machine. See
[PRIVACY.md](PRIVACY.md).

## License

[GPL-3.0](LICENSE.md)
