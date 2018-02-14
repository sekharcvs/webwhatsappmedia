import os

# Add the current folder to the path at the end
os.environ["PATH"] += os.pathsep + os.getcwd()

os.system("pip install -r requirements.txt")