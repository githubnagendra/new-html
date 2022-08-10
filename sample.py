import xlsxwriter

workbook = xlsxwriter.Workbook('Excelsheet.txt')
worksheet = workbook.add_worksheet()


row = 10
column = 100

content = ["ankit", "rahul", "priya", "harshita",
					"sumit", "neeraj", "shivam"]


for item in content :


	worksheet.write(row, column, item)

	
	row += 10
	
workbook.close()
