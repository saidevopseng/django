# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("127.0.0.1", 9999))  # Connect to Server

# while True:
#     msg = input("You: ")
#     client.send(msg.encode())
#     if msg.lower() == "exit":
#         print("Chat ended.")
#         break
#     reply = client.recv(1024).decode()
#     print("Server:", reply)

# client.close()
##############################################################
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            chat_display.insert(tk.END, f"Server: {message}\n")
        except:
            break

def send_message():
    message = message_entry.get()
    chat_display.insert(tk.END, f"You: {message}\n")
    client_socket.send(message.encode("utf-8"))
    message_entry.delete(0, tk.END)

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))  # Change IP if needed

# GUI setup
root = tk.Tk()
root.title("Client Chat")

chat_display = scrolledtext.ScrolledText(root, width=50, height=20)
chat_display.pack()

message_entry = tk.Entry(root, width=40)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start receiving messages in a new thread
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
