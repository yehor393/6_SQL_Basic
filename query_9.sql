SELECT DISTINCT Subjects.SubjectName
FROM Students
JOIN Grades ON Students.StudentID = Grades.StudentID
JOIN Subjects ON Grades.SubjectID = Subjects.SubjectID
WHERE Students.StudentID = 23;