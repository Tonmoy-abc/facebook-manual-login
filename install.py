import os
import platform
try:
    import virtualenv
except:
    os.system('pip install virtualenv')

os.system('virtualenv env')
os.system('.\env\scripts\python -m pip install -r requirements.txt')
print("Install Successful!")
