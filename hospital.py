# Hospital Management System - Python + MySQL


import mysql.connector

# Update ONLY your MySQL password here
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "aryan123",  
    "database": "hospital_db"
}

def get_connection():
    """Create MySQL connection."""
    return mysql.connector.connect(**DB_CONFIG)


def add_patient():
    print("\n--- Add Patient ---")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (M/F): ")
    disease = input("Enter disease: ")
    room_no = input("Enter room number: ")
    bill_amount = float(input("Enter bill amount: "))

    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO patients (name, age, gender, disease, room_no, bill_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cur.execute(query, (name, age, gender, disease, room_no, bill_amount))
    conn.commit()

    print("✔ Patient added successfully!\n")

    cur.close()
    conn.close()


def view_patients():
    print("\n--- All Patients ---")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients")
    rows = cur.fetchall()

    if not rows:
        print("No patient records found.\n")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, "
                  f"Disease: {row[4]}, Room: {row[5]}, Bill: {row[6]}")
        print()

    cur.close()
    conn.close()


def search_patient():
    print("\n--- Search Patient by ID ---")
    pid = int(input("Enter patient ID: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients WHERE id = %s", (pid,))
    row = cur.fetchone()

    if row:
        print("\nPatient Found:")
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Age: {row[2]}")
        print(f"Gender: {row[3]}")
        print(f"Disease: {row[4]}")
        print(f"Room No: {row[5]}")
        print(f"Bill Amount: {row[6]}\n")
    else:
        print("No patient found with that ID.\n")

    cur.close()
    conn.close()


def delete_patient():
    print("\n--- Delete Patient ---")
    pid = int(input("Enter patient ID to delete: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM patients WHERE id = %s", (pid,))
    conn.commit()

    if cur.rowcount > 0:
        print("✔ Patient deleted successfully.\n")
    else:
        print("No patient found with that ID.\n")

    cur.close()
    conn.close()


def main_menu():
    while True:
        print("===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main_menu()
