import sqlite3
class Queries(object):
    def __init__(self,cursor):
        self.cursor = cursor
    def getStudentNames(self):
        "Get all of the student in the students table"
        query = "SELECT * FROM Project"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
if __name__ == '__main__':
    conn = sqlite3.connect("worker_project.db")
    cursor = conn.cursor()
    s = Queries(cursor)
    res = s.getStudentNames()
    for i in res:
        print(i)


    

