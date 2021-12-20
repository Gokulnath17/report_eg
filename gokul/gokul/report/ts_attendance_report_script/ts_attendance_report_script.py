# Copyright (c) 2013, gokulnath and contributors
# For license information, please see license.txt

import frappe
from frappe import _
def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns=get_columns(filters)
	data = get_data(filters)
	return columns,data
def get_columns(filters):
	columns = [
		{
			"fieldname": "ts_emp_id",
			"fieldtype": "Data",
			"label": "Employee_Id"
            
            
        },
		{
			"fieldname": "ts_emp_name",
			"fieldtype": "Data",
			"label": "Employee_name"
		},
		{
			"fieldname": "ts_date",
			"fieldtype": "Date",
			"label": "Date"
		},
		{
			"fieldname": "ts_in_time",
			"fieldtype": "Time",
			"label": "In Time"
		},
		{
			"fieldname": "ts_out",
			"fieldtype": "Time",
			"label": "Out Time"
		}
	]
	return columns

def get_conditions(filters):
	conditions = {}

	if filters.ts_date:
		conditions["ts_date"] = filters.ts_date 
	if filters.ts_emp_name:
		conditions["ts_emp_name"] = filters.ts_emp_name
	return conditions
def get_data(filters):
	data = []
	conditions = get_conditions(filters)
	atten = frappe.db.get_all("ts_Attendance", fields=["ts_date","ts_emp_id","ts_emp_name","ts_in_time","ts_out"],
		filters=conditions,order_by="ts_date")
	for d in atten:
		r = {"ts_date": d.ts_date, "ts_emp_id": d.ts_emp_id, "ts_emp_name": d.ts_emp_name,"ts_in_time":d.ts_in_time,"ts_out":d.ts_out}

		data.append(r)

	return data