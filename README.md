# 🔒 Encrypted Keylogger with Remote Transmission

## 📜 Project Description
This project is a Python-based **keylogger** designed to:
- Capture keystrokes in real-time.
- Encrypt the recorded data using the **Fernet encryption algorithm**.
- Transmit the encrypted file to a remote server for decryption and secure storage.

It demonstrates the integration of key programming concepts such as cryptography, socket programming, and file handling, making it a practical application of Python in cybersecurity.

> ⚠️ **Disclaimer**: This project is intended for educational purposes only. Do not deploy it in environments without explicit permission.

---

## 🎯 Purpose
The project is designed to:
- Demonstrate how to capture real-time keyboard events.
- Showcase file encryption using modern cryptographic techniques.
- Illustrate secure file transfer via socket programming.
- Implement client-server communication in Python.
- Explore file handling, hiding, and management.

---

## ✨ Features
1. **Real-Time Keystroke Logging**
   - Logs all keyboard activity, including key presses and releases.

2. **Secure Data Encryption**
   - Encrypts the recorded data using the **Fernet encryption algorithm**, ensuring privacy and security.

3. **File Hiding**
   - Hides the recorded file (`strokes.txt`) on Windows systems for secure management.

4. **Remote Transmission**
   - Transmits the encrypted file and its key to a remote server using socket programming.

5. **Robust Decryption**
   - The server decrypts the file only with the correct key, ensuring data integrity.

---

## 💻 Technologies Used
- **Python Libraries**:
  - `pynput`: Capturing keyboard events.
  - `cryptography`: Encrypting and decrypting files.
  - `socket`: Client-server communication.
  - `os` and `ctypes`: File handling and hiding.

---

## ⚙️ How It Works

### **1. Client-Side Workflow**
- **Keystroke Logging**:
  - The client uses the `pynput` library to capture keyboard events.
  - Records key presses/releases in `strokes.txt`.

- **Encryption**:
  - Encrypts the file using the **Fernet encryption algorithm**.
  - Generates a unique encryption key.

- **File Hiding (Windows Only)**:
  - Hides the encrypted file using the `ctypes` library to avoid casual detection.

- **Data Transmission**:
  - Sends the encrypted file and its encryption key to a remote server via a secure socket connection.

### **2. Server-Side Workflow**
- **Listening for Connections**:
  - The server listens for incoming connections using the `socket` library.

- **Receiving Data**:
  - Receives the encryption key and the encrypted file from the client.

- **Decryption**:
  - Decrypts the file using the **Fernet encryption algorithm** and the received key.

- **Storing Keystrokes**:
  - Saves the decrypted data in `capture.txt` for further analysis.
---


---

## 📚 Conclusion
This project demonstrates the capabilities of Python in creating secure, networked applications. By integrating keylogging, encryption, and remote data transmission, it serves as a foundational project for exploring **cybersecurity** and **ethical hacking** concepts.

---

This improved version is professional, visually structured, and includes all your points while enhancing readability. Let me know if you want further tweaks!

