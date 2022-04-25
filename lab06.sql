USE university;

DROP TABLE IF EXISTS takes;
DROP TABLE IF EXISTS teaches;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS prereq;
DROP TABLE IF EXISTS section;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS department;


CREATE TABLE department (
	dept_name VARCHAR(25), 
	building VARCHAR(10), 
	budget INTEGER, 
	PRIMARY KEY(dept_name)
);
CREATE TABLE instructor (
	ID INTEGER, 
	name VARCHAR(20), 
	dept_name VARCHAR(25), 
	salary INTEGER, 
	PRIMARY KEY(ID), 
	FOREIGN KEY(dept_name) REFERENCES department(dept_name)
);
CREATE TABLE course (
	course_ID VARCHAR(8), 
    title VARCHAR(32), 
    dept_name VARCHAR(32), 
    credits INTEGER, 
    PRIMARY KEY(course_ID), 
    FOREIGN KEY(dept_name) REFERENCES department(dept_name)
);
CREATE TABLE prereq (
	course_ID VARCHAR(8), 
    prereq_ID VARCHAR(8),
    PRIMARY KEY(course_ID, prereq_ID),
    FOREIGN KEY(course_ID) REFERENCES course(course_ID),
    FOREIGN KEY(prereq_ID) REFERENCES course(course_ID)
);

CREATE TABLE student (
	ID INTEGER UNSIGNED,
    NAME VARCHAR(32),
    dept_name VARCHAR(32),
    total_credits INTEGER UNSIGNED,
    PRIMARY KEY(ID),
    FOREIGN KEY(dept_name) REFERENCES department(dept_name)
);

CREATE TABLE section (
	
	course_ID VARCHAR(8),
    sec_ID VARCHAR(3),
    semester TINYINT UNSIGNED,
    year SMALLINT UNSIGNED,
    building VARCHAR(10),
    room VARCHAR(10),
    capacity SMALLINT UNSIGNED,
    PRIMARY KEY(course_ID, sec_ID, semester, year),
    FOREIGN KEY(course_ID) REFERENCES course(course_ID)
);

CREATE TABLE teaches (

	course_ID VARCHAR(8),
    sec_ID VARCHAR(3),
    semester TINYINT UNSIGNED,
    year SMALLINT UNSIGNED,
    ID INTEGER,
    
    FOREIGN KEY(course_ID, sec_ID, semester, year) REFERENCES section(course_ID, sec_ID, semester, year),
--     FOREIGN KEY(course_ID) REFERENCES section(course_ID),
--     FOREIGN KEY(sec_ID) REFERENCES section(sec_ID),
-- 	   FOREIGN KEY (semester) REFERENCES section(semester),
--     FOREIGN KEY(year) REFERENCES section(year),
    FOREIGN KEY(ID) REFERENCES instructor(ID)
    
);

CREATE TABLE takes (

	ID INTEGER UNSIGNED,
    course_ID VARCHAR(8),
    sec_ID VARCHAR(3),
    semester TINYINT UNSIGNED,
    year SMALLINT UNSIGNED,
    grade VARCHAR(2),
    
    FOREIGN KEY(ID) REFERENCES student(ID),
    FOREIGN KEY(course_ID, sec_ID, semester, year) REFERENCES section(course_ID, sec_ID, semester, year)
--     FOREIGN KEY(course_ID) REFERENCES section(course_ID),
--     FOREIGN KEY(sec_ID) REFERENCES section(sec_ID),
--     FOREIGN KEY(semester) REFERENCES section(semester),
--     FOREIGN KEY(year) REFERENCES section(year)
);    
    

INSERT INTO department(dept_name, building, budget)
VALUES
('ECE', 'CAMP', 65000),
('CS', 'SC', 80000),
('Economics', 'Snell', 55000),
('Physics', 'SC', 80000),
('Math','SC',50000),
('ART', 'SNELL', 10000),
('EE', 'SC', 60000),
('PHIL', 'ERC', 24000),
('Computers', 'Snell', 30000),
('PHY', 'SC', 86000),
('Applied Math', 'SC', 10000),
('ANTH', 'Snell', 1000),
('POL', 'virtual', 75000),
('BIDA', 'Snell', 70000),
('Business', 'Snell', 35000),
('HIST', 'Snell', 25000),
('BY', 'SC', 30000),
('Music', 'Student', 10000);

INSERT INTO course(course_ID, title, dept_name, credits)
VALUES
('EE468', 'Databases','ECE', 3),
('CS460', 'Databases','CS', 3),
('CS421', 'computer drawing', 'CS', 3),
('AT100', 'Introduction to Art', 'ART', 3),
('AT200', 'Drawing', 'ART', 3),
('ANTH220', 'Understanding the Americas', 'ANTH',3), 
('EE221', 'Linear Circuits','ECE',3), 
('MA339', 'Applied Linear Algebra', 'Math', 3), 
('CS445', 'Compiler Construction', 'CS', 3), 
('CS455', 'Computer Networks', 'CS', 3),
('STAT383', 'Probability and Statistics', 'Math', 3), 
('CS470', 'Deep Learning', 'CS', 3), 
('EE568', 'Database Systems', 'CS', 3), 
('MA132', 'Calculus 2', 'Math', 3), 
('SS220', 'Intro to Gender', 'ANTH', 3), 
('POL220', 'American Politics', 'POL', 3), 
('CS142', 'Intro to Computer Science','CS', 4), 
('CS344', 'Algorithms', 'CS', 3), 
('BS331', 'Introduction to Tax Avoidance', 'Business', 3), 
('IS415', 'Data Warehousing for Analytics', 'BIDA', 3),
('EE316', 'Computer Eng. Jr. Lab', 'ECE', 4),
('CS141', 'Intro to Computer Science I', 'CS', 4),
('CS345', 'Automata and Formal Languages', 'CS', 3),
('CS242', 'Advanced Programming Concepts', 'CS', 3),
('MA131', 'Calculus I', 'Math', 3);

