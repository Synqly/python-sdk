# Ticketing Connector Example

This example demonstrates how to use the Ticketing Connector to create and query tickets. It uses
Jira as an example provider, though can work with a mock ticketing provider as well if you do not
have a Jira account.

## Prerequisites

- Synqly Organization Access Token
- For Jira usage:
  - Jira account
  - Jira API token
  - Jira site URL

## Usage

To run the example with the mock provider, use the following command from the root of the repository:

```bash
python3 examples/ticketing-connector/main.py  --project-key $PROJECT_KEY --synqly-org-token $SYNQLY_ORG_TOKEN
```

Where `PROJECT_KEY` is the id of the project you want to create a ticket in and `SYNQLY_ORG_TOKEN` is
your Synqly organization access token.

To run the example with Jira, use the following command:

```bash
python3 examples/ticketing-connector/main.py --jira-url {value} --jira-username {value} --jira-token {value} --project-key $PROJECT_KEY --synqly-org-token $SYNQLY_ORG_TOKEN
```
