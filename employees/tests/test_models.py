import pytest
from employees.models import Department, Employee


@pytest.mark.django_db
def test_department_creation():
    dept = Department.objects.create(name="Engineering")
    assert dept.name == "Engineering"
