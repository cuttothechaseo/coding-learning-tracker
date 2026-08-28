# Blackjack Project

## Project Overview

Build a terminal-based blackjack game in Python. One player competes against a
computer-controlled dealer using a standard 52-card deck.

The project should remain simple and understandable. Each new function should
be added only when it has a clear responsibility.

## Version 1 Scope

The first complete version should support:

- A standard deck with ranks and suits
- A shuffled deck
- A player hand and dealer hand
- An initial two-card deal
- Correct numeric and face-card values
- Aces counting as 1 or 11 when appropriate
- Player hit and stand choices
- Dealer drawing until reaching at least 17
- Bust detection
- Win, loss, and tie outcomes
- Validated terminal input
- Repeated rounds

Keep the first version focused:

- One player and one dealer
- Dealer stands on all totals of 17 or more
- A fresh shuffled deck may be created for each round
- No splitting, doubling down, insurance, or surrender
- Betting and bankroll tracking can be added after the card game works

## Development Progression

### Phase 1 — Card Movement

Choose a simple representation for a card, build a small deck, and draw one
card from the deck into a hand.

Reinforces:

- Lists and dictionaries or tuples
- List mutation
- Parameters and return values
- Moving one value between collections

Goal: draw one card and clearly show the changed deck and hand.

### Phase 2 — Full Deck and Initial Deal

Build and shuffle a 52-card deck, then deal two cards each to the player and
dealer.

Reinforces:

- Nested loops
- Constructing collections
- Random shuffling
- Repeated function calls
- Multiple changing hands

Goal: every card is valid, no card is dealt twice, and both hands contain two
cards.

### Phase 3 — Hand Values

Calculate the value of a hand.

Rules:

- Number cards use their printed value
- Jack, Queen, and King count as 10
- An Ace counts as 11 unless that would bust the hand, in which case it can
  count as 1

Reinforces:

- Accumulators
- Conditional calculations
- Multiple Aces
- Separating representation from calculation

Goal: correctly value ordinary hands, face cards, soft hands, and hands with
multiple Aces.

### Phase 4 — Player Turn

Let the player repeatedly choose hit or stand.

Reinforces:

- Input validation
- `while` loops
- Changing hand state
- Bust and stopping conditions

Goal: the player's turn ends only after standing or busting.

### Phase 5 — Dealer Turn

Have the dealer draw automatically until reaching at least 17.

Reinforces:

- Automated decisions
- Reusing draw and hand-value functions
- Separating player behavior from dealer behavior

Goal: the dealer follows one consistent rule without user input.

### Phase 6 — Determine the Outcome

Compare the completed hands and report a win, loss, or tie.

Reinforces:

- Ordering conditional rules
- Handling busts before comparing totals
- Returning a useful result instead of only printing

Goal: every completed round produces one correct outcome.

### Phase 7 — Repeated Games and Bankroll

Allow repeated rounds and optionally add betting after the core game is stable.

Reinforces:

- One-round versus whole-game responsibilities
- State across rounds
- Validation against a current bankroll
- Function orchestration

Goal: the game can continue cleanly without mixing deck, hand, and bankroll
state between rounds.

## Definition of Success

The project is successful when the learner can explain:

- How a card is represented
- How the deck is built, shuffled, and reduced as cards are drawn
- How player and dealer hands change independently
- How hand values and Aces are calculated
- Why each turn continues or stops
- How the outcome is determined
- How data moves between the major functions

Completing the advanced casino rules is not required for Version 1.

