"""
The script develops the user application. This application accepts user inputs and 
feeds them to the model. The resulting model predictions are displayed in the application.    
"""

import pandas as pd
import streamlit as st
import pickle as pkl
import os
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("bank-additional.csv",sep=";")

st.title('Deposit Prediction for Bank Marketing Campaign')

st.write("This app is based on 13 inputs that predict whether a customer will deposit or not? Using this app, a bank can identify specific customer segments; that will make deposits.")
st.write("Please use the following form to get started!")
st.write('<p class="big-font">(NOTE: For convenience, usual values are pre-selected in the form.)</p>', unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.mozo.com.au/redactor/pictures/9885/short-or-long-term-deposit_original.png");
             
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# selecting age
st.subheader("Select Customer's Age")
selected_age = st.slider("Select Customer's Age", min_value = 18, max_value = 95, 
                         step = 1, value = 41)    # Slider does not tolerate dtype value mismatch df.age.max() was thus not used.
st.write("Selected Age:", selected_age)


# selecting job
st.subheader("Select Customer's Job")
selected_job = st.radio("", df['job'].unique(), index=3)
st.write("Selected Job:", selected_job)


## Encode the job entered by user
### Declaring function for encoding
def encode_job(selected_item):
    dict_job = {'admin.':0, 'blue-collar':1, 'entrepreneur':2, 'housemaid':3, 'management':4, 'retired':5, 'self-employed':6, 'services':7, 'student':8, 'technician':9, 'unemployed':10}
    return dict_job.get(selected_item, -1)

### Using function for encoding
selected_job = encode_job(selected_job)  


# selecting marital status
st.subheader("Select Customer's Marital")
selected_marital = st.radio("", df['marital'].unique())
st.write("Selected Marital:", selected_marital)


## Encode the marital entered by user
### Declaring function for encoding
def encode_marital(selected_item):
    dict_marital = {'divorced':0, 'married':1, 'single':2}
    return dict_marital.get(selected_item, -1)

### Using function for encoding
selected_marital = encode_marital(selected_marital)  



# selecting education
st.subheader("Select Customer's Education")
selected_education = st.radio("", df['education'].unique())
st.write("Selected Education:", selected_education)

## Encode the education entered by user
### Declaring function for encoding

def encode_education(selected_item):
    dict_education = {'basic.4y':0, 'basic.6y':1, 'basic.9y':2, 'high.school':3, 'illiterate':4, 'professional.course':5, 'university.degree':6}
    return dict_education.get(selected_item, -1)

### Using function for encoding
selected_education = encode_education(selected_education)  


# selecting default status
st.subheader("Select Customer's Default Status")
selected_default = st.radio("", df['default'].unique()[::-1])
st.write("Selected Default Status", selected_default)

## Encode the default entered by user
### Declaring function for encoding
def encode_default(selected_item):
    dict_default = {'no':0, 'yes':1}
    return dict_default.get(selected_item, -1)

### Using function for encoding
selected_default = encode_default(selected_default)


# selecting housing status
st.subheader("Select Customer's Housing Status")

selected_housing = st.radio("", df['housing'].unique(), 
                            index = 1, key = "1")
st.write("Selected Housing Status", selected_housing)


## Encode the housing entered by user
### Declaring function for encoding
def encode_housing(selected_item):
    dict_housing= {'no':0, 'yes':1}
    return dict_housing.get(selected_item, -1)

### Using function for encoding
selected_housing = encode_housing(selected_housing)  


# selecting loan status
st.subheader('Select Loan Status')

selected_loan = st.radio("", df['loan'].unique()[::-1], index=1, key="2")
st.write("Selected Loan Status", selected_loan)

## Encode the loan entered by user
### Declaring function for encoding
def encode_loan(selected_item):
    dict_loan= {'no':0, 'yes':1}
    return dict_loan.get(selected_item, -1)

### Using function for encoding
selected_loan = encode_loan(selected_loan)  


# selecting contact
# st.title("Select Customer's Contact")
st.subheader("Select Customer's Contact")

selected_contact = st.radio("Select Contact", df['contact'].unique(), 
                            index = 1)
st.write("Selected Contact Type", selected_contact)

## Encode the contact entered by user
### Declaring function for encoding
def encode_contact(selected_item):
    dict_contact= {'cellular':0, 'telephone':1}
    return dict_contact.get(selected_item, -1)

### Using function for encoding
selected_contact = encode_contact(selected_contact)


# selecting day
st.subheader('Select day')
selected_day = st.radio("Select Day", df['day_of_week'].unique(),
                     index=1)
st.write('Selected Day:', selected_day)

## Encode the day entered by user
### Declaring function for encoding
def encode_day(selected_item):
    dict_day = {'thu':0, 'mon':1, 'tue':2, 'wed':3, 'fri':4}
    return dict_day.get(selected_item, -1)

### Using function for encoding
selected_day = encode_day(selected_day)

# selecting month
st.subheader('Select Last Contact Month of Customer')
selected_month = st.radio("Select Month", df['month'].unique(), 
                            index = 1)
st.write("Selected Month", selected_month)

## Encode the month entered by user
### Declaring function for encoding
def encode_month(selected_item):
    dict_month = {'apr':0, 'aug':1, 'dec':2, 'feb':3, 'jan':4, 'jul':5, 'jun':6, 'mar':7, 'may':8, 'nov':9, 'oct':10, 'sep':11}
    return dict_month.get(selected_item, -1)

### Using function for encoding
selected_month = encode_month(selected_month)  


# selecting duration
st.subheader("Select Customer's Duration")
selected_duration = st.slider('Select Customer Duration', min_value = 2,
                     max_value = 3881, step = 1, 
                     value = int(df.duration.mean()))
st.write("Selected Customer Duration", selected_duration)



# selecting campaign
st.subheader('Select Number of Contacts Peroformed in this Campaign')
campaign_range = list(range(df['campaign'].min(), df['campaign'].max()))
selected_campaign = st.selectbox('Select Campaign:',(campaign_range), index=0)
st.write('You selected:', selected_campaign)


# selecting poutcome
st.subheader('Select Outcome of Previous Campaign') 
selected_poutcome = st.radio("Select poutcome", df['poutcome'].unique(), index=0)
st.write("Selected poutcome:", selected_poutcome)

## Encode the poutcome entered by user
### Declaring function for encoding
def encode_pout(selected_item):
    dict_pout = {'failure':0, 'other':1, 'success':2}
    return dict_pout.get(selected_item, -1)

### Using function for encoding
selected_poutcome = encode_pout(selected_poutcome)


pickle_in = open("https://github.com/ggkasman/Default-Prediction-Web-App-Streamlit/blob/main/model2.pkl", "rb")
classifier = pkl.load(pickle_in)


prediction = classifier.predict([[selected_age, selected_job,
                                  selected_marital, selected_education,
                                  selected_default, selected_housing,
                                  selected_loan, selected_contact,
                                  selected_month, selected_day,
                                  selected_duration, selected_campaign,
                                  selected_poutcome,
                                  ]])



# Adding Predict Button
predict_button = st.button('Predict')
# st.write(predict_button)

if predict_button:
    if prediction == 1 :
        st.success('This customer segment will Deposit')
    else:
        st.success('This customer segment will NOT Deposit')


st.write('\n')
about = st.expander('More about app')
