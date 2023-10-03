from normalize import normalize
import os
import shutil
from pathlib import Path

Path('archives').mkdir(exist_ok=True)
Path('video').mkdir(exist_ok=True)
Path('audio').mkdir(exist_ok=True)
Path('documents').mkdir(exist_ok=True)
Path('images').mkdir(exist_ok=True)


for file in os.listdir():
    for name in file:
        normalize(name)
    
    if file in ('archives', 'video', 'audio', 'documents', 'images'):
        continue
    if file.lower().endswith(('.jpg', '.png', '.jpeg', '.svg')) == True:
        shutil.move(file, 'images')
        
    if file.lower().endswith(('.pdf', '.txt', '.doc', '.docx', '.xlsx', '.pptx')) == True:
        shutil.move(file, 'documents')
    
    if file.lower().endswith(('.avi', '.mp4', '.mov', '.mkv')) == True:
        shutil.move(file, 'video')
        
    if file.lower().endswith(('.mp3', '.ogg', '.wav', '.amr')) == True:
        shutil.move(file, 'audio')
        
    if file.lower().endswith(('.zip', '.gz', '.tar')) == True:
        shutil.move(file, 'archives')
    else: 
        continue 
