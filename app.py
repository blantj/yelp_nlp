#Import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from pickle import load

#
st.title('Yelp Review Business Type Classifier')
st.markdown('Enter a 140 character review snippet and nlp modeling will determine if it is for a gym or barber class business')

#
label = 'Enter an English gym or barbershop review of 140 characters'
review = [st.text_input(label, max_chars=140)]

#
vectorizer = load(open('Pickles/vectorizer.pickle', 'rb'))
x = vectorizer.transform(review)


#
nb = load(open('Pickles/naive_bayes.pickle', 'rb'))
y_pred = nb.predict(x)

#
columns = ['Review Business Class']
output = pd.DataFrame(columns=columns)
output.loc[0] = [y_pred]
output_dict = {0: 'Barber', 1: 'Gym'}
output.replace(output_dict, inplace=True)
output.index = [' ']


#
st.table(output)