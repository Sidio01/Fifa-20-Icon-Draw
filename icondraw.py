import random
from prettytable import PrettyTable


def icon_choice(squad, count):
    try:
        for _ in range(count):
            player = random.choice(squad)
            team1_squad.append(player)
            squad.remove(player)
            player = random.choice(squad)
            team2_squad.append(player)
            squad.remove(player)
            player = random.choice(squad)
            team3_squad.append(player)
            squad.remove(player)
            player = random.choice(squad)
            team4_squad.append(player)
            squad.remove(player)
    except IndexError:
        pass


def player_choice(squad, count):
    try:
        for _ in range(count):
            player = random.choice(squad)
            team1_name.append(player)
            squad.remove(player)
            player = random.choice(squad)
            team2_name.append(player)
            squad.remove(player)
            player = random.choice(squad)
            team3_name.append(player)
            squad.remove(player)
            player = random.choice(squad)
            team4_name.append(player)
            squad.remove(player)
    except IndexError:
        pass


# Разбивка игроков по позициям и качеству
icon_keepers = ['E. Van Der Sar', 'L. Yashin', 'P. Schmeichel', 'J. Lehmann']
icon_cb_defenders = ['F. Baresi',  'C. Puyol', 'B. Moore', 'A. Nesta',
                     'F. Cannavaro', 'F. Hierro', 'M. Desailly',  'R. Koeman', ]
icon_fb_defenders = ['C. Alberto', 'R. Carlos', 'J. Zanetti', 'G. Zambrotta']
icon_midfielders = ['R. Baggio', 'R. Giggs', 'A. Pirlo', 'M. Laudrup', 'P. Scholes', 'G. Hagi',
                    'R. Pires',  'S. Gerrard', 'P. Nedved', 'C. Seedors', 'M. Ballack', 'Socrates',
                    'J. Litmanen', 'J. Okocha', 'F. Rijkaard', 'M. Overmars', 'Deco', 'E. Petit', 'R. Costa',
                    'R. Keane', 'F. Lampard','C. Makelele', 'S. Veron', 'P. Guardiola', 'G. Gattuso',
                    'H. Nakata']
icon_strikers = ['Kaka',  'M. Garrincha', 'M. Van Basten', 'G. Best', 'T. Henry',  'L. Figo', 'A. Del Piero',
                 'G. Lineker', 'E. Butragueno', 'R. Van Nistelrooy', 'D. Bergkamp', 'H. Stoichkov', 'Rivaldo', 'Raul',
                 'H. Sanchez', 'M. Owen', 'A. Shearer', 'A. Shevchenko', 'P. Kluivert', 'D. Trezeguet',
                 'M. Klose', 'I. Rush', 'D. Drogba', 'F. Inzaghi', 'H. Larsson', 'H. Crespo', 'L. Hernandez', 'G. Zola',
                 'C. Vieri', 'J. Barnes', 'I. Wright']
icon_best_defenders = ['P. Maldini', 'R. Ferdinand', 'L. Blanc', 'S. Campbell']
icon_best_def_midfielders = ['P. Vieira', 'R. Gullit', 'M. Essien', 'L. Matthaus']
icon_best_att_midfielders = ['Z. Zidane', 'Pele', 'D. Maradona', 'Ronaldinho']
icon_best_strikers = ['Ronaldo', 'J. Cruyff', 'Eusebio', 'K. Dalglish']

# Объявление команд и ввод участников
team1_squad = []
team2_squad = []
team3_squad = []
team4_squad = []
team1_name = []
team2_name = []
team3_name = []
team4_name = []
print('Введите имена сильных игроков:')
good_players = input().split()
print('Введите имена новичков:')
bad_players = input().split()

# Жеребьевка участников
player_choice(good_players, 1)
player_choice(bad_players, 1)

# Выбор вратарей
icon_choice(icon_keepers, 1)  # всего 4, остаток 0

# Выбор защитников
icon_choice(icon_cb_defenders, 2)  # всего 8, остаток 0
icon_choice(icon_fb_defenders, 1)  # всего 4, остаток 0
icon_choice(icon_best_defenders, 1)

# Выбор полузащитников
icon_choice(icon_midfielders, 6)  # всего 26, остаток 2
icon_choice(icon_best_def_midfielders, 1)
icon_choice(icon_best_att_midfielders, 1)

# Выбор нападающих
icon_choice(icon_strikers, 4)  # всего 31, остаток 15
icon_choice(icon_best_strikers, 1)

# Вывод жеребьевки
# print('-' * 95)
# print('{:<25s}{:<25s}{:<25s}{:<25s}'.format(str(team1_name), str(team2_name), str(team3_name), str(team4_name)))
# print('-' * 95)
table = PrettyTable()
table.field_names = [team1_name, team2_name, team3_name, team4_name]
teams = [team1_squad, team2_squad, team3_squad, team4_squad]
i = 0
for _ in range(len(team1_squad)):
    # print('{:<25s}{:<25s}{:<25s}{:<25s}'.format(str(teams[0][i]), str(teams[1][i]), str(teams[2][i]), str(teams[3][i])))
    table.add_row([str(teams[0][i]), str(teams[1][i]), str(teams[2][i]), str(teams[3][i])])
    i += 1
    if i == 1:
        table.add_row(['-' * 10, '-' * 10, '-' * 10, '-' * 10])
        # print('-' * 95)
    if i == 5:
        table.add_row(['-' * 10, '-' * 10, '-' * 10, '-' * 10])
        # print('-' * 95)
    if i == 13:
        table.add_row(['-' * 10, '-' * 10, '-' * 10, '-' * 10])
        # print('-' * 95)
# print('-' * 95)
table.align = 'l'
print(table)
