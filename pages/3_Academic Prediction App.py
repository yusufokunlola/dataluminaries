# import libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle

st.set_page_config(page_title="Academic Performance Prediction", page_icon="🎓", layout="wide")

st.title("")
st.markdown("<h1 style='text-align: center; color: black;'>Academic Performance Prediction</h1>", unsafe_allow_html=True)
# st.write("This app uses predicts academic performance of students based on the selected features.")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data.csv")
    return df

df = load_data()

# Create a new column 'jamb_performance' based on the 'jamb_score'
df['jamb_performance'] = df['jamb_score'].apply(lambda x: 'fail' if x < 200 else 'pass')

# Define the bins and labels for 'no_of_siblings'
bins_siblings = [0, 3, 6, float('inf')]
labels_siblings = ['Low', 'Medium', 'High']
df['siblings_category'] = pd.cut(df['no_of_siblings'], bins=bins_siblings, labels=labels_siblings, right=True)

# Define the bins and labels for 'average_days_absent'
bins_absent = [-1, 3, 6, float('inf')]
labels_absent = ['Low', 'Moderate', 'High']
df['absence_category'] = pd.cut(df['average_days_absent'], bins=bins_absent, labels=labels_absent)

# Drop unnecessary columns
df = df.drop(columns=['jamb_score', 'no_of_siblings', 'average_days_absent', 'created_time', 'exam_prep_challenges', 'recommendations'])

# Simplified mapping for each categorical feature
age_mapping = {
    '16 -20': 0, 
    '21-25': 1, 
    '25-30': 2, 
    '30-34': 3, 
    '35 - 40': 4, 
    'above 40': 5
}

gender_mapping = {
    'Female': 0, 
    'Male': 1
}

income_mapping = {
    'low': 0, 
    'low-middleclass': 1, 
    'upper-middleclass': 2, 
    'High': 3
}

education_mapping = {
    'Informal': 0, 
    'Secondary School Cert': 1, 
    'National Diploma': 2, 
    'HND': 3, 
    'Bachelors Degree': 4, 
    'Post Graduate': 5
}

marital_mapping = {
    'Single': 0, 
    'Married': 1, 
    'Divorced': 2, 
    'Widowed': 3
}

residence_mapping = {
    'Rural': 0, 
    'Sub-Urban': 1, 
    'Urban': 2
}

family_mapping = {
    'Nuclear': 0, 
    'Extended': 1
}

distance_mapping = {
    'less than 1km': 0, 
    '1-3km': 1, 
    '3-5km': 2, 
    'Above 5km': 3
}

participation_mapping = {
    'Low': 0, 
    'Moderate': 1, 
    'High': 2
}

jamb_mapping = {
    'fail': 0, 
    'pass': 1
}

siblings_mapping = {
    'Low': 0, 
    'Medium': 1, 
    'High': 2
}

absence_mapping = {
    'Low': 0, 
    'Moderate': 1, 
    'High': 2
}

# Apply mappings
df['Age'] = df['Age'].replace(age_mapping)
df['Gender'] = df['Gender'].replace(gender_mapping)
df['average_household_income'] = df['average_household_income'].replace(income_mapping)
df['parents_educational_qualification'] = df['parents_educational_qualification'].replace(education_mapping)
df['marital_status_of_parents'] = df['marital_status_of_parents'].replace(marital_mapping)
df['Residence'] = df['Residence'].replace(residence_mapping)
df['Type_of_family'] = df['Type_of_family'].replace(family_mapping)
df['distance_btwn_home_school'] = df['distance_btwn_home_school'].replace(distance_mapping)
df['class_participation'] = df['class_participation'].replace(participation_mapping)
df['jamb_performance'] = df['jamb_performance'].replace(jamb_mapping)
df['siblings_category'] = df['siblings_category'].replace(siblings_mapping)
df['absence_category'] = df['absence_category'].replace(absence_mapping)


# Select only numeric columns from the DataFrame
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Fill missing values (incase there is any) with the mean of each column
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Define the list of features for the model based on the  Recursive Feature Elimination method
model_features = [
    'Age', 
    'Gender', 
    'average_household_income',
    'parents_educational_qualification', 
    'distance_btwn_home_school',
    'use_of_library_and_study_spaces', 
    'use_of_internet', 
    'stress_levels',
    'extracurricular_activities', 
    'study_satasifaction'
]

# Create explanatory variable (X) and response variable (y)
X = df[model_features]  # Use square brackets to select multiple columns
y = df['jamb_performance']

# Split the dataset into training and testing sets (70:30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale numeric features
sc = StandardScaler()
numeric = X_train.columns
X_train[numeric] = sc.fit_transform(X_train[numeric])
X_test[numeric] = sc.transform(X_test[numeric])

# Train the model
model = SVC()
model.fit(X_train, y_train)

# Save the model as a pickle file
pickle.dump(model, open('model.pkl', 'wb'))

# Load the model
cla_model = pickle.load(open('model.pkl', 'rb'))


