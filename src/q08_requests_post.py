import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts"

def main():
    payload = {"title": "OOPs Assignment", "body": "Learning Python requests", "userId": 101}
    resp = requests.post(URL, json=payload, timeout=10)
    print("Status:", resp.status_code)
    try:
        print("JSON:", json.dumps(resp.json(), indent=2))
    except ValueError:
        print("Text:", resp.text)

if __name__ == "__main__":
    main()
