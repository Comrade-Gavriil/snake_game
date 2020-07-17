from client import client

class ai(client): #inherits client class

    def __init__ (self,key,url):
        super.__init__(key, url)
    
    def _make_path(self):
        
        food = self.food
        board = self.board
        heads = self.heads

        
