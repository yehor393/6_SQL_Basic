from faker import Faker
from random import randint

fake = Faker("uk")


def insert_random_data(conn):
    for _ in range(30):
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Students (FirstName, LastName, GroupID)
                VALUES (%s, %s, %s)
            ''', (fake.first_name(), fake.last_name(), randint(1, 4)))

    for group_id in range(1, 4):
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Groups (GroupName)
                VALUES (%s)
            ''', (f'Group {group_id}',))

    for _ in range(5):
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Professors (FirstName, LastName)
                VALUES (%s, %s)
            ''', (fake.first_name(), fake.last_name()))

    for _ in range(5):
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO Subjects (SubjectName, ProfessorID)
                VALUES (%s, %s)
            ''', (fake.random_element(elements=('Математика', 'Фізика', 'Хімія', 'Історія', 'Література')),
                  randint(1, 5)))

    for student_id in range(1, 31):
        for subject_id in range(1, 5):
            with conn.cursor() as cur:
                cur.execute('''
                    INSERT INTO Grades (StudentID, SubjectID, Grade, ExamDate)
                    VALUES (%s, %s, %s, %s)
                ''', (student_id, subject_id, randint(60, 100), fake.date_this_decade()))
