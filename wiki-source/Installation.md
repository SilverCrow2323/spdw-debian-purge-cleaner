# Install SPDW Purge

The recommended installation is the published `.deb` package. The application targets MX Linux and other Debian-based distributions and uses Python 3 with Tkinter.

## Install the release package

1. Open [GitHub Releases](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner/releases).
2. Download `spdw-purge_<version>_all.deb`.
3. Open a terminal in the download folder.
4. Install the local package:

```bash
sudo apt install ./spdw-purge_1.1.0_all.deb
```

5. Launch **SPDW Purge** from the application menu or run `spdw-purge`.

## Run from source

```bash
sudo apt install python3 python3-tk
git clone https://github.com/SilverCrow2323/spdw-debian-purge-cleaner.git
cd spdw-debian-purge-cleaner
make run
```

- `make run` starts the GUI without a system-wide installation.
- `sudo make install` installs the app under the system prefix.
- `make deb` builds the Debian package under `dist/`.

## Optional dependencies

- `pkexec`: privilege elevation when an operation needs root.
- `deborphan`: orphan-library detection.
- `flatpak`: Flatpak inventory and unused-runtime cleanup.

> [!NOTE]
> Without `python3-tk`, the GUI is unavailable; use the CLI options or install Tkinter.
