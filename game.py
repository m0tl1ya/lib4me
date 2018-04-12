#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import itertools
from collections import defaultdict



class PlayOffGame(object):
    def __init__(self, team_main, team_opp):
        self.team = team_main
        self.opp = team_opp

    def match(self):
        team_posession = self.team.pass_accuracy * self.team.pass_speed / self.opp.defense
        opp_posession = self.opp.pass_accuracy * self.opp.pass_speed / self.team.defense
        possetion_rate = team_posession / (team_posession + opp_posession)

        team_attack = (possetion_rate * self.team.attack - \
                       self.opp.defense + 100) * \
                       self.team.shoot_rate * (1 - self.opp.save_rate)
        opp_attack = (possetion_rate * self.opp.attack - \
                      self.team.defense + 100) *  \
                       self.opp.shoot_rate * (1 - self.team.save_rate)

        team_counter = (self.team.defense - self.opp.attack * self.team.shoot_rate + 100) \
                        * self.team.shoot_rate * (1 - self.opp.save_rate)
        opp_counter = (self.opp.defense - self.team.attack * self.opp.shoot_rate + 100) \
                        * self.opp.shoot_rate * (1 - self.team.save_rate)

        team_power_rate = team_attack / (team_attack + opp_attack)
        team_counter_rate = team_counter / (team_counter + opp_counter)

        win_rate = (team_power_rate + team_counter_rate) * 0.5
        score = np.random.rand()
        if score <= (win_rate):
            return self.team
        else:
            return self.opp


class Game(object):
    def __init__(self, team_main, team_opp):
        self.team = team_main
        self.opp = team_opp

    def match(self):
        team_posession = self.team.pass_accuracy * self.team.pass_speed / self.opp.defense
        opp_posession = self.opp.pass_accuracy * self.opp.pass_speed / self.team.defense
        possetion_rate = team_posession / (team_posession + opp_posession)

        team_attack = (possetion_rate * self.team.attack - \
                       self.opp.defense + 100) * \
                       self.team.shoot_rate * (1 - self.opp.save_rate)
        opp_attack = (possetion_rate * self.opp.attack - \
                      self.team.defense + 100) *  \
                       self.opp.shoot_rate * (1 - self.team.save_rate)

        team_counter = (self.team.defense - self.opp.attack * self.team.shoot_rate + 100) \
                        * self.team.shoot_rate * (1 - self.opp.save_rate)
        opp_counter = (self.opp.defense - self.team.attack * self.opp.shoot_rate + 100) \
                        * self.opp.shoot_rate * (1 - self.team.save_rate)

        team_power_rate = team_attack / (team_attack + opp_attack)
        team_counter_rate = team_counter / (team_counter + opp_counter)

        win_rate = (team_power_rate + team_counter_rate) * 0.5
        score = np.random.rand()
        if score < (win_rate - 0.15):
            team_point = 3
            opp_point = 0
        elif score > (win_rate + 0.15):
            team_point = 0
            opp_point = 3
        else:
            team_point = 1
            opp_point = 1
        self.team.results[self.opp.name].append(team_point)
        self.opp.results[self.team.name].append(opp_point)



