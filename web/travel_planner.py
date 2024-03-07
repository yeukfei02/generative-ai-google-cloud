import streamlit as st
import time
from services.get_itinerary_api import get_itinerary_api

st.title("Travel Planner")

st.write("")

day = st.number_input('Number of days to travel', min_value=1, value=3)
country = st.text_input('Country', 'Hong Kong')

submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if day and country:
        print(f"day = {day}")
        print(f"country = {country}")

        result = get_itinerary_api(day, country)
        if result:
            with st.spinner('Loading...'):
                time.sleep(2)
                st.markdown(result)