# Option to make predictions on new data
# st.subheader("Make Predictions on New Data")
st.text('Select the fields below to predict academic performance.')

st.text('')
col1, col2 = st.columns(2)

with col1:
    age_category = st.selectbox('Age', (
        '16 -20', 
        '21-25', 
        '25-30', 
        '30-34', 
        '35 - 40', 
        'above 40'
    ))

    age_category = 0 if age_category == '16 -20' else \
                1 if age_category == '21-25' else \
                2 if age_category == '25-30' else \
                3 if age_category == '30-34' else \
                4 if age_category == '35 - 40' else \
                5

    gender_category = st.selectbox('Gender', (
        'Female', 
        'Male'
    ))

    gender_category = 0 if gender_category == 'Female' else 1
    
    income_category = st.selectbox('average_household_income', (
        'Low', 
        'Low - Middleclass', 
        'Upper - Middleclass', 
        'High'
    ))

    income_category = 0 if income_category == 'Low' else \
                    1 if income_category == 'Low - Middleclass' else \
                    2 if income_category == 'Upper - Middleclass' else \
                    3

    education_category = st.selectbox('parents_educational_qualification', (
        'Informal', 
        'Secondary School Cert', 
        'National Diploma', 
        'HND', 
        'Bachelors Degree', 
        'Post Graduate'
    ))

    education_category = 0 if education_category == 'Informal' else \
                        1 if education_category == 'Secondary School Cert' else \
                        2 if education_category == 'National Diploma' else \
                        3 if education_category == 'HND' else \
                        4 if education_category == 'Bachelors Degree' else \
                        5
    
    distance_category = st.selectbox('distance_btwn_home_school', (
        'less than 1km', 
        '1-3km', 
        '3-5km', 
        'Above 5km'
    ))

    distance_category = 0 if distance_category == 'less than 1km' else \
                        1 if distance_category == '1-3km' else \
                        2 if distance_category == '3-5km' else \
                        3

with col2:
    library_usage_category = st.selectbox('use_of_library_and_study_spaces', (
        'Strongly Disagree', 
        'Disagree', 
        'Neutral', 
        'Agree', 
        'Strongly Agree'
    ))

    library_usage_category = 1 if library_usage_category == 'Strongly Disagree' else \
                            2 if library_usage_category == 'Disagree' else \
                            3 if library_usage_category == 'Neutral' else \
                            4 if library_usage_category == 'Agree' else \
                            5
                                                 
    internet_usage_category = st.selectbox('use_of_internet', (
        'Never', 
        'Rarely', 
        'Sometimes', 
        'Often', 
        'Always'
    ))

    internet_usage_category = 1 if internet_usage_category == 'Never' else \
                            2 if internet_usage_category == 'Rarely' else \
                            3 if internet_usage_category == 'Sometimes' else \
                            4 if internet_usage_category == 'Often' else \
                            5
    
    stress_category = st.selectbox('stress_levels', (
        'Low', 
        'Moderate', 
        'High'
    ))

    stress_category = 0 if stress_category == 'Low' else \
                    1 if stress_category == 'Moderate' else \
                    2

    extracurricular_category = st.selectbox('extracurricular_activities', (
        'No', 
        'Yes'
    ))

    extracurricular_category = 0 if extracurricular_category == 'No' else 1

    study_satasifaction_category = st.selectbox('study_satasifaction', (
        'Very Unsatisfied', 
        'Unsatisfied', 
        'Neutral', 
        'Satisfied', 
        'Very Satisfied'
    ))

    study_satasifaction_category = 1 if study_satasifaction_category == 'Very Unsatisfied' else \
                                2 if study_satasifaction_category == 'Unsatisfied' else \
                                3 if study_satasifaction_category == 'Neutral' else \
                                4 if study_satasifaction_category == 'Satisfied' else \
                                5


# Create a DataFrame with the user inputs using original column names
input_data = pd.DataFrame({
    'Age': [age_category],
    'Gender': [gender_category],
    'average_household_income': [income_category],  # Original name
    'parents_educational_qualification': [education_category],  # Original name
    'distance_btwn_home_school': [distance_category],  # Original name
    'use_of_library_and_study_spaces': [library_usage_category],  # Original name
    'use_of_internet': [internet_usage_category],  # Original name
    'stress_levels': [stress_category],  # Use the correct variable name
    'extracurricular_activities': [extracurricular_category],  # Use the correct variable name
    'study_satasifaction': [study_satasifaction_category]  # Use the correct variable name
})

# Scale the input data
# input_data[numeric] = sc.transform(input_data[numeric])

# Make predictions
if st.button('Predict Academic Performance'):
    prediction = cla_model.predict(input_data)
    prediction_result = 'Pass' if prediction[0] == 1 else 'Fail'
    st.success(f'The predicted result for the data is: **{prediction_result}**')
    
    
st.text('')
st.text('')
st.markdown('`Code:` [GitHub](https://github.com/iamthedarksaint/dataluminaries)')