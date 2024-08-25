class StarCinema:
    hall_list = []

    def __init__(self):
        pass

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(StarCinema):
    def __init__(self, hall_no, rows, cols):
        super().__init__()
        self.hall_no = hall_no
        self.rows = rows
        self.cols = cols
        self.show_list = []
        self.seats = {}
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        self.show_list.append((show_id, movie_name, time))
        self.seats[show_id] = [[False for _ in range(self.cols)] for i in range(self.rows)]

    def book_seats(self, name, phone, show_id, seat_list):
        for show in self.show_list:
            if show[0] == show_id:
                for seat in seat_list:
                    row, col = seat
                    if row >= self.rows or col >= self.cols:
                        print(f"INVALID SEAT NO - {chr(row + 65)}{col}. TRY AGAIN!")
                        return
                    if self.seats[show_id][row][col]:
                        print(f"SEAT {chr(row + 65)}{col} IS ALREADY BOOKED. TRY AGAIN!")
                        return
                for seat in seat_list:
                    row, col = seat
                    self.seats[show_id][row][col] = True
                booked_seats = [f"{chr(row + 65)}{col}" for row, col in seat_list]
                print("TICKET BOOKED SUCCESSFULLY!")
                print(f"NAME: {name}, PHONE: {phone}")
                print(f"MOVIE: {show[1]}, TIME: {show[2]}")
                print(f"SEATS: {', '.join(booked_seats)}")
                print(f"HALL: {self.hall_no}")
                return
        print("SHOW ID NOT FOUND. TRY AGAIN!")

    def view_show_list(self):
        if not self.show_list:
            print("NO SHOWS AVAILABLE TODAY.")
        else:
            print("SHOWS AVAILABLE TODAY:")
            for show in self.show_list:
                print(f"SHOW ID: {show[0]}, MOVIE: {show[1]}, TIME: {show[2]}")

    def view_available_seats(self, show_id):
        for show in self.show_list:
            if show[0] == show_id:
                print(f"AVAILABLE SEATS FOR {show[1]} AT {show[2]}:")
                for row in range(self.rows):
                    for col in range(self.cols):
                        if self.seats[show_id][row][col]:
                            print("X", end=" ")
                        else:
                            print(f"{chr(row + 65)}{col}", end=" ")
                    print()
                return
        print("SHOW ID NOT FOUND. TRY AGAIN!")

star = StarCinema()
my_hall = Hall("A10", 3, 5)
my_hall.entry_show("ae123", "Black Adam", "Sep 26 2024 10:00 PM")
my_hall.entry_show("ae50", "Superman", "Sep 26 2024 8:00 PM")

while True:
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    option = int(input("ENTER OPTION: "))
    if option == 1:
        my_hall.view_show_list()
    elif option == 2:
        show_id = input("ENTER SHOW ID: ")
        my_hall.view_available_seats(show_id)
    elif option == 3:
        name = input("ENTER CUSTOMER NAME: ")
        phone = input("ENTER CUSTOMER PHONE NUMBER: ")
        show_id = input("ENTER SHOW ID: ")
        num_tickets = int(input("ENTER NUMBER OF TICKETS: "))
        seat_list = []
        for _ in range(num_tickets):
            seat = input("ENTER SEAT NO (e.g., A0): ")
            row, col = ord(seat[0]) - 65, int(seat[1:])
            seat_list.append((row, col))
        my_hall.book_seats(name, phone, show_id, seat_list)
    else:
        break
