import xlsxwriter
from parser_tass import array
import datetime
 
current_date = datetime.date.today().isoformat()
def writer(parametr):
	print(parametr)
	book = xlsxwriter.Workbook(r"C:\Users\Markel\Desktop\popa.xlsx")
	page = book.add_worksheet("Москва" + current_date)

	row = 0
	column = 0

	page.set_column("A:A", 100)
	page.set_column("B:B", 60)
	page.set_column("C:C", 60)
	page.set_column("D:D", 100)
	page.set_column("E:E", 100)

	for item in parametr():
		page.write(row, column, item[0])
		page.write(row, column+1, item[1])
		page.write(row, column+2, item[2])
		page.write(row, column+3, item[3])
		page.write(row, column+4, item[4])
		row += 1

		book.close()

writer(array)