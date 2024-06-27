import csv 
import sqlite3 
import sqlalchemy 
csvFile = open("books2.csv", "rt") 
book = csv.DictReader(csvFile, fieldnames = ["first", "last"]) 
book = [row for row in csvFile] 
dataBase = sqlite3.connect("books.db") 
cursor = dataBase.cursor() 
insert = "INSERT INTO books(Title, Author, Year) VALUES(?,?,?)" 
cursor.execute("""INSERT INTO books VALUES("Title", "Author", "Year")""") 
data = csvFile.read() 
cursor.execute(insert, (data)) 
data = "SELECT INTO books VALUES('Title')" 
print(sorted(data)) 
data = "SELECT INTO books VALUES('Year')" 
print(sorted(data)) 
app = Flask(__name__) 
app.config[SQLALCHEMY_DATABASE_URI] ="sqlite:///data.db" 
db = SQLAlchemy(app) 
bookData = data 
print(sorted(bookData)) 