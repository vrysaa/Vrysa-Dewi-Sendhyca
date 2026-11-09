#tanpa fixture
from employee import Employee


def test_give_default_raise():
    employee = Employee('vrysa', 'sendhyca', 60000)
    employee.give_raise()

    assert employee.annual_salary == 65000


def test_give_custom_raise():
    employee = Employee('vrysa', 'sendhyca', 60000)
    employee.give_raise(10000)

    assert employee.annual_salary == 70000

#menggunakan fixture

import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee('John', 'Smith', 60000)


def test_give_default_raise(employee):
    employee.give_raise()

    assert employee.annual_salary == 65000


def test_give_custom_raise(employee):
    employee.give_raise(10000)

    assert employee.annual_salary == 70000