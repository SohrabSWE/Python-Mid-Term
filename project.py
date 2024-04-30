class star_cinema:
    __hall_list = []
    def entry_hall(self,hall):

        self.__hall_list.append(hall)

class hall(star_cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.__seats = {}
        self.show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)
    def entry_show(self,id,movie_name,time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        matrix = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

        self.__seats[id] = matrix

    def book_seats(self,id,seat):
        a = seat[0]
        b = seat[1]
        if(self.__seats[id][a][b] == 1):
            print(f'SEAT NUMBER ({row},{col}) IS ALREADY BOOKED\n')

        elif(self.__seats[id][a][b] == 0):
            self.__seats[id][a][b] = 1
            print(f'SEAT NUMBER ({row},{col}) IS BOOKED SUCCESSFULLY !!!\n')

    def view_show_list(self):
        for x in self.show_list:
            print(f'Movie Name : {x[1]}\t SHOW ID : {x[0]}\t Date : 30/04/2024 Time: {x[2]} PM')

    def view_available_seats(self,id):
        available_seats = 0
        print(f'AVAILABLE SEATS FOR SHOW ID {id}')
        for x in range(self.__rows):
            for y in range(self.__cols):
                print(self.__seats[id][x][y],end=" ")
                if(self.__seats[id][x][y]==0):
                    available_seats +=1
            print()

    def available_seats_count(self, id):
        available_seats = 0
        for x in range(self.__rows):
            for y in range(self.__cols):
                if (self.__seats[id][x][y] == 0):
                    available_seats += 1
        return available_seats
    
hall_one = hall(5,5,1)
hall_one.entry_show(111,'jawan maji', '4:00')
hall_one.entry_show(333,'sujan maji', '7:00')


while True:
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    option = int(input("CHOOSE A OPTION : "))
    if(option==1):
        print()
        hall_one.view_show_list()
        print()
    elif(option==2):
        id = int(input("ENTER SHOW ID : "))
        if(id==111 or id==333):
            hall_one.view_available_seats(id)
        else:
            print("ENTER A VALID SHOW ID")
    elif(option==3):
        show_id = int(input("SHOW ID : "))
        n = int(input("NUMBER OF TICKETS : "))
        if (hall_one.available_seats_count(show_id)==0):
            print("NO SEATS AVAILABLE")
        elif(hall_one.available_seats_count(show_id)-n <0):
            available_seats = hall_one.available_seats_count(show_id)
            if(available_seats==1):
                print(f'SEAT AVAILABLE : {available_seats}')
            elif(available_seats>1):
                print(f'SEATS AVAILABLE : {available_seats}')
        else:
            while (n > 0):
                row = int(input("ENTER SEAT ROW : "))
                col = int(input("ENTER SEAT COL : "))
                if ((row < 1 or row > 5) or (col < 1 or col > 5)):
                    print("Please enter raw and columnn between 5")
                else:
                    tuple = (row - 1, col - 1)
                    hall_one.book_seats(show_id, tuple)
                    n = n - 1
    elif(option==4):
        break
    else:
        print("enter a valid option")