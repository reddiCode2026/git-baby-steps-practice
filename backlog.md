# Weekly Status Report Generator Backlog

## Planning Decisions

- MVP-first priority: deliver a working end-to-end report before hardening and polish.
- Phases may overlap when dependencies permit; keep the end-to-end happy path visible throughout implementation.
- Initial metrics denominator: all open and recently completed project issues in scope for the report.
- If Jira cannot provide a flagged timestamp, render the blocker duration as `unknown`.
- v1 remains manual, single-project, rolling 7-day, Markdown-only, and local-file based.

## Setup

- [ ] Review the existing `module03-task` calculator scaffold and define the replacement module layout without changing unrelated workspace files.
- [ ] Add a dependency manifest or installation instructions for the Jira HTTP client, environment loader, and test tooling selected for the implementation.
- [ ] Add `.env.example` with placeholder values for `JIRA_SITE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, and `JIRA_PROJECT_KEY`.
- [ ] Confirm `.gitignore` excludes `.env` and `.env.*`, and verify that no real credentials are tracked.
- [ ] Create the `reports/` output directory and keep generated dated reports separate from source code.
- [ ] Define shared configuration constants for the rolling window, RAG expected-pace threshold (default `70%`), and project key.
- [ ] Establish a test layout for unit tests, API/client tests, report rendering tests, and end-to-end tests.
- [ ] Add a small fixture dataset representing completed, in-progress, blocked, unestimated, and empty-result Jira issues.

## Core Features

### Configuration and CLI

- [ ] Implement environment loading and validation for the four required Jira settings.
- [ ] Implement the manual entry point `generate_status_report.py` so `python generate_status_report.py` runs one report generation.
- [ ] Fail before any API request when required configuration is missing, with a clear actionable message.
- [ ] Normalize the Jira site URL and construct the Jira Cloud REST API base URL consistently.
- [ ] Calculate the rolling 7-day date range from the run date and use it in queries and report headings.

### Jira Data Access

- [ ] Implement authenticated Jira Cloud REST API access using email plus API token.
- [ ] Add a reusable search helper for `/rest/api/3/search` with JQL, pagination, requested fields, and response validation.
- [ ] Implement the completed-items JQL using `statusCategory = Done AND resolved >= -7d`.
- [ ] Implement the in-progress/at-risk JQL using `statusCategory = "In Progress"`.
- [ ] Implement the blocker JQL using the flagged impediment or `blocked` label signals, excluding Done issues.
- [ ] Request only the fields required for issue keys, summaries, issue types, statuses, story points/estimates, labels, flags, and timestamps.
- [ ] Normalize Jira responses into internal issue records so report logic does not depend on raw API payloads.
- [ ] Handle pagination so large projects do not silently produce incomplete sections.
- [ ] Add safe extraction for missing, null, or differently named story-point fields.
- [ ] Add a changelog/timestamp lookup only when available for deriving blocker age; otherwise preserve `unknown` duration.

### Metrics and RAG Logic

- [ ] Define the project-scope issue set used for metrics as open plus recently completed issues for the configured project.
- [ ] Calculate completed story points, total in-scope story points, percentage complete, and To Do/In Progress/Done counts.
- [ ] Define how missing story-point estimates are excluded from point totals and represented in the report.
- [ ] Calculate RAG status deterministically: any blocker is Red; otherwise below the configurable 70% threshold is Amber; otherwise Green.
- [ ] Generate a one-line rationale that names the controlling condition, including blocker presence or completion percentage.
- [ ] Ensure zero-point and empty-result cases do not cause division-by-zero or misleading percentages.

### Markdown Report Generation

- [ ] Render the header with project name/key, rolling week date range, and generation date.
- [ ] Render the Overall Health section with the computed Red/Amber/Green indicator and rationale.
- [ ] Render Completed This Week with issue key, summary, and issue type, or an explicit `None` placeholder.
- [ ] Render In-Progress / At-Risk Items with key, summary, status, and story points/estimate, or `None`.
- [ ] Render Blockers / Impediments with key, summary, and blocker duration; use `unknown` when duration is unavailable, or `No blockers reported.` when empty.
- [ ] Render Metrics Summary with points completed versus total in scope, percentage complete, and status counts.
- [ ] Preserve the required section order and produce valid readable Markdown.
- [ ] Write only after all Jira calls, calculations, and rendering succeed.
- [ ] Save each report to `reports/status_report_<YYYY-MM-DD>.md` without overwriting prior dates.

## Integration

- [ ] Connect configuration loading, Jira client calls, issue normalization, metrics/RAG calculation, Markdown rendering, and dated file writing through the CLI entry point.
- [ ] Verify the API request uses the configured project key and rolling 7-day window rather than a hard-coded project or sprint.
- [ ] Verify all three report queries use the expected JQL and that results are mapped to the correct sections.
- [ ] Verify the metric issue set and section issue sets are combined without duplicate counting.
- [ ] Add a dry-run or injected-client path for integration tests so tests do not require live Jira credentials.
- [ ] Run one authorized local report against Jira using a real `.env` without exposing credentials in logs or generated output.
- [ ] Confirm successful output appears in `reports/` and a second run on a different date preserves the earlier report.
- [ ] Confirm API failures, authentication failures, malformed responses, and missing configuration exit nonzero and create no partial report.

## Testing

### Unit Tests

- [ ] Test environment validation for complete, missing, and malformed configuration.
- [ ] Test rolling date-range and dated filename generation around month/year boundaries.
- [ ] Test JQL construction with a normal project key and reject unsafe/invalid project-key input as appropriate.
- [ ] Test Jira response normalization with complete fields, missing estimates, null values, and unexpected status data.
- [ ] Test metrics for normal estimates, zero totals, missing estimates, no issues, and mixed status categories.
- [ ] Test RAG rules for blockers, below-threshold completion, exactly-threshold completion, and above-threshold completion.
- [ ] Test blocker duration formatting for a derivable timestamp and `unknown` fallback.
- [ ] Test each Markdown section for populated and empty results, including required placeholders.
- [ ] Test that report rendering escapes or safely formats issue text that contains Markdown-sensitive characters.

### API and Integration Tests

- [ ] Mock successful paginated Jira search responses and verify all pages are consumed.
- [ ] Mock non-2xx responses and authentication failures and verify clear errors with no output file.
- [ ] Mock malformed or incomplete API payloads and verify controlled handling.
- [ ] Run an end-to-end test with fixture responses and assert the complete report structure, RAG status, metrics, and output path.
- [ ] Run the test suite from the project directory using the documented command.

## Documentation

- [ ] Replace the calculator-focused README content with setup, configuration, and usage instructions for the status report generator.
- [ ] Document Python version, dependency installation, `.env` setup, and the manual execution command.
- [ ] Document the rolling 7-day scope, single-project limitation, query behavior, and generated report naming.
- [ ] Document the metrics denominator decision, treatment of missing estimates, and 70% RAG threshold.
- [ ] Document that blocker duration may display as `unknown` when Jira history does not expose a usable timestamp.
- [ ] Document expected error behavior and confirm failed runs do not write partial reports.
- [ ] Add a sample or fixture-based example of the generated Markdown report without real Jira data or credentials.
- [ ] Record v1 exclusions and future enhancements from the specification so out-of-scope requests remain explicit.
- [ ] Perform a final onboarding pass from a clean environment and update instructions for any missing step.

## Definition of Done

- [ ] A PM can configure local Jira credentials and generate one dated Markdown report with the documented command.
- [ ] The report contains every required section in the specified order, including explicit empty-result placeholders.
- [ ] RAG status, metrics, blocker handling, and rolling-window behavior are covered by automated tests.
- [ ] Jira/auth/API failures leave no partial report behind and provide an actionable error.
- [ ] Tests pass and documentation enables a new contributor to run the generator without access to committed secrets.