from client import client

class ai(client): #inherits client class

    def __init__ (self,key,url):
        super.__init__(key, url)

    def _direction_(self):
        self.current_x_cord = self.heads()[0][0]
        self.current_y_cord = self.heads()[0][1]
        current_x_cord = self.current_x_cord
        current_y_cord = self.current_y_cord
        self.direction = ""
        direction = self.direction
        self.ep_placeholder = []
        ep_placeholder = self.ep_placeholder
        if ep_placeholder[0] == current_x_cord and ep_placeholder[1] == current_y_cord:
            direction = "Error: Current Position"
        elif ep_placeholder[0] == current_x_cord and ep_placeholder[1] > current_y_cord:
            direction = "South"
        elif ep_placeholder[0] == current_x_cord and ep_placeholder[1] < current_y_cord:
            direction = "North"
        elif ep_placeholder[0] > current_x_cord and ep_placeholder[1] == current_y_cord:
            direction = "East"
        elif ep_placeholder[0] < current_x_cord and ep_placeholder[1] == current_y_cord:
            direction = "West"

    