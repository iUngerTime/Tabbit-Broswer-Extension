# Privacy Policy for Tabbit

**Effective date:** 25 August 2026

Tabbit is a browser extension that automatically organizes tabs into tab groups. This policy
describes everything the extension does with data. It is short because Tabbit does very little.

## Tabbit does not collect your data

Tabbit sends nothing anywhere. It has no server, makes no network requests, and contains no
analytics, telemetry, tracking, or advertising code. No data about you or your browsing ever leaves
your computer. Nothing is sold, shared, or transferred to anyone, ever.

The extension requests no host permissions and runs no content scripts, so it cannot read the
contents of any web page you visit.

## What Tabbit reads, and why

To put a new tab in a group with the tab that opened it, Tabbit reads the following from the
browser, at the moment a tab is opened, closed, or switched to:

- **The URL of the tab that opened a new tab.** Used to derive the group's name from the site's
  domain, and to check that domain against your custom rules and your blacklist.
- **The page title of that tab**, only if you set group naming to "opener's title."
- **Which window a tab is in, whether it is pinned, and which group it belongs to.** Used to decide
  whether the tab should be grouped at all.
- **Whether the browser window is focused.** Used to tell a link you opened inside the browser from
  one opened by another application, so that links arriving from your mail or chat client are not
  grouped with whatever tab you happened to be on.

This information is used in the moment, in memory, to make a single grouping decision, and is then
discarded. Tabbit does not keep a history of the pages you visit, does not write URLs to storage,
and does not log them.

## What Tabbit stores

Tabbit stores your settings, and nothing else, using the browser's local extension storage
(`storage.local`) on your own computer:

- Your grouping mode, group naming convention, and pretty-names preference
- Your maximum group size, and the auto-ungroup and auto-collapse toggles
- The custom rules you create — the domain, alias, and color for each
- The domains you add to your blacklist

The custom rules and blacklist contain domains that you typed in yourself. This data stays on your
machine. It is not synced to any account and is not transmitted anywhere. Uninstalling the
extension removes it.

## Permissions

Tabbit requests three permissions, each required for the grouping feature:

- **`tabs`** — to see that one tab opened another, and to read the opening tab's URL so the group
  can be named after the site and matched against your rules.
- **`tabGroups`** — to create groups and set their name, color, and collapsed state.
- **`storage`** — to save the settings listed above on your device.

## Children

Tabbit is not directed at children and collects no information from anyone, including children.

## Changes to this policy

If this policy changes, the updated version will be published in this repository and the effective
date above will be revised. Because the extension is open source, every change to what it does is
visible in its commit history.

## Contact

Questions or concerns: open an issue at
<https://github.com/iUngerTime/Tabbit-Broswer-Extension/issues>.

## Source

Tabbit is free software, licensed under the GPL-3.0. You can read every line of it at
<https://github.com/iUngerTime/Tabbit-Broswer-Extension>.
