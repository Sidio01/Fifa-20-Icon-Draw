import random


icon_list = ['D. Maradona', 'Eusebio', 'Z. Zidane', 'D. Trezeguet', 'R. Carlos', 'E. Van Der Sar', 'G. Best', 'R. Gullit', 9]
icon_keepers = []
icon_defenders = []
icon_midfielders = []
icon_strikers = []
icon_best = []
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
try:
    for _ in range(2):
        player = random.choice(icon_list)
        team1_squad.append(player)
        icon_list.remove(player)
        player = random.choice(icon_list)
        team2_squad.append(player)
        icon_list.remove(player)
        player = random.choice(icon_list)
        team3_squad.append(player)
        icon_list.remove(player)
        player = random.choice(icon_list)
        team4_squad.append(player)
        icon_list.remove(player)
except IndexError:
    pass
print('-' * 75)
print('{:<20s}{:<20s}{:<20s}{:<20s}'.format(str(team1_name), str(team2_name), str(team3_name), str(team4_name)))
print('-' * 75)
teams = [team1_squad, team2_squad, team3_squad, team4_squad]
i = 0
for _ in range(2):
    print('{:<20s}{:<20s}{:<20s}{:<20s}'.format(str(teams[0][i]), str(teams[1][i]), str(teams[2][i]), str(teams[3][i])))
    i += 1
print('-' * 75)
