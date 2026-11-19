
# Project No. 46
# Exam Result Management System

import json
import os

FILE_NAME = "results.txt"
PASS_MARK = 40
TOTAL_SUBJECTS = 3


# Load saved student records
def load_records():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                records = json.load(file)
                return records
        except (json.JSONDecodeError, OSError):
            return []
    return []


# Save student records
def save_records(records):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(records, file, indent=4)
    except OSError:
        print("Error saving records to file!")


# Calculate total, percentage and result
def calculate_result(marks):
    total = sum(marks)
    percentage = total / TOTAL_SUBJECTS

    if all(mark >= PASS_MARK for mark in marks):
        result = "Pass"
    else:
        result = "Fail"

    return total, percentage, result


# Add a new student record
def add_student(records):
    try:
        roll = int(input("Enter Roll Number: "))

        # Check duplicate roll number
        for student in records:
            if student["roll"] == roll:
                print(f"Roll number {roll} already exists.")
                return

        name = input("Enter Student Name: ").strip()

        if name == "":
            print("Student name cannot be empty.")
            return

        marks = []

        # Input marks for three subjects
        for i in range(1, TOTAL_SUBJECTS + 1):
            mark = float(input(f"Enter Marks of Subject {i}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        # Calculate result
        total, percentage, result = calculate_result(marks)

        # Create student record
        student = {
            "roll": roll,
            "name": name,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "result": result
        }

        # Add and save record
        records.append(student)
        save_records(records)

        print(f"Record added: {roll} | {name}")
        print(
            f"Total: {total} | "
            f"Percentage: {percentage:.2f}% | "
            f"Result: {result}"
        )

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# Display all student records
def view_all(records):
    if len(records) == 0:
        print("No records found.")
        return

    print("\n========== All Student Records ==========")
    print("-" * 75)

    print(
        f"{'Roll':<10}"
        f"{'Name':<15}"
        f"{'Total':<10}"
        f"{'Percentage':<15}"
        f"{'Result':<10}"
    )

    print("-" * 75)

    for student in records:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<15}"
            f"{student['total']:<10}"
            f"{student['percentage']:.2f}%{'':<10}"
            f"{student['result']:<10}"
        )

    print("-" * 75)


# Display rank list according to percentage
def rank_list(records):
    if len(records) == 0:
        print("No records found.")
        return

    # Sort records from highest to lowest percentage
    sorted_records = sorted(
        records,
        key=lambda student: student["percentage"],
        reverse=True
    )

    print("\n============== Rank List ==============")
    print("-" * 80)

    print(
        f"{'Rank':<8}"
        f"{'Roll':<10}"
        f"{'Name':<15}"
        f"{'Total':<10}"
        f"{'Percentage':<15}"
        f"{'Result':<10}"
    )

    print("-" * 80)

    for rank, student in enumerate(sorted_records, start=1):
        print(
            f"{rank:<8}"
            f"{student['roll']:<10}"
            f"{student['name']:<15}"
            f"{student['total']:<10}"
            f"{student['percentage']:.2f}%{'':<9}"
            f"{student['result']:<10}"
        )

    print("-" * 80)


# Main program
def main():
    records = load_records()

    while True:
        print("\n===== Exam Result Management System =====")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Rank List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(records)

        elif choice == "2":
            view_all(records)

        elif choice == "3":
            rank_list(records)

        elif choice == "4":
            save_records(records)
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")


# Run program
if __name__ == "__main__":
    main()
