# Troubleshooting

Start with the app log and the exact selected path/category. Avoid deleting more data to troubleshoot a cleanup problem.

## Common issues

| Symptom | First check |
|---|---|
| GUI does not open | Install `python3-tk`; otherwise use the CLI |
| Root prompt is declined | Continue in limited user mode or launch the specific root operation intentionally |
| A category is unavailable | Check whether its optional tool is installed and whether root is required |
| APT simulation fails | Refresh package metadata and inspect the package manager state before retrying |
| A category reports zero size | Check the category's target paths and whether the data exists |
| A scan seems smaller than file sizes | It measures allocated blocks and de-duplicates hardlinks |
| Flatpak category is missing | Install Flatpak if it is part of your system |
| Cleanup says protected path | The target is covered by a system/user safety rule; do not bypass the guard |

## Logs and tests

- Audit log: `~/.local/state/spdw-purge/actions.log`
- Run `spdw-purge --selftest` for built-in sanity checks.
- Run `make test` from a source checkout for the unit test suite.

## Report an issue

Include the distribution/version, SPDW Purge version, command or tab, selected category/path, dry-run output and relevant redacted audit entries.

> [!WARNING]
> Remove usernames, private directory names and personal filenames before posting logs publicly.
