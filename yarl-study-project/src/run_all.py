import sys

from demo_basics import run as run_basics
from demo_idn_fragment import run as run_idn_fragment
from demo_join_update import run as run_join_update
from demo_paths import run as run_paths
from demo_queries import run as run_queries


def main() -> None:
    # Avoid UnicodeEncodeError in Windows terminals with legacy code pages.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("yarl-study-project: запуск всех учебных примеров")
    run_basics()
    run_queries()
    run_paths()
    run_join_update()
    run_idn_fragment()


if __name__ == "__main__":
    main()
