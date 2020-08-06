# Example 1
import csv
with open('employee_birthday.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department", "birthday month"])
    writer.writerow(["John Smith", "Accounting","November"])
    writer.writerow(["Erica Meyers","IT", "March"])
    writer.writerow(["Jennifer maik","Math","June"])


# Example 2
import csv
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
         if line_count == 0:
              print(f'Column names are {", ".join(row)}')
              line_count += 1
         else:
              print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
              line_count += 1
    print(f'Processed {line_count} lines.\n\n\n')


# Output
# Column names are name, department, birthday month
# John Smith works in the Accounting department, and was born in November.   
# Erica Meyers works in the IT department, and was born in March.
# Jennifer maik works in the Math department, and was born in June.
# Processed 4 lines.


# Example 3
from lxml import etree
#The etree object parses the entire lxml file into a tree structure, with each tag as a branch, and nested tags become its children or branches.

def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)  # read string type file text and convert into XML format using etree.
    book_dict = {}
    books = []
    for book in root.getchildren():  # The .getchildren() accesses the sub-tags within a tree. 
        for elem in book.getchildren():  #The method called on book gives access to the contents of the book (author, genre, etc)
            if elem.text:   # elem.text accesses the text inside each of the tags whereas, tag gives the tag names such as author, price, etc.
                text = elem.text
            else:
                text = ''
            if elem.tag == 'author':
                last_name, first_name = text.split(',')
                print(elem.tag + ':', first_name, last_name)
            else:
                print(elem.tag + ": " + text)
            book_dict[elem.tag] = text
        if book.tag == "book":
            books.append(book_dict) 
            book_dict = {}
    return books

my_books = parseBookXML("books.xml")
# The entire information is collected and stored in a variable my_books.
my_books  # print all data

