from importlib import import_module
import mercury
from tag import JukeBox
from spotifyapi import SpotifyAPI

device = "tmr:///dev/cu.usbmodem141201"
reader = mercury.Reader(device, baudrate=115200)

print(reader.get_model())
print(reader.get_supported_regions())

reader.set_region("NA")
reader.set_read_plan([1], "GEN2",  read_power=2000)



# epcs = list(map(lambda t: t.epc, reader.read()))
# print(epcs)

CASE = 3 #num of tags being tested (1,2,3)

box = JukeBox()
spotify = SpotifyAPI()

run = True
if CASE == 1:
    while run:
        reads = reader.read()
        for t in reads:
            try:
                tag = box.add_tag(t)
                print(t.epc)
                print('freq', t.frequency)
                print('rssi', t.rssi)
                # print('avg', tag.avg)
                # print('reads', tag.readings)
                # tag.update(t.rssi)
                # print('reads updated', tag.readings)

                # play a song within RRSI > -40
                if (t.rssi >= -40) and (box.current != spotify.id2albums[t.epc]['id']): #not playing current song
                    spotify.play(box, t.epc, False)
                
            except:
                print("Can't read tag ")
                # tag.update(0) #RSSI = 0
elif CASE == 2:
    pass

elif CASE == 3:
    l = 0 # counts how many iterations it is stopped for
    prev_tag = None
    while run:
        reads = reader.read()
        for t in reads:
            try:
                if t.epc not in box.id2tags:
                    tag = box.add_tag(t)
                    print("should ont be in here")
                else:
                    tag = box.get_tag(t.epc)  

                    if tag.diff < 15: #tag has stopped 
                        #play id with max rssi
                        max_rssi = -1000
                        max_tag = None
                        for i in box.id2tags: #compare all the RSSIs
                            tag_val = box.id2tags[i] 
                            print(tag_val.tag.epc, tag_val.tag.rssi)
                            if tag_val.avg > max_rssi:
                                max_rssi = tag_val.avg
                                max_tag = tag_val
                                if prev_tag is None:
                                    prev_tag = max_tag

                        print("l")
                        print(l)
                        if (l > 15): #only play music if wheel constantly stagnant
                            print("wheel stopping")
                            spotify.play(max_tag.tag.epc, False) 
                            run = False
                            break
                        else:
                            if prev_tag != max_tag:
                                print("stuck here??")
                                l = 0
                            else:
                                prev_tag = 
                                print("increasing l")
                                l += 1
                    else:
                        print("here")
                        l = 0
                    
                    tag.update(t.rssi)

            except Exception as e: 
                print(e)


    

