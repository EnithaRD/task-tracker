# Changelog

## Unreleased

### Added

- Added reusable Claude Code command templates for reviewing and refactoring code in this project.
- Tasks can now have a due date (validated as an ISO `YYYY-MM-DD` string), be archived, and be looked up by tag.
- Added a debugging workflow write-up describing how issues in the task store were diagnosed.

### Fixed

- Fixed `completion_rate` to calculate the done percentage against the total task count instead of only outstanding tasks.
- Fixed `TaskStore.add` so tasks no longer share a single default tags list across instances.
- Fixed `TaskStore.all()` to return a snapshot of tasks instead of the internal list, preventing external code from mutating stored tasks directly.
- Fixed status updates on an unknown task id to raise `KeyError` instead of failing silently.

### Changed

- Simplified repeated "task not found" checks in `TaskStore` into a single internal helper (no behavior change).
- Ignored Python bytecode cache files so they no longer show up as tracked changes.