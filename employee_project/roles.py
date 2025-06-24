from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'create_employee': True,
        'delete_employee': True,
        'view_sensitive_data': True,
    }


class HR(AbstractUserRole):
    available_permissions = {
        'create_employee': True,
        'edit_employee': True,
        'view_sensitive_data': True,
    }


class Employee(AbstractUserRole):
    available_permissions = {
        'view_own_data': True,
    }
