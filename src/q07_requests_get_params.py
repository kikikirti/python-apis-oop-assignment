import requests
import json

URL = "https://jsonplaceholder.typicode.com/comments"

def main():
    params = {"postId": 1}
    resp = requests.get(URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print("Count:", len(data))
    print("First 2:")
    print(json.dumps(data[:2], indent=2))

if __name__ == "__main__":
    main()
