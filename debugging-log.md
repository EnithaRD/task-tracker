# Day 9 Debugging Log

## Bug 1 — Unknown Task ID

### Symptom
`set_status(99, "done")` raised a TypeError instead of KeyError.

### My Hypothesis
`find(99)` returns `None`, and `set_status()` attempts to update
the status of `None`.

### Actual Cause
`set_status()` did not check whether the task existed before
updating its status.

### Was My Hypothesis Correct?
Yes.

### How I Proved It
I followed the stack trace from `set_status()` to `find()`.
`find(99)` returned `None`, which caused the TypeError.

### How I Verified the Fix
I added a test expecting `KeyError`, fixed the production code,
and ran the full test suite.


## Bug 2 — Shared Task Tags

### Symptom
Adding a tag to one task also added the tag to another task.

### My Hypothesis
The `tags=[]` mutable default argument was shared between calls
to `add()`.

### Actual Cause
Multiple tasks were using the same list object for their tags.

### Was My Hypothesis Correct?
Yes.

### How I Proved It
I created two tasks, added a tag to the first task, and observed
that the second task received the same tag.

### How I Verified the Fix
I added a failing test for independent tag lists, fixed the
production code, and ran the test suite.


## Bug 3 — Task List Snapshot

### Symptom
A snapshot returned by `all()` changed after another task was added.

### My Hypothesis
`all()` returned the internal `_tasks` list directly.

### Actual Cause
The returned list referenced the same list maintained internally
by the store.

### Was My Hypothesis Correct?
Yes.

### How I Proved It
I stored the result of `all()`, added another task, and observed
that the previously returned list also changed.

### How I Verified the Fix
I added a failing snapshot test, fixed `all()`, and ran the
full test suite.


## Bug 4 — Completion Rate

### Symptom
The program ran successfully but calculated the wrong completion
percentage.

### My Hypothesis
The calculation used the number of outstanding tasks as the
denominator instead of the total number of tasks.

### Actual Cause
The formula used:

`done / outstanding * 100`

instead of:

`done / total * 100`

### Was My Hypothesis Correct?
Yes.

### How I Proved It
I tested different combinations of done and pending tasks and
compared the expected and actual results.

### How I Verified the Fix
I added tests for all-done and mixed cases, fixed the calculation,
and ran the complete test suite.