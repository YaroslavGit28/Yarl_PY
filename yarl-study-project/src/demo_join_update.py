from yarl import URL


def run() -> None:
    print("\n=== DEMO 4: join и with_* методы ===")
    root = URL("https://docs.example.com/base/")
    relative = URL("guide/start.html")
    joined = root.join(relative)

    print("root:", root)
    print("relative:", relative)
    print("joined:", joined)

    original = URL("http://old.example.com/path?a=1#old")
    modified = (
        original.with_scheme("https")
        .with_host("new.example.com")
        .with_path("/new/path")
        .with_fragment("section-2")
    )

    print("\nОригинал (не изменился):", original)
    print("Новый URL после цепочки with_*:", modified)


if __name__ == "__main__":
    run()
