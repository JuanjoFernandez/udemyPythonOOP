import random
import string
import sqlite3

class User:
    def __init__(self, name) -> None:
        self.name = name
        pass
    
    def buy(self, seat, card):

        return


class Seat:
    database = 'cinema.db'
    
    def __init__(self) -> None:
        self.seat_id = seat_id

        pass

    def get_price(self):

        return

    def is_free(self):

        return

    def occupy(self):

        return


class Card:
    database = 'banking.db'
    def __init__(self, card_type, card_number, card_cvc, holder) -> None:
        self.type = card_type
        self.card_number = card_number
        self.card_cvc = card_cvc
        self.holder = holder
        pass

    def validate(self, price):

        return


class Ticket:
    def __init__(self, user, price, seat_number) -> None:
        self.ticket_id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat_number = seat_number
        pass

    def to_pdf(self, path):

        return

name = input ("Welcome to the cinema booking app. What's your name?:")


