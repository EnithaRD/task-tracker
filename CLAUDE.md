# CLAUDE.md

## Purpose

This project is a small in-memory task tracker. Keep changes focused, test-driven, and consistent with the existing behavior.

## Commands

Run the full test suite:

```bash
python -m unittest discover tests
```

Run the store tests:

```bash
python -m unittest tests.test_store
```

Run one test:

```bash
python -m unittest tests.test_store.TestTaskStore.test_add_assigns_sequential_ids
```

Run the demo:

```bash
python demo.py
```

## Structure

* `tasks/store.py` — task storage and task operations.
* `tasks/reports.py` — task reporting and summary calculations.
* `tests/test_store.py` — tests for task storage behavior.
* `tests/test_reports.py` — tests for reporting behavior.
* `demo.py` — manual demonstration of the application.

## Conventions

* Diagnose the root cause using the failing test, stack trace, and source code before changing code.
* Add or preserve tests that capture the expected behavior.
* Keep changes focused on the relevant files.
* Unknown task IDs must raise `KeyError`.
* `all()` and other list-returning operations must return snapshots, not internal list references.
* Each task must have its own independent tags list.
* Completion rate must use `done / total * 100`.

## Testing

Use Python's standard-library `unittest` framework.

Run the full test suite after production-code changes. Tests should verify the expected behavior rather than being weakened to accommodate an incorrect implementation.

## Do Not

* Do not modify or weaken tests just to make them pass.
* Do not patch only where a crash appears without tracing the bad value to its source.
* Do not use mutable default arguments such as `tags=[]`.
* Do not return internal mutable lists directly.
* Do not use outstanding tasks instead of total tasks as the completion-rate denominator.
* Do not make unrelated changes outside the relevant files.

## Maintenance

Update this file when a project convention changes or a new repeated project-specific rule is established. Keep it short and remove rules that are no longer true.
