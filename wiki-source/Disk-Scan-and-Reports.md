# Scan disks and export reports

The SCAN tab shows where allocated disk space is used. It provides a treemap, a size-sorted folder tree, a largest-files list and a file-type breakdown.

## Start a scan

1. Open **SCAN**.
2. Choose a directory or filesystem to inspect.
3. Wait for the scan to finish.
4. Use the treemap to identify large folders and files.
5. Double-click a folder to dive into it; use **UP** to return to its parent.

## Interpret the result

- Sizes use allocated disk blocks, which can differ from the logical file size.
- Hardlinks are counted once.
- The scan stays on the starting filesystem and skips system virtual filesystems such as `/proc`, `/sys`, `/dev` and `/run`.
- Top files and file-type totals help identify large media, disk images, archives, ROMs and development caches.

## Context menu

Right-click a selected item for the supported actions, such as opening it in the file manager, copying its path or scanning that folder.

## Export a report

Use the Markdown report action from SCAN to save a summary of the measured disk usage. Review the exported paths before sharing: filenames and directory names can reveal personal information.

> **Optional** — Use the CLI for a quick terminal summary:

```bash
spdw-purge --top "$HOME"
```
