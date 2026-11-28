# Roadmap — SPDW Debian Purge Cleaner

## M0 — Safe inspection
- [x] Scan directory trees and aggregate sizes/types.
- [x] Identify large files, package residue and old kernels.
- [x] Protect fixed system roots and sensitive directories.
- [x] Provide a dry-run path and action audit log.
- [x] Add a regression test for mount-point protection.

## M1 — Accurate cleanup outcomes
- [ ] Make every deletion path report actual success/failure and bytes freed.
- [ ] Preserve failed paths in the review list with a clear error.
- [ ] Test permission errors, busy mounts, read-only filesystems and partial directory failures.
- [ ] Keep source changes and cleanup decisions separate from package-manager simulation.

## M2 — Package cleanup safety
- [ ] Revalidate package state immediately before removal.
- [ ] Keep essential packages and the running/newest kernel protected.
- [ ] Verify APT/Flatpak dry-run results before showing a final plan.

## M3 — UX and distribution
- [ ] Improve keyboard/screen-reader labels and low-resolution layouts.
- [ ] Add reproducible Debian package build and install/uninstall tests.
- [ ] Test on MX Linux XFCE and a non-MX Debian derivative.

## Acceptance
No protected path or mount point can be selected for deletion; dry-run changes nothing; failed deletion is never reported as success; package-manager plans are revalidated; tests use disposable fixtures only.

## Release target
Maintain the 1.1.x maintenance line until deletion outcome reporting and package-manager revalidation pass the full test suite. No release is created by this change.

## Evening verification — 2026-11-28

- Verified [unit-and-self-tests run #46177103975](https://github.com/SilverCrow2323/spdw-debian-purge-cleaner/actions/runs/46177103975) on `f9757c2`; Python module compilation, unit tests and the application self-test passed.
- This is test-runner evidence only. No cleanup was executed on the host. Mount-point protection still requires a disposable-filesystem/manual integration test before release.
