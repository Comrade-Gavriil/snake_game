from client import client
import numpy as np
from time import sleep

class ai(client): #inherits client class

    def __init__ (self,key,url):
        super().__init__(key, url)
    
    @staticmethod
    def vector_add(v1,v2):
        return [ (v1[0]+v2[0]), (v1[1] + v2[1])]
    
    @staticmethod
    def vector_sub(v1,v2):
        return [ (v1[0]-v2[0]), (v1[1] - v2[1])]
    
    @staticmethod
    def vector_mult(v1,v2):
        return [ (v1[0]*v2[0]), (v1[1] * v2[1])]

    def coilision_aviodance(self, board):
        map_aviod = board
        snakes = self.heads[1:3]
        for head in snakes:
            connections = [[0,1],[0,-1],[1,0],[-1,0]]
            try:
                for edge in connections:
                    cord = self.vector_add(head,edge)
                    map_aviod[cord[0]][cord[1]] = 1
            except IndexError:
                pass
        return map_aviod


    def _make_path(self, src, dst, board): #uses the A* path find algo
        
        #could be manipulated or non manipulated board
        board = board
        
        #init positions
        x_0 = src[0]
        y_0 = src[1]

        open_set = [src] #explorable nodes
        came_from = {} #linking path back to src

        # gscore is the distance from the desination
        gScore_map = np.empty((len(board),len(board))) 
        gScore_map[:] = 1000

        gScore_map[x_0][y_0] = 0


        # numb to card and cord to numb are becuase im dumb
        
        def numb_to_cord (numb): #takes number and turns to cord
            a = np.arange(len(board)*len(board))
            a = np.resize(a,(len(board),len(board)))
            cord = np.where(a == numb)
            return [cord[0][0], cord[1][0]]
        
        def cord_to_numb(cord):#takes cord and turns to numb
            return cord[0]*len(board) + cord[1]

        
        
        def h(current): #basicaly manhaten distance, returns int
            dif = self.vector_sub(dst,current)
            return dif[0] + dif[1]

        

        def reconstucted_path(current): #make a path from the dst to the src, returns list
            totalpath = []
            totalpath.insert(0,current)
            while current in came_from.keys():
                current = came_from[current]
                totalpath.insert(0,current)
            
            cord_path = []

            for numb in totalpath:
                cord_path.append(numb_to_cord(numb))

            return cord_path
        
        def if_unrechable():
            connections = [[0,1],[0,-1],[1,0],[-1,0]]
            neighbors = []
            for edge in connections:
                    neighbor = self.vector_add(current, edge)
                    if neighbor[0] >= 0 and neighbor[0] <= 24 and neighbor[1] >=0 and neighbor[1] <= 24:
                        if board[neighbor[0]][neighbor[1]] < 0: #checks for colisions
                             neighbors.append(neighbor)
            
            for node in neighbors:
                fScore = fScore_map[node[0], node[1]]

                if fScore < best_value:
                    good_nodes  = [node]
                    best_value = fScore

                elif fScore == best_value:
                    good_nodes.append(node)
            
            best_node = None
            best_hScore = 100000

            #finds best node in matching node list
            for node in good_nodes:
                hScore = h(node)
                if hScore <= best_hScore:
                    best_node = node

            return best_node
            
        
        def best_fScore(): #finds the best fscore in the map, returns cord

            good_nodes = []
            best_value = 100000
            
            #finds best or equal nodes based on fscore
            for node in open_set:
                fScore = fScore_map[node[0], node[1]]

                if fScore < best_value:
                    good_nodes  = [node]
                    best_value = fScore

                elif fScore == best_value:
                    good_nodes.append(node)
            
            best_node = None
            best_hScore = 100000

            #finds best node in matching node list
            for node in good_nodes:
                hScore = h(node)
                if hScore <= best_hScore:
                    best_node = node

            return best_node

         # fscore is the distance from the desination and goal
        fScore_map = np.empty((len(board),len(board)))
        fScore_map[:] = 1000

        fScore_map[x_0][y_0] = h(src)

        
        while len(open_set) != 0: #A* algo
            
            current = best_fScore() #set current node to the node with the best score

            if current == dst: #checks to see if we are at our dst
                
                current_numb = cord_to_numb(current)
                return reconstucted_path(current_numb)
                
            
            open_set.remove(current) #removes bc the cord is expolored

            #entire chunk finds the niehbors to the node
            connections = [[0,1],[0,-1],[1,0],[-1,0]]
            neighbors = []
            for edge in connections:
                    neighbor = self.vector_add(current, edge)
                    if neighbor[0] >= 0 and neighbor[0] <= 24 and neighbor[1] >=0 and neighbor[1] <= 24:
                        if board[neighbor[0]][neighbor[1]] < 0: #checks for colisions
                             neighbors.append(neighbor)
                        


            for neighbor in neighbors: #intarates through each neighbor
                tentative_gScore = gScore_map[current[0]][[current[1]]] + 1 #probalbly gscore is just the gscore of the curent node and the distance wich is always 1



                if tentative_gScore < gScore_map[neighbor[0]][[neighbor[1]]]: #updates gscore on neighbor if it is lower
                    came_from[cord_to_numb(neighbor)] = cord_to_numb(current)
                    gScore_map[neighbor[0]][[neighbor[1]]] = tentative_gScore
                    fScore_map[neighbor[0]][[neighbor[1]]] = tentative_gScore + h(neighbor)

                    if neighbor not in open_set:
                        open_set.append(neighbor)

        
    

    def best_cordinate(self, map): 
        path = self._make_path(self.heads[0], self.food, map)
        up = [0,1]
        move = self.vector_add(self.heads[0], up)
        try:
            return path[1]
        except TypeError:
            print('help')
            return move

        
    def direction(self, cord): #forgoten parameter
        current_x_cord = self.heads[0][0] #self doesn't need to be used bc its a local var
        current_y_cord = self.heads[0][1] #self doesn't need to be used bc its a local var
      

        #use a couple of new lines to prevent cluter


        move_ep = cord 

        #the one part of the code that is executed almost perfectly
        if move_ep[0] == current_x_cord and move_ep[1] == current_y_cord:
            print ("Error: Current Position") #there is a way we raise errors

        elif move_ep[0] == current_x_cord and move_ep[1] > current_y_cord:
            return 3 #we can return this install of setting a var and the api calls for a direction id in souths case it is "3"
            
        elif move_ep[0] == current_x_cord and move_ep[1] < current_y_cord:
            return 1 # return 1

        elif move_ep[0] > current_x_cord and move_ep[1] == current_y_cord:
            return 2 #return 2

        elif move_ep[0] < current_x_cord and move_ep[1] == current_y_cord:
            return 0 #return 0
        
    def make_move(self):
        board = self.coilision_aviodance(self.board)
        move_cord = self.best_cordinate(board)

        move = self.direction(move_cord)
        # print(move)
        self.post_move(move)
    
    def run(self):
        while True:
            if self.move_needed:
                self.make_move()
    
    def best_move(self):
        dif_0 = self.vector_sub(self.food, self.heads[0])
        dif_1 = self.vector_sub(self.food, self.heads[1])
        dif_2 = self.vector_sub(self.food, self.heads[2])
        dif_3 = self.vector_sub(self.food, self.heads[3])
        
        self.destination = []
        if dif_0[0] + dif_0[1] > dif_1[0] + dif_1[1] or dif_0[0] + dif_0[1] > dif_2[0] + dif_2[1] or dif_0[0] + dif_0[1] > dif_3[0] + dif_3[1]:
            self.destination = [self.food]
        else:
            self.destination = [12,12]


# url = 'http://localhost:8080'
# key0 = 'key0'
# key1 = 'key1'
# key2 = 'key2'
# key3 = 'key3'
# snake0 = ai(key0,url)
# snake1 = ai(key1,url)
# snake2 = ai(key2,url)
# snake3 = ai(key3,url)

# while True:
#     snake0.make_move()
#     snake1.make_move()
#     snake2.make_move()
#     snake3.make_move()
