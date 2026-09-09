# Module 10 Completion Report

## Instruction Files
authenticate-jira-cloud.agent.md
create-status-report.agent.md
creating-instructions.agent.md
main.agent.md
python-best-practices.agent.md
run-status-report-cli.agent.md
save-status-report.agent.md

## main.agent.md Contents
# Instruction Catalog

- [`./instructions/create-status-report.agent.md`](./create-status-report.agent.md) â€” Weekly status report in Markdown with fixed sections and concise bullet points.
- [`./instructions/creating-instructions.agent.md`](./creating-instructions.agent.md) â€” Setup, cataloging, and maintenance workflow for project instruction files.
- [`./instructions/save-status-report.agent.md`](./save-status-report.agent.md) â€” Save each generated report as a dated Markdown file without overwriting earlier files.
- [`./instructions/authenticate-jira-cloud.agent.md`](./authenticate-jira-cloud.agent.md) â€” Configure Jira Cloud REST access with email and API token before any API requests.
- [`./instructions/run-status-report-cli.agent.md`](./run-status-report-cli.agent.md) â€” Connect config loading, Jira queries, normalization, metrics, rendering, and dated file output through the CLI entry point.
- [`./instructions/python-best-practices.agent.md`](./python-best-practices.agent.md) â€” Apply Python coding standards for readable, maintainable, and safe code.

## Sample Instruction
- File: authenticate-jira-cloud.agent.md
- Contents:
---
name: authenticate-jira-cloud
description: Configure authenticated Jira Cloud REST API access using email and API token.
---

- Input format:
  + Accept Jira site URL, Jira email address, Jira API token, and optional project key from environment variables or explicit config.
  + Treat the website URL as the base Jira Cloud host such as `https://your-company.atlassian.net`.
  + Require the email and API token to be present before any network call is attempted.
- Processing steps:
  + Validate that `JIRA_SITE_URL`, `JIRA_EMAIL`, and `JIRA_API_TOKEN` are set and non-empty.
  + Normalize the site URL to a consistent Jira Cloud base URL without trailing slashes or duplicate path fragments.
  + Build the HTTP session with `requests.Session()` and set basic authentication using the Jira email and API token.
  + Keep the token in memory only for the request lifetime and never log it or write it to output files.
  + Use the session for `/rest/api/3/...` requests and verify the HTTP response before processing payloads.
  + Raise a clear error on authentication failure, invalid URL, or missing credentials before making a request.
- Output format:
  + Return a configured authenticated session or client object ready to call Jira Cloud endpoints.
  + Preserve the original site URL and project configuration in the client state.
  + Surface a clear success or failure signal without exposing secrets in messages or logs.
- Constraints:
  + Never use username/password authentication for Jira Cloud when email plus API token is required.
  + Never log, print, or persist the API token.
  + Never proceed with API calls when configuration values are missing or malformed.
  + Keep the authentication logic separate from report rendering and business logic.
  + Use the same authenticated client for all Jira Cloud requests to keep behavior consistent.
