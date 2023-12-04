SELECT Students.FirstName, Students.LastName, AVG(Grades.Grade) AS AvgGrade
FROM Students
JOIN Grades ON Students.StudentID = Grades.StudentID
JOIN Subjects ON Grades.SubjectID = Subjects.SubjectID
WHERE Subjects.SubjectName = 'Історія'
GROUP BY Students.StudentID
ORDER BY AvgGrade DESC
LIMIT 1;

