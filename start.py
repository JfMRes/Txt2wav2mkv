import time 
from os import walk
import pyttsx3,subprocess,sys
lang='spanish'
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('voice', lang)
engine.setProperty('volume', 1)
path="  PATH  "
filenames=next(walk(path))
cont=0
inicio=time.time()
for i in filenames:
    cont+=1
    if type(i)==list:
        for a in range(0,len(i)):
            if type(i[a])==str:
                filename=path+'/'+i[a]
                if filename.split('.')[-1]=="txt":
                    print("Procesando:          "+ filename.split('/')[-1].split('.')[0])
                    inicio=time.time()
                    with open(filename, 'r', encoding="utf8") as file:
                        data = file.read().replace('\n', '')
                    
                    engine.save_to_file(data, filename.split('.')[0]+".wav")
                    engine.runAndWait()
                    fin=time.time()
                    print("Procesado en : " +str(int(fin-inicio))+ " segundos "+ filename.split('/')[-1].split('.')[0]+"\n")
filenames=next(walk(path))

for i in filenames:
    if type(i)==list:
        for a in range(0,len(i)):
            if type(i[a])==str:
                filename=path+"/"+i[a]
                if filename.split('.')[-1]=="wav":
                    name=filename.split('.')[-2]
                    print("Procesando video:           "+ filename.split('/')[-1].split('.')[0]+"\n\n")
                    inicio=time.time()
                    cmd = path.split('"\"')[0]+" & cd "+path.split('":"')[0]+" & "+'ffmpeg -y -i '+name+'.wav -i '+name+'.jpg   -filter:a aresample=async=1 -c:a flac -c:v copy '+name+'.mkv'
                    subprocess.call(cmd, shell=True)
                    fin=time.time()
                    print("Procesado en : " +str(int(fin-inicio))+ " seconds "+ filename.split('/')[-1].split('.')[0]+"\n\n")

print("\n\nHa tardado "+str(int(time.time()-inicio))+" segundos en procesar "+str(cont)+" archivos")
