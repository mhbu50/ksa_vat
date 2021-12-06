import frappe
from ksa_vat.events.accounts.sales_invoice import create_qr_code, delete_qr_code_file


def execute():
    invoices = frappe.db.get_all("Sales Invoice", {
        "posting_date": [">=", "01-11-2021"]
    })

    for record in invoices:
        doc = frappe.get_doc("Sales Invoice", record.name)
        delete_qr_code_file(doc)
        create_qr_code(doc)
