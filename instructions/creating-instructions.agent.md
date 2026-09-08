---
name: creating-instructions
description: Create and maintain project instruction files and agent workflows.
---

- Place reusable workflows in `./instructions` as `.agent.md` files.
- Keep each file focused on one SDLC task or workflow.
- Use the catalog in `./instructions/main.agent.md` to list each instruction with a one-line description.
- Name files with verb-first hyphenated names such as `create-status-report.agent.md`.
- Use bullet-point rules and avoid long explanations.
- Keep instructions tool-agnostic and platform-safe.
- When adding a new instruction, add its reference to the main catalog.
- When updating an instruction, read the existing version first and make targeted edits.
- Prefer reusable sub-instructions over duplicated logic.
- For VS Code + Copilot, add `.github/copilot-instructions.md` and `.vscode/settings.json` entries that load the catalog on every prompt.
- For fallback automation, keep `AGENTS.md` in the project root with the same entry-point guidance.
