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
    
    if file == 'archives' or file == 'video' or file == 'audio' or file == 'documents' or file == 'images':
        continue
    if file.lower().endswith('.jpg') == True or file.lower().endswith('.png') == True or file.lower().endswith('.jpeg') == True or file.lower().endswith('.svg') == True:
        shutil.move(file, 'images')
        
    if file.lower().endswith('.pdf') == True or file.lower().endswith('.txt') == True or file.lower().endswith('.doc') == True or file.lower().endswith('.docx') == True or file.lower().endswith('.xlsx') == True or file.lower().endswith('.pptx') == True:
        shutil.move(file, 'documents')
    
    if file.lower().endswith('.avi') == True or file.lower().endswith('.mp4') == True or file.lower().endswith('.mov') == True or file.lower().endswith('.mkv') == True:
        shutil.move(file, 'video')
        
    if file.lower().endswith('.mp3') == True or file.lower().endswith('.ogg') == True or file.lower().endswith('.wav') == True or file.lower().endswith('.amr') == True:
        shutil.move(file, 'audio')
        
    if file.lower().endswith('.zip') == True or file.lower().endswith('.gz') == True or file.lower().endswith('.tar') == True:
        shutil.move(file, 'archives')
    else: 
        continue 