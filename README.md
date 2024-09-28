# Student-Report_Management-System

This is a Student Report Management System basde on Python-based terminal application. It allows users to perform various operations such as adding new student records, updating student details, deleting records, and viewing all stored records. The application uses a CSV file to store data persistently, making it simple and easy to manage student information.

Features

1. Create Student Record:
Users can create a new student record by entering the roll number, student name, marks for FA1, FA2, FA3, FA4, Mid-Term, and Final Term.
The system will calculate and store the total marks for each section and the overall percentage.
2. Update Student Information:
Users can update the roll number, name, or marks for any subject.
The system recalculates the totals and the percentage after each update.
3. Delete Student Record:
Users can delete a student record by specifying the roll number.
Once deleted, the record is permanently removed from the CSV file.
4. View Student Records:
Users can view all stored records in a tabular format.
Each record includes details such as roll number, student name, individual subject marks, total marks, and the overall percentage.
Data Validation
Input validation is included to ensure that valid marks and roll numbers are entered.
Users can update specific marks or details by selecting the subject or attribute they want to modify.
How It Works
The system performs four main operations:

1) Write: Adds new records to the student.csv file.
2) Read: Displays all student records from the file.
3) Update: Modifies existing student details.
4)Delete: Removes a student record.

CSV Format:
The records are stored in a CSV file (student.csv) with the following columns:

Roll No.

Name

FA1

FA2

Total (FA1 + FA2)

FA3

FA4

Total (FA3 + FA4)

Mid-Term

Final Term

Total (Mid-Term + Final Term)

Overall Percentage
