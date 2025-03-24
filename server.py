# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("127.0.0.1", 9999))  # Localhost, Port 9999
# server.listen(1)

# print("Waiting for a connection...")
# conn, addr = server.accept()
# print(f"Connected to {addr}")

# while True:
#     msg = conn.recv(1024).decode()
#     if msg.lower() == "exit":
#         print("Chat ended.")
#         break
#     print("Client:", msg)
#     reply = input("You: ")
#     conn.send(reply.encode())

# conn.close()
# server.close()
##################################################
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive_messages():
    while True:
        try:
            message = server_socket.recv(1024).decode("utf-8")
            chat_display.insert(tk.END, f"Client: {message}\n")
        except:
            break

def send_message():
    message = message_entry.get()
    chat_display.insert(tk.END, f"You: {message}\n")
    server_socket.send(message.encode("utf-8"))
    message_entry.delete(0, tk.END)

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))  # Listen on all interfaces
server.listen(1)
print("Waiting for connection...")

server_socket, addr = server.accept()
print(f"Connected with {addr}")

# GUI setup
root = tk.Tk()
root.title("Server Chat")

chat_display = scrolledtext.ScrolledText(root, width=50, height=20)
chat_display.pack()

message_entry = tk.Entry(root, width=40)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start receiving messages in a new thread
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()

