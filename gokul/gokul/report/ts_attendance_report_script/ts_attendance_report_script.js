// Copyright (c) 2016, gokulnath and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ts Attendance Report Script"] = {
	"filters": [
		{
			fieldname:"ts_date",
			label: __("date"),
			fieldtype: "Date"
		},
		{
			fieldname:"ts_emp_name",
			label: __("Employee Name"),
			fieldtype: "Select",
			options:[
				{ "value": "Gokulnath M", "label": __("GOKULNATH M") },
				{ "value": "Chandana S P", "label": __("CHANDANA S P") },
				{ "value": "Naveen S R", "label": __("NAVEEN S R") }
			]
		}
	]
};
