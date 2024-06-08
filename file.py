import os

sys = os.uname()
dir = os.getcwd()
home = os.listdir("/home")
c_user = os.getlogin()

print(f"System Information: {sys}", f"Current Directory: {dir}", f"Home Directories: {home}", f"Current user logged in: {c_user}")
