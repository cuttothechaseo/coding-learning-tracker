# Coding learning handoff for next project

## Purpose

Carry this context into the next chat and repository. The next selected project
is a coding-learning-tracker CLI with persistent JSON data.

## Learner profile and experience

- The user is an early-stage Python learner who can now independently build
  small terminal programs from multiple cooperating functions.
- Prior completed projects include War and Tic-Tac-Toe.
- In the most recent learning sequence, the user completed:
  - A European roulette color-betting CLI with validation, bankroll state,
    repeated rounds, quitting, and bankruptcy handling.
  - A blackjack CLI with a 52-card deck, tuple card representation, shuffling,
    dealing, hand totals, multiple-Ace adjustment, player and dealer turn
    loops, hidden dealer card, outcome logic, and replay.
- The user writes the implementation. The assistant should act as tutor,
  reviewer, and debugger, not as the primary implementation agent.

## Current Python capabilities

The user has demonstrated working knowledge of:

- Variables, strings, integers, Booleans, and comparisons
- Lists, dictionaries, sets, and tuples
- List mutation with append and pop
- Tuple unpacking
- Dictionary lookup and accumulators
- If, elif, else, for loops, while loops, and break
- Functions, parameters, arguments, local variables, and return values
- Multiple helper functions coordinated through main
- Module-level constants
- Nested loops
- Random number generation and in-place shuffling
- Input validation and normalization
- Try and except for invalid numeric input
- Repeated state changes across loops
- Creating one-round functions and whole-program orchestration
- Reading tracebacks and fixing targeted issues

JSON, file I/O, durable IDs, CRUD organization, persistence across runs, and
natural multi-file architecture are the main new layers for the next project.

## Strengths

- Isolated functions have become relatively easy and quick for the user.
- Once a conceptual mismatch is identified, the user usually fixes it rapidly
  and cleanly.
- The user often starts with most of the correct structure and misses one value,
  type, placement, or stopping condition.
- The user has good architectural instincts. They independently questioned
  putting too much work in main and correctly sees main as an orchestrator.
- The user makes conscious design choices instead of always following the
  suggested structure. Examples include choosing tuple cards and choosing a
  print-oriented winner function for a terminal-only scope.
- The user can use targeted web searches for forgotten syntax, adapt the result,
  and integrate it without blindly copying full solutions.
- The user is increasingly able to interpret tracebacks and identify the area
  of failure.
- The user recognizes when a project has delivered its learning value and is
  comfortable stopping at a coherent v1 instead of adding features from a long
  roadmap purely for completeness.

## Main bottlenecks

The recurring bottleneck is tracing data across function boundaries, not
writing basic function logic.

Common failure patterns:

- Confusing a caller's variable name with a callee's local parameter name
- Calling a function but discarding the returned value when state must be
  reassigned
- Comparing the caller's value against the wrong representation, such as a
  Boolean versus a string
- Reassigning a local parameter when the intention was to mutate the original
  list
- Replacing a collection with one item returned by a helper
- Losing track of data shape, such as list of tuples versus one tuple versus one
  string
- Reusing one stored value instead of calling the state-changing function again
- Reaching the end of a function unintentionally and receiving None
- Placing a state-changing operation outside a loop when it must happen once per
  iteration
- Adapting an online example whose input representation differs from the current
  program

The user often experiences recognition before independent recall: an
explanation makes the issue immediately obvious, but locating that issue alone
is not yet automatic. Treat this as an automaticity and debugging-practice gap,
not a lack of understanding.

## Most effective teaching style

- Give one meaningful step at a time.
- Keep preliminary learning very short. The user learns most from building the
  actual project.
- Let the user attempt the code before giving exact syntax.
- Review the attempt and give the smallest useful hint.
- Explain conceptual mistakes before syntax mistakes.
- Do not replace a nearly working implementation with a different solution.
- Explicitly state function contracts when functions cooperate:
  - what the function receives
  - what local names represent
  - what it mutates
  - what it returns
  - what the caller stores
- When the user demonstrates understanding, move forward immediately and avoid
  repetitive drills.
- Let valid, understandable code exist before introducing a more concise or
  Pythonic alternative.
- Explain tradeoffs honestly when multiple designs are valid.
- Avoid unnecessary classes and premature architecture.
- Use a separate learning.py only for a narrow blocker. Do not turn it into a
  long curriculum.
- Targeted syntax searches are normal professional behavior. Evaluate whether
  the user understands and can adapt the result rather than discouraging
  lookups.
- Match the user's casual, energetic tone while staying concrete. Do not be
  patronizing.

## Preferred debugging process

Before revealing the faulty line, guide the user through:

1. What state or output was expected?
2. What state or output actually occurred?
3. What are the current values and types?
4. What is the current data shape?
5. Which function owns each variable?
6. Which exact line changes the relevant state?
7. How many times does that line execute?
8. Does the helper mutate an object, return a value, or both?
9. Is the caller storing and passing the correct returned value?

When a function has multiple paths, isolate one path at a time. For example,
the blackjack player turn became manageable by fixing stand, then hit, then
repetition rather than debugging the whole function simultaneously.

## Observed learning trends

- The user may initially express strong frustration or self-doubt, but concrete
  evidence of what is already correct helps them recalibrate quickly.
- The user frequently says they were very close after seeing one missing link.
  This is usually accurate.
- Function logic becomes easy once expressed in plain control-flow language,
  such as calculate state, check stopping condition, get action, change state,
  repeat.
- Clear variable names reduce confusion substantially. Prefer names describing
  the value's role, such as result_color, bet_won, current_record, or record_id.
- The user benefits from seeing caller expression, actual value, and callee
  parameter mapped explicitly.
- The user prefers building a coherent v1 and moving to a new challenge once
  additions feel repetitive.

## Next project: coding-learning-tracker CLI

The selected next project is a terminal application for tracking coding
projects, skills, or learning records.

Reasonable v1 capabilities:

- Add a record
- View all records
- Mark one record complete
- Delete one record
- Search records by title
- Filter records by status
- Save all records to JSON
- Load records when the program starts

New concepts to introduce only when relevant:

- File reading and writing
- JSON serialization and deserialization
- CRUD thinking: create, read, update, delete
- Persistent state across separate program runs
- Stable record IDs
- Searching and filtering collections of dictionaries
- Separating storage logic from business logic
- A first natural multi-file structure
- File-not-found, empty-file, and malformed-data handling

Potential eventual structure:

- main.py for terminal orchestration and menus
- logic.py for record operations and search or filtering
- storage.py for JSON loading and saving
- data.json for persisted records

Do not create all modules prematurely. Start with the smallest working data
flow, then split modules when storage and record operations have clear separate
responsibilities. The user has strong instincts about keeping main focused, so
explain why each responsibility belongs where it does.

## Recommended kickoff and progression

- In the new repository, first create concise LEARNING_STYLE.md,
  CODING_LEARNING_TRACKER_PROJECT.md, and README.md files based on this handoff.
- Use learning.py only if a very short diagnostic is needed for the new data
  shape. Move into the actual project immediately afterward.
- Start by agreeing on one record's shape, likely a dictionary with a stable ID,
  title, status, and a small amount of optional metadata.
- Build in-memory CRUD behavior before persistence so JSON does not obscure
  record logic.
- Add persistence after add and view work in one run.
- Add update, delete, search, and filter incrementally.
- Split storage and logic into modules once those boundaries are real.
- Add a few lightweight tests only after there are pure logic functions worth
  testing.

The project should be a meaningful step up from games but remain a bounded
terminal v1. The primary learning goal is understanding how structured data
moves from user input to business logic to persistent storage and back again.