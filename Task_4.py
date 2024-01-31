def input_error(func):
    """Декоратор для обробки помилок введення користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Enter a valid command or argument."

    return inner

@input_error
def add_contact(args, contacts):
    """Додавання контакту."""
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    """Отримання номеру телефону."""
    if len(args) != 1:
        raise ValueError
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def list_contacts(args, contacts):
    """Виведення списку контактів."""
    if len(args) != 0:
        raise ValueError
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

if __name__ == "__main__":
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower().split()
        if command:
            action = command[0]
            args = command[1:]
            if action == "add":
                print(add_contact(args, contacts))
            elif action == "phone":
                print(get_phone(args, contacts))
            elif action == "all":
                print(list_contacts(args, contacts))
            else:
                print("Enter a valid command.")

