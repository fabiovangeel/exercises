import pytest
from datetime import date, timedelta
from calenders import CalendarStub
from tasks import Task, TaskList


@pytest.fixture
def today():
    return date(2005, 1, 12)


@pytest.fixture
def future(today):
    return today + timedelta(2)


@pytest.fixture
def past(today):
    return today - timedelta(2)


@pytest.fixture
def cal(today):
    return CalendarStub(today)


@pytest.fixture
def taskl(cal):
    return TaskList(cal)


def test_creation(taskl):
    assert 0 == len(taskl)
    assert [] == taskl.due_tasks
    assert [] == taskl.finished_tasks
    assert [] == taskl.overdue_tasks


def test_adding_task_with_due_day_in_future(taskl, future):

    task = Task("Study", future)

    taskl.add_task(task)

    assert 1 == len(taskl)
    assert [task] == taskl.due_tasks
    assert [] == taskl.finished_tasks
    assert [] == taskl.overdue_tasks


def test_adding_task_with_due_day_in_past(taskl, past):

    task = Task("Study", past)

    with pytest.raises(RuntimeError):
        taskl.add_task(task)


def test_task_becomes_overdue(taskl, future, cal):
    next_week = date(2005, 1, 15)
    task = Task('description', future)
    taskl.add_task(task)

    cal.today = next_week

    assert [task] == taskl.overdue_tasks


def test_task_becomes_finished(taskl, future):
    task = Task("Study", future)
    taskl.add_task(task)

    task.finished = True

    assert [task] == taskl.finished_tasks
    assert [] == taskl.due_tasks
