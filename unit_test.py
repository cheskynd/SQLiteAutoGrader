import unittest
import sqlite3
from template import Queries

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
        query1 = "SELECT ProjNo FROM Project;"
        studentQ1 = Queries.getStudentNames(self)

        self.cursor.execute(query1)
        result1 = self.cursor.fetchall()

        # assert that the results are equal
        self.assertEqual(result1, studentQ1)

if __name__ == '__main__':
    unittest.main()
