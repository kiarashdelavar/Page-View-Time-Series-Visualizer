# Page-View Time Series Visualizer 
This project involves visualizing time series data using line charts, bar charts, and box plots. The dataset contains the number of daily page views on the "freeCodeCamp.org" forum from 2016-05-09 to 2019-12-03. By leveraging Pandas, Matplotlib, and Seaborn, we aim to uncover patterns in visit data and identify yearly and monthly growth trends.

Project Overview:

Objectives:

1- Data Import and Cleaning:

    1- Import the data from "fcc-forum-pageviews.csv" using Pandas.
    2- Set the date column as the index.
    3- Filter out the days where page views fall in the top or bottom 2.5% of the dataset to clean the data.

2- Data Visualization:

    1- Line Chart: Create a function draw_line_plot to generate a line chart visualizing daily page views.
    2- Bar Chart: Create a function draw_bar_plot to generate a bar chart showing average daily page views for each month, grouped by year.
    3- Box Plots: Create a function draw_box_plot to generate two adjacent box plots to display the distribution of page views by year and by month.

3- Bar Chart:

    1- implement draw_bar_plot to show average daily page views per month, grouped by year.
    2- The legend should include month labels with a title "Months".
    3- Label the x-axis as "Years" and the y-axis as "Average Page Views".

4- Box Plots:

    1- Implement draw_box_plot using Seaborn to create two box plots:
         *Year-wise Box Plot (Trend): Displays distribution of page views by year.
         *Month-wise Box Plot (Seasonality): Displays distribution of page views by month.
    2- Ensure month labels on the x-axis start at January.
    3- Label the axes appropriately.

Implementation:

        # Importing libraries
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        # Load and clean data
        def load_and_clean_data(file_path):
            df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
            df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
            return df

        # Line plot
        def draw_line_plot():
            df = load_and_clean_data('fcc-forum-pageviews.csv')
            plt.figure(figsize=(12, 6))
            plt.plot(df.index, df['value'], color='red')
            plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
            plt.xlabel('Date')
            plt.ylabel('Page Views')
            plt.savefig('line_plot.png')
            return plt.gca()

        # Bar plot
        def draw_bar_plot():
            df = load_and_clean_data('fcc-forum-pageviews.csv')
            df['year'] = df.index.year
            df['month'] = df.index.month
            df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
            df_bar.plot(kind='bar', figsize=(12, 6))
            plt.title('Average Daily Page Views per Month')
            plt.xlabel('Years')
            plt.ylabel('Average Page Views')
            plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
            plt.savefig('bar_plot.png')
            return plt.gca()

        # Box plots
        def draw_box_plot():
            df = load_and_clean_data('fcc-forum-pageviews.csv')
            df['year'] = df.index.year
            df['month'] = df.index.strftime('%b')
            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    sns.boxplot(x='month', y='value', data=df, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.savefig('box_plot.png')
    return plt.gca()

        # Load data and prepare the visualizations
        df = load_and_clean_data('fcc-forum-pageviews.csv')
        draw_line_plot()
        draw_bar_plot()
        draw_box_plot()

Conclusion:

By visualizing the time series data with line charts, bar charts, and box plots, we can better understand the patterns in page views on the freeCodeCamp.org forum. This project demonstrates effective data cleaning, analysis, and visualization techniques using Pandas, Matplotlib, and Seaborn.
