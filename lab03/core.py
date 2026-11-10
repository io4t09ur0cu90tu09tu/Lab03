"""Чисті операції над незмінною моделлю курсу."""
from dataclasses import replace
from typing import Iterable

from model import Course, Module, make_settings


def add_module(course: Course, module: Module) -> Course:
    """Повертає курс із доданим модулем, не змінюючи початковий."""
    return replace(course, modules=course.modules + (module,))


def add_tag(course: Course, tag: str) -> Course:
    """Повертає курс із новою міткою."""
    return replace(course, tags=course.tags | frozenset({tag}))


def update_setting(course: Course, key: str, value: str) -> Course:
    """Повертає курс із оновленим параметром налаштувань."""
    settings = dict(course.settings)
    settings[key] = value
    return replace(course, settings=make_settings(**settings))


def rename_course(course: Course, new_title: str) -> Course:
    """Повертає копію курсу з новою назвою."""
    return replace(course, title=new_title)


def total_hours(course: Course) -> int:
    """Обчислює загальну тривалість усіх модулів."""
    return sum(module.hours for module in course.modules)


def courses_by_tag(courses: Iterable[Course], tag: str) -> tuple[Course, ...]:
    """Відбирає курси з указаною міткою у незмінний кортеж."""
    return tuple(course for course in courses if tag in course.tags)


def longest_courses(courses: Iterable[Course], limit: int = 3) -> tuple[Course, ...]:
    """Повертає limit курсів із найбільшою сумарною тривалістю."""
    if limit < 0:
        raise ValueError("limit не може бути від'ємним")
    return tuple(sorted(courses, key=lambda c: (-c.total_hours(), c.id))[:limit])
