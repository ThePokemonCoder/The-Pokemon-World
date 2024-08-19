import sqlite3

# Define the database file
DATABASE_FILE = 'pokemon.db'
DATABASE2_FILE = 'trainers_potions.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

conn = sqlite3.connect(DATABASE2_FILE)
cursor = conn.cursor()

# Create a table for Pokémon
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type_1 TEXT NOT NULL,
            type_2 TEXT,
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            sp_attack INTEGER,
            sp_defense INTEGER,
            speed INTEGER
        )
    ''')
    conn.commit()
    

# Insert Pokémon data
def insert_pokemon():
    print("To save details, please enter the nessecary information:")
    name = input("Name: ")
    type_1 = input("Type 1: ")
    type_2 = input("Type 2 (or leave blank if none): ")
    hp = int(input("HP(use numerical values): "))
    attack = int(input("Attack(use numerical values): "))
    defense = int(input("Defense(use numerical values): "))
    sp_attack = int(input("Special Attack(use numerical values): "))
    sp_defense = int(input("Special Defense(use numerical values): "))
    speed = int(input("Speed(use numerical values): "))

    cursor.execute('''
        INSERT INTO pokemon (name, type_1, type_2, hp, attack, defense, sp_attack, sp_defense, speed)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, type_1, type_2 if type_2 else None, hp, attack, defense, sp_attack, sp_defense, speed))
    conn.commit()
    print(f"Pokémon {name} added successfully.")

# View all Pokémon data
def view_pokemon():
    cursor.execute('SELECT * FROM pokemon')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Type 1: {row[2]}, Type 2: {row[3]}, HP: {row[4]}, Attack: {row[5]}, Defense: {row[6]}, Special Attack: {row[7]}, Special Defense: {row[8]}, Speed: {row[9]}")
    else:
        print("No Pokémon found.")

# Add the Trainers and Potions

# Create a table for Trainers
def create_trainer_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trainer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            badges INTEGER
        )
    ''')
    conn.commit()
    print("Trainer table created successfully.")

# Create a table for Potions
def create_potion_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS potion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            effect TEXT NOT NULL,
            potency INTEGER
        )
    ''')
    conn.commit()
    print("Potion table created successfully.")

# Insert Trainer data
def insert_trainer():
    print("To save trainer details, please enter the necessary information:")
    name = input("Trainer Name: ")
    age = int(input("Age(use numerical values): "))
    badges = int(input("Number of Badges(use numerical values): "))

    cursor.execute('''
        INSERT INTO trainer (name, age, badges)
        VALUES (?, ?, ?)
    ''', (name, age, badges))
    conn.commit()
    print(f"Trainer {name} added successfully.")

# Insert Potion data
def insert_potion():
    print("To save potion details, please enter the necessary information:")
    name = input("Potion Name: ")
    effect = input("Effect: ")
    potency = int(input("Potency Level: "))

    cursor.execute('''
        INSERT INTO potion (name, effect, potency)
        VALUES (?, ?, ?)
    ''', (name, effect, potency))
    conn.commit()
    print(f"Potion {name} added successfully.")

# View the Trainers

def view_trainers():
    cursor.execute('SELECT * FROM trainer')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Badges: {row[3]}")
    else:
        print("No trainers found.")

# View the Potions

def view_potions():
    cursor.execute('SELECT * FROM potion')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Effect: {row[2]}, Potency: {row[3]}")
    else:
        print("No potions found.")




# View the update patch notes

def update_notes():
    print("This is the offical update notes for the World of Pokemon")
    print("Update 1.0 - The application was realeased in our first update")
    print("Update 1.01 - Brand new user interaction was created")
    print("Update 1.1 - Brand new trainers and potions were added, to enhance the experience")
    print("Update 1.2 - Developer Ideas input usage : Easier Usage(In Development)")
    print("Update 1.3 - Coming Soon")

    
    
# Main function to execute the script
def main():
    create_table()
    create_trainer_table()
    create_potion_table()
    
    while True:
        print('')
        print('')
        print("\n. Welcome to the world of Pokemon")
        print("Menu:")
        print("1. Add a Pokémon")
        print("2. View all Pokémon")
        print("3. Add Trainers")
        print("4. View the trainers")
        print("5. Add the potions")
        print("6. View the potions")
        print("7. Exit")
        print("8. Update Patch Notes")
        
        choice = input("Choose an option (1/2/3/4/5/6/7/8): ")
        
        if choice == '1':
            insert_pokemon()
        elif choice == '2':
            view_pokemon()
        elif choice == '3':
            insert_trainer()
        elif choice == '4':
            view_trainers()
        elif choice == '5':
            insert_potion()
        elif choice == '6':
            view_potions()
        elif choice == '7':
            print("Exiting...  Credits all go to the maker : Pranav Kunjoor")
            conn.close()
            break
        elif choice == '8':
           update_notes()
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, 7, or 8")

if __name__ == "__main__":
    main()
