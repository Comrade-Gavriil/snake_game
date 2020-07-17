from client import client

class ai(client): #inherits client class

    def __init__ (self,key,url):
        super.__init__(key, url)
    
    @staticmethod
    def vector_add(v1,v2):
        return [ (v1[0]+v2[0]), (v1[1] + v2[1])]
    
    @staticmethod
    def vector_sub(v1,v2):
        return [ (v1[0]-v2[0]), (v1[1] - v2[1])]
    
    @staticmethod
    def vector_mult(v1,v2):
        return [ (v1[0]*v2[0]), (v1[1] * v2[1])]

    

    def _make_path(self, scr, dst):
        
        rel_pos = self.vector_sub(dst, scr)

        def direction(rel):
            direction = []
            for cord in cords:
                if cord > 1:
                    direction.append(1)
                elif cord == 0:
                    direction.append(0)
                elif cord == 0:
                    direction.append(-1)
        
        move_rel_cords = direction(rel_pos)

        








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

