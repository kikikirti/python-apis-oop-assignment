import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

def main():
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print("JSON:", data)
    print("Title:", data.get("title"))

if __name__ == "__main__":
    main()