class League(object):
    def __init__(self, group1, group2, group3, group4):
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.group4 = group4
        self.all_teams = group1 + group2 + group3 + group4
        self.group_champions = []
        self.wildcards = []

    def games_in_group(self, group):
        for v in list(itertools.combinations(group,2)):
            Game(v[0], v[1]).match()

    def all_games(self):
        self.games_in_group(self.group1)
        self.games_in_group(self.group2)
        self.games_in_group(self.group3)
        self.games_in_group(self.group4)
        self.games_in_group(self.all_teams)

    def calculate_win_score(self, group):
        for team in group:
            sum_of_win_score = 0
            for key in team.results.keys():
                sum_of_win_score += np.sum(team.results[key])
            team.total_win_score = sum_of_win_score


    def calculate_results(self):
        self.calculate_win_score(self.group1)
        self.calculate_win_score(self.group2)
        self.calculate_win_score(self.group3)
        self.calculate_win_score(self.group4)

    def print_results(self, group):
        group_sorted = sorted(group, key=lambda x:x.total_win_score, reverse=True)
        for team in group_sorted:
            print('{0}:score{1}'.format(team.name, team.total_win_score))
        for team in group_sorted:
            print(team.name)
            print('gemes:{0}'.format(team.results))
        print('\n')
        return group_sorted[0]

    def print_all_results(self):
        self.group_champions.append(self.print_results(self.group1))
        self.group_champions.append(self.print_results(self.group2))
        self.group_champions.append(self.print_results(self.group3))
        self.group_champions.append(self.print_results(self.group4))

    def determine_wild_card(self):
        all_sorted = sorted(self.all_teams, key=lambda x:x.total_win_score, reverse=True)
        for team in all_sorted:
            if team not in self.group_champions:
                self.wildcards.append(team)
                if len(self.wildcards) == 2:
                    break

    def determine_play_off(self):
        self.determine_wild_card()
        self.group_champions = sorted(self.group_champions, key=lambda x:x.total_win_score, reverse=True)
        self.wildcards = sorted(self.wildcards, key=lambda x:x.total_win_score, reverse=True)
        clinched = self.group_champions + self.wildcards
        for team in clinched:
            print('{}:{}'.format(team.name, team.total_win_score))
        print('\n')
        return clinched


class InterLeague(object):
    def __init__(self, main_league, other_league):
        self.main_league = main_league
        self.other_league = other_league

    def all_games(self):
        for i in range(len(self.main_league)):
            for j in range(len(self.other_league)):
                Game(self.main_league[i][0], self.other_league[j][(4-i+j)%4]).match()
                Game(self.main_league[i][1], self.other_league[j][(4-i+j+1)%4]).match()
                Game(self.main_league[i][2], self.other_league[j][(4-i+j+2)%4]).match()
                Game(self.main_league[i][3], self.other_league[j][(4-i+j+3)%4]).match()


class PlayOff(object):
    def __init__(self, league1, league2):
        self.league1 = league1
        self.league2 = league2

    def print_survivers_name(self, title, survivers):
        print(title)
        for team in survivers:
            print(team.name)
        print('\n')

    def run_league_playoff(self, league):
        first_round_bye = [league[0], league[1]]
        clinched_first = []
        clinched_first.append(PlayOffGame(league[2], league[5]).match())
        clinched_first.append(PlayOffGame(league[3], league[4]).match())
        self.print_survivers_name('first round bye', first_round_bye)
        self.print_survivers_name('clinched_first', clinched_first)

        clinched_second = []
        if clinched_first[0].name == league[2].name:
            clinched_second.append(PlayOffGame(first_round_bye[0], clinched_first[1]).match())
            clinched_second.append(PlayOffGame(first_round_bye[1], clinched_first[0]).match())
        else:
            clinched_second.append(PlayOffGame(first_round_bye[0], clinched_first[0]).match())
            clinched_second.append(PlayOffGame(first_round_bye[1], clinched_first[1]).match())
        self.print_survivers_name('clinched_second', clinched_second)

        clinched_semifinal = PlayOffGame(clinched_second[0], clinched_second[1]).match()
        print('League Champion:{}\n'.format(clinched_semifinal.name))

        return clinched_semifinal

    def final(self, finalist):
        self.print_survivers_name('finalist', finalist)
        champion = PlayOffGame(finalist[0], finalist[1]).match()
        return champion

    def run_tournament(self):
        finalist = []
        finalist.append(self.run_league_playoff(self.league1))
        finalist.append(self.run_league_playoff(self.league2))
        champion = self.final(finalist)
        print('Champion:{}'.format(champion.name))


class Team(object):
    def __init__(self, name, pass_accuracy, pass_speed,
                 attack, defense, shoot_rate, save_rate):
        self.name = name
        self.pass_accuracy = pass_accuracy
        self.pass_speed = pass_speed
        self.attack = attack
        self.defense = defense
        self.shoot_rate = shoot_rate
        self.save_rate = save_rate
        self.results = defaultdict(lambda: [])
        self.total_win_score = 0
