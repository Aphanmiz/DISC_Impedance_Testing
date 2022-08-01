import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import statsmodels


def significance_plot(x1, x2, y, p_value):
    h=0
    plt.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=1.5, color='black')
    # h=h-1
    if p_value <= 0.001:
        plt.text((x1 + x2) * .5, y + h, "***", ha='center', va='bottom', fontsize=11)
    elif p_value <= 0.01:
        plt.text((x1 + x2) * .5, y + h, "**", ha='center', va='bottom', fontsize=11)
    else:
        plt.text((x1 + x2) * .5, y + h, "*", ha='center', va='bottom', fontsize=11)



data=pd.read_csv('~/Desktop/Seymour Lab/Stats/IDE/MG 221507 IDE_life_span.csv')
order_list = ["2", "4", '8','16']

# fig=plt.figure(figsize=[15, 6])

ax=sns.boxplot(x="IDE", y="Converted Date", data=data, color='lightgrey',showmeans=True,    meanprops={"marker":"_",
                       "markerfacecolor":"black",
                       "markeredgecolor":"black",
                      "markersize":"10"})#meanprops={'color': 'red', 'ls':'.', 'lw': 5})
ax=sns.swarmplot(x="IDE", y="Converted Date", data=data, hue='Type', size=10, dodge=True, linewidth=1, edgecolor="gray", alpha=.8)

ax.set_ylabel('Day', fontsize=18, fontname='Arial')
ax.set_xlabel('\n Gap Size', fontsize=18, fontname='Arial')
# ax.set_title("By Whisker", fontsize=22, fontname='Arial')
plt.xticks(fontsize=15, fontname='Arial')
# ax.yaxis.tick_right()
# plt.yticks(fontsize=15, fontname='Arial')
# ax.set_ylim([0, 110])

plt.subplots_adjust(wspace=0, hspace=0)
# plt.savefig('Accuracy.eps', format='eps')

plt.show()


