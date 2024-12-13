import keyboard
import uuid
import time
from PIL import Image
from mss import mss


mon={"top":500,"left":680,"width":250,"height":125}

sct=mss()

i=0


def record_screen(recordin_id,key):
    global i
    
    i+=1
    
    print("{}:{}".format(key,i))
    img=sct.grab(mon)
    im=Image.frombytes("RGB",img.size,img.rgb)
    im.save("./img/{}_{}_{}.png".format(key,recordin_id,i))
    
is_exit=False

def exit():
    global is_exit
    is_exit=True

keyboard.add_hotkey("esc",exit)


recordin_id=uuid.uuid4()
while True:
    
    if is_exit:break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(recordin_id,"up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(recordin_id,"down") 
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            record_screen(recordin_id,"right")
            time.sleep(0.1)
    except RuntimeError:continue    
            
        
        
        
        
        
        
        
        