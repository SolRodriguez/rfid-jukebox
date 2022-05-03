from importlib import import_module
import mercury
from tag import AlbumTags
from tag import TagReads
from spotifyapi import SpotifyAPI

device = "tmr:///dev/cu.usbmodem143201"
reader = mercury.Reader(device, baudrate=115200)


print(reader.get_model())
print(reader.get_supported_regions())

reader.set_region("NA")
reader.set_read_plan([1], "GEN2",  read_power=2000)

# epcs = list(map(lambda t: t.epc, reader.read()))
# print(epcs)

albums = AlbumTags()
spotify = SpotifyAPI()



run = True
while run:
    reads = reader.read()
    for t in reads: 
        try:
            tag = albums.add_tag(t)
            print(t.epc)
            print('rssi', t.rssi)
            spotify.play(t.epc, False)
           
            # print('avg', tag.avg)
            # print('reads', tag.readings)
            # tag.update(t.rssi)
            # print('reads updated', tag.readings)
            
            
            
        except:
            print("Can't read")
            # tag.update(0) #RSSI = 0
