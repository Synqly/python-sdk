# Siem Connector Example

The `examples` directory of this repository contains example implementations that demonstrate how to incorporate Synqly SDKs into a Python application.

This section acts as supporting documentation for the sample program in `examples/siem-connector`. The `siem-connector` example demonstrates how to use the Synqly's SIEM Connector to send events to a SIEM Provider (Splunk) from within a multi-tenant application.

The `siem-connector` example will:

- Define multiple tenants in a sample application
- Define an `Integration` for each tenant (one tenant uses the SIEM Mock Provider and the second uses Splunk as the target SIEM Provider)
- Run a background job to simulate load for each tenant
- Send events from the background job to Synqly
- Demonstrate that events are sent in OCSF format and transformed by Synqly before being forwarded to the target SIEM Provider.


## Prerequisites

- A [Synqly](https://synqly.com) `Organization`
- Your Synqly Organization ID and API Token
- Python 3
- A Splunk account -- [sign up for a free trial](https://www.splunk.com/en_us/download.html)
- A Splunk HTTP Event Collector (HEC) endpoint and API token -- [create a new HEC token](https://docs.splunk.com/Documentation/Splunk/8.1.3/Data/UsetheHTTPEventCollector#Create_an_Event_Collector_token)

## Setup and Run

All commands are run from the root of this SDK repository.

1. Install `github.com/Synqly/python-sdk` and its dependencies by running the following command:

    ```bash
    pip3 install -r examples/siem-connector/requirements.txt
    ```

2. The example depends on environment variables to connect to Synqly and Splunk. To allow the sample program to connect to Synqly, set the following environment variables to your Organization ID and API Token values.

    ```bash
    export SYNQLY_API_TOKEN=<your-api-token>
    ```

3. Access to Splunk is also configured via environment variable. Set the following variables in your terminal:

    ```bash
    export SPLUNK_URL=https://<your-org>.splunkcloud.com:8088/services/collector/event
    export SPLUNK_TOKEN=<your-splunk-token>
    ```

4. Run the example
    ```bash
    python3 examples/siem-connector/main.py --synqly-org-token $SYNQLY_API_TOKEN --splunk-url $SPLUNK_URL --splunk-token $SPLUNK_TOKEN
    ```


# Local Development

While the files under `/src` are auto-generated, it can sometimes be useful to install a local copy of the SDK in order to debug issues such as type mismatches. The following command will install the local version of `SynqlyPythonClient`, overriding the upstream repository.

```bash
cd ~/python-sdk

pip install -e .
```
