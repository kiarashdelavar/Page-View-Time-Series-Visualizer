import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():

    fig, ax = plt.subplots(figsize=(15,5))

    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    fig = df_bar.plot(kind ='bar', figsize=(15, 10)).figure
    plt.xlabel('Years', fontsize=10)
    plt.ylabel('Average Page Views', fontsize=10)
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1,13)])

    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
    
    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax1)
    sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax2)

    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    plt.savefig('box_plot.png')
    return fig
