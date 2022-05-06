import mercury
import numpy as np

class JukeBox():
    """Keeps all the tags and their reads together"""
    def __init__(self):
        self.current = "" #epc of the tag whose album is currently playing
        self.queued = "" #epc of next song to play
        self.max_tag = None #epc of the tag w largest tag.avg

        self.times_seen = 0
        

        self.id2tags = {
            # b'E200204700000000000000C6' : Tag(),
            # b'E20020470000000000000D32' : Tag(),
            # b'E200204700000000000000B6' : Tag(),
            # etc.
        }



    def add_tag(self, tag):
        """adds tag to dict"""
        new = TagReads(tag)
        read = self.id2tags.setdefault(tag.epc, new)
        return read
    
    def set_current(self, album):
        "sets currently playing album"
        self.current = album
        return

    def get_tag(self,epc):
        "returns Tag object for a specific RFID tag (using its epc)"
        return self.id2tags[epc]
    
    def update_max_tag(self):
        "updates tag w max avg rssi"
        max_avg = float('-Inf')
        for epc, tag  in self.id2tags.items():

            if tag.avg > max_avg:
                max_avg = tag.avg
                self.max_tag = epc
                self.queued = epc

                # print(self.max_tag,self.queued)
                if (self.max_tag != self.queued):
                    self.queued = epc
                    self.times_seen = 0
                else:
                    self.times_seen += 1
                    
        return 




class TagReads():
    """Keeps track of the average RSSI for each tag from its previous 3 rdgs"""
    def __init__(self, tag):
        self.tag = tag
        self.readings = [0,0,0]
        self.avg = np.mean(self.readings)
        self.diff = 0

    def update(self, rssi):
        """updates the running average"""
        new_rdgs = self.readings[1:]+[rssi]
        self.avg = np.mean(new_rdgs)
        self.readings = new_rdgs
        self.diff = np.abs(self.readings[-1]-self.readings[0])
        return
    



    
