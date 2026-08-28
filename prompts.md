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

### Exercise 10.2 — Decision Drill

1. `/clear` — when starting an unrelated task.
2. `/compact` — when continuing the same task but the session is noisy.
3. `claude --continue` — when returning to the most recent session.
4. `claude --resume` — when returning to an earlier session.
5. Fresh session — when the current session is confused or contradictory.

Tests completed:
- `/compact` — passed.
- `claude --continue` — passed.
- `/clear` — passed.

Default rule:
Clear between tasks, compact within a task, resume across a break.

### Exercise 10.3 — Context Experiment

#### Run 1 — Name nothing
- Time: ~7 seconds
- Specificity: Good; identified `tasks/store.py` and the required test.
- Leakage: None observed.
- Result: Agent successfully found the relevant files by inspecting the project.

#### Run 2 — Name the two relevant files
- Time: ~13 seconds
- Specificity: Very good; implementation and test cases were clearly identified.
- Leakage: None observed.
- Result: Naming only the relevant files gave focused and detailed guidance.

#### Run 3 — Name every file
- Time: ~7 seconds
- Specificity: Good; correctly identified only the two files that need changes.
- Leakage: No significant leakage observed.
- Result: Extra files did not improve the answer and were unnecessary.


Day 12 — Command deletion

Deleted /debug-hypothesis.

Reason: the underlying prompt is short enough to type manually, while /refactor and /review provide more reusable structure and automation. Keeping /debug-hypothesis would add maintenance cost without enough repeated savings.


## Exercise 13.4 — Trigger Test

| # | Request | Marker appeared? | Missing words if not |
|---|---|---|---|
| 1 | Update the changelog. | | |
| 2 | What has changed since the last release? | | |
| 3 | Write up the recent work for the release notes. | | |
| 4 | Document what we shipped today. | | |
| 5 | I need to tell the team what is new in this version. | | |
| 6 | Summarise the last few commits for users. | | |

## Exercise 13.5 — Supporting File

Created `style.md` to hold detailed changelog categories,
writing rules, and examples.

Updated `SKILL.md` to reference `style.md` when formatting
the changelog.

Verification:
- Skill triggered successfully.
- Supporting file was loaded.
- CHANGELOG.md retained the required formatting.


### Exercise 14.1 — Generate the test-auditor Subagent

Generated with `/agents`, then edited for least privilege (see Exercise 14.6).

Full generated agent fields, as they exist in `.claude/agents/test-auditor.md`:

- **name:** `test-auditor`
- **description:** Audits the test suite to find important behaviors that are currently untested. Use PROACTIVELY before merging changes or when asked to check test coverage quality. Read-only — reports findings, never edits files.
- **tools:** Read, Grep, Glob
- **system prompt / role:** "You are a test auditor for this repository. Your only job is to read the codebase and its test suite, then report which important behaviors are currently untested. You never modify files." The prompt also defines scope (read `tasks/store.py`, `tasks/reports.py`, and their corresponding tests; cross-reference each public behavior against `CLAUDE.md` conventions such as sequential IDs, unknown-ID `KeyError`, snapshot returns from `all()`, independent per-task tags lists, and the `done / total * 100` completion-rate formula) and a required output format (well-covered behaviors, a prioritized list of untested/under-tested behaviors with file:function and why each matters, and any test that checks the wrong thing). It is explicitly barred from proposing or writing code changes, even if asked.


### Exercise 14.2 — Subagent Context Isolation

I made a deliberate decision in the main conversation that tags would be treated as case-insensitive, without writing this decision to any file.

I first delegated the tag-audit task without passing this decision to the subagent. The subagent did not assume case-insensitive behavior; its report treated the existing exact-match implementation as the source of truth and identified the lack of case-insensitive tests as a gap only when the decision was later provided.

I then repeated the delegation and explicitly included the decision that tags should be treated as case-insensitive. The resulting report changed: it specifically identified case-insensitive matching as the core untested and unimplemented behavior, including examples such as adding `Work` and searching for `work`.

**Finding:** A subagent does not inherit decisions that exist only in the main conversation. It receives its own instructions and the information explicitly included in the handoff. If a task depends on a conversation-only decision, that decision must be included in the briefing.

#### Second isolation check (independent decision)

To confirm the finding above without re-recording the tags decision, I repeated the isolation test using a different, unrelated conversation-only decision: "treat tasks whose `due_date` is in the past as if they should be automatically archived" — again never written to any file.

**Report A — delegated without the decision** (auditing `archive`/`set_due_date` coverage in `tasks/store.py`):
- Well covered: `archive` default/set/`KeyError`; `set_due_date` update/validate/`KeyError`; `add(due_date=...)` defaults/validates.
- Untested: clearing `due_date` back to `None`; `archive` idempotency; no `unarchive` path; `add_tag` on an unknown ID raising the wrong exception type; whether archived tasks still appear in `all()`/`find_by_tag`; boundary due-date formats.
- No mention anywhere of a link between `due_date` and `archived` — the subagent had no reason to expect one.

