contacts=[]
def add_contact() :
    name=input("Enter name :")
    phone=input("Enter phone :")
    email=input("Enter email :")
    contacts.append({"name":name,"phone":phone,"email":email})

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
        print("\n📇 CONTACT MANAGER")
        print("-"*25)

        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Exit")

        print("-"*25)

        choice=input("Enter Choice :")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalide Choice . Try Again ")

main()