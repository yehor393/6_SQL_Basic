SELECT Students.FirstName, Students.LastName, AVG(Grades.Grade) AS AvgGrade
FROM Students
JOIN Grades ON Students.StudentID = Grades.StudentID
GROUP BY Students.StudentID
ORDER BY AvgGrade DESC
LIMIT 5;

