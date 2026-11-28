# Project: SPDW Debian Purge Cleaner

## Purpose
Provide a cautious desktop utility for finding and removing recoverable disk usage on Debian-family Linux systems, especially MX Linux XFCE. It combines storage inspection, package cleanup, old-kernel selection, residue discovery and a dry-run-first deletion workflow.

## Users and use cases
- Linux desktop users reviewing large files, caches, package leftovers and unused kernels.
- Maintainers validating safe path handling, dry-run behavior and audit output.
- Administrators using the tool with explicit privilege escalation and a real-user context.

## Scope and boundaries
In scope: read-only tree scanning, treemap summaries, file-type grouping, APT/Flatpak cleanup planning, old-kernel identification, residue detection, protected-path policy, dry-run and confirmed deletion.

Out of scope: unattended cleanup, automatic removal of arbitrary system files, filesystem repair, repartitioning, malware scanning and claiming that every large file is disposable. The tool must never delete protected roots or follow a symlink target during deletion.

## Target
- Debian/Ubuntu/MX Linux desktop, with MX Linux XFCE as the primary user environment.
- Python 3 and Tkinter; APT/dpkg and optional Flatpak.
- Root actions are narrowly scoped and retain the invoking user's HOME/UID context.

## Architecture
- Core: filesystem scan, type/size aggregation, protection policy and deletion primitives.
- Finder: large-file and residue discovery.
- Package helpers: APT simulation, Flatpak listing and old-kernel selection.
- GUI: treemap, review lists, explicit dry-run and confirmation.
- Audit: append-only record of requested cleanup actions.

## Safety and accessibility
Default to dry-run. Protect system roots, home roots, mount points and sensitive directories. Never recursively follow symlinks. Report bytes actually removed, not estimates as success. Require confirmation for destructive actions and keep the interface readable with keyboard navigation.

## Verified baseline
The repository contains core scanning/deletion helpers, package inventory functions, GUI and unit tests for protected paths and dry-run behavior. A test for arbitrary mount-point protection is added in this branch; no system cleanup was run during this task.
