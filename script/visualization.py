from audioop import error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/result.csv", header=None, skiprows=1)
array = df.values

x_opts = ["Two Options", "Three Options", "Four Options", "Five Options"]
y_opts = [array[:, 0].mean(), 0.2 * (array[:, 2] + array[:, 4] + array[:, 6] + array[:, 8] + array[:, 10]).mean(),
          array[:, 12].mean(), array[:, 14].mean()]
error_opts = [abs(array[:, 0] - y_opts[0]).max(),
              abs(0.2 * (array[:, 2] + array[:, 4] + array[:, 6] + array[:, 8] + array[:, 10]) - y_opts[1]).max(),
              abs(array[:, 12] - y_opts[2]).max(),
              abs(array[:, 14] - y_opts[3]).max()]

x_mods = ["Audio & Vedio (1)", "Audio & Vedio (2)", "Only Vedio (1)", "Only Vedio (2)", "Only Audio (1)",
          "Only Audio (2)"]
y_mods = [array[:, 16].mean(), array[:, 18].mean(), array[:, 20].mean(), array[:, 22].mean(), array[:, 24].mean(),
          array[:, 26].mean()]
error_mods = [abs(array[:, 16] - y_mods[0]).max(), abs(array[:, 18] - y_mods[1]).max(),
              abs(array[:, 20] - y_mods[2]).max(), abs(array[:, 22] - y_mods[3]).max(),
              abs(array[:, 24] - y_mods[4]).max(), abs(array[:, 26] - y_mods[5]).max(),
              ]

x_3op = ["Exp1", "Exp2", "Exp3", "Exp4", "Exp5"]
y_3op = [array[:, 2].mean(), array[:, 4].mean(), array[:, 6].mean(), array[:, 8].mean(), array[:, 10].mean()]
error_3op = [abs(array[:, 2] - y_3op[0]).max(), abs(array[:, 4] - y_3op[1]).max(), abs(array[:, 6] - y_3op[2]).max(),
             abs(array[:, 8] - y_3op[3]).max(), abs(array[:, 10] - y_3op[4]).max(), ]

plt.figure(figsize=(10, 6))
plt.errorbar(x_opts, y_opts, yerr=error_opts, fmt='o', capsize=5, label='Average Time with Error Bar')
plt.xlabel('Number of Options')
plt.ylabel('Reaction Time (ms)')
plt.title('Simulated Reaction Times Based on Number of Options')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(x_mods, y_mods, yerr=error_mods, fmt='o', capsize=5, label='Average Time with Error Bar')
plt.xlabel('Different Modalities')
plt.ylabel('Reaction Time (ms)')
plt.title('Simulated Reaction Times Based on Different Modalities')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(x_3op, y_3op, yerr=error_3op, fmt='o', capsize=5, label='Average Time with Error Bar')
plt.xlabel('Different Experiment')
plt.ylabel('Reaction Time (ms)')
plt.title('Simulated Reaction Times For Different Experiments')
plt.legend()
plt.show()
