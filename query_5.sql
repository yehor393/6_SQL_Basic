SELECT Subjects.SubjectName, Professors.FirstName, Professors.LastName
FROM Professors
JOIN Subjects ON Professors.ProfessorID = Subjects.ProfessorID
WHERE Professors.ProfessorID = 2;
