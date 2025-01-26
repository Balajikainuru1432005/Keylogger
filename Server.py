import socket
from cryptography.fernet import Fernet  # For decrypting the received file
import os  # For accessing environment variables
from dotenv import load_dotenv  # To load environment variables from the .env file
# Load environment variables from .env file
load_dotenv()


# Function to receive the encrypted file from the client
def receive_file(client_connection):
    try:
        key = client_connection.recv(1024)
        with open("capture.txt", "ab") as file:
            while True:
                chunk = client_connection.recv(1024)
                if not chunk:
                    break
                file.write(chunk)
        print("File received successfully.")
    except Exception as e:
        print(f"Error receiving file: {e}")
    return key


# Function to establish the server connection
def connection():
    server = os.getenv('MY_SERVER')
    port = int(os.getenv('MY_PORT'))
    try:
        # Set up the server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server, port))
        server_socket.listen(1)
        print("Server is listening for connections...")
        return server_socket
    except Exception as e:
        print(f"Error setting up the server: {e}")
        exit(1)


# Function to decrypt the received file using the provided key
def decrypt_file(key, file_path):
    try:
        f = Fernet(key)


        with open(file_path, "rb") as file:
            encrypted_data = file.read()


        decrypted_data = f.decrypt(encrypted_data)


        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        print("Decryption successful.")
    except Exception as e:
        print(f"Decryption not successful: {e}")


# Main program to set up the server and handle communication
if __name__ == "__main__":
    server_socket = connection()
    try:
        # Accept the incoming connection from the client
        client_connection, address = server_socket.accept()
        print(f"Connection established with {address}")

        key = receive_file(client_connection)


        decrypt_file(key, "capture.txt")
    except Exception as e:
        print(f"Error during communication: {e}")
    finally:

        client_connection.close()
        server_socket.close()
        print("Server connection closed.")
