import psutil
import time
import os.path

while(True):

        #find
        path = "C:\\Program Files\\DyKnow\\"
        a = []

        dinos = []

        for roots, dirs, files in os.walk(path):
            a.append(files)


        for s in psutil.pids():
            try:
                    fil = psutil.Process(s).name()
            except:
                    fil = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.xxx"

        
            for fils in a:
                for dinoo in fils:
                    if(dinoo==fil):
                        #print(dinoo)
                        dinos.append(psutil.Process(s))
                        #print(psutil.Process(s).connections())

        #print(dinos)

        for din in dinos:
            port = din.pid
            #print(din.name())


            dino = True


            p = psutil.Process(port)


        #if connections only are 1 or thier is a not established one
            if(len(p.connections()) <= 1):
                dino = False
            else:
                for x in p.connections():
                    if(x.status != 'ESTABLISHED'):
                        dino = False

            #print(dino)
            #if dino
            if(dino==True):
                print dino
                print p.name()
                #p.kill() #use to mess with dyknow

        #time.sleep(5)
