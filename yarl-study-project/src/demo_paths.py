from yarl import URL


def run() -> None:
    print("\n=== DEMO 3: Пути и безопасная сборка ===")
    base = URL("https://example.com/api")

    users = base / "v1" / "users"
    user_profile = users / "john doe"

    print("base:", base)
    print("users:", users)
    print("user_profile (пробелы кодируются):", user_profile)
    print("decoded path:", user_profile.path)
    print("raw path:", user_profile.raw_path)


if __name__ == "__main__":
    run()
