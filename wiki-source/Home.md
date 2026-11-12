# SPDW Purge — quick guide

SPDW Purge is a disk analyzer and cleaner for MX Linux and Debian-based systems. It combines a disk-usage treemap, junk-category cleanup, APT/Flatpak removal, duplicate-file finder and CLI.

> [!IMPORTANT]
> **MUST KNOW!!** This tool deletes files and removes packages. Start with **DRY-RUN**, read the selected categories and keep important backups. The final deletion is your responsibility.

## Start here

- [Install SPDW Purge](Installation)
- [Understand the safety model](Safety-and-Dry-Run)
- [Scan disks and export reports](Disk-Scan-and-Reports)
- [Choose junk categories](Junk-Categories)
- [Remove packages safely](Package-Removal)
- [Use the CLI](CLI-Reference)
- [Fix common problems](Troubleshooting)
- [Quick answers](FAQ)

## What the tabs do

| Tab | Purpose |
|---|---|
| **SCAN** | Treemap, sorted folder tree, largest files and file-type breakdown |
| **JUNK** | Measured cleanup categories grouped by SAFE / MED / AGGR |
| **APPS** | Installed APT packages and Flatpaks, with removal simulation |
| **FINDER** | Duplicates, empty files/folders, broken symlinks and big/old files |

## Project links

- [Latest releases](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner/releases)
- [Source repository](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner)
- [Report a problem](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner/issues)
- [Detailed README](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner/blob/main/README.md)
