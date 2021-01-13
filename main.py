import random
import matplotlib.pyplot as plt

number_repeat = 10000

point_x = 0
point_y = 0
state = '0'

payoff = {'T': 5, 'R': 3, 'P': 1, 'S': 0}

p = {'CC': 1/2, 'CD': 1/2, 'DC': 1/2, 'DD': 1/2, '0': 1/2}
q = {'CC': 1/2, 'CD': 1/2, 'DC': 1/2, 'DD': 1/2, '0': 1/2}

payoff_hist_x = []
payoff_hist_y = []
time_list = []

for t in range(number_repeat):
    action_x = 'C' if random.random() <= p[state] else 'D'
    action_y = 'C' if random.random() <= q[state] else 'D'

    if action_x == 'C' and action_y == 'C':
        point_x += payoff['R']
        point_y += payoff['R']
    elif action_x == 'C' and action_y == 'D':
        point_x += payoff['S']
        point_y += payoff['T']
    elif action_x == 'D' and action_y == 'C':
        point_x += payoff['T']
        point_y += payoff['S']
    elif action_x == 'D' and action_y == 'D':
        point_x += payoff['P']
        point_y += payoff['P']
    state = action_x + action_y

    payoff_hist_x.append(point_x / (t+1))
    payoff_hist_y.append(point_y / (t+1))
    time_list.append(t)

plt.figure(figsize=(7, 5))
plt.rcParams["font.size"] = 15
plt.ylabel('Average Score')
plt.xlabel('Number of repetitions')
plt.xscale("log")
plt.ylim(-0.5, 5.5)

plt.plot(time_list, payoff_hist_x, label='Player X')
plt.plot(time_list, payoff_hist_y, label='Player Y')

plt.legend()
plt.savefig("img.png")

# 各プレイヤーの平均点数を出力
print(f'Player X: {point_x / number_repeat} Points')
print(f'Player Y: {point_y / number_repeat} Points')
