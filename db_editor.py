import sqlite3


connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name text,address text,phone text,company text)")

choice = None

while choice != "6":
    print("1) Display Contacts")
    print("2) Add Contact")
    print("3) Update Contact")
    print("4) Delete contact")
    print("5) Query")
    print("6) Quit")
    choice = input("> ")
    print(" ")
    print(" ")

    if choice == "1":

        cursor.execute("SELECT * FROM contacts");

        # attempt to not hard code the index numbers for fetch all
        # db_len = len(cursor.fetchall())
        #db_index_range = range(db_len)

        for i in cursor.fetchall():
            print(i[0])
            print(i[1])
            print(i[2])
            print(i[3])


    elif choice =="2":
        # add new contact
        print("Adding new contact")
        print(" ")
        
        name = input(" Name: ")
        address = input(" Address: ")
        phone = input(" Phone: ")
        company = input(" Company: ")
        print(" ")

        values = (name, address, phone, company)

        cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", values)
        connection.commit()


    elif choice =="3":
        print("Update Contact")
        name = input("WHo do you want to update?: ")
        update_choice = None
        
        print("What do you want to update?")
        print("1) Name")
        print("2) Address")
        print("3) Phone")
        print("4) Company")
        update_choice = input("> ")
        print(" ")
        print(" ")

        if update_choice == "1":
            new = input("enter new name: ")
            values = (new,name)

            cursor.execute("UPDATE contacts SET name = ? WHERE name = ?", values)
            connection.commit()


        if update_choice == "2":
            new = input("enter address: ")

            values = (new,name)

            cursor.execute("UPDATE contacts SET address = ? WHERE name = ?", values)
            connection.commit()

        if update_choice == "3":
            new = input("enter phone: ")

            values = (new,name)

            cursor.execute("UPDATE contacts SET phone = ? WHERE name = ?", values)
            connection.commit()

        if update_choice == "4":
            new = input("enter company: ")

            values = (new,name)

            cursor.execute("UPDATE contacts SET company = ? WHERE name = ?", values)
            connection.commit()






    elif choice =="4":
        # delete a contact

        name = input("Who do you want to delete? ")
        # why does this need a comma after name?
        values = (name, )

        cursor.execute("DELETE FROM contacts WHERE name = ?", values)
        connection.commit()
        



    elif choice =="5":
        print("What do you want to Query?")
        print("enter fields (such as name). When done enter Q")
        
        q_choice = None
        query_list = []
        while q_choice != "Q" and q_choice != "q":
            query_list.append(q_choice)
            
            q_choice = input("> ")

            

        query_list.pop(0)
        print("")

        select_string = ','.join(query_list)
        print(select_string) 

        cursor.execute("SELECT "+select_string+" FROM contacts")

        q_results = cursor.fetchall()

        for i in q_results:
            print(i[0] + " , " + i[1])

        print("")

        