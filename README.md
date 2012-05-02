# PyRoamz

A Python wrapper for the Roamz internal data API.

## Usage

Set the environment variable `PYROAMZ_BASE_URL`, check .env.sample for details.

Create a Roamz instance:

    import pyroamz
    client = pyroamz.create()


## Tests

The data api needs to be running for the tests to run. Then call:

    make test
