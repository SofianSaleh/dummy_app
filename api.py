import frappe

@frappe.whitelist(allow_guest=False, methods=["POST"])
def get_hello_world():
    return "Hello World"

@frappe.whitelist(allow_guest=True, methods=["POST"])
def create_user():
    return 'User Created'