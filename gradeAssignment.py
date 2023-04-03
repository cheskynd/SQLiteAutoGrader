import sqlite3
import sys


def connect_to_database(database_name):
    """
    Connect to database and create a cursor object.
    :param database_name: The name of the database to connect
    :return: Returns a tuple containing connection and cursor objects
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor

def tearDown(conn,cursor):
    # close cursor and connection objects
    cursor.close()
    conn.close()


def runStudentQueries(studentFile,cursor):
    """
    This Function runs the queries in the Student file or the student queries
    :param studentFile: The student text file that contains their SQL solutions
    :param cursor: Cursor object
    :return: The results of the query solutions
    """
    studentSolutions = open(studentFile, 'r')
    studentSolutionsLines = studentSolutions.readlines()
    studentAnswers = []
    studentResults = []
    for studentLine in studentSolutionsLines:
        studentAnswers.append(studentLine.rstrip())
    for answer in studentAnswers:
        cursor.execute(answer)
        studentResult = cursor.fetchall()
        studentResults.append(studentResult)
    return studentResults


def runKeyQueries(answerFile,cursor):
    """
    This Function runs the queries in the answer file
    :param answerFile: The text file that holds the SQL solutions
    :param cursor: Cursor object
    :return: Returns the results of the SQL queries
    """
    solutionFile = open(answerFile, 'r')
    solutionLines = solutionFile.readlines()
    AnswerKey = []
    solutionResults = []

    for line in solutionLines:
        AnswerKey.append(line.rstrip())

    for keyAnswer in AnswerKey:
        cursor.execute(keyAnswer)
        solutionResult = cursor.fetchall()
        solutionResults.append(solutionResult)
    return solutionResults


def test_query_results(studentAns, Answers):
    """
    This function compares the student queries to the solutions and results of how
    were correct or wrong.
    :param studentAns:
    :param Answers:
    :return: None
    """
    passed, failed, total = 0, 0, 0
    total = len(Answers)
    for x, answer in enumerate(Answers):
        if answer == studentAns[x]:
            passed += 1
            print(f"Question {x + 1} is Correct")
        else:
            failed += 1
            print(f"Question {x + 1} is Wrong")
    print(f"\n{passed} out of {total} questions are correct.")
    print('You received ' + str((passed / total) * 100) + '%')


def main():
    if len(sys.argv) < 2:
        print('Please specify student solution text file')
    elif len(sys.argv) == 2:
        studentAnsFileName = sys.argv[1]
        AnswersFileName = 'solutions.txt'
    elif len(sys.argv) == 3:
        studentAnsFileName = sys.argv[1]
        AnswersFileName = sys.argv[2]
    else:
        print('Invalid number of arguments')
        print(len(sys.argv))
        sys.exit(1)

    conn, cursor = connect_to_database("worker_project.db")
    studentAns = runStudentQueries(studentAnsFileName,cursor)
    Answers = runKeyQueries(AnswersFileName,cursor)
    test_query_results(studentAns, Answers)
    tearDown(conn,cursor)


main()
