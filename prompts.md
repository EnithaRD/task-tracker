# Day 9 Claude Prompts

## Bug 1 — Unknown Task ID

### Prompt
I am debugging the task-tracker project.

The test expects KeyError when set_status() is called with a
nonexistent task ID.

The stack trace shows a TypeError because task is None.

Do not modify any files. Evaluate my hypothesis and explain the
root cause.

### Judgment
Accepted.

### Reason
Claude's explanation matched the stack trace and the behavior of
find() and set_status().


## Bug 2 — Shared Tags

### Prompt
I am debugging test_tags_are_not_shared_between_tasks.

My hypothesis is that the default tags=[] list is shared between
multiple calls to add().

Do not modify any files. Evaluate my hypothesis and explain why
the tasks share the same list.

### Judgment
Accepted.

### Reason
The behavior was reproduced and matched Python's mutable default
argument behavior.


## Bug 3 — Snapshot

### Prompt
I am debugging test_all_returns_a_snapshot.

My hypothesis is that all() returns the internal _tasks list
directly instead of a copy.

Do not modify any files. Evaluate my hypothesis and explain the
reference behavior.

### Judgment
Accepted.

### Reason
The snapshot changed when the underlying task list changed,
confirming that the same list was being returned.


## Bug 4 — Completion Rate

### Prompt
I am debugging completion_rate().

The expected behavior is the percentage of total tasks that are
done.

The current implementation divides the number of done tasks by
the number of outstanding tasks.

Do not modify any files. Evaluate my hypothesis and explain the
root cause.

### Judgment
Accepted.

### Reason
The observed results of 0.0 and 300.0 were explained by using
outstanding tasks as the denominator.


## Claude Answer Evaluation

I did not blindly accept Claude's suggestions.

For each bug, I first formed my own hypothesis from the stack
trace, failing test, and source code. I then used Claude to
evaluate the hypothesis and explain the cause.

Where Claude's answer did not match my evidence, I would reject
the answer and verify the behavior independently.


## Day 10 — Exercise 10.1

### Session Degradation

Symptoms observed:
- Drift: old/abandoned decisions came back into discussion.
- Contradiction: priority changed from number to word.
- Over-reach: unrelated Flask context appeared.
- Stale picture: earlier project context could become outdated.
- Lost constraints: latest decisions could be forgotten.
- Hedging: responses became less focused.

### Earliest Warning Sign
Contradiction — the session had difficulty keeping the latest priority decision.

### Lesson
Too much unrelated context makes the session less reliable. Keep sessions focused
and use clear/compact/resume when appropriate.
-