import unittest
import sqlite3
#from template import Queries
from Assignment import Queries

class TestSqliteQueries(unittest.TestCase):

    def setUp(self):
        # create connection and cursor objects
        self.conn = sqlite3.connect("worker_project.db")
        self.cursor = self.conn.cursor()
        self.queries = Queries(self.cursor)

    def tearDown(self):
        # close cursor and connection objects
        self.cursor.close()
        self.conn.close()

    def test_query_results(self):
        # define the two queries to compare
        question1 = "SELECT * FROM Project"
        question2 = "SELECT lastName, firstName FROM Project CROSS JOIN Worker WHERE projNo = 1001 ORDER BY lastName ASC"
        question3 = "SELECT lastName, firstName FROM WORKER WHERE empId not in (SELECT projMgrId FROM Project)"
        Questions = [question1,question2,question3]
        studentSolutions = Queries.questions(self)
        #studentSolutions = 
        print(studentSolutions)
        #for solution in studentSolutions:
        for question, solution in enumerate(studentSolutions):
            self.cursor.execute(Questions[question])
            result = self.cursor.fetchall()
        print(self.assertEqual(result, solution))








if __name__ == '__main__':
    unittest.main()
