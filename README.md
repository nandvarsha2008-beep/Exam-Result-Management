
📌 Project Overview

The Exam Result Management System is a simple Python-based console application designed to manage student examination results. It allows users to add student records, calculate total marks and percentages, view all student results, and generate a rank list based on students' percentages.

The system uses a JSON file (results.txt) to store student records permanently, so data remains available even after closing the program.

✨ Features
Add Student Result: Add a new student's roll number, name, and marks in three subjects.
Duplicate Roll Number Check: Prevents adding students with an already existing roll number.
Input Validation: Checks that marks are between 0 and 100 and that the student's name is not empty.
Automatic Calculation: Calculates total marks, percentage, and pass/fail status automatically.
Pass/Fail Status: A student passes only if they score at least 40 marks in all three subjects.
View All Results: Displays all saved student records in a formatted table.
Rank List: Generates a ranking based on percentage, from highest to lowest.
File Handling: Saves and loads student records using JSON.
Error Handling: Handles invalid inputs and file-related errors.
🛠️ Technologies Used
Programming Language: Python
Modules:
json – For storing and retrieving student records.
os – For checking whether the data file exists.
Storage: JSON file (results.txt)
📂 Project Structure
text
Exam-Result-Management-System/
│
├── main.py
├── results.txt
└── README.md


File Description:

main.py – Contains the complete Python source code.
results.txt – Stores student records in JSON format. It is automatically created when records are saved.
README.md – Contains project information and instructions.
⚙️ System Requirements
Python 3.x
Any Python-supported operating system (Windows, Linux, or macOS).
A code editor such as VS Code, PyCharm, or IDLE.
🚀 How to Run the Project

Step 1: Clone or Download the Repository

Download the project or clone the repository using:

bash
git clone <repository-url>


Step 2: Open the Project Folder

bash
cd Exam-Result-Management-System


Step 3: Run the Python Program

bash
python main.py


No external Python libraries are required.

📋 Main Menu

When you run the program, the following menu appears:

text
===== Exam Result Management System =====
1. Add Student Result
2. View All Results
3. Rank List
4. Exit

Enter your choice:

📖 How the System Works
1. Add Student Result
Enter the student's roll number.
Enter the student's name.
Enter marks for three subjects.
The system validates the input.
Total marks, percentage, and result are calculated automatically.
The record is saved in results.txt.
2. View All Results

Displays all student records in tabular format, including:

Roll Number
Student Name
Total Marks
Percentage
Pass/Fail Result
3. Rank List

Displays students in descending order according to their percentages.

The student with the highest percentage receives Rank 1.

4. Exit

Saves all student records and safely exits the program.

🧮 Calculation Logic

Total Marks:

python
total = sum(marks)


Percentage:

python
percentage = total / 3


Pass/Fail Condition:

python
if all(mark >= 40 for mark in marks):
    result = "Pass"
else:
    result = "Fail"


Example:

Subject	Marks
Subject 1	85
Subject 2	75
Subject 3	90
Total	250
Percentage	83.33%
Result	Pass
💾 Data Storage

Student records are stored in a JSON format inside results.txt.

Example:

json
[
    {
        "roll": 101,
        "name": "Rahul",
        "marks": [85, 75, 90],
        "total": 250,
        "percentage": 83.33333333333333,
        "result": "Pass"
    }
]


The program automatically loads existing records when it starts and saves updated records whenever a new student is added or the program exits.

🎯 Learning Outcomes

By developing this project, you can understand:

Python functions and modular programming.
Lists and dictionaries.
Conditional statements and loops.
Exception handling using try-except.
File handling in Python.
JSON data storage and retrieval.
Sorting and ranking techniques.
User input validation.
Basic CRUD-style record management.
🔮 Future Enhancements
Add student record search functionality.
Update existing student records.
Delete student records.
Generate individual student report cards.
Add subject-wise performance analysis.
Export results to PDF or Excel.
Develop a graphical user interface (GUI).
👨‍💻 Project Information
**Project
