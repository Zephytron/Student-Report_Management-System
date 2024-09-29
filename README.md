# Student Report Management System



Welcome to the **Student Report Management System** – A Python-based terminal application designed to make managing student records simple, efficient. With this tool, you can easily create, update, delete, and view student data, all stored securely in a CSV file.

---

## ✨ Features

1. **Create Student Record**  
   Add a new student record by entering the roll number, name, and marks for FA1, FA2, FA3, FA4, Mid-Term, and Final Term. The system automatically calculates and stores:
   - Total marks for each section.
   - Overall percentage.

2. **Update Student Information**  
   Modify an existing record by updating the roll number, name, or subject marks. The system will recalculate the totals and percentage in real-time.

3. **Delete Student Record**  
   Remove a student’s record permanently by providing their roll number. Once deleted, the record is gone from the CSV file.

4. **View Student Records**  
   See all stored records displayed neatly in a tabular format. This includes:
   - Roll number
   - Student name
   - Marks for each subject
   - Total marks and overall percentage

---

## 🛠️ How It Works

The system revolves around four core operations:
- **Write**: Add new student records to the CSV file (`student.csv`).
- **Read**: Display all the student records from the CSV.
- **Update**: Modify the details of existing records.
- **Delete**: Permanently remove a student’s record from the file.

### Input Validation
The system includes validation to ensure correct data entry for:
- Marks
- Roll numbers
- Names

---

## 📋 CSV File Format

Records are stored in a CSV file (`student.csv`) with the following columns:

| Roll No. | Name | FA1 | FA2 | Total (FA1+FA2) | FA3 | FA4 | Total (FA3+FA4) | Mid-Term | Final Term | Total (Mid + Final) | Overall % |
|----------|------|-----|-----|-----------------|-----|-----|-----------------|----------|------------|--------------------|------------|

---

## 🚀 Getting Started

### Prerequisites
- **Python**: Ensure Python is installed on your system.  
  [Download Python](https://www.python.org/downloads/)

- **IDE**: Use any preferred IDE like:
  - [Python IDLE](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare) (comes bundled with Python)
  - [VS Code](https://code.visualstudio.com/)
  - [PyCharm](https://www.jetbrains.com/pycharm/)

### Steps to Run the Program

1. ### **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd Student-Report_Management-System

2. ### **Create a Python File:** 
Open your IDE and create a new Python file (e.g., student_management.py). Copy and paste the provided code into this file.

3. ### **Run the Program:** 
In Python IDLE, go to the Run menu and select Run Module (or press F5 on your keyboard). This will execute the code and display the prompts in the output console. Follow the instructions in the console to 
create, update, delete, or view student records.

4. ### **View Output:**
The program stores all student records in a CSV file named student.csv. To check the stored data, search for the student.csv file in the directory where you saved the Python file and open it with any text editor 
or spreadsheet software like Excel.

## 🤝How to contribute
To ensure a smooth process, please follow these guidelines:

1. **Fork the Repository**: Start by forking the repository and cloning it to your local machine.
2. **Work on a Feature Branch**: Always create a new branch for your work (e.g., `feature/your-feature-name` or `bugfix/issue-number`) to keep the main branch stable.
3. **Raise Issues**: If you've found a bug or have a suggestion, feel free to raise an issue before working on it.
4. **Testing**: Before submitting a pull request, make sure your code is tested locally.
5. **Pull Request**: Once your work is complete, submit a pull request with a detailed description of the changes and link it to the corresponding issue.

Thank you for checking out the Student Report Management System! I hope you find it helpful. All feedbacks and contributions are welcomed !
