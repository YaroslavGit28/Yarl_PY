from yarl import URL


def run() -> None:
    print("\n=== DEMO 1: Базовая работа с URL ===")
    url = URL("https://example.com:8443/api/v1/users?id=42#profile")

    print("Исходный URL:", url)
    print("scheme:", url.scheme)
    print("host:", url.host)
    print("port:", url.port)
    print("path:", url.path)
    print("query_string:", url.query_string)
    print("fragment:", url.fragment)
    print("parts:", url.parts)


if __name__ == "__main__":
    run()
