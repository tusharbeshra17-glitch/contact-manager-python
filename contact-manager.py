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
            print(f"name:{c['name']},phone:{c['phone']},email:{c['email']},")


def search_contact():
    query=input("search by name or phone :")
    found=False
    for c in contacts :
        if query.lower() in c["name"].lower() or query in c["phone"]:
            print(f"name:{c['name']},phone:{c['phone']},email:{c['email']}")
            found=True
    if not found :
        print("❌ Contact not found.")

def main ():
    while True :
        print("\n=====CONTACT-APP=====")
        print("\n1.Add Contact")
        print("\n2.View Contact")
        print("\n3.Search Contact")
        print("\n4.Exit")

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