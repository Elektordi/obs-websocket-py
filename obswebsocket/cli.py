import argparse
import inspect
import json
import logging
import os
import sys

import obswebsocket
import obswebsocket.requests


def setup_parser():
    parser = argparse.ArgumentParser(
        description="OBS Studio CLI using OBS Websocket Plugin",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(
        help="OBS Commands", title="Recognized commands", dest="command"
    )

    parser.add_argument("--host", default="localhost", help="Hostname to connect to")
    parser.add_argument("--port", default=4444, type=int, help="Port to connect to")
    parser.add_argument(
        "--password",
        default=os.environ.get("OBS_WEBSOCKET_PASS", None),
        help="Password to use. Defaults to OBS_WEBSOCKET_PASS env var",
    )
    parser.add_argument(
        "--debug", default=False, action="store_true", help="Enable debugging output"
    )

    for subclass in obswebsocket.base_classes.Baserequests.__subclasses__():
        # Generate a subcommand for each subclass with argument
        subparser = subparsers.add_parser(subclass.__name__)
        for arg in inspect.getargspec(subclass.__init__).args:
            if arg == "self":
                continue
            # TODO: add defaults and maybe deal with optional args?
            subparser.add_argument(arg)

    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    if not args.command:
        parser.error("No command specified")

    log_level = logging.INFO
    if args.debug:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)

    client = obswebsocket.obsws(args.host, args.port, args.password or "")
    try:
        client.connect()
    except obswebsocket.exceptions.ConnectionFailure as e:
        logging.error(e)
        sys.exit(1)

    for subclass in obswebsocket.base_classes.Baserequests.__subclasses__():
        if subclass.__name__ != args.command:
            continue

        # OK, found which request class we need to instantiate.
        # Now let's populate the arguments if we can
        command_args = []
        for arg in inspect.getfullargspec(subclass.__init__).args:
            if arg == "self":
                continue
            val = args.__dict__.get(arg)
            if val.startswith("json:"):
                # Support "objects" by parsing JSON strings if the argument is
                # prefixed with "json:"
                val = json.loads(val[5:])
            else:
                # Try to convert numbers from string
                try:
                    val = int(val)
                except ValueError:
                    pass
            command_args.append(val)

        # Instantiate the request class based on collected args
        instance = subclass(*command_args)
        ret = client.call(instance)
        if not ret.status:
            # Call failed let's report and exit
            logging.error("Call to OBS failed: %s", ret.datain["error"])
            client.disconnect()
            sys.exit(1)

        print(json.dumps(ret.datain, indent=4))

    client.disconnect()


if __name__ == "__main__":
    main()
