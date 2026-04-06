# yarl-study-project

Учебный проект по библиотеке `yarl` для Python.

Цель: показать на понятных примерах, как работать с URL как со структурированным объектом, а не строкой.

## Что внутри

- `src/run_all.py` — единая точка запуска всех демо;
- `src/demo_basics.py` — базовая работа с `URL`;
- `src/demo_queries.py` — чтение и изменение query-параметров;
- `src/demo_paths.py` — работа с путями и безопасная сборка URL;
- `src/demo_join_update.py` — методы `join`, `with_*` и иммутабельность;
- `src/demo_idn_fragment.py` — домены IDN, кодирование и фрагменты;
- `wiki/` — полная учебная wiki со схемами и пояснениями.

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/run_all.py
```

## Почему именно yarl

- меньше ошибок от ручной конкатенации строк;
- удобное API для query, path и частей URL;
- предсказуемая иммутабельность: методы возвращают новый объект URL.

Подробное руководство: `wiki/Home.md`.
