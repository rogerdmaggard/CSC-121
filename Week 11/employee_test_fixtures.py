import pytest
from employee import Employee

# Fixture to provide a new Employee instance for each test
@pytest.fixture
def employee():
    return Employee('roger', 'maggard', 100000)

def test_default_raise(employee):
    # Give the employee a default raise (assumed to be $5,000)
    employee.give_raise()
    expected_salary = 100000 + 5000
    assert employee.salary == expected_salary, (
        f"Expected salary after default raise to be ${expected_salary}, but got ${employee.salary}"
    )

def test_custom_raise(employee):
    # Give the employee a custom raise of $20,000
    employee.give_raise(20000)
    expected_salary = 100000 + 20000
    assert employee.salary == expected_salary, (
        f"Expected salary after custom raise to be ${expected_salary}, but got ${employee.salary}"
    )