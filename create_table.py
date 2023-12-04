import psycopg2


def create_table(conn, create_table_sql):
    try:
        with conn.cursor() as c:
            c.execute(create_table_sql)
    except psycopg2.Error as err:
        print(err)


sql_create_students_table = '''
    CREATE TABLE IF NOT EXISTS Students (
        StudentID SERIAL PRIMARY KEY,
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        GroupID INTEGER
    )
'''

sql_create_groups_table = '''
    CREATE TABLE IF NOT EXISTS Groups (
        GroupID SERIAL PRIMARY KEY,
        GroupName VARCHAR(255)
    )
'''

sql_create_professors_table = '''
    CREATE TABLE IF NOT EXISTS Professors (
        ProfessorID SERIAL PRIMARY KEY,
        FirstName VARCHAR(255),
        LastName VARCHAR(255)
    )
'''

sql_create_subjects_table = '''
    CREATE TABLE IF NOT EXISTS Subjects (
        SubjectID SERIAL PRIMARY KEY,
        SubjectName VARCHAR(255),
        ProfessorID INTEGER
    )
'''

sql_create_grades_table = '''
    CREATE TABLE IF NOT EXISTS Grades (
        GradeID SERIAL PRIMARY KEY,
        StudentID INTEGER,
        SubjectID INTEGER,
        Grade INTEGER,
        ExamDate DATE,
        FOREIGN KEY (StudentID) REFERENCES Students (StudentID),
        FOREIGN KEY (SubjectID) REFERENCES Subjects (SubjectID)
    )
'''


def create_all_tables(conn):
    create_table(conn, sql_create_students_table)
    create_table(conn, sql_create_groups_table)
    create_table(conn, sql_create_professors_table)
    create_table(conn, sql_create_subjects_table)
    create_table(conn, sql_create_grades_table)
