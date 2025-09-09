import sys
import json
import requests

VALID_METHODS = {"GET", "POST", "PUT", "DELETE"}

def usage():
    print("Usage:")
    print("  python q12_cli_http_client.py GET <url>")
    print('  python q12_cli_http_client.py POST <url> \'{"k":"v"}\'')

def main(argv):
    # Friendly behavior for smoke tests: no args -> show usage, exit 0
    if len(argv) < 2:
        usage()
        return 0

    method = argv[0].upper()
    url = argv[1]
    body = None

    if method not in VALID_METHODS:
        print(f"Invalid method '{method}'. Choose from {sorted(VALID_METHODS)}.")
        return 2

    if method in {"POST", "PUT"}:
        if len(argv) < 3:
            print(f"{method} requires a JSON body argument.")
            return 3
        raw = argv[2]
        try:
            body = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON body: {e}")
            return 4

    try:
        resp = requests.request(method, url, json=body, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 5

    print("Status:", resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2))
    except ValueError:
        print(resp.text)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
