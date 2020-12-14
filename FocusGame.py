#name: Jonghyun Lee
#date: November 20th 2020
#description: Portfolio Project

class FocusGame:

    def __init__(self, first, second):
        '''
        Takes two tuples comprised of player name and assigned color as parameters.
        Initializes 5x5 board in order for the players to begin the game.
        '''

        # user argument broken into Player name, and assigned game piece color
        self._first_player, self._red = first
        self._second_player, self._green = second

        # FocusGame board template
        self._board = [ [{(0, 0): [first[1]]}, {(0, 1): [first[1]]}, {(0, 2): [second[1]]}, {(0, 3): [second[1]]}, {(0, 4): [first[1]]},{(0, 5): [first[1]]}],

                        [{(1, 0): [second[1]]}, {(1, 1): [second[1]]}, {(1, 2): [first[1]]}, {(1, 3): [first[1]]}, {(1, 4): [second[1]]}, {(1, 5): [second[1]]}],

                        [{(2, 0): [first[1]]}, {(2, 1): [first[1]]}, {(2, 2): [second[1]]}, {(2, 3): [second[1]]}, {(2, 4): [first[1]]}, {(2, 5): [first[1]]}],

                        [{(3, 0): [second[1]]}, {(3, 1): [second[1]]}, {(3, 2): [first[1]]}, {(3, 3): [first[1]]}, {(3, 4): [second[1]]}, {(3, 5): [second[1]]}],

                        [{(4, 0): [first[1]]}, {(4, 1): [first[1]]}, {(4, 2): [second[1]]}, {(4, 3): [second[1]]}, {(4, 4): [first[1]]}, {(4, 5): [first[1]]}],

                        [{(5, 0): [second[1]]}, {(5, 1): [second[1]]}, {(5, 2): [first[1]]}, {(5, 3): [first[1]]}, {(5, 4): [second[1]]}, {(5, 5): [second[1]]}]]

        # Used to alternate player turns after each play
        self._first_turn = True
        self._second_turn = True

        # represents reserved and captured pieces by player
        self._first_res_cap = {'reserved': [],
                               'captured': []
                              }

        self._second_res_cap = {'reserved': [],
                                'captured': []
                               }

        ################Test Box##################
        # print(len(self._board[0][1][(0,1)]))
        # temp = self._board[0][0][0,0][-1::]
        # print(temp)
        ################Test Box##################

    def display_board(self):
        '''
        Displays the current status of the board
        '''

        for row in self._board:
            print(row)

    def move_piece(self, player_name, start_coord, end_coord, num):
        '''
        Takes the following parameters: Player name, starting and ending coordinates,
        and a numerical value indicating number of pieces being moved. Intent is to
        validate move conditions and return the corresponding message if conditions fail.
        Otherwise, returns the player method to execute the move.
        '''

        # invalid move conditions - out of turn, false locations,
        # and user selected quantity exceeds actual pieces

        if player_name == self._first_player and self._first_turn is False:
            return False
        elif player_name == self._second_player and self._second_turn is False:
            return False
        elif start_coord not in self._board[start_coord[0]][start_coord[1]] or end_coord not in self._board[end_coord[0]][end_coord[1]]:
            return False
        elif start_coord[0] != end_coord[0] and start_coord[1] != end_coord[1]:
            return False
        elif num > len(self._board[start_coord[0]][start_coord[1]][start_coord]):
            return False
        else:
            # conditions to execute the move for player A and player B
            if player_name == self._first_player and self._first_turn is True:
                return self.move_first_player(start_coord, end_coord, num)
            elif player_name == self._second_player and self._second_turn is True:
                return self.move_second_player(start_coord, end_coord, num)

    def move_first_player(self, start_coord, end_coord, num):
        '''
        Takes the following parameters: starting / ending coordinates and number of pieces
        the user wants moved. Intent is to move the pieces specified by the user.
        Triggered by the move method. Confirms all conditions have been met to move the
        players piece in accordance with the coordinates and quantity selected by the user.
        '''

        # checks to make sure the top piece belongs to the first player prior to making the move
        if self._board[start_coord[0]][start_coord[1]][start_coord][-1] != 'R':
            return False

        # temp isolates the value(s) that are being removed from the starting coordinates
        temp = self._board[start_coord[0]][start_coord[1]][start_coord][-num::]

        ############################################
        # print('Values being moved-->', temp)
        ############################################

        # updates the board by removing the value(s) from the starting coordinates and
        # adding them to the ending coordinates
        del self._board[start_coord[0]][start_coord[1]][start_coord][-num::]
        self._board[end_coord[0]][end_coord[1]][end_coord].extend(temp)

        # checks to see if pieces need to go in the reserves or are captured
        if len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:
            while len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:

                # bottom is zero index position
                if self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'R' and self._first_turn is True:
                    self._first_res_cap['reserved'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]
                elif self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'G' and self._first_turn is True:
                    self._first_res_cap['captured'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]

        # switch player turns
        self._first_turn = False
        self._second_turn = True

        # checks for winning conditions
        if len(self._first_res_cap['captured']) >= 6:
            return 'PlayerA wins'
        else:
            return 'successfully moved'

        # print('Updated Board')
        # for row in self._board:
        #     print(row)

    def move_second_player(self, start_coord, end_coord, num):
        '''
        Takes the following parameters: starting / ending coordinates and number of pieces
        the user wants moved. Intent is to move the pieces specified by the user.
        Triggered by the move method. Confirms all conditions have been met to move the
        players piece in accordance with the coordinates and quantity selected by the user.
        '''

        #checks to make sure the top piece belongs to the second player prior to making the move
        if self._board[start_coord[0]][start_coord[1]][start_coord][-1] != 'G':
            return False

        #temp isolates the value(s) that are being removed from the starting coordinates
        temp = self._board[start_coord[0]][start_coord[1]][start_coord][-num::]

        ############################################
        # print('Values being moved-->', temp)
        ############################################

        # updates the board by removing the value(s) from the starting coordinates and
        # adding them to the ending coordinates
        del self._board[start_coord[0]][start_coord[1]][start_coord][-num::]
        self._board[end_coord[0]][end_coord[1]][end_coord].extend(temp)

        # checks to see if pieces need to go in the reserves or are captured
        if len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:
            while len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:

                # bottom is zero index position
                if self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'R' and self._second_turn is True:
                    self._second_res_cap['captured'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]

                elif self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'G' and self._second_turn is True:
                    self._second_res_cap['reserved'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]

        # switch player turns
        self._first_turn = True
        self._second_turn = False

        # checks for winning conditions
        if len(self._second_res_cap['captured']) >= 6:
            return 'PlayerB wins'
        else:
            return 'successfully moved'

        # print('Updated Board')
        # for row in self._board:
        #     print(row)

    def show_pieces(self, grid_coordinates):
        '''
        Takes the following parameters: Coordinates of the piece(s) that the user
        wants displayed from the board. Method will return all the pieces located
        in the coordinates from the bottom (0th index) of the stack to the top.
        '''

        return self._board[grid_coordinates[0]][grid_coordinates[1]][grid_coordinates]

    def show_reserve(self, player_name):
        '''
        Takes the following parameters: Player's name. Intent is to show the pieces
        that the player has in reserve. Returns a 0 numerical value if the player
        has no pieces in the reserve.
        '''

        # shows current quantity of pieces in the reserves
        if player_name == self._first_player:
            if len(self._first_res_cap['reserved']) > 0:
                return len(self._first_res_cap['reserved'])

            else:
                return 0

        # shows current quantity of pieces in the reserves
        elif player_name == self._second_player:
            if len(self._second_res_cap['reserved']) > 0:
                return len(self._first_res_cap['reserved'])

            else:
                return 0

    def show_captured(self, player_name):
        '''
        Takes the following parameters: Player's name. Intent is to show number of pieces
        that the player has "captured" by returning the numerical value that the player
        has taken from the opposing player. Returns a 0 numerical value if the player
        has not captured any pieces.
        '''

        # shows current quantity of pieces that are captured
        if player_name == self._first_player:
            if len(self._first_res_cap['captured']) > 0:
                return len(self._first_res_cap['captured'])

            else:
                return 0
        # shows current quantity of pieces that are captured
        elif player_name == self._second_player:
            if len(self._second_res_cap['captured']) > 0:
                return len(self._second_res_cap['captured'])

            else:
                return 0

    def reserved_move(self, player_name, end_coord):
        '''
        Takes the following parameters: Player's name, and placement coordinates for
        the reserve piece. Checks to see if the player’s turn is valid and
        whether there are any pieces in the reserve. If all of the move conditions
        have been met, the method will execute the corresponding player reserve move
        method. If the conditions have not been met, the operation will not proceed.
        Instead, returns "no pieces in reserve" if the player does not have any
        reserve pieces.
        '''

        # invalid move conditions - out of turn, false locations,
        # and player has no pieces in reserve
        if player_name == self._first_player and self._first_turn is False:
            return False
        elif player_name == self._second_player and self._second_turn is False:
            return False
        elif end_coord not in self._board[end_coord[0]][end_coord[1]]:
            return False
        elif player_name == self._first_player and len(self._first_res_cap['reserved']) <= 0:
            return False
        elif player_name == self._second_player and len(self._second_res_cap['reserved']) <= 0:
            return False

        else:
            # conditions to execute the move for player A and player B
            if player_name == self._first_player and self._first_turn is True:
                return self.first_player_res_move(end_coord)
            elif player_name == self._second_player and self._second_turn is True:
                return self.second_player_res_move(end_coord)

    def first_player_res_move(self, end_coord):
        '''
        Takes the following parameters: grid coordinates. Intent is to place the reserve piece
        at the location passed in the parameter. Triggered by the reserved_move method.
        Confirms all conditions have been met to move the players piece in accordance
        with the coordinates selected by the user.
        '''

        # takes a piece from the reserve list and places it on the board
        self._board[end_coord[0]][end_coord[1]].extend(self._first_res_cap['reserved'][0])
        self._first_res_cap['reserved'].remove('R')

        # checks to see if pieces need to go in the reserves or are captured
        if len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:
            while len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:

                # zero index position is the bottom
                if self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'R' and self._first_turn is True:
                    self._first_res_cap['reserved'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]
                elif self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'G' and self._first_turn is True:
                    self._first_res_cap['captured'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]

        #switches player turns
        self._first_turn = False
        self._second_turn = True

        #checks for winning conditions
        if len(self._first_res_cap['captured']) >= 6:
            return 'PlayerA wins'
        else:
            return 'successfully moved'

    def second_player_res_move(self, end_coord):
        '''
        Takes the following parameters: grid coordinates. Intent is to place the reserve piece
        at the location passed in the parameter. Triggered by the reserved_move method.
        Confirms all conditions have been met to move the players piece in accordance
        with the coordinates selected by the user.
        '''

        # takes a piece from the reserve list and places it on the board
        self._board[end_coord[0]][end_coord[1]].extend(self._second_res_cap['reserved'][0])
        self._second_res_cap['reserved'].remove('G')

        # checks to see if pieces need to go in the reserves or are captured
        if len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:
            while len(self._board[end_coord[0]][end_coord[1]][end_coord]) > 5:

                # zero index position is the bottom
                if self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'R' and self._second_turn is True:
                    self._second_res_cap['captured'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]

                elif self._board[end_coord[0]][end_coord[1]][end_coord][0] == 'G' and self._second_turn is True:
                    self._second_res_cap['reserved'].extend(self._board[end_coord[0]][end_coord[1]][end_coord][0])
                    del self._board[end_coord[0]][end_coord[1]][end_coord][0]

        # switches player turns
        self._first_turn = True
        self._second_turn = False

        # checks for winning conditions
        if len(self._second_res_cap['captured']) >= 6:
            return 'PlayerB wins'
        else:
            return 'successfully moved'
