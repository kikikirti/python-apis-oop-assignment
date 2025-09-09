def classify_status(code: int) -> str:
    if code == 201:
        return "Created"
    if 200 <= code <= 299:
        return "Success"
    if 400 <= code <= 499:
        return "Client Error"
    if 500 <= code <= 599:
        return "Server Error"
    return "Other"

if __name__ == "__main__":
    codes = [200, 201, 400, 401, 403, 404, 500, 502, 503]
    for c in codes:
        print(c, "->", classify_status(c))
