import streamlit as st
import pandas as pd
import numpy as np
import io
import time
import json
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000, key="dataframerefresh")

max_personen = 15

aangemeld = json.load(open("Aanmeldingen.json"))


st.title('LLC clubavond aanmelden')

col1, col2 = st.columns(2)

ingevoerde_naam = col1.text_input("Vul hier je naam in")

bevestigen = col2.button("Bevestigen")




if bevestigen:
    if len(aangemeld["Naam"]) >= max_personen:
        st.warning("Te veel aanmeldingen, we zitten vol")
    else:
        aangemeld["Naam"].append(ingevoerde_naam)
        with open('Aanmeldingen.json', 'w') as f:
            json.dump(aangemeld, f)

        st.balloons()


st.title(f"Er zijn nog {max_personen-len(aangemeld['Naam'])} plekken beschikbaar")


st.write("Aanmeldingen:")
for naam in aangemeld["Naam"]:
    st.write("\t" + str(naam))

st.sidebar.title("Admin")

password = st.sidebar.text_input("Password")

if password == st.secrets["wachtwoord"]:
    delete_users = st.sidebar.button("Verwijder alle aanmeldingen")

    if delete_users:
        aangemeld["Naam"] = []
        with open('Aanmeldingen.json', 'w') as f:
            json.dump(aangemeld, f)


    users = st.sidebar.multiselect(label="Selecteer om te verwijderen:", options=aangemeld["Naam"])
    confirm_users_delete = st.sidebar.button("Klik om te verwijderen")

    if confirm_users_delete:
        aangemeld["Naam"] = [x for x in aangemeld["Naam"] if x not in users]
        with open('Aanmeldingen.json', 'w') as f:
            json.dump(aangemeld, f)




