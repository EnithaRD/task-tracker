---
name: changelog-update
description: Updates CHANGELOG.md and prepares release notes by summarising recent git commits, explaining what changed, what was fixed, what was added, and what was shipped. Use when asked to update the changelog, summarise recent changes, prepare release notes, document what was shipped, explain what is new in a version, or summarise recent commits for users.
---

# Changelog Update

Keep CHANGELOG.md current from the commit history.

## Steps

1. Read the most recent commits with:
   git log --oneline -n 20
2. Ignore any commit already described in CHANGELOG.md.
3. Group the remaining commits under Added, Fixed, or Changed.
4. Write one line per change, describing the effect on someone using this project. Do not restate the commit subject verbatim.
5. Put them under the Unreleased heading, newest first.

## Rules

- Never invent a change that is not in the commit history.
- Never remove or reword an existing entry.
- If nothing new has happened, say so and change nothing.
- Always begin your reply with the line CHANGELOG SKILL ACTIVE.


## Style

For changelog categories, writing style, and examples, read
`.claude/skills/changelog-update/style.md` when formatting the changelog.

Read `.claude/skills/changelog-update/style.md` before formatting
or updating CHANGELOG.md.

## Rules

- Never invent a change that is not in the commit history.
- Never remove or reword an existing entry.
- If nothing new has happened, say so and change nothing.
- Always begin your reply with the line CHANGELOG SKILL ACTIVE.