---
name: save-status-report
description: Save generated Markdown reports as dated files without overwriting prior reports.
---

- Input format:
  + Accept a complete Markdown report body plus the report date in `YYYY-MM-DD` format.
  + Use the report date from the run context or the generated content header when available.
  + Require a valid `reports/` output directory for the final file path.
- Processing steps:
  + Build the output path as `reports/status_report_<YYYY-MM-DD>.md`.
  + Confirm the `reports/` directory exists; create it if missing.
  + Check whether a file already exists for the same date before writing.
  + If the same date already exists, stop with a clear error instead of overwriting it.
  + Write the report only after the full Markdown content is ready and validated.
  + Return the final output path after the file is successfully saved.
- Output format:
  + Save the report as a Markdown file named exactly `status_report_<YYYY-MM-DD>.md`.
  + Keep the file under the `reports/` directory and preserve valid Markdown structure.
  + Store each dated report separately so older files remain available for reference.
- Constraints:
  + Never overwrite prior dated reports for the same date.
  + Never write outside the `reports/` directory.
  + Always use the ISO date format `YYYY-MM-DD` in the filename.
  + Fail clearly and explicitly when a duplicate date is detected.
  + Only write a final report after all content generation and validation succeed.
