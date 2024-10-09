import streamlit as st

st.set_page_config(page_title="Academic Performance Prediction Modelling Documentation", page_icon="🎓", layout="wide")

st.title("📚 Academic Performance Prediction Application Documentation")

st.header("Overview")
st.write("""
This Streamlit application predicts the academic performance of students based on various input features. 
It employs a Support Vector Machine (SVC) model trained on a dataset containing relevant information about students. 
The application allows users to input data and receive predictions on whether a student will pass or fail based on their provided characteristics.
""")

st.header("Libraries Used")
st.markdown("""
- **Streamlit**: For creating the web application interface.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For machine learning model training, preprocessing, and evaluation.
- **Pickle**: For saving and loading the trained model.
""")

st.header("Application Structure")

st.markdown("""
1. **Setup**:
    - The application is configured with a title and layout.
    - Libraries are imported, and the dataset is loaded from a CSV file.

2. **Data Preparation**:
    - A new column, `jamb_performance`, is created based on the `jamb_score` to categorize students as 'pass' or 'fail'.
    - The `no_of_siblings` and `average_days_absent` columns are categorized into 'Low', 'Medium', and 'High' using binning.
    - Unnecessary columns are dropped from the dataset.
    - Categorical features are mapped to numeric values using predefined dictionaries for easier processing by the machine learning model.
    - Missing values are filled with the mean of their respective columns.

3. **Feature Selection**:
    - A list of features was selected using the Recursive Feature Elimination method, and the data was divided into explanatory variables (X) and the target variable (y).
    - The dataset is divided into training and testing sets using a 70-30 split.

4. **Data Scaling**:
    - Numeric features are scaled using `StandardScaler` to standardize the data, improving the model's performance.

5. **Model Training**:
    - Four models were trained and evaluated based on their F1 score and accuracy metrics. The models included Logistic Regression, Support Vector Classifier, Decision Tree Classifier, and Random Forest Classifier. Each model was assessed to determine its effectiveness in predicting academic performance.
    - The SVC model was trained on the training dataset and chosen as the final model due to its superior performance in accuracy (50%) and F1 Score (57%), offering a good balance between precision and recall.
    - The trained model is saved as a pickle file for later use.

6. **User Input for Prediction**:
    - Users can input their data through a form in the Streamlit interface.
    - Input categories are selected via dropdown menus, and corresponding numeric values are assigned based on predefined mappings.

7. **Prediction and Output**:
    - Upon clicking the "Predict Academic Performance" button, the model uses the provided inputs to predict whether the student will pass or fail.
    - The prediction result is displayed on the interface.
""")

st.header("Key Features")
st.markdown("""
- **User-Friendly Interface**: The application provides a simple and interactive way for users to input data and receive predictions.
- **Data Preprocessing**: The application handles data preparation and feature mapping automatically.
- **Model Performance**: Utilizes a Support Vector Machine model for effective classification of academic performance.
""")

st.header("Usage")
st.markdown("""
1. Run the Streamlit application.
2. Input the required data using the dropdown menus provided.
3. Click on the "Predict Academic Performance" button to see the prediction result.
""")

st.header("Future Improvements")
st.markdown("""
- Collect more data based on other factors.
- Implement additional machine learning models for comparison.
- Allow users to upload their datasets for predictions on multiple entries at once.
""")
