---
name: run-status-report-cli
description: Orchestrate the CLI pipeline for Jira configuration, data access, metrics, rendering, and dated file output.
---

- Input format:
  + Accept environment variables or explicit arguments for the Jira site URL, email, API token, and project key.
  + Accept a manual CLI invocation from the project root or a test harness that injects a Jira client.
  + Treat the runtime context as a single end-to-end report generation request.
- Processing steps:
  + Load and validate configuration before any Jira request or file write.
  + Construct the authenticated Jira client with the configured email and API token.
  + Fetch the required issue sets for completed work, in-progress work, and blockers using the configured project and rolling 7-day window.
  + Normalize raw Jira payloads into internal issue records and compute metrics/RAG status from those records.
  + Render the Markdown report in the required section order using the metric results and issue summaries.
  + Write the completed report to `reports/status_report_<YYYY-MM-DD>.md` only after all earlier steps succeed.
  + Exit non-zero and leave no partial report behind if configuration, API, parsing, or rendering fails.
- Output format:
  + Produce a valid Markdown status report for the project in the configured dated file path.
  + Keep the final file under `reports/` with a date-based filename that does not overwrite earlier dated reports.
  + Return a clear success or failure result to the CLI without exposing secrets in logs or output.
- Constraints:
  + Never run Jira calls before configuration validation succeeds.
  + Never mix rendering logic with API access or configuration logic.
  + Never overwrite an existing dated report for the same day.
  + Never write partial output files on failure.
  + Keep the CLI entry point as the single orchestration layer that connects all stages together.
