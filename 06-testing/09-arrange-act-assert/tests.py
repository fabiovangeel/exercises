import pytest
from datetime import date, timedelta
from calenders import CalendarStub
from tasks import Task, TaskList


def test_creation():
    today = date(2005, 1, 12)
    cal = CalendarStub(today)

    taskl = TaskList(cal)

    assert 0 == len(taskl)
    assert [] == taskl.due_tasks
    assert [] == taskl.finished_tasks
    assert [] == taskl.overdue_tasks


def test_adding_task_with_due_day_in_future():
    today = date(2005, 1, 12)
    future = today + timedelta(2)
    cal = CalendarStub(today)
    taskl = TaskList(cal)
    task = Task("Study", future)

    taskl.add_task(task)

    assert 1 == len(taskl)
    assert [task] == taskl.due_tasks
    assert [] == taskl.finished_tasks
    assert [] == taskl.overdue_tasks


def test_adding_task_with_due_day_in_past():
    today = date(2005, 1, 12)
    past = today - timedelta(2)
    cal = CalendarStub(today)
    taskl = TaskList(cal)
    task = Task("Study", past)

    with pytest.raises(RuntimeError):
        taskl.add_task(task)


def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)

    calendar.today = next_week

    assert [task] == task_list.overdue_tasks


def test_task_becomes_finished():
    today = date(2005, 1, 12)
    future = today + timedelta(2)
    cal = CalendarStub(today)
    taskl = TaskList(cal)
    task = Task("Study", future)
    taskl.add_task(task)

    task.finished = True

    assert [task] == taskl.finished_tasks
    assert [] == taskl.due_tasks
