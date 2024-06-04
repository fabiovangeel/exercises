import pytest
from datetime import date, timedelta
from calenders import CalendarStub
from tasks import Task, TaskList


def setup_function():
    global today
    global future
    global past
    global cal
    global taskl

    today = date(2005, 1, 12)
    future = today + timedelta(2)
    past = today - timedelta(2)
    cal = CalendarStub(today)
    taskl = TaskList(cal)


def test_creation():
    assert 0 == len(taskl)
    assert [] == taskl.due_tasks
    assert [] == taskl.finished_tasks
    assert [] == taskl.overdue_tasks


def test_adding_task_with_due_day_in_future():

    task = Task("Study", future)

    taskl.add_task(task)

    assert 1 == len(taskl)
    assert [task] == taskl.due_tasks
    assert [] == taskl.finished_tasks
    assert [] == taskl.overdue_tasks


def test_adding_task_with_due_day_in_past():

    task = Task("Study", past)

    with pytest.raises(RuntimeError):
        taskl.add_task(task)


def test_task_becomes_overdue():
    next_week = date(2005, 1, 15)
    task = Task('description', future)
    taskl.add_task(task)

    cal.today = next_week

    assert [task] == taskl.overdue_tasks


def test_task_becomes_finished():
    task = Task("Study", future)
    taskl.add_task(task)

    task.finished = True

    assert [task] == taskl.finished_tasks
    assert [] == taskl.due_tasks
