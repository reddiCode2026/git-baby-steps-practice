# Jira Sprint Dashboard — Requirements

## 1. Purpose
Generate a report showing the team's current sprint progress, pulled live from Jira.

## 2. Output Format
- **Static HTML report file** — the script generates a self-contained `.html` file that can be opened manually in a browser (no server required).

## 3. Data Source
- **Jira Cloud REST API**, authenticated via API token (email + `JIRA_API_TOKEN`).
- Sprint data retrieved using JQL search (`/rest/api/3/search`).

## 4. Scope Selection
- User provides a **Project Key** (e.g., `PROJ`) only.
- Script auto-detects the **active sprint** via JQL: `project = PROJ AND sprint in openSprints()`.
- No manual Board ID or Sprint ID lookup required.

## 5. Per-Issue Fields (Standard set)
For each ticket in the sprint, display:
- Issue key
- Summary
- Status
- Assignee
- Story points / estimate
- Issue type (Bug / Story / Task / etc.)
- Priority

## 6. Sprint Summary Metrics
- Status counts (e.g., To Do / In Progress / Done totals)
- Story point burndown: completed points vs. remaining points
- Overall **% complete** metric (based on story points)

## 7. Execution Model
- **Manual run**: user executes `python generate_dashboard.py` whenever a fresh report is needed.
- Script fetches live data from Jira and (re)writes the output HTML file.
- Scheduling (e.g., Task Scheduler) may be added later but is out of scope for v1.

## 8. Project Location
- New standalone folder: `work/jira-dashboard/` (separate from `module03-task`).

## 9. Configuration / Credentials
Required environment variables (to be supplied by user later in a local `.env`, **never committed**):
- `JIRA_SITE_URL` — e.g. `https://yourcompany.atlassian.net`
- `JIRA_EMAIL` — Atlassian account email used with the API token
- `JIRA_API_TOKEN` — Jira API token
- `JIRA_PROJECT_KEY` — e.g. `PROJ`

A `.env.example` with placeholder values will be provided; `.env` will be gitignored.

## 10. Out of Scope (v1)
- Live/auto-refreshing web app
- Scheduled/automated runs
- Per-assignee workload breakdown
- Labels, due dates, last-updated timestamps
- Historical/past-sprint comparison
