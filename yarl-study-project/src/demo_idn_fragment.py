from yarl import URL


def run() -> None:
    print("\n=== DEMO 5: IDN, кодирование и fragment ===")
    url = URL("https://пример.рф/каталог/товар?цвет=синий#описание")

    print("Пользовательское представление:", url)
    print("host:", url.host)
    print("human_repr:", url.human_repr())
    print("raw_host (punycode):", url.raw_host)
    print("raw_path:", url.raw_path)
    print("fragment:", url.fragment)


if __name__ == "__main__":
    run()
