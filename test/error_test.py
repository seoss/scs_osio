#!/usr/bin/env python3

"""
Created on 30 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
{"error": {"body-params": {"client-id": "disallowed-key", "org-id": "disallowed-key", "owner-id": "disallowed-key"}}}
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth
from scs_core.osio.client.client_excepion import ClientException
from scs_core.osio.manager.device_manager import DeviceManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------
# resource...

api_auth = APIAuth.load_from_host(Host)

if api_auth is None:
    print("APIAuth not available.", file=sys.stderr)
    exit()

print(api_auth)


client_auth = ClientAuth.load_from_host(Host)

if client_auth is None:
    print("ClientAuth not available.", file=sys.stderr)
    exit()

print(client_auth)


http_client = HTTPClient()

manager = DeviceManager(http_client, api_auth.api_key)

print(manager)


# --------------------------------------------------------------------------------------------------------------------
# run...

device = manager.find(api_auth.org_id, client_auth.client_id)

print(device)
print("-")

try:
    manager.update(api_auth.org_id, client_auth.client_id, device)
except ClientException as exc:
    print(JSONify.dumps(exc))