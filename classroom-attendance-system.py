import csv
import os

# File to store attendance records
ATTENDANCE_FILE = "attendance.csv"

def initialize_csv():
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Date", "Status"])

# Add a student to the attendance list
def add_student(student_id, name):
    with open(ATTENDANCE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, "", ""])
    return "Student added successfully!"

# Mark attendance for a student
def mark_attendance(date, student_id, status):
    found = False
    rows = []

    # Read current records
    with open(ATTENDANCE_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == student_id:
            row[2] = date
            row[3] = status
            found = True
            break

    if not found:
        return "Student ID not found. Please add the student first."
    else:
        # Write updated records
        with open(ATTENDANCE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return "Attendance marked successfully!"

# View attendance record
def view_attendance():
    records = []
    with open(ATTENDANCE_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    return records

# Simulated Menu for testing
# Replacing input() with function arguments to make it testable
def menu_simulated(actions):
    results = []
    for action in actions:
        if action["choice"] == '1':
            results.append(add_student(action["student_id"], action["name"]))
        elif action["choice"] == '2':
            results.append(mark_attendance(action["date"], action["student_id"], action["status"]))
        elif action["choice"] == '3':
            results.append(view_attendance())
        elif action["choice"] == '4':
            results.append("Exiting the system. Goodbye!")
            break
        else:
            results.append("Invalid choice. Please try again.")
    return results

# Main driver code
if __name__ == "__main__":
    initialize_csv()
    # Example simulation
    actions = [
        {"choice": '1', "student_id": "S001", "name": "John Doe"},
        {"choice": '2', "date": "2025-01-28", "student_id": "S001", "status": "Present"},
        {"choice": '3'},
        {"choice": '4'}
    ]
    results = menu_simulated(actions)
    for result in results:
        print(result)