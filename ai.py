from client import client
import numpy as np

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

    

    def _make_path(self, src, dst, map): #uses the A* path find algo
        
        #could be manipulated or non manipulated board
        board = map
        
        #init positions
        x_0 = src[0]
        y_0 = src[1]

        open_set = [src] #explorable nodes
        came_from = {} #linking path back to src

        # gscore is the distance from the desination
        gScore_map = np.empty((len(board),len(board))) 
        gScore_map[:] = 10000000

        gScore_map[x_0][y_0] = 0

        # fscore is the distance from the desination and goal
        fScore_map = np.empty((len(board),len(board)))
        fScore_map[:] = 10000000

        fScore_map[x_0][y_0] = h(src)

        # numb to card and cord to numb are becuase im dumb
        
        def numb_to_cord (numb): #takes number and turns to cord
            a = np.arange(len(board)*len(board)).resize((len(board),len(board)))
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
            while current in came_from:
                current = came_from[current]
                totalpath.insert(0,current)
            
            cord_path = []

            for numb in totalpath:
                cord_path.append(numb_to_cord(numb))

            return cord_path


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
                if board[neighbor[0]][[neighbor[1]]] < 0: #checks for colisions
                    neighbors.append(neighbor)
            

            for neighbor in neighbors: #intarates through each neighbor
                tentative_gScore = gScore_map[current[0]][[current[1]]] + 1 #probalbly gscore is just the gscore of the curent node and the distance wich is always 1


                if tentative_gScore < gScore_map[neighbor[0]][[neighbor[1]]]: #updates gscore on neighbor if it is lower
                    came_from[cord_to_numb(current)] = cord_to_numb(neighbor)
                    gScore_map[neighbor[0]][[neighbor[1]]] = tentative_gScore
                    fScore_map[neighbor[0]][[neighbor[1]]] = tentative_gScore + h(neighbor)

                    if neighbor not in open_set:
                        open_set.append(neighbor)
    

    def best_cordinate(self, map): 
        path = self._make_path(self.heads[0], self.food, map)
        return path[0]

        
    def direction(self, cord): #forgoten parameter
        current_x_cord = self.heads()[0][0] #self doesn't need to be used bc its a local var
        current_y_cord = self.heads()[0][1] #self doesn't need to be used bc its a local var
      

        #use a couple of new lines to prevent cluter


        ep_placeholder = cord 

        #the one part of the code that is executed almost perfectly
        if ep_placeholder[0] == current_x_cord and ep_placeholder[1] == current_y_cord:
            print ("Error: Current Position") #there is a way we riase errors

        elif ep_placeholder[0] == current_x_cord and ep_placeholder[1] > current_y_cord:
            return 3 #we can return this install of seting a var and the api calls for a direction id in souths case it is "3"
            
        elif ep_placeholder[0] == current_x_cord and ep_placeholder[1] < current_y_cord:
            return 1 # return 1

        elif ep_placeholder[0] > current_x_cord and ep_placeholder[1] == current_y_cord:
            return 2 #return 2

        elif ep_placeholder[0] < current_x_cord and ep_placeholder[1] == current_y_cord:
            return 0 #return 1

        #overall good programing just needs work on the syntax and conventions

snake = ai("key1", "http://localhost:8080")
print (snake.direction(8,0))