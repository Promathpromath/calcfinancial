# Финансовый калькулятор 

Три функции для финансовых расчётов:
- `calculate_simple_interest` — простые проценты
- `calculate_compound_interest` — сложные проценты  
- `calculate_tax` — расчёт налога

При некорректных аргументах вызывают `ValueError`.


## Установка
```bash
uv init
uv add pytest

# Запуск тестов

```bash
uv run pytest           # все тесты
uv run pytest -v        # подробно
