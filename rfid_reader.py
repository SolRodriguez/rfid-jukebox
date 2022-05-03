from importlib import import_module
import mercury
from tag import JukeBox
from spotifyapi import SpotifyAPI

device = "tmr:///dev/cu.usbmodem143201"
reader = mercury.Reader(device, baudrate=115200)

print(reader.get_model())
print(reader.get_supported_regions())

reader.set_region("NA")
reader.set_read_plan([1], "GEN2",  read_power=2000)



# epcs = list(map(lambda t: t.epc, reader.read()))
# print(epcs)

CASE = 1 #num of tags being tested (1,2,3)

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
                print("Can't read tag "+ t.epc)
                # tag.update(0) #RSSI = 0
elif CASE == 2:
    pass
else CASE == 3:
    pass

