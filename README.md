\*\*\*\*\*\***CONFIDENTIAL**\*\*\*\*\*\*

# Synqly Python SDK

This repository contains the `SynqlyPythonClient` package, which can be used to integrate a Python application with Synqly APIs. 

The Python Pydantic type checker can, in cases, be stricter than other SDKs. If you run into any type resolution errors such as the following, please report them on Slack and we'll work on patching it as quickly as possible.

```
Error configuring event logging for Tenant XYZ: 1 validation error for ProviderConfig_Siem
config
  none is not an allowed value (type=type_error.none.not_allowed)
```

# SDK Access

Access to this repository is currently restricted to authenticated users, necessitating a couple extra steps in order to use the packages locally. The steps in this section will cover how to configure access to `github.com/Synqly/python-sdk` for use in your application.

## Configure Github credentials

In order for `pip` to successfully pull `github.com/Synqly/python-sdk`, your local machine must be able to authenticate with Github. The two most common ways to authenticate are through either a Github Personal Access Token or an SSH key linked to a Github account. The following sections describe the local configuration for both methods.

If your local machine is already configured to authenticate as the Github user which has been granted access to `github.com/Synqly/python-sdk`, you can skip to Step 2.

### Github Personal Access Token (PAT)

This section describes how to use a Github Personal Access Token (PAT) to pull `github.com/Synqly/python-sdk`. The method below relies on Git's built-in [gitcredentials](https://git-scm.com/docs/gitcredentials) to cache a PAT for use with `go mod`.

First, attempt to install `github.com/Synqly/python-sdk` using `pip3`:

```bash
pip3 install git+https://github.com/Synqly/python-sdk.git
```

If the system is not already authenticated to pull from Github, it should prompt for a Username, then a Password. The Password field expects a Personal Access Token.

```bash
# pip3 install output
Defaulting to user installation because normal site-packages is not writeable
Collecting git+https://github.com/Synqly/python-sdk.git
  Cloning https://github.com/Synqly/python-sdk.git to /private/var/folders/hj/10ls64s54t70qw25nxhnc62m0000gn/T/pip-req-build-zn2q0gan
  Running command git clone --filter=blob:none --quiet https://github.com/Synqly/python-sdk.git /private/var/folders/hj/10ls64s54t70qw25nxhnc62m0000gn/T/pip-req-build-zn2q0gan
Username for 'https://github.com': <MY_USER_NAME>
Password for 'https://<MY_USER_NAME>@github.com': <PAT_VALUE>
  Resolved https://github.com/Synqly/python-sdk.git to commit 7af56ac31a18057d5c8be1513c5b0e29029b2d52
```

Enter a Username and Token value for the Github user that has been granted access to Synqly's python-sdk. This will cache the provided values using git's credential helper, making them available for future `pip3` installations.

If the authentication values provided are valid, the `SynqlyPythonClient` package should install successfully.

```bash
# git clone output
  Resolved https://github.com/Synqly/python-sdk.git to commit 7af56ac31a18057d5c8be1513c5b0e29029b2d52
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
# Requirements checking omitted for brevity
Building wheels for collected packages: SynqlyPythonClient
  Building wheel for SynqlyPythonClient (pyproject.toml) ... done
  Created wheel for SynqlyPythonClient: filename=synqlypythonclient-0.1.9-py3-none-any.whl size=1006869 sha256=5ed337a30d0552c711804aba0cc0417af8d0630c5328b7c9f664437bd29be3de
  Stored in directory: /private/var/folders/hj/10ls64s54t70qw25nxhnc62m0000gn/T/pip-ephem-wheel-cache-4aczn76o/wheels/58/20/4a/37a5d1b47dd7ce3ae002f7967be9f674d458f43294bb5d6667
Successfully built SynqlyPythonClient
Installing collected packages: SynqlyPythonClient
Successfully installed SynqlyPythonClient-0.1.9
```

### SSH Key

This section describes how to to use an SSH key when installing `github.com/Synqly/python-sdk`. This section assumes you have already followed Github's [Generate a new SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and [Add a New SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) guides. 

Once local SSH authentication with Github is configured, install `github.com/Synqly/python-sdk` by formatting the pip3 command to use SSH. 

Note that installing a pip package over SSH requires a username be set, thus we add `git@` as a preface to the repository url.

```bash
pip3 install git+ssh://git@github.com/Synqly/python-sdk.git
```

## Requirements.txt

Adding `github.com/Synqly/python-sdk` to a Python project's `requirements.txt` is very similar to the command line package installations above. The `examples/siem-connector/requirements.txt` file contains examples of how to install the repository using either a Github PAT or an SSH key. 

# Siem Connector Example

The `examples` directory of this repository contains example implementations that demonstrate how to incorporate Synqly SDKs into a Python application.

This section acts as supporting documentation for the sample program in `examples/siem-connector`. The `siem-connector` example demonstrates how to use the Synqly's SIEM Connector to send events to a SIEM Provider (Splunk) from within a multi-tenant application. 

The `siem-connector` example will:

- Define multiple tenants in a sample application
- Define an `Integration` for each tenant (using Splunk as the target SIEM Provider)
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

1. Install `github.com/Synqly/python-sdk` and its dependencies by running the following command:

    ```bash
    pip3 install -r examples/siem-connector/requirements.txt
    ```

2. The example depends on environment variables to connect to Synqly and Splunk. To allow the sample program to connect to Synqly, set the following environment variables to your Organization ID and API Token values.

    ```bash
    export SYNQLY_ORG_ID=<your-org-id>
    export SYNQLY_API_TOKEN=<your-api-token>
    ```

3. Access to Splunk is also configured via environment variable. Set the following variables in your terminal:

    ```bash
    export SPLUNK_URL=https://<your-org>.splunkcloud.com:8088/services/collector/event
    export SPLUNK_TOKEN=<your-splunk-token>
    ```

4. Run the example
    ```bash
    python3 examples/siem-connector/main.py
    ```


# Local Development

While the files under `/src` are auto-generated, it can sometimes be useful to install a local copy of the SDK in order to debug issues such as type mismatches. The following command will install the local version of `SynqlyPythonClient`, overriding the upstream repository. 

```bash
cd ~/python-sdk

pip install -e .
```