
import streamlit as st
import pandas as pd
import pickle
from sklearn.datasets import load_iris
import seaborn as sns

st.set_page_config(page_title="🌸 Streamlit Multi-Page App", layout="wide")

# -------------------------------
# Sidebar Navigation
# -------------------------------
page = st.sidebar.radio("Navigate to:", ["Home", "Iris Prediction", "Contact"])

# Load Iris dataset and model
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in iris.target]

try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None

# -------------------------------
# Home Page
# -------------------------------
if page == "Home":
    st.title("🌼 Welcome to My Streamlit App")
    st.header("Main Home Page")

    st.write("""
    👋 Hi! Welcome to my Streamlit multipage app.
    Use the left sidebar to navigate between pages:
    - **Iris Prediction App** (for ML model demo)
    - **Contact Page** (to reach out)
    """)

    st.subheader("📘 Quick Demo")
    st.write("Here’s a quick overview of the Iris dataset used in the model:")
    st.dataframe(df.head())

    st.success("✅ Use the sidebar above to switch pages.")

# -------------------------------
# Iris Prediction Page
# -------------------------------
elif page == "Iris Prediction":
    st.title("🌸 Iris Flower Prediction App")
    st.write("This app predicts the Iris species using a trained Random Forest model.")

    if model is None:
        st.error("⚠️ Model not found! Make sure `model.pkl` is in the folder.")
    else:
        # Sidebar inputs for prediction
        st.sidebar.header("Input Parameters for Prediction")
        sepal_length = st.sidebar.slider('Sepal length (cm)', 4.0, 8.0, 5.8)
        sepal_width = st.sidebar.slider('Sepal width (cm)', 2.0, 4.5, 3.0)
        petal_length = st.sidebar.slider('Petal length (cm)', 1.0, 7.0, 4.3)
        petal_width = st.sidebar.slider('Petal width (cm)', 0.1, 2.5, 1.3)

        # Predict button
        if st.button("Predict"):
            input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                                      columns=iris.feature_names)
            prediction = model.predict(input_data)[0]
            pred_species = iris.target_names[prediction]
            st.success(f"🔍 The predicted species is **{pred_species.capitalize()}**")

        # Dataset preview
        st.subheader("📊 Dataset Overview")
        st.dataframe(df.head())

        # Pairplot visualization
        st.subheader("🌿 Pairplot of Features")
        st.pyplot(sns.pairplot(df, hue='species').fig)

# -------------------------------
# Contact Page
# -------------------------------
elif page == "Contact":
    st.title("📞 Contact Page")
    st.write("Fill in your details below 👇")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been sent successfully.")
        else:
            st.warning("⚠️ Please fill in all fields before submitting.")