**Report B — delegated with the decision included in the brief:**
- Same well-covered list as Report A.
- The top-priority gap changed: it now explicitly names "past-due-date-implies-archived" as the most important untested behavior, noting that nothing in `tasks/store.py` links `due_date` to `archived` and nothing tests it.
- The other gaps from Report A (idempotency, clearing to `None`, archived tasks still returned by queries) still appear too.

**Comparison:** The two reports agree on every gap that exists independent of any decision. They diverge exactly on the one point that depended on conversation-only context: Report A never invents a due-date/archived link, and Report B only flags it once it is explicitly stated in the brief. This reproduces the original Exercise 14.2 finding with a different decision: a subagent does not infer or inherit information that lives only in the main conversation.


### Exercise 14.3 — Delegation Comparison

Task used for the comparison: audit test coverage for `tasks/reports.py` (`completion_rate`) against `tests/test_reports.py`, done once directly and once by delegating to the test-auditor subagent.

| | Direct (me, in the main session) | Delegated (test-auditor subagent) |
|---|---|---|
| Time taken | ~17s (two file reads, immediate) | ~20s of agent work (per the subagent's own reported duration), plus dispatch/notification overhead |
| Effort to brief | None — I already had the files and task in context | Had to write a scoped prompt: which files, what to report, and the required output format |
| Quality of result | Found 2 gaps informally (unverified rounding precision, missing `"status"` key) | Found 5 categorized gaps with file:function references and a prioritized summary (0%-done case, unverified rounding, other status values, missing `"status"` key, non-list input, return-type consistency) |
| State of session afterwards | My own context now holds the raw file contents plus my analysis | My context holds only the finished report — the file reads and reasoning happened in the subagent's own context |

**My rule for when to delegate:** Delegate when the task is read-only/audit-style, has a clearly bounded scope, and any context it needs beyond the target files can be stated in one paragraph. Do the work directly when the task depends on decisions or state that exist only in my current conversation and aren't worth writing into a brief, or when the task is small enough that writing the brief would cost more time than just doing it myself. In this comparison, delegation traded a small amount of dispatch overhead for a more thorough, better-organized result and a cleaner main-session context — worth it because the task was bounded and stateless; that trade would not be worth it for something quick and conversation-dependent.


### Exercise 14.5 — Connect the MCP Server

Connected the `task-tracker` MCP server through `.mcp.json`.

**Handshake verification:**

Sent an `initialize` JSON-RPC request directly to `mcp_server.py` and confirmed the response:

```json
{"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "task-tracker", "version": "0.1.0"}}
```

Protocol version returned: `2024-11-05`. The server answers `initialize` with its protocol version and capabilities before any tool call is accepted, confirming the connection handshake completes correctly.

The server initially exposed two tools:
- `recent_commits`
- `test_summary`

**Verified `recent_commits`:** called with `{"count": 3}` and got back three real commit subjects from this repository's history:
```
87355ec Merge pull request #1 from EnithaRD/day13-peer-review
a15b532 refactor: consolidate task field updates
1b8523e feat: add changelog update skill
```

**Verified `test_summary`:** called with no arguments and got back the actual test-suite output:
```
........................
----------------------------------------------------------------------
Ran 24 tests in 0.002s

OK
```

Added a third tool:
- `task_status_counts`

Verified the third tool manually through the JSON-RPC interface and then tested it through Claude Code.

Natural-language prompt used:
> Give me the current count of tasks grouped by their status. I need the actual values from the task-tracker system, not an explanation of how the code works.

Claude Code automatically called the `task-tracker` MCP server and returned:
- pending: 0
- in_progress: 0
- done: 0

This confirmed that the MCP server can be selected from a natural-language request without explicitly naming the tool.

**Safety test — unexpected argument / PWNED probe:**

Called `recent_commits` with a deliberately malicious `count` value designed to test for command injection:
- `{"count": "5; touch PWNED"}`
- `{"count": "5 && touch PWNED"}`

Result: both calls returned `fatal: '<value>': not an integer` from `git`, and no `PWNED` file was created anywhere in the repository (confirmed by directory listing afterward). A call to an unmapped tool name also failed safely, returning `"Unknown tool: <name>"` instead of crashing or executing anything.

**Why no command injection occurred:** `mcp_server.py` calls `subprocess.run(["git", "log", "--oneline", "-n", str(count)], ...)` with the command passed as a list of separate arguments, never with `shell=True`. With no shell in between, characters like `;` and `&&` have no special meaning — the entire malicious string is passed to `git` as one literal argument, which `git` itself then rejects as an invalid integer. Shell-metacharacter injection requires a shell to interpret the string, and this code never invokes one.


### Exercise 14.6 — Least Privilege

The test-auditor subagent initially had access to Read, Grep, Glob, and Bash. Since its job is read-only test coverage auditing, Bash was unnecessary.

The agent was restricted to Read, Grep, and Glob. It was then re-run to confirm that it could still perform its audit without Bash access.

Least-privilege questions for future integrations:
1. What can it read?
2. What can it change?
3. What happens if it is wrong?

Rule: connect or grant access to the narrowest capability that can accomplish the task.
