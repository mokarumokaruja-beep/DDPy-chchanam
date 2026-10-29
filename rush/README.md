# Rush00

## 1. Interactive Menu and User Input
- Contain at least 4 main menu. (excluding Exit)
- Receive meaningful user input with `input()` and display result with `print()`.
- Keep the application running until the user choose to exit.

## 2. Data Structure and Data Management
- Use at least `one list` and `one dict` to manage the application data.
- Support multiple records or objects, not just a single saved value.
- Allow users to `add`, `view`, `update` or `remove` records.

## 3. Conditional Logic and Decision Making
- use `if`, `elif` and `else` for program decisions.
- Implement `at least three meaningful rules` or validations that `change the outcome of a user action`.
- Examples: prevent duplicate bookings, reject insufficient funds, check schedule conflicts,
or reject unavailable items.


## 4. Loops and Iteration
- Use `both for and while` in meaningful ways.
- Iterate over stored data and return to the menu after completing an action.
- Avoid unintended infinite loops.

## 5. Functions and Program Organization
- Define and use at least four custom functions with def.
- At least two functions must accept parameters.
- At least one function must return a meaningful value using return.
- Divide responsibilities into functions rather than placing everything in a single block.

## 6. Algorithm and Data Processing
- Implement at least two meaningful operations on stored data.
- Examples: conditional search, sorting, totals or averages, conflict detection, or finding
maximum/minimum values.
- The operations must be relevant to your chosen application and demonstrate actual data
processing.

## 7. Input Validation and Error Handling
- Handle invalid menu choices and unexpected input types.
- Reject invalid values, for example negative quantities, when inappropriate.
- Handle searches or actions on records that do not exist.
- After an invalid entry, return control to the user without crashing.

## 8. Functional Application
- The application must have a clear purpose and complete working features.
- Demonstrate a meaningful start-to-finish workflow, including data changes and results.
- The required features must work without unhandled errors during normal and
invalid-input tests.
- Each teammate must explain the logic, data structures, functions, and validation choices.

```
Reminder: Passing the Rush requires all eight mandatory categories. Bonus
features never replace missing mandatory requirements.
```

Example: a possible application workflow

```
===== MY PYTHON APPLICATION =====
1. Add Record
2. View Records
3. Update Record
4. Search and Summary
5. Exit
Choose: 1
Enter record name: Example
Record added successfully!
Choose: 4
Matching records: 1
Choose: 5
Goodbye!
```

This output is an illustration only. Your team must create its own menu, domain logic, and working
implementation.