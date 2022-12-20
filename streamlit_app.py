import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, floodRank  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": floodRank.app, "title": "Flood Risk Rank", "icon": "water"},

]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
## **Team139**:


*   [Ahmad AbuHussein Butmah](https://www.linkedin.com/in/ahmad-abuhussein-butmah-583aa3107/)
*   [Ifechukwu MBAMALI](https://www.linkedin.com/in/ifechukwu-mbamali/)
*   [Moeen M. Arbid](https://www.linkedin.com/in/moeen-m-arbid-2a474216/)
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
