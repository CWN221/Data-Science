import matplotlib.pyplot as plt
import numpy as np

x1 = [50, 53, 59, 56, 62]
y1 = [39, 47, 42, 51, 51]
z1 = [70, 80, 91, 87, 92]

months = ["07/2019", "08/2019", "09/2019", "10/2019", "11/2019"]

# Bars plotting
width = 0.30
x = np.arange(len(months)) * 1.2
plt.bar(x - width, x1, width=width, color="blue")
plt.bar(x, y1, width=width, color="pink")
plt.bar(x + width, z1, width=width, color="orange")

plt.xticks(x, months)
plt.tick_params(bottom=False)
plt.legend(
    ["Searches", "Direct", "Social Media"],
    loc="lower center",
    bbox_to_anchor=(0.5, -0.30),
    ncol=3,
    fontsize=12,
    frameon=False,
)
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Labels Section
plt.xlabel("months", loc="right")
plt.ylabel("visitors \n in thousands", loc="top", rotation=0)
plt.title("Visitors by web traffic sources", pad=50, fontsize=18)
for i in range(len(x)):
    plt.text(x[i] - width, x1[i] + 1, str(x1[i]), ha="center", fontsize=9)
    plt.text(x[i], y1[i] + 1, str(y1[i]), ha="center", fontsize=9)
    plt.text(x[i] + width, z1[i] + 1, str(z1[i]), ha="center", fontsize=9)
ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()
