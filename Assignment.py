import sqlite3
import unittest
import TestSolutions


class Queries(object):
    def __init__(self, cursor):
        self.cursor = cursor

    def questions(self):
        results = []
        question1 = "SELECT * FROM Project"
        question2 = "SELECT lastName FROM Project CROSS JOIN Worker WHERE projNo = 1001 ORDER BY lastName ASC"
        question3 = "SELECT lastName FROM WORKER WHERE empId not in (SELECT projMgrId FROM Project)"
        Questions = [question1, question2, question3]
        for question in Questions:
            self.cursor.execute(question)
            result = self.cursor.fetchall()
            results.append(result)
        return results


if __name__ == '__main__':
    conn = sqlite3.connect("worker_project.db")
    cursor = conn.cursor()
    s = Queries(cursor)
    res = s.questions()
    for i in res:
        print("\n",i)
