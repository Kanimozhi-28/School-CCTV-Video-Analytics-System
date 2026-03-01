-- Insert Students (Matching your 9 image files: 1, 10, 11, 2, 3, 5, 6, 7, 8)
INSERT INTO students (name, class_id, face_id) VALUES ('Aarav Sharma', '4A', '1');
INSERT INTO students (name, class_id, face_id) VALUES ('Vivaan Gupta', '4A', '2');
INSERT INTO students (name, class_id, face_id) VALUES ('Ananya Rao', '4B', '3');
INSERT INTO students (name, class_id, face_id) VALUES ('Ishaan Singh', '4B', '5');
INSERT INTO students (name, class_id, face_id) VALUES ('Sia Patel', '5A', '6');
INSERT INTO students (name, class_id, face_id) VALUES ('Reyansh Das', '5A', '7');
INSERT INTO students (name, class_id, face_id) VALUES ('Myra Jain', '5B', '8');
INSERT INTO students (name, class_id, face_id) VALUES ('Kabir Verma', '5B', '10');
INSERT INTO students (name, class_id, face_id) VALUES ('Zoya Khan', '6A', '11');

-- Insert Parents (Matching your 2 image files in parents folder)
INSERT INTO parents (name, phone, face_id, student_id) VALUES ('Vikram Sharma', '9876543210', 'image1', 1);
INSERT INTO parents (name, phone, face_id, student_id) VALUES ('Meera Gupta', '9123456789', 'image2', 2);

-- Note: 'Unknown' images (image1, image2 in data/faces/unknown) are NOT in these tables 
-- because the system should detect them as unknown dynamically.

