import requests
import json


class client:

    def __init__(self, player_key, game_url):

        #innitialize info for connection
        self.player_key = player_key
        self.game_url = game_url + '/api/'

        self.con_params = {'key':self.player_key}

        # #check connection
        # if requests.get(self.game_url).status_code == 200:
        #     print('Valid Cnnection Established')
        # else:
        #     raise ConnectionError

        #make Endpoints
        self.board_ep = self.game_url + 'board/'
        self.move_needed_ep = self.game_url + 'move_needed/'
        self.move_ep = self.game_url + 'move/'

    def _get_board_data(self):
        
        #gets raw board data
        r = requests.get(self.board_ep, params= self.con_params)
        return r.json()

    @property
    def board(self):
        #method to get only board data
        data = self._get_board_data()
        return data['board']

    @property
    def heads(self):
        #method to get only heads data
        data = self._get_board_data()
        return data['heads']

    @property
    def food(self):
        #method to get only food data
        data = self._get_board_data()
        return data['food']
    
    @property
    def move_needed(self):
        #tells us if we need to move
        r = requests.get(self.move_needed_ep, params= self.con_params)
        data = r.json()
        return data
    

    def post_move(self, move_id):
        #makes move

        #makes payload
        payload = self.con_params
        payload['move'] = move_id


        #makes post
        r = requests.post(self.move_ep, data= payload)
        print(r)



    

url = 'http://localhost:8080'
client1 = client('key1', url)

print(client1.board)

