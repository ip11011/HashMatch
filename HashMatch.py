import hashlib

# Load passwords from passwords.txt
try:
    with open("passwords.txt", "r", encoding="utf-8") as file:
        password_list = []
        print("Loading passwords.txt...")
        for line in file:
            password_list.append(line.strip())
        print("Loaded successfully")
except FileNotFoundError:
    print("❌ passwords.txt not found!")
    exit()

user_hash = input("Enter SHA-256 hash: ").strip().lower()

for password in password_list:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password == user_hash:
        print("\n✅ Hash matched!")
        print("🔓 Original password:", password)
        break
else:
    print("No matching passwords in the list :<")
    print("search for a good list dumbo")

# Pause the program so the window doesn't close
input("\nPress Enter to exit...")
