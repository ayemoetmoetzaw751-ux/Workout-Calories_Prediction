import streamlit as st
import pickle 
import pandas as pd

df=pd.read_csv("calories_data_.csv")
df.columns =df.columns.str.strip()
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
df['Height'] = df['Height'].fillna(df['Height'].median())
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')
df['Duration'] = df['Duration'].fillna(df['Duration'].median())
df['Gender']=df['Gender'].str.lower()
df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])

def load_model():
    with open('Cal_Predict.pkl','rb') as f:
        return pickle.load(f)

st.header("Predict Calories Burnt Durung Exercises")

with st.sidebar:
    st.image('parami.jpg')
    st.text("Student Name: Aye Moet Moet Zaw")
    st.text("Student ID:PIUS20230004")
    st.text("Class of 2027")
    st.text("Machine Learning_Midterm Project")

    
col1,col2=st.columns(2)
with col1:
    var1=st.selectbox("Enter your Gender",df['Gender'].unique())
    var2=st.number_input("Enter your Age", max_value=int(df['Age'].max()),min_value=int(df['Age'].min()),value=20)
    var3=st.number_input("Enter your Height in Centimeter",max_value=int(df['Height'].max()),min_value=int(df['Height'].min()),value=int(df['Height'].median()))
    var4=st.slider("Enter your weight in Kilogram",max_value=df['Weight'].max(),min_value=df['Weight'].min(),step=1.0)

with col2:
    var5=st.number_input("Enter your Workout Duration Minutes",max_value=int(df['Duration'].max()),min_value=int(df['Duration'].min()),value=int(df['Duration'].median()))
    var6=st.number_input("Enter your Average Heart Rate During Workout",max_value=int(df['Heart_Rate'].max()),min_value=int(df['Heart_Rate'].min()),value=int(df['Heart_Rate'].median()))
    var7=st.number_input("Enter your Average Body Temperature During Workout in Degress Celcius",max_value=int(df['Body_Temp'].max()),min_value=int(df['Body_Temp'].min()),value=int(df['Body_Temp'].median()))

predict_button= st.button("Predict Total Calories Burn")
if predict_button:
    input_data = pd.DataFrame(
        [
            {
                'gender': var1,
                'age': var2,
                'height': var3,
                'weight': var4,
                'duration': var5,
                'heart_rate': var6,
                'body_temp': var7
            }
        ]
    )

    model = load_model()
    result = model.predict(input_data)[0]

    st.write(f"Total Calories Burnt in your Workout Duration: {result:.2f}")


feedback = st.feedback("faces",key="faces_feedback")
if feedback:
    st.button("Submiit feedback!")

if feedback:
    st.write("Thanks for using my Prediction Web Page")
