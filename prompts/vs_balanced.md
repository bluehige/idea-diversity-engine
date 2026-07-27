# VS Balanced Portfolio Prompt

Create a balanced portfolio across the response distribution.

For five candidates, target:

- one conventional/head candidate,
- two mid-distribution candidates,
- two plausible tail candidates.

Treat these bands as exploration guidance, not a reason to invent false numeric precision. Every candidate must satisfy the hard constraints and pass a minimum usefulness check.

Use the common candidate schema. Do not force values to sum to 1.
