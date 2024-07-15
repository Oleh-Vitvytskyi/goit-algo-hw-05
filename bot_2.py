def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me name and phone please."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact phone number updated."
    else:
        raise KeyError

@input_error   
def get_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError

@input_error    
def list_all_contacts(contacts):
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(list_all_contacts(contacts))
        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()