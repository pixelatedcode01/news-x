import pandas as pd
import matplotlib.pyplot as plt
import ISO_CODES
import requests


class News:
    """Class for managing news data."""

    def __init__(self, news_csv):
        # Initialize the News object with a CSV file containing news data
        self.news = pd.read_csv(news_csv)

    def filter_news(self, categories=None, number=10):
        # Filter news data based on categories and the number of articles to display
        if categories:
            filtered_news = self.news[self.news["Category"].isin(categories)].head(
                number
            )
        else:
            filtered_news = self.news.head(number)
        return filtered_news

    def get_categories(self):
        # Get unique categories from the news data
        return self.news["Category"].unique()

    def bar_chart(self, start_date, end_date, categories=None):
        # Create a bar chart to visualize the number of articles per category
        # within a specified date range
        if categories:
            # Filter news data by categories if specified
            self.news["Date"] = pd.to_datetime(self.news["Date"], dayfirst=True)
            temp = self.news[self.news["Category"].isin(categories)]
            x = temp[
                (temp["Date"] > start_date) & (temp["Date"] < end_date)
            ].Category.unique()
            y = temp[
                (temp["Date"] > start_date) & (temp["Date"] < end_date)
            ].Category.value_counts()
        else:
            self.news["Date"] = pd.to_datetime(self.news["Date"], dayfirst=True)
            x = self.news[
                (self.news["Date"] > start_date) & (self.news["Date"] < end_date)
            ].Category.unique()
            y = self.news[
                (self.news["Date"] > start_date) & (self.news["Date"] < end_date)
            ].Category.value_counts()

        fig, ax = plt.subplots()
        ax.bar(x, y)
        ax.set_xlabel("Category")
        ax.set_ylabel("Number of Articles")
        ax.set_title("Articles per Category")
        return fig

    def pie(self, start_date, end_date, categories=None):
        # Create a pie chart to visualize the proportions of articles per category
        # within a specified date range
        if categories:
            # Filter news data by categories if specified
            self.news["Date"] = pd.to_datetime(self.news["Date"], dayfirst=True)
            temp = self.news[self.news["Category"].isin(categories)]
            x = temp[
                (temp["Date"] > start_date) & (temp["Date"] < end_date)
            ].Category.unique()
            y = temp[
                (temp["Date"] > start_date) & (temp["Date"] < end_date)
            ].Category.value_counts()
        else:
            self.news["Date"] = pd.to_datetime(self.news["Date"], dayfirst=True)
            x = self.news[
                (self.news["Date"] > start_date) & (self.news["Date"] < end_date)
            ].Category.unique()
            y = self.news[
                (self.news["Date"] > start_date) & (self.news["Date"] < end_date)
            ].Category.value_counts()

        fig, ax = plt.subplots()
        ax.pie(y, labels=x)
        ax.set_title(f"Proportions of Articles from {start_date} to {end_date}")
        return fig

    def trends(self, cateogories=None):
        # Create a line chart to visualize category trends over time
        self.news["Date"] = pd.to_datetime(self.news["Date"], dayfirst=True)
        final = (
            self.news.groupby(self.news.Date.dt.year)["Category"]
            .value_counts()
            .reset_index(name="Count")
        )
        fig, ax = plt.subplots()
        for item in cateogories:
            ax.plot(
                final[final["Category"] == item]["Date"],
                final[final["Category"] == item]["Count"],
                label=item,
            )

        ax.set_xticks(range(2019, 2024))
        ax.legend()
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Articles")
        ax.set_title("Categories trends over time")
        return fig


class LatestNews(News):
    """Class for retrieving and displaying the latest news."""

    def __init__(self, country):
        # Retrieve the latest news data for a specific country using the News API
        for key, value in ISO_CODES.ISO_CODES.items():
            if value == country:
                country_code = key
        url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey=cdcfbdb49fc34fe1824b72090a7d502d"
        response = requests.get(url)
        response_json = response.json()
        self.news = pd.DataFrame(response_json["articles"])
        self.news["publishedAt"] = pd.to_datetime(self.news["publishedAt"])

    def get_latest(self):
        # Return the latest news data
        return self.news


class Favorites:
    """Class for managing user-favorite news articles."""

    def __init__(self):
        self.favorite_news = []

    def add_favorite(self, news_article):
        # Add a news article to the list of favorites
        self.favorite_news.append(news_article)

    def remove_favorite(self, news_article):
        # Remove a news article from the list of favorites
        if news_article in self.favorite_news:
            self.favorite_news.remove(news_article)

    def get_favorites(self):
        # Get the list of favorite news articles
        return self.favorite_news
