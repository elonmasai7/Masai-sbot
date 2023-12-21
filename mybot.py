import datetime
import os
import sqlite3
import webbrowser
import sqlite3

def main():
    try:
        connection = sqlite3.connect('chatbot.db')
        cursor = connection.cursor()

        # Check if the user exists
        user_name = 'Elon Musk'
        user_id = cursor.execute("""SELECT id FROM users WHERE name = ?""", (user_name,)).fetchone()

        # If the user exists, send a greeting message
        if user_id:
            print("Hello, {}! How are you today?".format(user_name))
        else:
            print("Sorry, I don't recognize you. Would you like to create an account?")

        connection.close()
    except sqlite3.Error as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

# Create the database
connection = sqlite3.connect('bot_database.db')
cursor = connection.cursor()

# Create the tables
cursor.execute("""Elon masai users (
    elon_masai_table = {
    "English": ["Hello", "Thank you", "Goodbye", "Yes", "No", "Water", "Food", "House", "Car", "Money"],
    "Swahili": ["Hujambo", "Asante", "Kwaheri", "Ndiyo", "Hapana", "Maji", "Chakula", "Nyumba", "Gari", "Pesa"]
}
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS plans (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date TEXT,
    plans TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    task TEXT,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)""")

# Insert the super admin user
cursor.execute("""INSERT OR IGNORE INTO users (name, email, password)
    VALUES ('Elon Masai', 'elonmasai7@gmail.com', 'password')""")

# Commit the changes to the database
connection.commit()

# Define the bot's functions
def greet_user():
    """Greet the user by name."""
    name = input("What is your name? ")
    print(f"Good morning, {name}!")

def get_user_plans():
    """Get the user's plans for the day."""
    date = input("What is today's date? (YYYY-MM-DD) ")
    plans = input("What are your plans for today? ")
    return date, plans

def add_plans_to_database(user_id, date, plans):
    """Add the user's plans to the database."""
    cursor.execute("""INSERT INTO plans (user_id, date, plans)
        VALUES (?, ?, ?)""", (user_id, date, plans))
    connection.commit()

def get_user_tasks():
    """Get the user's tasks for the day."""
    tasks = input("What tasks do you need to complete today? (separate tasks with commas) ")
    return tasks

def add_tasks_to_database(user_id, tasks):
    """Add the user's tasks to the database."""
    for task in tasks.split(','):
        cursor.execute("""INSERT INTO tasks (user_id, task, status)
            VALUES (?, ?, ?)""", (user_id, task, 'incomplete'))
    connection.commit()

def research_topic():
    """Research a topic on the internet."""
    topic = input("What topic would you like to research? ")
    webbrowser.open(f"https://www.google.com/search?q={topic}")

def learn_from_user():
    """Learn from the user's input."""
    input("What have you learned today? ")

# Start the bot

    # Get the current user
    user_id = cursor.execute("""SELECT id FROM users WHERE name = 'Elon Masai'""").fetchone()[0]

    # Greet the user
    greet_user()

    # Get the user's plans fdef main():or the day
    date, plans = get_user_plans()

    # Add the user's plans to the database
    add_plans_to_database(user_id, date, plans)

    # Get the user's tasks for the day
    tasks = get_user_tasks()

    # Add the user's tasks to the database
    add_tasks_to_database(user_id, tasks)

    # Research a topic
    research_topic()

    # Learn from the user
    learn_from_user()

# Start the bot when the computer is powered on
if __name__ == "__main__":
    main()