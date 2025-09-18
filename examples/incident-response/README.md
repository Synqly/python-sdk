# Synqly Python SDK PagerDuty Incident Response Example

This example demonstrates how to use the Synqly Python SDK to create a PagerDuty incident response integration.

## Prerequisites

- A Synqly organization token
- A PagerDuty API token with appropriate permissions
- A PagerDuty service ID (optional - for ticketing actions)
- Email address of a valid PagerDuty user (optional - for ticketing actions)

## Usage

### Full Example (with ticketing actions):
```bash
python main.py \
  --synqly-org-token YOUR_ORG_TOKEN \
  --pagerduty-token YOUR_PAGERDUTY_TOKEN \
  --service-id YOUR_SERVICE_ID \
  --creator-email YOUR_PAGERDUTY_USER_EMAIL
```

### Basic Example (incident response actions only):
```bash
python main.py \
  --synqly-org-token YOUR_ORG_TOKEN \
  --pagerduty-token YOUR_PAGERDUTY_TOKEN
```

**Note**: The `--pagerduty-token` is required to create the PagerDuty integration. The `--service-id` and `--creator-email` arguments are optional. If provided, the script will run both incident response actions and ticketing actions. If omitted, only incident response actions will be performed.

## What it does

This example will:
1. Create a Synqly account and integration for PagerDuty

### Always performed (Incident Response Actions):
2. Query PagerDuty escalation policies
3. Display on-call agents for the first escalation policy

### Conditionally performed (Ticketing Actions - requires optional arguments):
4. Create a sample incident in PagerDuty
5. Query incident details
6. Query all incidents
7. Update the incident status to "acknowledged" then "resolved"

### Cleanup:
8. Clean up the created Synqly resources

### Required for all operations:
- PagerDuty API URL (defaults to https://api.pagerduty.com)
- Authentication token

### Required for ticketing actions:
- Service ID
- Creator email address
