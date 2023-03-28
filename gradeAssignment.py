import sqlite3

# create connection and cursor objects
conn = sqlite3.connect("worker_project.db")
cursor = conn.cursor()


def tearDown():
    # close cursor and connection objects
    cursor.close()
    conn.close()


def runStudentQueries(studentFile):
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


def runKeyQueries(answerFile):
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
    studentAns = runStudentQueries("solution2.txt")
    Answers = runKeyQueries('solutions.txt')
    test_query_results(studentAns, Answers)
    tearDown()


main()
