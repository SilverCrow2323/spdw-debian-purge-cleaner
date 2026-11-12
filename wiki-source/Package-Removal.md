# Remove packages safely

The APPS tab lists installed APT packages and Flatpaks. It can simulate APT's removal plan before running a real purge, including dependencies that would be removed along with the selected package.

## Review a package

1. Open **APPS**.
2. Search or browse the installed package list.
3. Select a package to inspect its size and status.
4. Review the simulated removal output.
5. Confirm only when the package and dependency list are understood.

## Safety checks

- Essential/system packages are locked.
- APT removal is simulated with `apt-get -s`.
- The operation can run `purge` and `autoremove --purge`.
- After removal, the app searches selected configuration/cache locations for likely leftovers.

> [!IMPORTANT]
> **MUST KNOW!!** A package can be required by other applications. Read the dependency simulation; do not assume that removing one visible app removes only that app.

## Flatpak

Unused Flatpak runtimes are listed separately when Flatpak is installed. Review the selected scope before confirming cleanup.

## Recovery

Reinstalling a package does not always restore its previous application data or configuration. Keep backups of important settings before purging.
