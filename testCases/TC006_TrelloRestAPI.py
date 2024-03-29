import logging
import requests
import unittest

API_KEY = '89490e1e5ab8c2a998dd7c0ab3bf67c6'
TOKEN = '06c029430141a14f1112f8020f1ea5d51c360656a4fe579eb602e0f971efd0c2'


class TrelloApiTest(unittest.TestCase):

    # created board
    def setUp(self):
        self.board_id = self.create_board()
        list_id = self.create_list(self.board_id, name=" ChecKlist")
        first_card_id = self.create_card(list_id, name="first_card")
        second_card_id = self.create_card(list_id, name="second_card")
        third_card_id = self.create_card(list_id, name="third_card")
        fifth_card_id = self.create_card(list_id, name='fifth_card_id')
        sixth_card = self.create_card(list_id, name="sixth_card")
        seventh_card = self.create_card(list_id, name="seventh_card")
        UKTALENTHUB_card = self.create_card(list_id, name="UKTALENTHUB_card")


        self.edit_card(second_card_id, name="Edit second card", desc=' add a new description')
        self.delete_card(first_card_id)
        self.add_comment_to_card(third_card_id, text="  New Comment")
        self.add_comment_to_card(sixth_card, text="  New  Test comment")
        self.add_comment_to_card(seventh_card, text="  New  Test comment")
        self.edit_card(fifth_card_id, text="New  Card comment")
        self.add_comment_to_card(UKTALENTHUB_card, text="UKTALENTHUB_card")


    def tearDown(self):
        self.delete_board(self.board_id)

    def test_something(self):
        print('Testing Trello API  Hello')

    def delete_board(self, board_id):  # DELETE /1/boards/{id}
        response = requests.put(f"https://api.trello.com/1/boards/{board_id}?key={API_KEY}&token={TOKEN}")
        assert response.status_code == 200

    def create_board(self):  # POST /1/boards
        response = requests.post(f'https://api.trello.com/1/boards?key={API_KEY}&token={TOKEN}',
                                 json={"name": "UKTalentHub_Trello", "defaulList": False})
        assert response.status_code == 200
        logging.info("Created board %s", response.json())
        return response.json()["id"]

    def create_list(self, board_id, name):  # POST /1/lists
        response = requests.post(f'https://api.trello.com/1/lists/?key={API_KEY}&token={TOKEN}',
                                 json={"idBoard": board_id, "name": name})
        assert response.status_code == 200
        return response.json()["id"]

    def create_card(self, list_id, **params):  # POST /1/cards/{id}
        response = requests.post(f'https://api.trello.com/1/cards?key={API_KEY}&token={TOKEN}',
                                 json={**{"idList": list_id}, **params})
        return response.json()["id"]

    def edit_card(self, card_id, **params):  # PUT /1/cards/{id}
        return requests.put(f'https://api.trello.com/1/cards/{card_id}?key={API_KEY}&token={TOKEN}',
                            json={**{"idCard": card_id}, **params})

    def delete_card(self, card_id):  # DELETE /1/cards/{id}
        return requests.delete(f'https://api.trello.com/1/cards/{card_id}?key={API_KEY}&token={TOKEN}')

    def add_comment_to_card(self, card_id, text):  # POST /1/cards/{id}/actions/comments
        return requests.post(f'https://api.trello.com/1/cards/{card_id}/actions/comments?key={API_KEY}&token={TOKEN}',
                             json={'text': text})



if __name__ == "__main__":
    unittest.main()
