# Safety and DRY-RUN

SPDW Purge is designed to show what an operation will touch before it changes the system. Use this page before deleting files, cleaning caches or purging packages.

> [!IMPORTANT]
> **MUST KNOW!!** Turn on **DRY-RUN** first. Review the operation log and the selected paths/categories before switching to a real cleanup.

## Protection layers

- System-critical paths such as `/`, `/usr`, `/etc`, `/boot`, `/home`, mount points and the detected user's home are hard-protected.
- Dangerous paths and package targets require additional confirmation in the GUI.
- Essential packages are locked in the APPS tab.
- APT removal is simulated before execution to show dependencies that would also be removed.
- Every operation is written to the per-user audit log.

## Use DRY-RUN

### GUI

1. Open SPDW Purge.
2. Enable **DRY-RUN** before selecting cleanup actions.
3. Run the scan or category measurement.
4. Review the log. Entries marked `[dry-run]` describe what would happen.
5. Disable DRY-RUN only after checking the paths, categories and package list.

### CLI

```bash
spdw-purge --list
spdw-purge --clean safe --dry-run
spdw-purge --clean apt_cache,journal,tmp --dry-run
```

## Confirmation and automation

- The CLI normally asks for `YES` before executing a real cleanup.
- `--yes` skips that prompt. Use it only for a reviewed, explicit selection.
- Do not combine `--yes` with broad or destructive cleanup until the DRY-RUN output has been checked.
- The `all` selection is not literally every category: categories listed as destructive in the application are excluded.

## Audit log

The action log is stored at:

```
~/.local/state/spdw-purge/actions.log
```

When the app runs with elevated permissions, it attempts to keep the audit directory and file owned by the invoking user.

## Shred option

Shredding is not a guaranteed secure erase on SSDs, copy-on-write filesystems, snapshots or storage with wear levelling. Treat it as an extra overwrite attempt, not proof that data is irrecoverable.
