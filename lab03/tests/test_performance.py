"""Невеликий тест операції для запуску з pytest --durations=5."""
from core import add_module
from model import Module, create_sample_course


def test_repeated_immutable_updates() -> None:
    course = create_sample_course()
    for index in range(100):
        course = add_module(course, Module(index + 10, f"Модуль {index}", 1))
    assert len(course.modules) == 102
