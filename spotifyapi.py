import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAPI():
    """Spotify API"""
    def __init__(self):
        self.scope = "user-modify-playback-state"  
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = 'd9109990854044c580294e9f4cf2ce28',
                                                client_secret = 'fd1fd05cf4e34b2686908d9bb21e0cf7',
                                                redirect_uri = "http://localhost/8080", 
                                                scope = self.scope
                                                ))
        self.jasmin_device_id = "7031c89bdad1f7dbd7dc8a90c39e34370de3b784"
        self.sol_device_id = "fb7706bb9b901a4410cfa232b2720fd7d9d5110f"
        self.device = self.jasmin_device_id

        self.id2albums = {
            b'E200204700000000000000C6' : {"name": "Adele", "id": "spotify:album:21jF5jlMtzo94wbxmJ18aa"},
            b'E20020470000000000000D32' : {"name": "Michael Jackson", "id": "spotify:album:2ANVost0y2y52ema1E9xAZ"},
            b'E200204700000000000000B6' : {"name": "70s Hits", "id": "spotify:playlist:00KjsgI9t715OJFEUFziGJ"},
            b'E200204700000000000000B7' : {"name": "Adele", "id": "spotify:album:21jF5jlMtzo94wbxmJ18aa"} #TODO: Change
            # , b'E200204700000000000000C3' : {"name": "Adele", "id": "spotify:album:6126O4XLYAfzU3961ziahP"},
            # b'30342CBD1C1D1390891F3759' : {"name": "Adele", "id": "spotify:album:21jF5jlMtzo94wbxmJ18aa"},
        }
    
    def play(self, epc, debug = False):
        """plays album of designated tag"""
        album = self.id2albums[epc]['id']
        name = self.id2albums[epc]['name']
        if debug:
            # print(epc)
            print('playing ', name)
        else:
            self.sp.start_playback(device_id = self.device,
                                    context_uri = album)
        return
    

    def adjust_vol(self, volume, debug = False):
        """adjusts the volume of song currently playing"""
        if debug:
            print(volume)
        else:
            self.sp.volume(volume,device_id=self.device)

        return
    
    def pause(self, debug= False):
        """pauses or plays song currently playing"""
        if debug:
            print('pause')
        else:
            self.sp.pause_playback(device_id=self.device)
        return


song = "spotify:artist:3VNITwohbvU5Wuy5PC6dsI"
#{"uris": ["spotify:track:561F1zqRwGPCTMRsLsXVtL", "spotify:track:51ueZKM83MTRv9rgiDfI6Y"]}


