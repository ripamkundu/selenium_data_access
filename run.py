import os

os.system("python -m venv .venv")
os.system(".venv/Scripts/activate")
os.system("pip install -r requirements.txt")
os.system("python main.py")
