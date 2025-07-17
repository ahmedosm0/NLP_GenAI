# 🔮 Customer Churn Prediction App

A **Streamlit** application that predicts the probability of a customer leaving a bank using a pre-trained **TensorFlow deep learning model**. Powered by historical customer behavior, the model analyzes demographics and account features to forecast churn risk.

---

## 🚀 Features

- 📊 Takes customer details like geography, gender, age, credit score, and more
- 🤖 Predicts **churn probability** using a trained neural network model
- 📈 Displays a user-friendly **churn likelihood** output
- ⚙️ Uses **label encoding**, **one-hot encoding**, and **scaling** for input transformation
- 🧠 Model trained with **TensorFlow** and saved as `.h5`

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## 📸 Demo

![App Screenshot](./app.png)

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- TensorFlow (tested with v2.11+)
- Pre-trained model file (`model.h5`)
- Serialized encoders:
  - `label_encoder_gender.pkl`
  - `onehot_encoder.pkl`
  - `scaler.pkl`

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
streamlit run app.py
