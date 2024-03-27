# Structural pattern matching

* Pattern matching statement to Python, inspired by similar syntax found in Scala, Erlang, and other languages.

* A match statement compares a value (the subject) to several different shapes (the patterns) until a shape fits.

* Each pattern describes the type and structure of the accepted values as well as the variables where to capture its
  contents.

* Syntactically, a match statement contains:
    * a subject expression
    * one or more case clauses

* Each case clause specifies:
    * a pattern (the overall shape to be matched)
    * an optional “guard” (a condition to be checked if the pattern matches)
    * a code block to be executed if the case clause is selected

* The match statement tries to match a single subject to each of the patterns in its case clauses.
  At the first successful match to a pattern in a case clause the variables in the pattern are assigned, and a
  corresponding block is executed.
  Each case clause can also specify an optional boolean condition, known as a guard.

```python
    match subject:  # Subject
    # Patterns
    case ...
```

## Sources

* [PEP 622 – Structural Pattern Matching](https://peps.python.org/pep-0622/)
* [PEP 634 – Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)
* [PEP 635 – Structural Pattern Matching: Motivation and Rationale](https://peps.python.org/pep-0635/)
* [PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)