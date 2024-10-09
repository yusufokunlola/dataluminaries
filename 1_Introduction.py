import streamlit as st
import numpy as np

st.set_page_config(page_title="Academic Performance Prediction", page_icon="🎓", layout="wide")

st.title("Academic Performance Prediction")
st.markdown("### A project submitted by Data Luminaries for the DataFestAfrica Hackathon 2024") 

def main():

    st.text('')
    st.text('')
    # Heading 1
    st.markdown("## Introduction")
    st.write("An important general concern all over the African continent has been the sub-par quality of elementary and secondary education which has been further highlighted by the recent push to Computer-Based tests for students in ultimate classes (especially SSS3). In fairness, there has been some action taken by CSOs, governments and other bodies to improve the quality of education, and by extension, students’ performance. \n \n Recent statistics from JAMB (a Nigerian pre-tertiary examination governing body) shows that 76% (approx. 4 out of 5) of students who participated in the 2024 UTME scored less than 200 (50%). This interesting insight emphasizes the need to find proactive solutions to this problem.")

    # Heading 2
    st.markdown("## Research Methododology")
    st.write("This tool is developed with the goal of predicting student academic performance. The research population are 59 students (as at the time of submitting this report) who wrote the 2024 JAMB examination in Kaduna State, Nigeria.")

    # Heading 3
    st.markdown("## Scope")
    st.write("1. Data Collection: Data was collected using questionnaire survey [Google Forms](https://docs.google.com/forms/d/e/1FAIpQLScZKh95sc8X2Iq-1azZUC-gXhFzy5Tvv58Oqy-h2j-GgRY87A/viewform) and stored on the database.")
    st.write("2. Data Warehouse: Docker and PostgreSQL was used to warehouse the data.")
    st.write("3. Analytical Model: An analysis was conducted on the cleaned data extracted from the database. This process was utilized to generate insights and develop an optimized model that predicts a student's likelihood of passing or failing their upcoming exam based on their academic history.")
    
    st.text('')
    st.text('')
    st.markdown('`Code:` [GitHub](https://github.com/iamthedarksaint/dataluminaries)')
    
if __name__ == '__main__':
    main()