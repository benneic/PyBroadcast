# PyRoamz

A Python wrapper for the Roamz internal broadcast API.

## Usage

Set the environment variable `PYBROADCAST_BASE_URL`, check .env.sample for details.

Create a PyBroadcast instance:

    import pybroadcast
    broadcast = pybroadcast.create()
    broadcast.facebook.status()

## Tests

The broadcast api needs to be running for the tests to succeed. Then call:

    make test
