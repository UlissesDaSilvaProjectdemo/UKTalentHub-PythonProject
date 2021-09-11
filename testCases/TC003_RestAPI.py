import logging
import requests
import unittest

API_KEY = '89490e1e5ab8c2a998dd7c0ab3bf67c6'
TOKEN = '06c029430141a14f1112f8020f1ea5d51c360656a4fe579eb602e0f971efd0c2'

class TrelloApiTest(unittest.TestCase):

    # created board
    def setUp(self):
        self.board_id = self.create_board()
        list_id = self.create_list(self.board_id, name="Plentific_ChecKlist")
        first_card_id = self.create_card(list_id, name="first_card")
        second_card_id = self.create_card(list_id, name="second_card")
        third_card_id = self.create_card(list_id, name="third_card")

        #self.edit_Card(second_card_id)
        #self.delete_Card()

    def tearDown(self):
        self.delete_board(self.board_id)

    def test_something(self):
        print('hello')

    def delete_board(self, board_id):  # DELETE /1/boards/{id}
        response = requests.delete(f"https://api.trello.com/1/boards/{board_id}?key={API_KEY}&token={TOKEN}")
        assert response.status_code == 200


    def create_board(self): #POST /1/cards
        response = requests.post(f'https://api.trello.com/1/boards?key={API_KEY}&token={TOKEN}',
                                 json={"name": "Plentific_Trello", "defaulList": False})
        assert response.status_code == 200
        logging.info("Created board %s", response.json())
        return response.json()["id"]


    def create_list(self, board_id, name):  #  POST / 1 / checklists
        response = requests.post(f'https://api.trello.com/1/lists/?key={API_KEY}&token={TOKEN}',
                                 json={"idBoard": board_id, "name": name})
        return response.json()["id"]

    def create_card(self, list_id, name):  # PUT /1/boards/{id}
        response = requests.post(f'https://api.trello.com/1/cards?key={API_KEY}&token={TOKEN}',
                                 json={"name": name, "idList": list_id})
        return response.json()["id"]

    def edit_Card(self):  # PUT /1/boards/{id}
        self.edit_Card = requests.put(f'https://api.trello.com/1/baords/{id}?key={API_KEY}&token={TOKEN}',
                                      json={"name" "Third_Card"})

    def comment_card(self): #PUT /1/cards/{id}
        self.comment_Card = requests.put(f'https://api.trello.com/1/cards/{id}?key={API_KEY}&token={TOKEN}',
                                      json={"name" "comment in the cards"})


    def delete_Card(self):  # DELETE /1/boards/{id}
        self.delete_Card = requests.post(f'https://api.trello.com/1/boards{id}?key={API_KEY}&token={TOKEN}',
                                         json={"name" "Third_Card"})

if __name__ == "__main__":
    unittest.main()