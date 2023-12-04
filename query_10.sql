SELECT DISTINCT Subjects.SubjectName
FROM Students
JOIN Grades ON Students.StudentID = Grades.StudentID
JOIN Subjects ON Grades.SubjectID = Subjects.SubjectID
JOIN Professors ON Subjects.ProfessorID = Professors.ProfessorID
WHERE Students.StudentID = 23
  AND Professors.ProfessorID = 2;