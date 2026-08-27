# Changelog Style Guide

## Categories

Use these categories:

### Added
Use for new features or capabilities.

### Fixed
Use for bug fixes or corrected behavior.

### Changed
Use for changes that do not clearly belong under Added or Fixed.

## Writing Style

- Describe the user-facing effect of the change.
- Keep each entry concise.
- Do not copy commit messages word-for-word.
- Use one bullet per change.
- Keep the newest changes first.
- Do not invent information that is not supported by Git history.

## Example

### Added
- Users can now archive tasks and look them up by tag.

### Fixed
- Completion-rate calculations now use the total number of tasks.

### Changed
- Repeated task lookup logic was consolidated into a shared helper.