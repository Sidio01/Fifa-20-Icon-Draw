import random


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


icon_keepers = ['E. Van Der Sar', 'L. Yashin', 'P. Schmeichel', 'J. Lehmann']
icon_defenders = ['F. Baresi', 'C. Alberto', 'C. Puyol', 'B. Moore', 'J. Zanetti',
                  'A. Nesta', 'L. Blanc', 'F. Hierro', 'M. Desailly', 'R. Carlos', 'R. Koeman', 'G. Zambrotta']
icon_midfielders = ['R. Baggio', 'R. Giggs', 'A. Pirlo', 'M. Laudrup', 'P. Scholes', 'G. Hagi',
                    'R. Pires',  'S. Gerrard', 'P. Nedved', 'C. Seedors', 'M. Ballack', 'Socrates',
                    'J. Litmanen', 'J. Okocha', 'F. Rijkaard', 'M. Overmars', 'Deco', 'L. Matthaus', 'R. Costa',
                    'R. Keane', 'F. Lampard','C. Makelele', 'S. Veron', 'P. Guardiola', 'G. Gattuso',
                    'H. Nakata']
icon_strikers = ['Ronaldinho',  'M. Garrincha', 'M. Van Basten', 'G. Best', 'T. Henry',  'L. Figo', 'A. Del Piero',
                 'G. Lineker', 'E. Butragueno', 'R. Van Nistelrooy', 'D. Bergkamp', 'H. Stoichkov', 'Rivaldo', 'Raul',
                 'H. Sanchez', 'M. Owen', 'A. Shearer', 'A. Shevchenko', 'P. Kluivert', 'D. Trezeguet',
                 'M. Klose', 'I. Rush', 'D. Drogba', 'F. Inzaghi', 'H. Larsson', 'H. Crespo', 'L. Hernandez', 'G. Zola',
                 'C. Vieri', 'J. Barnes', 'I. Wright']
icon_best_defenders = ['P. Maldini', 'R. Ferdinand', 'F. Cannavaro', 'S. Campbell']
icon_best_def_midfielders = ['P. Vieira', 'R. Gullit', 'M. Essien', 'E. Petit']
icon_best_att_midfielders = ['Z. Zidane', 'Pele', 'D. Maradona', 'Kaka']
icon_best_strikers = ['Ronaldo', 'J. Cruyff', 'Eusebio', 'K. Dalglish']
print(len(icon_midfielders))
print(len(icon_strikers))
print(len(icon_keepers) + len(icon_defenders) + len(icon_midfielders)+ len(icon_strikers) + len(icon_best_defenders)
      + len(icon_best_def_midfielders) + len(icon_best_att_midfielders) + len(icon_best_strikers))
print('Введите участников первой команды:')
# team1_name = input()
team1_name = 'Тимур и Диман'
print('Введите участников второй команды:')
# team2_name = input()
team2_name = 'Леха и Илюха'
print('Введите участников третьей команды:')
# team3_name = input()
team3_name = 'Женя и Руб'
print('Введите участников четвертой команды:')
# team4_name = input()
team4_name = 'Денис и Саня'
team1_squad = []
team2_squad = []
team3_squad = []
team4_squad = []

# Выбор вратарей
icon_choice(icon_keepers, 1)  # всего 4, остаток 0

# Выбор защитников
icon_choice(icon_defenders, 3)  # всего 12, остаток 0
icon_choice(icon_best_defenders, 1)

# Выбор полузащитников
icon_choice(icon_midfielders, 6)  # всего 26, остаток 2
icon_choice(icon_best_def_midfielders, 1)
icon_choice(icon_best_att_midfielders, 1)

# Выбор нападающих
icon_choice(icon_strikers, 4)  # всего 31, остаток 15
icon_choice(icon_best_strikers, 1)

# Вывод жеребьевки
print('-' * 75)
print('{:<20s}{:<20s}{:<20s}{:<20s}'.format(str(team1_name), str(team2_name), str(team3_name), str(team4_name)))
print('-' * 75)
teams = [team1_squad, team2_squad, team3_squad, team4_squad]
i = 0
for _ in range(len(team1_squad)):
    print('{:<20s}{:<20s}{:<20s}{:<20s}'.format(str(teams[0][i]), str(teams[1][i]), str(teams[2][i]), str(teams[3][i])))
    i += 1
    if i == 1:
        print('-' * 75)
    if i == 5:
        print('-' * 75)
    if i == 13:
        print('-' * 75)
print('-' * 75)
