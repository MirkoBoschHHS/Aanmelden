import streamlit as st
import pandas as pd
import numpy as np
import io
import time
import json

aangemeld = json.load(open("Aanmeldingen.json"))


st.title('LLC clubavond aanmelden\'s')

col1, col2 = st.columns(2)

ingevoerde_naam = col1.text_input("Vul hier je naam in")

bevestigen = col2.button("Bevestigen")

# if ingevoerde_naam != "":
#     st.balloons()


if bevestigen:
    aangemeld["Naam"].append(ingevoerde_naam)
    with open('Aanmeldingen.json', 'w') as f:
        json.dump(aangemeld, f)

    st.balloons()

st.write("Aanmeldingen:")
for naam in aangemeld["Naam"]:
    st.write("\t" + str(naam))

# st.write(aangemeld)