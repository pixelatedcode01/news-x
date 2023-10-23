import streamlit as st
from news import News, Favorites, LatestNews
from weather import Weather
import datetime as dt
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import ISO_CODES
import os

st.set_page_config("Dashboard", page_icon="📃", initial_sidebar_state="collapsed")

file = open(f"current.csv", "r+")
data = file.read().splitlines()
file.close()
currentsession = {}
for line in data:
    key, value = line.strip().split(",")
    if key not in currentsession:
        currentsession[key] = value

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
# value = st.session_state["uid"]


if st.button("Logout"):
    os.remove("current.csv")
    switch_page("home")

st.write(f"# Welcome, {currentsession['username']}")

weather = Weather(currentsession["country"])

st.write("Today's Weather")
current_weather = weather.get_current_weather()
col1, col2, col3, col4 = st.columns(4)
col1.image(f"icons/{current_weather['icon']}.svg", width=60)
col2.metric("Temperature", f'{current_weather["temp"]}°C')
col3.metric("Wind", f'{current_weather["windspeed"]}mph')
col4.metric("Humidity", f'{current_weather["humidity"]}%')


news = News("news_csv.csv")
userfav = Favorites()

tab0, tab1, tab2, tab3 = st.tabs(
    ["Latest News", "All News", "Favorites", "Visualizations"]
)


# def add_to_fav():
#     currentsession["favs"] = []
#     for key, value in st.session_state.items():
#         if value == True:
#             article = {
#                 "key": key,
#                 "title": articles["Title"].iloc[int(key)],
#                 "date": articles["Date"].iloc[int(key)],
#                 "content": articles["Excerpt"].iloc[int(key)],
#             }
#             if "favs" not in currentsession:
#                 currentsession["favs"] = [key]
#             else:
#                 currentsession["favs"].append(article)
#         elif value == False:
#             for item in currentsession["favs"]:
#                 if "key" in item and item["key"] == key:
#                     currentsession["favs"].remove(item)


with tab0:
    st.header("Catch the latest news from around the world")
    st.write("Click refresh to get started")
    country_select = st.selectbox(
        "Country",
        tuple(ISO_CODES.ISO_CODES.values()),
        index=None,
        placeholder=currentsession["country"],
        key="country_select",
    )

    if st.session_state.country_select is None:
        country = currentsession["country"]
    else:
        country = st.session_state.country_select
    if st.button("Refresh", type="primary", key="get"):
        latest = LatestNews(country)
        latest_articles = latest.get_latest()
        for i in range(len(latest_articles)):
            with st.expander(latest_articles["title"].iloc[i]):
                try:
                    st.image(latest_articles["urlToImage"].iloc[i])
                except AttributeError:
                    st.write("No Image to Display")
                st.write(latest_articles["publishedAt"].iloc[i])
                st.write(latest_articles["description"].iloc[i])
                st.write(latest_articles["url"].iloc[i])


with tab1:
    st.header("All news")
    cat_choice = st.multiselect("Select Categories", news.get_categories(), key="cat")
    num_articles = st.selectbox(
        "No. of Articles", ["10", "15", "20", "50", "100"], key="no"
    )

    favs = []
    articles = news.filter_news(
        categories=st.session_state["cat"], number=int(st.session_state["no"])
    )

    for i in range(len(articles)):
        with st.expander(articles["Title"].iloc[i]):
            st.write(articles["Date"].iloc[i])
            st.write(articles["Excerpt"].iloc[i])
            if st.checkbox("Favorite", key=i):
                userfav.add_favorite(
                    [
                        articles["Title"].iloc[i],
                        articles["Date"].iloc[i],
                        articles["Excerpt"].iloc[i],
                    ]
                )

                # favs.append(
                #     [
                #         articles["Title"].iloc[i],
                #         articles["Date"].iloc[i],
                #         articles["Excerpt"].iloc[i],
                #     ]
                # )

print(userfav.get_favorites())

with tab2:
    favorite_articles = userfav.get_favorites()
    st.header("Favorites")
    for item in favorite_articles:
        with st.expander(item[0]):
            st.write(item[1])
            st.write(item[2])

with tab3:
    st.header("Visualizations")
    st.date_input(
        "From",
        min_value=dt.datetime(2019, 1, 1),
        max_value=dt.datetime(2023, 3, 20),
        value=dt.datetime(2019, 1, 1),
        key="min",
    )
    st.date_input(
        "To",
        min_value=dt.datetime(2019, 1, 1),
        max_value=dt.datetime(2023, 3, 20),
        value=dt.datetime(2019, 1, 1),
        key="max",
    )
    st.multiselect("Categories", news.get_categories(), key="plotcat")
    st.radio("Graph Type", ["Bar Graph", "Pie", "Line"], key="type")
    if (
        pd.to_datetime(st.session_state.max) >= pd.to_datetime(st.session_state.min)
        and st.session_state.type == "Bar Graph"
    ):
        st.pyplot(
            news.bar_chart(
                pd.to_datetime(st.session_state.min),
                pd.to_datetime(st.session_state.max),
                categories=st.session_state["plotcat"],
            )
        )
    elif (
        pd.to_datetime(st.session_state.max) >= pd.to_datetime(st.session_state.min)
        and st.session_state.type == "Pie"
    ):
        st.pyplot(
            news.pie(
                pd.to_datetime(st.session_state.min),
                pd.to_datetime(st.session_state.max),
                categories=st.session_state["plotcat"],
            )
        )
    elif st.session_state.type == "Line":
        """ """
        st.pyplot(news.trends(cateogories=st.session_state["plotcat"]))

    else:
        st.write("# Please enter correct dates.")
