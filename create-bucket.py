#!/usr/bin/env python3

from pprint import pformat, pprint
import argparse
import json
import logging
import os
import requests
import urllib3

INVENIO_URL = "https://localhost:5000"


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    parser = argparse.ArgumentParser(description="Create bucket")
    parser.add_argument("invenio_url", nargs="?", default=INVENIO_URL)
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debugging"
    )
    args = parser.parse_args()

    level = logging.DEBUG if args.debug else logging.WARNING
    logging.basicConfig(format="%(levelname)s: %(message)s", level=level)


    token = os.environ["INVENIO_TOKEN"]

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    data = {"location": "suppressed"}

    api_url = f"{args.invenio_url}/api/files"

    response = requests.post(
        api_url, headers=headers, data=json.dumps(data), verify=False
    )

    pprint(dict(response.headers))
    print(response.text)


if __name__ == "__main__":
    main()