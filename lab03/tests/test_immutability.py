"""Перевірки незмінності та коректності pure updates."""
import pytest

from core import add_module, add_tag, rename_course, update_setting
from model import Module, create_sample_course


def test_add_module_does_not_mutate_original() -> None:
    course = create_sample_course()
    original_modules = course.modules
    updated = add_module(course, Module(3, "Практика", 4))
    assert course.modules is original_modules
    assert len(course.modules) == 2
    assert len(updated.modules) == 3
    assert updated is not course


def test_add_tag_returns_new_course() -> None:
    course = create_sample_course()
    updated = add_tag(course, "новий")
    assert "новий" not in course.tags
    assert "новий" in updated.tags
    assert updated is not course


def test_mapping_proxy_is_read_only() -> None:
    course = create_sample_course()
    with pytest.raises(TypeError):
        course.settings["level"] = "змінено"  # type: ignore[index]


def test_setting_update_is_pure() -> None:
    course = create_sample_course()
    updated = update_setting(course, "level", "поглиблений")
    assert course.settings["level"] == "початковий"
    assert updated.settings["level"] == "поглиблений"
    assert updated is not course


def test_module_is_hashable() -> None:
    first = Module(1, "Основи Python", 8)
    second = Module(2, "Тестування", 6)
    assert len({first, second}) == 2


def test_course_hashability_limitation_is_documented() -> None:
    # MappingProxyType є read-only, але не хешується; тому Course не є hashable.
    course = create_sample_course()
    with pytest.raises(TypeError):
        hash(course)


def test_rename_course() -> None:
    course = create_sample_course()
    updated = rename_course(course, "Новий курс")
    assert course.title == "Функціональне програмування"
    assert updated.title == "Новий курс"
