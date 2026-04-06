from yarl import URL


def run() -> None:
    print("\n=== DEMO 2: Query-параметры ===")
    url = URL("https://api.example.com/search?q=python&limit=10")

    print("Исходный URL:", url)
    print("query:", dict(url.query))
    print("q:", url.query.get("q"))

    with_single = url.with_query({"q": "yarl tutorial", "limit": 20})
    print("\nwith_query(...) заменяет весь query:")
    print(with_single)

    with_added = with_single.update_query(page=2, sort="desc")
    print("\nupdate_query(...) добавляет/обновляет ключи:")
    print(with_added)

    without_limit = with_added.with_query(
        [(k, v) for k, v in with_added.query.items() if k != "limit"]
    )
    print("\nУдаление параметра limit вручную через новую query-коллекцию:")
    print(without_limit)


if __name__ == "__main__":
    run()
