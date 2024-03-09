import pyodbc

#Function to establish connection to SQL Server Database
def connect_to_database():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=localhost\\SQLEXPRESS;'
                              'DATABASE=TASK_MANAGER;'
                              'Trusted_Connection=True;')

        return conn
    except pyodbc.Error as e:
        print("Error connecting to database: ", e)
        return None

#Function to create a new task
def create_task(conn, title, description, due_date):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tasks (Title, Description, DueDate) VALUES (?, ?, ?)", (title, description, due_date))
        conn.commit()
        print("Task created successfully.")
    except pyodbc.Error as e:
        print("Error creating task:", e)

#Function to display all tasks
def display_tasks(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tasks")
        rows = cursor.fetchall()
        print("Tasks:")
        for row in rows:
            print(row)
    except pyodbc.Error as e:
        print("Error displaying tasks:", e)

#Function to update a task's due date
def update_due_date(conn, task_id, due_date):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Tasks SET DueDate=? WHERE TaskID=?", (due_date, task_id))
        conn.commit()
        print("Task due date updated successfully.")
    except pyodbc.Error as e:
        print("Error updating due date for task:", e)

#Function to delete a task
def delete_task(conn, task_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Tasks WHERE TaskID=?", (task_id,))
        conn.commit()
        print("Task deleted successfully.")
    except pyodbc.Error as e:
        print("Error deleting task:", e)



def main():
    conn = connect_to_database()
    if conn:
        while True:
            print("\nTask Manager Menu:")
            print("1. Create a task")
            print("2. Display all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date (YYYY-MM-DD): ")
                create_task(conn, title, description, due_date)

            elif choice == '2':
                display_tasks(conn)
            elif choice == '3':
                task_id = input("Enter task ID to update: ")
                due_date = input("Enter new due date (YYYY-MM-DD): ")
                update_due_date(conn, task_id, due_date)
            elif choice == '4':
                task_id = input("Enter task ID to delete: ")
                delete_task(conn, task_id)
            elif choice == '5':
                print("Exiting Program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        conn.close()

if __name__ == "__main__":
    main()
