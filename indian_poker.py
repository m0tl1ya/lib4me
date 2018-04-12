# -*- coding: utf-8 -*-


class Player(object):
    def __init__(self, value):
        self.value = value
        self.candidate = None
        self.answer = []
        self.id = None

    def set_candidate(self, given_list):
        self.candidate = given_list

    def reduce_candidate(self, remove_list):
        if len(self.candidate) > len(remove_list):
            for v in remove_list:
                self.candidate.remove(v)


class Game(object):
    def __init__(self, value_list):
        self.value_list = value_list
        self.players = []
        self.id_of_current_player = 0
        self.n_players = 0
        self.all_values = []
        self.max_value = None
        self.min_value = None
        self.turn_count = 0

    def add_player(self, player):
        if player.value in self.value_list and \
           player.value not in self.all_values:
            self.players.append(player)
            self.all_values = sorted([player.value for player in self.players])
            player.id = self.n_players
            self.n_players += 1

    def print_players(self):
        for player in self.players:
            print('id:{}'.format(player.id))
            print('value:{}'.format(player.value))

    def print_value_list(self):
        print(self.value_list)

    def turn_next(self):
        current_id = self.id_of_current_player
        self.id_of_current_player = int((current_id + 1) % self.n_players)
        self.turn_count += 1

    def predict(self, clue):
        mode = '?'
        flag = None
        answer = None
        n_change_flag = 0
        for i, boolean in enumerate(clue):
            if i == 0:
                if boolean is True:
                    mode = 'MAXorMID'
                else:
                    mode = 'MINorUNKNOWN'
                flag = boolean
            else:
                if boolean != flag:
                    flag = boolean
                    n_change_flag += 1
        if mode == 'MAXorMID':
            if n_change_flag == 1:
                answer = 'MAX'
            elif n_change_flag == 2:
                answer = 'MID'
            else:
                answer = '?'
        else:
            if n_change_flag == 1:
                answer = 'MIN'
            else:
                answer = '?'
        return answer

    def simulate_pre_player_actions(self, current_id):
        """Infer actions of previous player in order to reduce candidate."""
        current_player = self.players[current_id]
        previous_id = int((current_id + 1) % self.n_players)
        # value_of_previous_player = self.players[previous_id].value
        visible_card = [player.value for player in self.players
                        if player.id != current_id
                        and player.id != previous_id]
        excluded = []
        for v in current_player.candidate:
            clue = [(i in visible_card) or (i == v) for i in self.value_list]
            answer = self.predict(clue)
            if answer != '?':
                excluded.append(v)
        return excluded

    def infer(self, current_id):
        current_player = self.players[current_id]
        # value_of_current_player = self.players[current_id].value
        visible_card = [player.value for player in self.players
                        if player.id != current_id]
        if self.turn_count != 0:
            excluded = self.simulate_pre_player_actions(current_id)
            visible_card += excluded
            try:
                current_player.reduce_candidate(excluded)
            except:
                pass
        clue = [i in visible_card for i in self.value_list]
        # print(clue)
        answer = self.predict(clue)
        print(answer)
        if answer != '?':
            return True
        else:
            return False

    def start(self):
        for player in self.players:
            player.set_candidate(self.value_list[:])
            # print(player.id)
            # print(player.value)
            # print(player.candidate)
            excluded = [other.value for i, other in enumerate(self.players)
                        if i != player.id]
            # print(excluded)
            player.reduce_candidate(excluded)
        self.max_value = max(self.value_list)
        self.min_value = min(self.value_list)
        # current_player_id = self.id_of_current_player

        while(True):
            if self.infer(self.id_of_current_player):
                break
            else:
                self.turn_next()


if __name__ == '__main__':
    a = Player(value=1)
    b = Player(value=2)
    c = Player(value=4)
    game = Game(value_list=[i for i in range(1, 6)])
    game.add_player(a)
    game.add_player(b)
    game.add_player(c)
    game.start()

    print('\n')

    a = Player(value=1)
    b = Player(value=4)
    c = Player(value=5)
    game = Game(value_list=[i for i in range(1, 6)])
    game.add_player(a)
    game.add_player(b)
    game.add_player(c)
    game.start()
