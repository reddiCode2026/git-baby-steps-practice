"""Generate a Jira status report for a specified project key."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parents[1] / "work" / "module03-task"
sys.path.insert(0, str(PROJECT_DIR))

from generate_status_report import (  # noqa: E402
    Config,
    ConfigurationError,
    JiraApiError,
    JiraClient,
    generate_report,
)


def parse_arguments() -> argparse.Namespace:
    """Parse the Jira project key from the command line."""
    parser = argparse.ArgumentParser(description="Generate a weekly Jira status report.")
    parser.add_argument("project_key", metavar="PROJECT_KEY", help="Jira project key")
    return parser.parse_args()


def main() -> int:
    """Generate and save a report for the requested Jira project."""
    arguments = parse_arguments()
    load_dotenv(PROJECT_DIR / ".env")
    os.environ["JIRA_PROJECT_KEY"] = arguments.project_key.strip().upper()

    try:
        config = Config.from_environment()
        output = generate_report(JiraClient(config), config)
    except (ConfigurationError, JiraApiError, requests.RequestException) as error:
        print(f"Error: {error}")
        return 1

    print(f"Report written to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
