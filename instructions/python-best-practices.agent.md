---
name: python-best-practices
description: Apply Python coding standards for readable, maintainable, and safe code.
---

- Input format:
  + Accept Python code, function bodies, scripts, or modules that need review, writing, or refactoring.
  + Treat the code as a candidate for implementation in a real project environment with a selected Python interpreter.
  + Use the current project context, package constraints, and repository conventions when available.
- Processing steps:
  + Keep the code simple, explicit, and easy to read.
  + Favor clear naming, narrow function scope, and small single-purpose helpers over complex abstractions.
  + Write deterministic logic, validate inputs early, and handle edge cases before returning output.
  + Use type hints and docstrings where they improve clarity, especially for public functions and data models.
  + Prefer standard library solutions before adding new dependencies.
  + Keep imports sorted, remove unused code, and avoid duplicate logic across modules.
  + Validate behavior with the smallest relevant test or execution check before finalizing changes.
  + Ensure script entry points and library code are separated cleanly when both exist.
- Output format:
  + Return corrected or newly written Python code in valid syntax.
  + Keep the result readable, maintainable, and aligned with the surrounding project style.
  + Include only necessary comments or docstrings, and avoid noisy explanation in the code itself.
- Constraints:
  + Do not write code that hides errors or silently suppresses exceptions.
  + Do not add unnecessary dependencies or broad abstractions.
  + Do not mix business logic with environment-specific execution details unless required.
  + Do not accept brittle or magic-value code when a named constant or helper improves clarity.
  + Do not claim correctness without a relevant validation step or test evidence.
