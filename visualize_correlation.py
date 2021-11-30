import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

N_COLORS = 256
PALETTE = sns.diverging_palette(150, 290, n=N_COLORS)
COLOR_MIN, COLOR_MAX = [-1, 1]


def value_to_color(val):
    val_position = float((val - COLOR_MIN)) / (COLOR_MAX - COLOR_MIN)
    ind = int(val_position * (N_COLORS - 1))
    return PALETTE[ind]


def make_heatmap(x, y, size, title="Feature Correlations"):
    plot_grid = plt.GridSpec(1, 20, hspace=0.2, wspace=0.1)
    fig = plt.subplots(figsize=(20,20))
    axes = plt.subplot(plot_grid[:,:-1])

    x_labels = [column for column in sorted(x.unique())]
    y_labels = [column for column in sorted(y.unique())]
    x_to_num = {p[1]:p[0] for p in enumerate(x_labels)}
    y_to_num = {p[1]:p[0] for p in enumerate(y_labels)}

    size_scale = 500
    axes.scatter(x=x.map(x_to_num), 
                y=y.map(y_to_num), 
                s=size.abs()*size_scale, 
                c=size.apply(value_to_color),
                marker='s')

    axes.set_xticks([x_to_num[column] for column in x_labels])
    axes.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
    axes.set_yticks([y_to_num[column] for column in y_labels])
    axes.set_yticklabels(y_labels)
    axes.grid(False, 'major')
    axes.grid(True, 'minor')
    axes.set_xticks([t + 0.5 for t in axes.get_xticks()], minor=True)
    axes.set_yticks([t + 0.5 for t in axes.get_yticks()], minor=True)
    axes.set_xlim([-0.5, max([v for v in x_to_num.values()]) + 0.5])
    axes.set_ylim([-0.5, max([v for v in y_to_num.values()]) + 0.5])
    axes.set_title(title)

    axes = plt.subplot(plot_grid[:, -1])
    col_x = [0]*len(PALETTE)
    bar_y = np.linspace(COLOR_MIN, COLOR_MAX, N_COLORS)
    bar_height = bar_y[1] - bar_y[0]
    axes.barh(
        y=bar_y,
        width=[5]*len(PALETTE),
        left=col_x,
        height=bar_height,
        color=PALETTE,
        linewidth=0
    )
    axes.set_xlim(1,2)
    axes.grid(False)
    axes.set_facecolor('white')
    axes.set_xticks([])
    axes.set_yticks(np.linspace(min(bar_y), max(bar_y), 3))
    axes.yaxis.tick_right()
    plt.savefig(title+".png")
    plt.show()
    plt.close()

def get_correlation(data):
    corr = data.corr()
    corr = pd.melt(corr.reset_index(), id_vars='index')
    corr.columns = ['x', 'y', 'value']
    return corr

def get_correlation_matrix(data, title):
    corr = get_correlation(data)
    make_heatmap(x=corr['x'], y=corr['y'], size=corr['value'], title=title)

def get_difference_correlation_matrix(data1, data2, title):
    data1_corr = get_correlation(data1)
    data2_corr = get_correlation(data2)

    corr_diff = data1_corr
    corr_diff['value'] = data1_corr['value'] - data2_corr['value']
    make_heatmap(x=corr_diff['x'], y=corr_diff['y'], size=corr_diff['value'], title=title)