---
description: Review current uncommitted changes
---

Review the current uncommitted changes below against the conventions in CLAUDE.md.

!`git diff`

Report anything that falls into these categories, and nothing else:

- A change to a file that looks out of scope for the rest of the diff.
- A test that was weakened or removed.
- An error path that is caught rather than prevented.
- A hardcoded value that should not be committed.
- Anything you cannot tell the purpose of.

If none of these apply, say so in one line.

Do not summarise the diff.
Do not report stylistic improvements.
Do not suggest unrelated changes.
Do not modify any files.