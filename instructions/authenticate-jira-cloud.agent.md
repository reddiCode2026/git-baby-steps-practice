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