INSERT INTO prereq(course_ID, prereq_ID)
VALUES
('EE468', 'CS141'),
('AT200', 'AT100'),
('CS421', 'AT200'),
('EE221', 'MA132'),
('CS344', 'CS142'),
('CS445', 'CS345'),
('CS470', 'CS142'),
('STAT383', 'MA132'),
('CS142','CS141'),
('BS331', 'MA132'),
('CS455', 'CS242');


INSERT INTO instructor(ID, name, dept_name, salary)
VALUES
(12345, 'Hou', 'ECE', 150000),
(28011, 'Hussain','ECE',100000),
(12365, 'White', 'Math', 105000),
(75310, 'Brown', 'ART', 40000),
(08463, 'Disilvestro', 'ECE', 90000),
(17703,'Smith','CS',75000),
(05533, 'John', 'Math', 15000),
(55515, 'Pendragon', 'Physics', 60000),
(10101, 'Maciel', 'CS', 100000),
(54321, 'Jeanna', 'CS', 40000),
(34859, 'Ford', 'Business', 15000),
(17539, 'Bill', 'Math', 70000),
(37785, 'Jukic', 'Business', 80000),
(69420, 'Miller', 'ECE', 100000),
(07101, 'Sean', 'CS', 110000),
(32454, 'Cohen', 'POL', 95000),
(43888, 'Hoffmann','ART',40000),
(58008, 'Breglia', 'ANTH', 10000),
(32321, 'Swain', 'HIST', 90000);

INSERT INTO student(ID, name, dept_name, total_credits)
VALUES
(00128, "Zhang", "CS", 102),
(12345, "Shankar", "CS", 32),
(19991, "Brandt", "HIST", 80),
(44553, "Peltier", "PHY", 56),
(45678, "Levy", "PHY", 46),
(54321, "Williams", "CS", 54),
(55739, "Sanchez", "Music", 38),
(70557, "Snow", "PHY", 0),
(05401, "Megan", "CS", 30),
(05405, "Alex", "CS", 93),
(76543, "Brown", "CS", 58),
(76653, "Aoi", "ECE", 60),
(98765, "Bourikas", "ECE", 98),
(98988, "Tanaka", "BY",120);

INSERT INTO section(course_ID, sec_ID, semester, year, building, room, capacity)
VALUES
("CS141", "01", 1, 2019, "CAMP", "194", 40),
("CS141", "02", 1, 2019, "CAMP", "194", 40),
("CS141", "01", 2, 2019, "CAMP", "194", 40),
("CS141", "02", 2, 2019, "CAMP", "194", 40),
("CS141", "03", 2, 2019, "CAMP", "194", 40),
("CS141", "01", 1, 2020, "CAMP", "194", 40),
("CS141", "02", 1, 2020, "CAMP", "194", 40),
("CS141", "03", 1, 2020, "CAMP", "194", 40),
("EE468", "01", 1, 2020, "CAMP", "194", 40),
("CS460", "01", 1, 2020, "CAMP", "194", 40),
("CS460", "01", 2, 2019, "CAMP", "194", 40),
("CS460", "01", 1, 2019, "CAMP", "194", 40),
("EE468", "02", 2, 2019, "CAMP", "194", 40),
("EE468", "01", 2, 2019, "CAMP", "194", 40),
("CS460", "02", 2, 2019, "CAMP", "194", 40),
("CS460", "02", 1, 2020, "CAMP", "194", 40),
("EE468", "01", 1, 2019, "CAMP", "194", 40);

INSERT INTO teaches(course_id, sec_id, semester, year, ID)
VALUES
("EE468", "01", 1, 2020, 12345),
("CS460", "01", 1, 2020, 12345),
("CS141", "01", 1, 2019, 07101),
("CS141", "02", 1, 2019, 10101),
("CS141", "01", 2, 2019, 07101),
("CS141", "02", 2, 2019, 10101),
("CS141", "03", 2, 2019, 17703),
("CS141", "01", 1, 2020, 07101),
("CS141", "02", 1, 2020, 10101),
("CS141", "03", 1, 2020, 17703);

INSERT INTO takes(ID, course_id, sec_id, semester, year, grade)
VALUES
(00128, "CS141", "01", 2, 2019, "A"),
(00128, "CS460", "01", 2, 2019, "A-"),
(12345, "CS141", "01", 2, 2019, "C"),
(12345, "CS460", "01", 1, 2020, "A"),
(12345, "CS460", "01", 1, 2019, "A"),
(45678, "CS141", "01", 1, 2020, "B+"),
(45678, "CS141", "01", 2, 2019, "F"),
(05401, "CS460", "02", 2, 2019, "C"),
(05405, "CS460", "02", 1, 2020, "D"),
(54321, "CS141", "01", 2, 2019, "F"),
(98765, "CS141", "01", 2, 2019, "C-"),
(98765, "CS460", "01", 1, 2019, "B");

SELECT name, salary
FROM instructor
WHERE salary > (
	SELECT MIN(salary)
	FROM instructor
    WHERE dept_name = 'CS'
);

SELECT DISTINCT course_id
FROM section
WHERE (semester = 2 AND year = 2019) OR (semester = 1 AND year = 2020);

SELECT DISTINCT name
FROM instructor, teaches
WHERE teaches.ID = instructor.ID AND teaches.year = 2019 AND semester = 1;

SELECT DISTINCT name
FROM student, takes, teaches
WHERE student.ID = takes.ID AND takes.sec_ID = teaches.sec_ID AND teaches.ID = 07101;