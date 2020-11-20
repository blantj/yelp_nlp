#Import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from pickle import load

#Set streamlit website header and subheader
st.title('Yelp Review Business Type Classifier')
st.markdown('Enter a 140 character review snippet and nlp modeling will determine if it is for a gym or barber class business')

#Create text box for website user to enter sample business review
label = 'Enter an English gym or barbershop review of 140 characters'
review = [st.text_input(label, max_chars=140)]

#Load pickled vectorizer and use to vectorize sample review
vectorizer = load(open('Pickles/vectorizer.pickle', 'rb'))
x = vectorizer.transform(review)

#Load pickled naive bayes model and use to predict sample review class
nb = load(open('Pickles/naive_bayes.pickle', 'rb'))
y_pred = nb.predict(x)

#Create df with sample review class prediction
columns = ['Review Business Class']
output = pd.DataFrame(columns=columns)
output.loc[0] = [y_pred]
output_dict = {0: 'Barber', 1: 'Gym'}
output.replace(output_dict, inplace=True)
output.index = [' ']


#Display sample review class prediction df on streamlit website
st.table(output)