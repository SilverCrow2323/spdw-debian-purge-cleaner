# CLI reference

Run `spdw-purge --help` for the options supported by the installed version.

## Common commands

| Command | Purpose |
|---|---|
| `spdw-purge` | Open the GUI |
| `spdw-purge --dry-run` | Start the GUI in rehearsal mode |
| `spdw-purge --list` | Measure and list cleanup categories |
| `spdw-purge --clean safe` | Run available SAFE cleanup categories |
| `spdw-purge --clean all` | Run available non-destructive selection (not every category) |
| `spdw-purge --clean apt_cache,journal,tmp --dry-run` | Rehearse named categories |
| `spdw-purge --top "$HOME"` | Show large folders/files under a path |
| `spdw-purge --selftest` | Run built-in sanity checks |

## Real cleanup example

First measure and rehearse:

```bash
spdw-purge --list
spdw-purge --clean safe --dry-run
```

Then run the reviewed cleanup with the required privileges:

```bash
sudo spdw-purge --clean safe
```

The CLI normally asks you to type `YES`. The `--yes` / `-y` option bypasses this prompt, so reserve it for reviewed scripts and explicit categories.

## Scheduled safe cleanup

A cron entry can run a selected safe cleanup:

```cron
0 4 * * 0 root /usr/bin/spdw-purge --clean safe --yes >> /var/log/spdw-purge.log 2>&1
```

> **Optional** — Before enabling scheduled cleanup, run the same command once without `--yes` and review its output. Check the audit log after scheduled runs.
