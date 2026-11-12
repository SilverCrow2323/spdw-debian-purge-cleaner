# Junk categories

The JUNK tab measures cleanup candidates and groups them by risk. Categories are not interchangeable: some data is regenerated, some must be downloaded again, and some may contain user information.

## Risk levels

| Level | Meaning |
|---|---|
| **SAFE** | Regenerable caches or routine cleanup targets |
| **MED** | May require re-download, review or additional care |
| **AGGR** | Can remove broad caches or user-managed data; explicit selection only |

## Common categories

| Key | Level | What it targets |
|---|---|---|
| `apt_cache` | SAFE | Downloaded APT package archives |
| `apt_auto` | SAFE | Packages APT marks as no longer required |
| `rc_conf` | SAFE | Residual config entries for removed packages |
| `journal` | SAFE | systemd journal, vacuumed to the configured size |
| `old_logs` | SAFE | Rotated logs |
| `crash` | SAFE | Crash reports and coredumps |
| `trash`, `thumbs`, `browser`, `flatpak` | SAFE | Trash, thumbnails, browser caches and unused Flatpak runtimes |
| `deborphan` | MED | Libraries identified by deborphan |
| `kernels` | MED | Older kernels and headers; keeps the running and newest |
| `biglogs` | MED | Truncates active logs larger than 20 MB |
| `tmp` | MED | Old entries in /tmp and /var/tmp |
| `docker`, `podman` | MED | Stopped containers and dangling images |
| `dev` | MED | Gradle, npm, Cargo, pip and Android caches |
| `privacy` | MED | Shell history and recently-used records |
| `mx_snapshots` | AGGR | MX Snapshot ISO and checksum files |
| `cache_user` | AGGR | The entire detected user's `~/.cache` |

Availability depends on installed tools and the running user.

## Choose a cleanup scope

- `--clean safe` selects only SAFE categories.
- `--clean all` selects usable categories except the app's destructive set (kernels, deborphan, MX snapshots, all-user-cache and privacy traces).
- A comma-separated list selects the named keys explicitly.

> [!IMPORTANT]
> **MUST KNOW!!** Before selecting MED or AGGR categories, inspect the measured size and the exact target paths. In particular, `cache_user` removes the whole `~/.cache` directory and `mx_snapshots` removes snapshots from `/home/snapshot`.

