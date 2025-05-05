
import streamlit as st
import joblib
import pandas as pd  

# Load the trained model and scaler
model = joblib.load('DiabeticsModel.pkl')
scaler = joblib.load("Scaler.pkl")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            color: #333333;
           
        }
        [data-testid="stMain"]{
            # background-color: white;
            background-image:url('https://www.shutterstock.com/image-photo/diabetes-concept-blood-sugar-meter-600nw-2464647841.jpg');
            background-size: cover;
            # background-blend-mode: overlay;
            background-color: rgba(1, 1, 1,0.002); /* Adjust transparency */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        [data-testid="stHeadingWithActionElements"] {
            color:white;
            text-align: center;
            background-color:black;
        }
        .stButton>button {
            background-color: red;
            color: white;
            font-size: 18px;
            border-radius: 5px;
            padding: 8px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Main App Layout
st.title('Diabetes Prediction App for Female')
st.markdown("""
    <style>
        .custom-text {
            font-size: 20px; /* Adjust text size */
            font-weight: bold; /* Make text bold */
            color: black; /* Set font color */
            font-family: 'Times New Roman', serif; /* Set font style */
            text-align: center; /* Center align text */
            background-color:rgba(209, 233, 234, 0.96);
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<p class="custom-text">This web app helps predict the likelihood of diabetes in females based on key health parameters. Enter your details, and our model will analyze the data to provide an assessment. Take a step towards better health with this simple and efficient tool!</p>', unsafe_allow_html=True)


# st.markdown("### Enter Your Details Below:")

# Using columns for better layout

col1, col2 = st.columns(2)

with col1:
    pregrency = st.number_input('Specify the Number of Pregnancies.',value=None,placeholder=" ")
    BloodPressure = st.number_input('Indicate your Diastolic Blood Pressure (mm Hg)',value=None,placeholder=" ")
    Insulin = st.number_input('Report your Serum Insulin Level (mu U/ml)',value=None,placeholder=" ")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Score',value=None,placeholder=" ")

with col2:
    Glucose = st.number_input('Provide your Plasma Glucose Level (mg/dL)',value=None,placeholder=" ")
    SkinThickness = st.number_input('Enter the Triceps Skin Fold Thickness (mm)',value=None,placeholder=" ")
    BMI = st.number_input('Provide your Body Mass Index (BMI',value=None,placeholder=" ")
    age = st.number_input('Enter your Age',value=None,placeholder=" ")


# Apply CSS styling using st.markdown
# Custom CSS for styling input boxes
st.markdown("""
    <style>
        div[data-testid="stNumberInput"] > label {
            font-size: 18px;
            font-weight: bold;
            color:rgb(23, 22, 22); /* White text */
        }

        div[data-testid="stNumberInput"] input {
            background:rgb(189, 227, 253); /* Dark background */
            padding: 8px;
            border-radius: 6px;
            box-shadow: 5px 8px 8px rgba(181, 163, 159, 0.9); /* Glow effect */
            color:rgb(10, 10, 10);
        }

        div[data-testid="stNumberInput"] {
            background:rgb(230, 230, 230); /* Dark background */
            padding: 8px;
            border-radius: 6px;
    </style>
""", unsafe_allow_html=True)

  


# Prepare input data
data = pd.DataFrame([{
    'Pregnancies': pregrency,
    'Glucose': Glucose,
    'BloodPressure': BloodPressure,
    'SkinThickness': SkinThickness,
    'Insulin': Insulin,
    'BMI': BMI,
    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
    'Age': age
}])

# Scale the input
scaled_data = scaler.transform(data)

# Prediction
# if st.button('Predict'):
#     prediction = model.predict(scaled_data)
#     if prediction == 1:
#         st.warning('⚠️ Likely to have Diabetes')
#     else:
#         st.success('✅ Not Likely to have Diabetes')
if st.button('Predict'):
    prediction = model.predict(scaled_data)
    if prediction == 1:
        st.markdown("""
            <div style="background-color:#fff3cd; padding:10px; border-radius:5px">
                <p style="color:red; font-weight:bold; font-size:18px;">⚠️ Likely to have Diabetes</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background-color:#d4edda; padding:10px; border-radius:5px">
                <p style="color:green; font-weight:bold; font-size:18px;">✅ Not Likely to have Diabetes</p>
            </div>
        """, unsafe_allow_html=True)

