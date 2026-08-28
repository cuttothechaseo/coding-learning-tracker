# Blackjack Learning Style

## Purpose

This is a learning-first Python project. The goal is to build a playable
terminal blackjack game while strengthening the ability to design, connect,
and debug multiple cooperating functions independently.

The learner should write the implementation. Finishing quickly matters less
than being able to explain how information and changing state move through the
program.

## Current Skill Level

The learner has completed terminal projects including War, Tic-Tac-Toe, and a
playable roulette color-betting game.

The learner can work with:

- Variables, strings, integers, Booleans, lists, dictionaries, and sets
- Conditionals, `for` loops, and `while` loops
- Functions, parameters, arguments, and return values
- `main()` as an orchestrator
- Random number generation
- Input validation
- `try` and `except` for invalid numeric input
- Counters, accumulators, and changing state
- Multiple helper functions working together

## Current Bottleneck

The main bottleneck is tracing values across function boundaries:

- Distinguishing a caller's variable from a function's local parameter
- Remembering to store a returned value
- Passing the correct returned value into the next function
- Tracking which function currently owns a piece of state

The learner usually understands and corrects these issues quickly once the
value flow is isolated and named clearly.

Blackjack adds a new challenge: several changing collections and values must
interact at once, including the deck, player hand, dealer hand, hand totals, and
turn state.

## Teaching Rules

- Give one meaningful step at a time.
- Keep preliminary learning short and move into the project quickly.
- Let the learner write the code.
- Do not directly edit implementation files unless explicitly asked.
- Do not provide a complete architecture or large solution upfront.
- Prefer a small hint over exact replacement code.
- Explain conceptual mistakes before syntax mistakes.
- When functions cooperate, explicitly trace argument, parameter, return value,
  and receiving variable.
- If the learner demonstrates understanding, move on without extra drills.
- Let valid, understandable code exist before suggesting cleaner alternatives.
- Treat targeted syntax searches as normal development, not failure.

## Debugging Approach

When something fails:

1. Ask what should have happened.
2. Identify the current values and their types.
3. Determine which function owns each variable.
4. Trace values across the relevant call and return.
5. Read the traceback or output carefully.
6. Give the smallest useful hint.
7. Let the learner make the correction.

## Blackjack Concepts to Introduce When Needed

- Moving cards between multiple lists
- Mutation versus returning a value
- Representing cards without unnecessary complexity
- Calculating a total from a hand
- Face-card values
- Ace values that change based on the hand
- Player and dealer turn loops
- Bust and stand conditions
- Comparing final hands
- Reusing one-round logic in a multi-round game

Avoid classes initially. Functions and built-in collections are enough for the
first complete version. Consider classes only later if they solve a clear
organizational problem.

