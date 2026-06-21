contacts=[]
history = []
def  update_contact():
    update_name=input("enter name to update :")
    new_name=input("enter new name  :")
    for c in contacts :
         if c["name"] == update_name:
             c["name"] = new_name
             file=open("contacts.txt","w")
             for c in contacts :
                  file.write(c["name"] + "," + c["phone"] + "," + c["email"] + "\n")
             file.close()
             print("update sucessfully!!")
             return 
    print("name not found")

def delet_contact():
    del_name=input("enter name to delet :")
    for c in contacts :
        if c["name"] == del_name:
            contacts.remove(c)
            file=open("contacts.txt","w")
            for c in contacts :
                file.write(c["name"] + "," + c["phone"] + "," + c["email"] + "\n")
            file.close()
            print("Deleted sucessfully!!")
            return 
    print("contact not found ")

def view_history():
    if  not  history :
        print("no history available!")
    else:
        print("\n History")
        for h in history :
            print(h)

def load_contacts():

    file = open("contacts.txt", "r")

    for line in file:

        name, phone, email = line.strip().split(",")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

    file.close()
def add_contact() :
    name=input("Enter name :")
    phone=input("Enter phone :")
    email=input("Enter email :")
    contacts.append({"name":name,"phone":phone,"email":email})
    history.append("Added: " + name)

    file = open("contacts.txt", "a")
    file.write(name + "," + phone + "," + email + "\n")
    file.close()

def view_contact():
    if not contacts:
        print("no contacts yet.")
    else:
        for c in contacts:
            print("\n-------------------")
            print("👤 Name :", c['name'])
            print("📞 Phone:", c['phone'])
            print("📧 Email:", c['email'])
            print("-------------------")


def search_contact():
    query=input("search by name or phone :")
    found=False
    for c in contacts :
        if query.lower() in c["name"].lower() or query in c["phone"]:
           print("\n-------------------")
           print("👤 Name :", c['name'])
           print("📞 Phone:", c['phone'])
           print("📧 Email:", c['email'])
           print("-------------------")
           found=True
    if not found :
        print("❌ Contact not found.")

def main ():
    while True :
        print(r"""
   ____            _             _
  / ___|___  _ __ | |_ __ _  ___| |_
 | |   / _ \| '_ \| __/ _` |/ __| __|
 | |__| (_) | | | | || (_| | (__| |_
  \____\___/|_| |_|\__\__,_|\___|\__|

        📒 CONTACT MANAGEMENT SYSTEM
""")
        print("-"*25)

        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Update Contact")
        print("5️⃣ Delete Contact")
        print("6️⃣ View History")
        print("7️⃣ Exit")

        print("-"*25)

        choice=input("Enter Choice :")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delet_contact()
        elif choice == "6":
            view_history()
        elif choice =="7":
            print("👋 Goodbye!")    
            break
        else:
            print("Invalide Choice . Try Again ")

load_contacts()
main()
