from employee import Employee

def test_default_raise():
    # Create an employee with a starting salary of $100,000.
    emp = Employee('roger', 'maggard', 100000)
    # Give the employee a default raise (assumed to be $5,000).
    emp.give_raise()
    # Assert that the new salary is $105,000.
    expected_salary = 100000 + 5000
    assert emp.salary == expected_salary, (
        f"Expected salary after default raise to be ${expected_salary}, but got ${emp.salary}"
    )

def test_custom_raise():
    # Create an employee with a starting salary of $100,000.
    emp = Employee('roger', 'maggard', 100000)
    # Give the employee a custom raise of $20,000.
    emp.give_raise(20000)
    # Assert that the new salary is $120,000.
    expected_salary = 100000 + 20000
    assert emp.salary == expected_salary, (
        f"Expected salary after custom raise to be ${expected_salary}, but got ${emp.salary}"
    )