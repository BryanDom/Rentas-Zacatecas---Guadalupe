import os
import shutil

for root, dirs, files in os.walk('.'):
    for dir in dirs:
        if dir == '__pycache__':
            shutil.rmtree(os.path.join(root, dir))
