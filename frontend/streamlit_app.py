import requests
import streamlit as st

###
# Set app config
###
st.set_page_config(
    page_title="Singapore Hawker Centre Finder",
    page_icon="🕵️",
    layout="centered"
)
st.title("🕵️ Singapore Hawker Centre Finder")

###
# Section to explain app
##
with st.expander("🛈 About this app", expanded=True):

    st.write("""
        This *Singapore Hawker Centre Finder* app returns you at least 5 hawker centres\
        that is closest to you based on the provided latitude and longitude \
        coordinates. Give it a shot and fill up that tummy with delicious hawker food!
    """)

    st.markdown("")

###
# Form section to take in coordinate inputs and number of hawkercentres
##
st.markdown("")
st.markdown("#### 🌎**Provide Coodinates Here**")

with st.form(key="finder"):
    cols = st.columns((1, 1, 1))
    latitude = cols[0].number_input(label="Latitude", value=1.3182)
    longitude = cols[1].number_input(label="Longitude", value=103.8931)
    num_hawkercentres = cols[2].slider(
        "# of hawker centres",
        min_value=5,
        max_value=152,
        value=5,
        help="You can choose how many hawker centres you would like to search for. \
            Between 5 and 152, default number is 5",
    )
    submitted = st.form_submit_button(label="Submit")

###
# Code to display results (both name and image of hawkercentre)
###
if submitted:
    try:
        results = requests.post(
            "http://localhost:8000/finder/nearest_hawkercentre",
            json={
                "latitude": latitude,
                "longitude": longitude,
                "num_hawkercentres": num_hawkercentres
            }
        )
        hawkercentres = results.json()["results"]

        # Show results if success
        st.success(f"Here are the nearest {num_hawkercentres} based on the coordinates \
            {latitude}N, {longitude}N \n (Ranked based on decreasing distance)")
        st.balloons()

        for num in range(len(hawkercentres)):
            with st.container():
                st.write(f"{num+1}) {hawkercentres[num]['name']}")
                if {hawkercentres[num]['name']} is not None:
                    st.image(hawkercentres[num]['photourl'], width=200)
                st.write("---")

    except Exception:
        # Error handling if the fastapi endpoint fails
        st.error("Sorry, seems like there is a problem with our application! \
            Please come back later and try again!")
