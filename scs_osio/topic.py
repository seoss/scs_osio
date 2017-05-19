#!/usr/bin/env python3

"""
Created on 16 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

workflow:
Use osio_publication instead.

command line example:
./topic.py /orgs/south-coast-science-dev/test/1/status -n "test" -d "test of status" -s 28 -v
"""

import sys

from scs_core.data.json import JSONify

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.data.topic import Topic
from scs_core.osio.data.topic_info import TopicInfo
from scs_core.osio.manager.topic_manager import TopicManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_topic import CmdTopic


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdTopic()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit()

    if cmd.verbose:
        print(cmd, file=sys.stderr)
        sys.stderr.flush()


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit()

    # manager...
    manager = TopicManager(HTTPClient(), api_auth.api_key)

    # check for existing registration...
    topic = manager.find(cmd.path)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        if topic:
            name = topic.name if cmd.name is None else cmd.name
            description = topic.description if cmd.description is None else cmd.description

            # update Topic...
            updated = Topic(None, name, description, topic.is_public, topic.info, None, None)
            manager.update(topic.path, updated)

            topic = manager.find(topic.path)

        else:
            if not cmd.is_complete():
                print("The topic does not exist, and not all fields required for its creation were provided.",
                      file=sys.stderr)
                cmd.print_help(sys.stderr)
                exit()

            info = TopicInfo(TopicInfo.FORMAT_JSON, None, None, None)   # for the v2 API, schema_id goes in Topic

            # create Topic...
            topic = Topic(cmd.path, cmd.name, cmd.description, True, True, info, cmd.schema_id)
            manager.create(topic)

    print(JSONify.dumps(topic))
