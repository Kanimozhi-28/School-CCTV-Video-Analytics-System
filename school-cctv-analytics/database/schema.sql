DROP TABLE IF EXISTS activity_logs;
DROP TABLE IF EXISTS parents;
DROP TABLE IF EXISTS students;

-- Students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    class_id VARCHAR(50),
    face_id VARCHAR(100) UNIQUE, -- Maps to filename in data/faces/students
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Parents table (renamed from guardians)
CREATE TABLE parents (
    parent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    face_id VARCHAR(100) UNIQUE, -- Maps to filename in data/faces/parents
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Activity Logs for Detections and Alerts
CREATE TABLE activity_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    person_type ENUM('student', 'parent', 'unknown') NOT NULL,
    person_id VARCHAR(100), -- face_id or 'unknown'
    status ENUM('SAFE', 'SUSPICIOUS', 'STRANGER') NOT NULL,
    snapshot_path VARCHAR(255),
    details TEXT
);



