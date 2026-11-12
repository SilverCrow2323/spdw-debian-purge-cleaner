# FAQ

## Is SPDW Purge only for MX Linux?

It is designed for MX Linux (Xfce) and works on Debian-based distributions. Some categories depend on optional tools or distro-specific paths.

## Does DRY-RUN modify anything?

No. It rehearses operations and logs what would happen without performing the selected changes.

## Does `--clean all` really select every category?

No. The application excludes its destructive category set from `all`. Select a destructive category explicitly only after reviewing its target and running a dry-run.

## Can it remove essential packages?

The APPS tab locks packages classified as essential and simulates APT's dependency removal before execution. Always review the simulation.

## Where is the audit log?

At `~/.local/state/spdw-purge/actions.log` for the invoking user.

## Does shred guarantee that a deleted file cannot be recovered?

No. SSD wear levelling, snapshots, copy-on-write filesystems and backups can retain older blocks. Shred is not a secure-erasure guarantee.

## Why does it need root?

System-level caches, packages and logs require elevated permissions. The app uses pkexec when needed; without elevation it offers a limited user mode.
