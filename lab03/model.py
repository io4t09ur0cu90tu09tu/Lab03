"""Незмінна предметна модель навчальних курсів (варіант 11)."""
from dataclasses import dataclass, replace
from types import MappingProxyType
from typing import Mapping


@dataclass(frozen=True, slots=True)
class Module:
    """Навчальний модуль курсу."""
    id: int
    title: str
    hours: int
    description: str = ""


@dataclass(frozen=True, slots=True)
class Course:
    """Навчальний курс із незмінними вкладеними колекціями."""
    id: int
    title: str
    instructor: str
    modules: tuple[Module, ...]
    tags: frozenset[str]
    settings: Mapping[str, str]

    def total_hours(self) -> int:
        return sum(module.hours for module in self.modules)

    def add_module(self, module: Module) -> "Course":
        return replace(self, modules=self.modules + (module,))

    def add_tag(self, tag: str) -> "Course":
        return replace(self, tags=self.tags | frozenset({tag}))

    def with_setting(self, key: str, value: str) -> "Course":
        updated = dict(self.settings)
        updated[key] = value
        return replace(self, settings=make_settings(**updated))


def make_settings(**kwargs: str) -> Mapping[str, str]:
    """Створює незалежну read-only копію налаштувань."""
    return MappingProxyType(dict(kwargs))


def create_sample_course() -> Course:
    """Початковий приклад курсу для демонстрації та тестів."""
    modules = (
        Module(1, "Вступ до Python", 8, "Основи синтаксису та типів даних"),
        Module(2, "Функціональне програмування", 10, "Чисті функції та композиція"),
    )
    return Course(
        id=11,
        title="Функціональне програмування",
        instructor="Сергій Андрійович",
        modules=modules,
        tags=frozenset({"python", "програмування"}),
        settings=make_settings(level="початковий", language="uk", certificate="так"),
    )
