# 🔒 Encrypted Keylogger with Remote Transmission

## 📜 Project Description
This project is a Python-based **keylogger** designed to:
- Capture keystrokes in real-time.
- Encrypt the recorded data using the **Fernet encryption algorithm**.
- Transmit the encrypted file to a remote server for decryption and secure storage.

It demonstrates the integration of key programming concepts such as cryptography, socket programming, and file handling, making it a practical application of Python in cybersecurity.

> ⚠️ **Disclaimer**: This project is for educational purposes only. Unauthorized use of keyloggers or any form of malicious surveillance is illegal and unethical. Always seek explicit consent before deploying any monitoring software.

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

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `pynput`
  - `cryptography`
  - `python-dotenv`

### Setup
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
2. Install all required dependencies:
   ```bash
   pip install -r requirements.txt
3. Set your server and port in the `.env` file:
   ```bash
   MY_SERVER=your_server_ip
   MY_PORT=your_server_port
4. Run the client and server:
   ```bash
   python client.py
   python server.py


## 📚 Conclusion
This project demonstrates the capabilities of Python in creating secure, networked applications. By integrating keylogging, encryption, and remote data transmission, it serves as a foundational project for exploring cybersecurity and ethical hacking concepts.
