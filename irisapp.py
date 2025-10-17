
import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
from sklearn.datasets import load_iris

st.set_page_config(page_title="🌸 Iris Prediction App", layout="wide")

# -------------------------------
# Iris App
# -------------------------------
st.title("🌸 Iris Flower Prediction App")
st.write("This app uses a trained Random Forest model to predict the Iris flower species.")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

# Sidebar input fields
st.sidebar.header("Input Parameters")
sepal_length = st.sidebar.slider('Sepal length (cm)', 4.0, 8.0, 5.8)
sepal_width = st.sidebar.slider('Sepal width (cm)', 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider('Petal length (cm)', 1.0, 7.0, 4.3)
petal_width = st.sidebar.slider('Petal width (cm)', 0.1, 2.5, 1.3)

# Make prediction
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                          columns=iris.feature_names)

prediction = model.predict(input_data)[0]
pred_species = iris.target_names[prediction]

st.subheader("🔍 Prediction Result")
st.write(f"The predicted species is **{pred_species.capitalize()}**")

# Dataset preview
st.subheader("📊 Dataset Overview")
st.dataframe(df.head())

# Visualization
st.subheader("🌿 Pairplot of Features")
st.pyplot(sns.pairplot(df, hue='species').fig)