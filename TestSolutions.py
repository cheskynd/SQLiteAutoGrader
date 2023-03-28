import unittest
import sqlite3
# from template import Queries
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

        studentSolutions = Queries.questions(self)
        AnswerKey = []

        solutionFile = open('solutions.txt', 'r')
        Lines = solutionFile.readlines()
        x = 0
        for line in Lines:
            AnswerKey.append(line.rstrip())

        passed, failed, total = 0, 0, 0
        for question, solution in enumerate(studentSolutions):
            self.cursor.execute(AnswerKey[question])
            result = self.cursor.fetchall()
            if result == solution:
                print(f"Question {question}: Passed")
                passed += 1
                total += 1
            else:
                print(f"Question {question}: Failed")
                failed += 1
                total += 1

        print(f"\n{passed} out of {total} questions are correct.")
        print('You received ' + str((passed/total)*100) + '%')
        # self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
