import random
from sqlite3.dbapi2 import connect
import string
import sqlite3
from fpdf import FPDF

class User:
    def __init__(self, name) -> None:
        self.name = name
        pass
    
    def buy(self, seat, card):

        return


class Seat:
    database = 'cinema.db'
    
    def __init__(self, seat_id) -> None:
        self.seat_id = seat_id

        pass

    def get_price(self):
        connection = sqlite3.connect('cinema.db')
        cursor = connection.cursor()
        query = f"SELECT price FROM Seat WHERE seat_id == '{self.seat_id}'"
        taken = cursor.execute(query)
        records = taken.fetchall()
        connection.close()
        price = records[0][0] 
        return price

    def is_free(self):
        connection = sqlite3.connect('cinema.db')
        cursor = connection.cursor()
        query = f"SELECT taken FROM Seat WHERE seat_id == '{self.seat_id}'"
        taken = cursor.execute(query)
        records = taken.fetchall()
        connection.close()
        if (records[0][0]) == 0:
            return True
        else:
            print("That seat is not available")
            return False

    def occupy(self):
        connection = sqlite3.connect('cinema.db')
        query = f"UPDATE Seat SET taken=1 WHERE seat_id == '{self.seat_id}'"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        
        return


class Card:
    def __init__(self, card_type, card_number, card_cvc, holder) -> None:
        self.type = card_type
        self.card_number = card_number
        self.card_cvc = card_cvc
        self.holder = holder
        pass

    def validate(self, price):
        connection = sqlite3.connect('banking.db')
        cursor = connection.cursor()
        query = f"SELECT * FROM Card WHERE number == '{self.card_number}';"
        exists = cursor.execute(query)
        record = exists.fetchall()
        if record:
            balance = record[0][4]
            new_balance = balance - int(price)
            balance = new_balance
            query = f"UPDATE Card SET balance={new_balance} WHERE number == '{self.card_number}';"
            cursor.execute(query)
            
        else: 
            query = "INSERT INTO Card VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, [self.type, self.card_number, self.card_cvc, self.holder, 1000])
            balance = 1000
        
        connection.commit()
        connection.close()
        return balance


class Ticket:
    def __init__(self, user, price, seat_number) -> None:
        self.ticket_id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat_number = seat_number
        pass

    def to_pdf(self, path):       
        # Generating the ticket
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='The CiNe Cinema Complex', border=1, align='C', ln=1)

        # Insert Ticket Info
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt='Ticket:', border=0)
        pdf.cell(w=150, h=40, txt= self.ticket_id, border=0, ln=1)
        pdf.cell(w=100, h=40, txt='Seat:', border=0)
        pdf.cell(w=150, h=40, txt= self.seat_number, border=0, ln=1)
        pdf.cell(w=100, h=40, txt='Name:', border=0)
        pdf.cell(w=150, h=40, txt= self.user, border=0, ln=1)
        pdf.cell(w=100, h=40, txt='Price:', border=0)
        pdf.cell(w=150, h=40, txt= str(self.price), border=0, ln=1)

        pdf.output(path)
        
        return "Ticket generated"

# Get client name

name = 'John'
# name = input("Welcome to the cinema booking app. What's your name?:")

# Get seat_id and validate
seat_valid = False
while not seat_valid:
    
    # seat = Seat(input("Please choose your seat (A1, A2, A3, B1, B2, B3):"))
    seat = Seat('A1')

    seat_valid = seat.is_free()

# Get all the credit card info
valid_card = False
while valid_card == False:
    card_number = '1234123412341234'
    card_cvc = '111'
    card_holder = 'JOHN S. DOE'
    price = seat.get_price()
    # card_number = input(f'Your seat {seat.seat_id} is available with a price of ${price} please enter your credit card number:')
    # card_cvc = input('Please enter the csv number:')
    # card_holder = input('Please enter the card holder name:')

    # Validate the credit card 
    if len(card_number) == 16 and card_number.isnumeric() and \
       len(card_cvc) == 3 and card_cvc.isnumeric():
       valid_card = True
    else:
        print ("Your credit card information is invalid")

# For mockup purposes, MasterCard and Visa numbers are actually different
if int(card_number[0:3]) <= 50:
    card_type = 'MasterCard'
else:
    card_type = 'Visa'

credit_card = Card(card_type, card_number, card_cvc, card_holder)
charge = credit_card.validate(price)

print ("Transaction succesfull, generating ticket, enjoy your movie")

# Generating ticket
seat.occupy()
ticket = Ticket(name, price, seat.seat_id)
gen_ticket = ticket.to_pdf("ticket.pdf")
print(gen_ticket)


