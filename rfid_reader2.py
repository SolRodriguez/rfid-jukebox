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

CASE = 2 #num of tags being tested (1,2,3)

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
                print('rssi', t.rssi)

                spotify.play(t.epc, False)
            
                # print('avg', tag.avg)
                # print('reads', tag.readings)
                # tag.update(t.rssi)
                # print('reads updated', tag.readings)
                
            except:
                print("Can't read tag "+ t.epc)
                tag.update(0) #RSSI = 0
elif CASE == 2:
    playing_song = False
    playing_epc1 = None
    playing_epc2 = None
    rssi1 = 0
    rssi2 = 0
    higher_epc = None
    while run:
        reads = reader.read()
        if not playing_song:
            for t in reads:
                tag = box.add_tag(t)
                print('rssi', t.rssi)
                print('epc1', t.epc)
                if t.rssi > -40:
                    playing_epc1 = t.epc
                    playing_epc2 = spotify.play2(playing_epc1, False)
                    playing_song = True

        if playing_song:
            for t in reader.read():
                if t.epc == playing_epc1:
                    rssi1 = t.rssi
                    tag = box.get_tag(playing_epc1)
                    tag.update(t.rssi)
                    print('rssi1', t.rssi)
                elif t.epc == playing_epc2:
                    rssi2 = t.rssi
                    tag = box.get_tag(playing_epc2)
                    tag.update(t.rssi)
                    print('rssi2', t.rssi)

            print('avg1', box.get_tag(playing_epc1).avg)
            print('avg2', box.get_tag(playing_epc2).avg)
            if box.get_tag(playing_epc1).avg > box.get_tag(playing_epc2).avg:
                new_higher_epc = playing_epc1
                print('epc1 is higher')
            else:
                new_higher_epc = playing_epc2
                print('epc2 is higher')

            if higher_epc is None:
                higher_epc = new_higher_epc
            elif new_higher_epc != higher_epc:
                higher_epc = new_higher_epc
                print('pause song')
                spotify.pause()
                break
else:
    pass

