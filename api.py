import frappe

@frappe.whitelist(allow_guest=False, methods=["POST"])
def get_hello_world():
  frappe.db.error_log('Webhook Triggered 1')
  return "Hello World"

@frappe.whitelist(allow_guest=True, methods=["POST"])
def create_user():
  frappe.db.error_log('Webhook Triggered 2')
  return 'User Created'