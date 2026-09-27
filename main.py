import pandas as pd

FILE_NAME = "students.csv"


def load_data():
    try:
        return pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Name", "Python", "Java", "SQL",
            "Total", "Percentage", "Grade"
        ])


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    python = float(input("Enter Python marks: "))
    java = float(input("Enter Java marks: "))
    sql = float(input("Enter SQL marks: "))

    total = python + java + sql
    percentage = total / 3
    grade = calculate_grade(percentage)

    df = load_data()

    new_student = pd.DataFrame([{
        "Name": name,
        "Python": python,
        "Java": java,
        "SQL": sql,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }])

    df = pd.concat([df, new_student], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("\nStudent added successfully!")
    print("Total:", total)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)


def view_students():
    df = load_data()

    if df.empty:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        print(df.to_string(index=False))


def search_student():
    df = load_data()

    name = input("Enter student name: ")

    result = df[
        df["Name"].str.lower() == name.lower()
    ]

    if result.empty:
        print("Student not found.")
    else:
        print(result.to_string(index=False))


def show_statistics():
    df = load_data()

    if df.empty:
        print("No data available.")
        return

    print("\n--- Statistics ---")

    print("Python Average:", round(df["Python"].mean(), 2))
    print("Java Average:", round(df["Java"].mean(), 2))
    print("SQL Average:", round(df["SQL"].mean(), 2))

    highest = df.loc[df["Percentage"].idxmax()]

    print("\nTop Student:", highest["Name"])
    print("Percentage:", highest["Percentage"])


def main():
    while True:

        print("\n===== Student Performance Analyzer =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            show_statistics()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()    