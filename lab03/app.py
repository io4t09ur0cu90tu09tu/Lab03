"""Демонстрація роботи з навчальними курсами."""
from core import add_module, add_tag, update_setting
from model import Module, create_sample_course


def main() -> None:
    course = create_sample_course()
    updated = add_module(course, Module(3, "Тестування", 6, "Pytest та перевірка коду"))
    updated = add_tag(updated, "лабораторна")
    updated = update_setting(updated, "level", "середній")

    print(f"Курс: {updated.title}")
    print(f"Кількість модулів: {len(updated.modules)}")
    print(f"Загальна тривалість: {updated.total_hours()} год.")
    print(f"Мітки: {', '.join(sorted(updated.tags))}")
    print(f"Налаштування: {dict(updated.settings)}")
    print(f"Початковий курс не змінено: {len(course.modules)} модулі")


if __name__ == "__main__":
    main()
