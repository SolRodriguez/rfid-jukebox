import mercury
import numpy as np

class JukeBox():
    """Keeps all the tags and their reads together"""
    def __init__(self):
        #TODO: REFACTOR
        self.id2tags = {
            # b'E200204700000000000000C6' : Tag(),
            # b'E20020470000000000000D32' : Tag(),
            # b'E200204700000000000000B6' : Tag(),
            # b'E200204700000000000000B7' : 
            # , b'E200204700000000000000C3' : {"name": "Adele", "id": "spotify:album:6126O4XLYAfzU3961ziahP"},
            # b'30342CBD1C1D1390891F3759' : {"name": "Adele", "id": "spotify:album:21jF5jlMtzo94wbxmJ18aa"},
        }

    def add_tag(self, tag):
        """adds tag to dict"""
        new = TagReads(tag)
        read = self.id2tags.setdefault(tag.epc, new)
        return read
        
    

class TagReads():
    """Keeps track of the average RSSI for each tag from its previous 3 rdgs"""
    def __init__(self, tag):
        self.tag = tag
        self.readings = [0,0,0]
        self.avg = np.mean(self.readings)
        self.diff = np.abs(self.readings[-1]-self.readings[0])

    def update(self, rssi):
        """updates the running average"""
        new_rdgs = self.readings[1:]+[rssi]
        self.avg = np.mean(new_rdgs)
        self.readings = new_rdgs
        return
    



    
