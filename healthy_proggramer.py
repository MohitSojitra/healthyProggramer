import pygame
import datetime
import time

def playMusic(music):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
   
    pygame.mixer.music.play(-1)
    while True:
        
        msg = input()
        if msg == "stop":
            pygame.mixer.music.stop()
            break
        

def logMaintain(msg):
    l = open("logs.txt", "a")
    l.write(f"[{datetime.datetime.now()}]   [{msg}] \n")
    l.close()


if __name__ == '__main__':
    total_time = 0;
    while True:
        time1 = time.time()

        time.sleep(1800)
        total_time = time.time() - time1 + total_time;
        
        print(f"\n \t you work total \t{total_time // 3600} hour {round(total_time // 60)} minutes\n")
        print("\t \t \tplease drink water \n")
        print("\t \t \twrite stop to music. \n")

        playMusic("drink water.mp3")
        logMaintain("drank watter")

        time1 = time.time();

        time.sleep(1800)
        total_time = time.time() - time1 + total_time;

        print(f"\t \t \tyou work total {total_time // 3600} hour {round(total_time // 60)} minutes\n")
        print("\t \t \tplease do excersise\n")
        print("\t \t \t write stop to music. \n")

        playMusic("excersise.mp3")
        logMaintain("exersise done \n")


    





