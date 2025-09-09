import requests
import json

PUT_URL = "https://jsonplaceholder.typicode.com/posts/1"
DEL_URL = "https://jsonplaceholder.typicode.com/posts/1"

def do_put():
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    resp = requests.put(PUT_URL, json=payload, timeout=10)
    print("PUT JSON:", json.dumps(resp.json(), indent=2))
    return resp.status_code

def do_delete():
    resp = requests.delete(DEL_URL, timeout=10)
    return resp.status_code

if __name__ == "__main__":
    print("PUT status:", do_put())
    print("DELETE status:", do_delete())
