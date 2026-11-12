# Wiki source and publishing

The `wiki-source/` directory is the canonical source for the GitHub Wiki. Keep the Wiki focused on practical operations; the root README and source code remain the detailed reference.

## Page rules

- One topic per page.
- Start with a short explanation of what the page covers and when it is useful.
- Use one concept per bullet.
- Use **MUST KNOW!!** only for required safety or compatibility information.
- Use **Optional** only for non-essential enhancements.
- Leave basic concepts unlabelled.
- Describe `safe`, `all` and explicit category selection precisely.
- Do not recommend bypassing DRY-RUN or confirmation prompts for destructive operations.

## First-time Wiki activation

1. Open the [SPDW Purge Wiki](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner/wiki).
2. Create and save a first page named **Home**.
3. From a clone with Git credentials, run `sh tools/publish_wiki.sh`.

The publisher copies tracked Markdown pages from `wiki-source/` to the GitHub Wiki. Edit the source files here, not only the live Wiki.

## Detailed reference

- [Root README](../README.md)
- [Changelog](../CHANGELOG.md)
- [Source code](../spdw_purge/)
