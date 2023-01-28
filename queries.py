query1 = """SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.fullname, s.id
ORDER BY avg_grade DESC
LIMIT 5;"""
query2 = """SELECT d.name, s.fullname, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 1
GROUP BY s.fullname, d.name
ORDER BY avg_grade DESC
LIMIT 1;"""
query3 = """SELECT d.name, gr.name, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3
GROUP BY gr.name, d.name
ORDER BY avg_grade DESC;"""
query4 = """SELECT round(avg(g.grade), 2) AS avg_grade 
FROM grades g;"""
query5 = """SELECT d.id, t.fullname, d.name 
FROM teachers t 
LEFT JOIN disciplines d ON t.id = d.teacher_id
WHERE t.id = 3;"""
query6 = """SELECT s.id, s.fullname, gr.name
FROM students s 
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 3;"""
query7 = """SELECT s.id, d.name, gr.name, s.fullname, g.grade, g.date_of  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3 AND gr.id = 3;
"""
query8 = """
SELECT s.id, d.name, gr.name, s.fullname, g.grade, g.date_of  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3 AND gr.id = 3 AND g.date_of = (SELECT g.date_of 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE g.discipline_id = 3 AND gr.id = 3
ORDER BY g.date_of DESC 
LIMIT 1);"""
query9 = """SELECT d.name, s.fullname 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE g.student_id = 1
GROUP BY d.name;"""
query10 = """SELECT s.fullname, t.fullname, d.name 
FROM grades g  
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1 AND g.student_id = 1
GROUP BY d.name;"""
query11 = """SELECT s.fullname, t.fullname, d.name 
FROM grades g  
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1 AND g.student_id = 1
GROUP BY d.name;"""
query12 = """SELECT t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g  
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
GROUP BY t.fullname;"""

queries = [query1, query2, query3, query4, query5, query6, query7, query8, query9, query10, query11, query12]
