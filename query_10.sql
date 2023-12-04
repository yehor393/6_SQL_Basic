SELECT DISTINCT Subjects.SubjectName
FROM Students
JOIN Grades ON Students.StudentID = Grades.StudentID
JOIN Subjects ON Grades.SubjectID = Subjects.SubjectID
JOIN Professors ON Subjects.ProfessorID = Professors.ProfessorID
WHERE Students.FirstName = 'певне імя' AND Students.LastName = 'певне прізвище'
  AND Professors.FirstName = 'певне імя' AND Professors.LastName = 'певне прізвище';