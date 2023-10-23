import pandas as pd
import matplotlib.pyplot as plt
import ISO_CODES
import requests


class News:
    """ """

    def __init__(self, news_csv):
        self.news = pd.read_csv(news_csv)

    def filter_news(self, categories=None, number=10):
        if categories:
            filtered_news = self.news[self.news["Category"].isin(categories)].head(
                number
            )
        else:
            filtered_news = self.news.head(number)
        return filtered_news

    def get_categories(self):
        return self.news["Category"].unique()

    def bar_chart(self, start_date, end_date, categories=None):
        """ """
        if categories:
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
            # plotable_news = self.news[self.news["Category"].isin(categories)]
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
        """"""
        if categories:
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
        """ """
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
        ax.set_title("Categories trends overtime")
        return fig


class LatestNews(News):
    """"""

    def __init__(self, country):
        for key, value in ISO_CODES.ISO_CODES.items():
            if value == country:
                country_code = key
        url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey=cdcfbdb49fc34fe1824b72090a7d502d"
        response = requests.get(url)
        response_json = response.json()
        self.news = pd.DataFrame(response_json["articles"])
        self.news["publishedAt"] = pd.to_datetime(self.news["publishedAt"])

    def get_latest(self):
        return self.news


class Favorites:
    """"""

    def __init__(self):
        self.favorite_news = []

    def add_favorite(self, news_article):
        self.favorite_news.append(news_article)

    def remove_favorite(self, news_article):
        if news_article in self.favorite_news:
            self.favorite_news.remove(news_article)

    def get_favorites(self):
        return self.favorite_news
