from cs50 import SQL
import csv


db = SQL("sqlite:///newroster.db")

with open("students.csv",'r') as file:
    rows = csv.DictReader(file)
    for row in rows :
        id = db.execute("INSERT INTO students (id, student_name) VALUES(?, ?)", row["id"], row["student_name"])
        houses= db.execute("select * from houses where house_name = ?", row["house"])
        if len(houses) == 0:
            id = db.execute("INSERT INTO houses (house_name) VALUES(?)", row["house"])
        id = db.execute("INSERT INTO head (student_id, house_name, head) VALUES(?, ?, ?)", row["id"], row["house"], row["head"])

