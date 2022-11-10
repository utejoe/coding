import sqlite3

def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def add_ingredient(cursor):
    ingredient = input("Name of ingredient: ")
    num = input("Number in storage: ")
    description = input("description: ")
    sql = '''insert into ingredients (title, amount, description) values("{title}", {amount}, "{description}")'''
    sql = sql.format(title=ingredient, amount=num, description=description)
    cursor.execute(sql)
    print ("Added!")

def find_ingredien(cursor, item):
    sql = '''SELECT title, amount FROM ingredients WHERE title="{item}"'''
    sql = sql.format(item=item)
    results = cursor.execute(sql)
    items = cursor.fetchall()
    if len(items) == 0:
        print("Sorry, that ingredient wasn't found")
    else:
        for item in items:
            print(item[0], "-", item[1])

def list_ingredients(cursor):
    sql = '''SELECT title, amount FROM ingredients'''
    results = cursor.execute(sql)
    items = results.fetchall()
    print ("Items in the inventory")
    for item in items:
        print(item[0], '-', item[1])

def menu():
    print
    print("What do you want to do?")
    print("A - Add an ingredient")
    print("S - Search for an ingredient")
    print("L - List all ingredients")
    print("Q - Quit")
    choice = input('Choice [A/S/L/Q]: ')
    return choice[0].lower()

def main():
    conn = open_database('inventory.db')
    cursor = conn.cursor()

    while True:
        choice = menu()
        if choice == 'a':
            add_ingredient(cursor)
        elif choice == 's':
            item = input('What ingredient? ')
            find_ingredient(cursor=cursor, ingredient=item)
        elif choice == 'l':
            list_ingredients(cursor)
        elif choice == 'q':
            print("Goodbye")
            break
        else:
            print("Sorry, that's not valid")
        
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()