from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

i = 9
G = [0, 255, 0]


for i in range(9,-1,-1): 
    
    G[0] += 20
    G[1] -= 20
    G[2] = 0
    sense.show_letter(str(i), G)
    sleep(1)
    i -= i
    
    
    if i == 0:
        sense.show_letter('0', [255,0,255])
        





R = [255, 0, 0]
X = [0, 0, 0]
