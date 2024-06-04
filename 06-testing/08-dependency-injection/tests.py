import pytest
from datetime import datetime, timedelta
from tasks import Task, TaskList
from calenders import *


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
