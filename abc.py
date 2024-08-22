import streamlit as st
import matplotlib.pyplot as plt

# Les données
ages = {
    'age1': 12,
    'age2': 24,
    'age3': 25
}

# Afficher les âges dans l'interface
st.title("Visualisation des âges")
st.write("Voici les âges disponibles :")
for key, value in ages.items():
    st.write(f"{key}: {value} ans")

# Visualiser les âges avec un graphique
st.write("Graphique des âges")
fig, ax = plt.subplots()
ax.bar(ages.keys(), ages.values())
ax.set_xlabel("Catégories")
ax.set_ylabel("Âges")
ax.set_title("Distribution des âges")
st.pyplot(fig)
