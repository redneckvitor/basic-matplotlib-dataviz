import matplotlib.pyplot as plt
from pathlib import Path
import json

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

path = Path('profits.json')
contents = path.read_text()
profits = json.loads(contents)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(input_values, profits, linewidth=2, color='limegreen')

ax.set_title("Lucros da empresa em 2023", fontsize=20)
ax.set_ylabel("Lucro (R$)", fontsize=14)
ax.set_xticks(input_values)
ax.set_xticklabels(months)
ax.tick_params(axis='both', labelsize=14)

plt.show()
