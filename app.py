import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

status_mapping = {
    0: "Graduate",
    1: "Enrolled",
    2: "Dropout"
}

model = joblib.load('model/model_knn.joblib') 

st.title("Prediksi Status Mahasiswa - Jaya Jaya Institute")

marital_status = st.selectbox("Status Pernikahan", ["single", "married", "divorced", "widower", "legally separated", "facto union"])
course = st.selectbox("Jurusan", [
    "Nursing", "Management", "Social Service", "Advertising and Marketing", 
    "Informatics Engineering", "Veterinary Nursing", "Tourism", "Oral Hygiene",
    "Basic Education", "Animation and Multimedia", "Agronomy", "Biofuel Production Techno.",
    "Communication Design", "Journalism and Communication", "Equinculture",
    "Social Service (evening)", "Management (evening)"
])
debtor = st.radio("Apakah Mahasiswa Memiliki Utang?", ["No", "Yes"])
scholarship_holder = st.radio("Apakah Memiliki Beasiswa?", ["No", "Yes"])
age = st.slider("Usia Saat Masuk", 15, 70, 20)
attendance = st.selectbox("Jadwal Kuliah", ["daytime", "evening"])

data_input = pd.DataFrame([{
    'Marital_status': marital_status,
    'Course': course,
    'Debtor': 1 if debtor == "Yes" else 0,
    'Scholarship_holder': 1 if scholarship_holder == "Yes" else 0,
    'Age_at_enrollment': age,
    'Daytime_evening_attendance': attendance
}])

label_encoder = LabelEncoder()
categorical_features = ['Marital_status', 'Course', 'Daytime_evening_attendance']
data_input[categorical_features] = data_input[categorical_features].apply(lambda x: label_encoder.fit_transform(x))

scaler = MinMaxScaler()
data_input[['Age_at_enrollment']] = scaler.fit_transform(data_input[['Age_at_enrollment']])


if st.button("Prediksi Status"):
    prediction = model.predict(data_input)[0]
    predicted_status = status_mapping.get(prediction, "Unknown")
    st.success(f"Status Prediksi Mahasiswa: **{predicted_status}**")
