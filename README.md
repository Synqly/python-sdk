# Synqly Python SDK

This repository contains the `SynqlyPythonClient` SDK package, which can be used to integrate a Python application with Synqly APIs. All Synqly SDKs require a valid Synqly Organization token to use.

If you aren't yet a Synqly customer, please feel free to [Schedule a Demo](https://synqly.com/demo/).

The Python Pydantic type checker can, in cases, be stricter than other SDKs. If you run into any type resolution errors such as the following, please report them on Slack and we'll work on patching it as quickly as possible.

```
Error configuring event logging for Tenant XYZ: 1 validation error for ProviderConfig_Siem
config
  none is not an allowed value (type=type_error.none.not_allowed)
```

# Import the SDK

To install the `SynqlyPythonClient` to your local Python environment, run the following command:

```bash
pip3 install git+https://github.com/Synqly/python-sdk.git
```


You should now be able to import packages from the `SynqlyPythonClient` as follows:

```python
from synqly import engine
from synqly import management as mgmt
```

For more detailed examples of how to use the Synqly Python SDK, please refer to the `examples` directory in this repository. Each sub-directory in `examples` contains a standalone example of how to work with a particular Synqly Connector.

# Local Development

While the files under `/src` are auto-generated, it can sometimes be useful to install a local copy of the SDK in order to debug issues such as type mismatches. The following command will install the local version of `SynqlyPythonClient`, overriding the upstream repository. 

```bash
cd ~/python-sdk

pip install -e .
```