import requests

def fetch_data(url: str) -> None:
    try:
        resp = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        print("Connection error: could not reach the server.")
        return
    except requests.exceptions.Timeout:
        print("Timeout: the request took too long.")
        return
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

    code = resp.status_code
    if code == 200:
        print("Success")
    elif 400 <= code <= 499:
        print("Client Error")
    elif 500 <= code <= 599:
        print("Server Error")
    else:
        print(f"Unexpected status code: {code}")

if __name__ == "__main__":
    print("Test 200:")
    fetch_data("https://jsonplaceholder.typicode.com/posts/1")
    print("\nTest 404:")
    fetch_data("https://jsonplaceholder.typicode.com/invalid")
    print("\nTest invalid host:")
    fetch_data("http://does-not-exist.example")
