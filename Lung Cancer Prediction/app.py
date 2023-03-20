import pandas as pd
from sklearn.linear_model import LogisticRegression
import streamlit as st
import joblib
import requests
from streamlit_lottie import st_lottie
from PIL import Image



st.set_page_config(page_title="Lung Cancer Prediction",page_icon=":tada:",layout="wide",initial_sidebar_state="expanded")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_0l21klz3.json")
lottie_coding2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_fiwvwbxo.json")
lottie_coding3 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_4MNbe9dpAb.json")
lottie_coding4 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5l2niiiq.json")
lottie_coding5 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_psA8ir.json")
lottie_coding6 = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_itkhmozo.json")
lottie_coding7 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_6bn30rnk.json")


st.header("Lung Cancer Prediction")

option=["Home","Types","Symptoms", "Prediction"]
icons=["house","notebook","graph-up","graph-up-arrow"]

choice = st.sidebar.selectbox("Menu",option)

if choice == "Home":
    with st.container():
        left_column, right_column = st.columns((1,2))
        with left_column:
            st.subheader("What is Lung Cancer")
            st.write("     ")
            st.write("Cancer is a disease in which cells in the body grow out of control. When cancer starts in the lungs, it is called lung cancer.")
            st.write("")
        with right_column:
            st_lottie(lottie_coding , height= 300, key="Lung1")

    with st.container():
        left_column2, right_column2 = st.columns((2,1))
        with right_column2:
            
            st.write("Lung cancer begins in the lungs and may spread to lymph nodes or other organs in the body, such as the brain. Cancer from other organs also may spread to the lungs. When cancer cells spread from one organ to another, they are called metastases.")
            st.write("[Learn More >>> ](https://www.cdc.gov/cancer/lung/basic_info/what-is-lung-cancer.htm)")
        
        with left_column2:
            st_lottie(lottie_coding2 , height= 300, key="Lung2")

elif choice == "Types":
    st.subheader("Types of Lung Cancer")   
    st.write("There are two main types of lung cancer: small cell lung cancer (SCLC) and non-small cell lung cancer (NSCLC). ")
    image = Image.open('Types.jpg')
    st.image(image, caption='Types of Lung Cancer')
    with st.container():
        left_column,middle_column,right_column = st.columns((1,1,1))
        with right_column:
            st.subheader("Non-Small Cell Lung Cancer (NSCLC)")
            st.write("Non-small cell lung cancer is more common. It makes up about 80 percent of lung cancer cases. This type of cancer usually grows and spreads to other parts of the body more slowly than small cell lung cancer does.")
            st.write("  ")
            st.write(" There are three different types of non-small cell lung cancer:")
            st.write(" ")
            st.write("- Adenocarcinoma :  A form of non-small cell lung cancer often found in an outer area of the lung. It develops in the cells of epithelial tissues, which line the cavities and surfaces of the body and form glands.")
            st.write("- Squamous cell carcinoma :  A form of non-small cell lung cancer usually found in the center of the lung next to an air tube (bronchus).")
            st.write("- Large cell carcinoma :  A form of non-small cell lung cancer that can occur in any part of the lung and tends to grow and spread faster than adenocarcinoma or squamous cell carcinoma.")                   
            st.write("  ")
            st.write("[Learn More >>> ](https://www.lung.org/lung-health-diseases/lung-disease-lookup/lung-cancer/basics/lung-cancer-types)")     
        with middle_column:
            st_lottie(lottie_coding3, height= 250, key="Lung3")
            st_lottie(lottie_coding4, height= 250, key="Lung4")
            st_lottie(lottie_coding5, height= 250, key="Lung5")


        with left_column:
            st.subheader("Small Cell Lung Cancer (SCLC)")
            st.write(" ")
            st.write("There are two different types of small cell lung cancer: ")
            st.write(" ")
            st.write("-  Small cell carcinoma and mixed small cell/large cell cancer or combined small cell lung cancer.")
            st.write("-  The types of small cell lung cancer are named for the kinds of cells found in the cancer and how the cells look when viewed under a microscope. Small cell lung cancer is almost always associated with cigarette smoking.")
            st.write("  ")
            st.write("-  Small cell lung cancer is usually treated with chemotherapy.")
        
elif choice == "Symptoms":
    st.subheader("Symptoms of Lung Cancer")
    with st.container():
        left_column, right_column = st.columns((1.5,1.5))
    with left_column:
        st.write("  ")
        st.write("What Are the Symptoms of Lung Cancer ?")
        st.write("Different people have different symptoms for lung cancer. Some people have symptoms related to the lungs. Some people whose lung cancer has spread to other parts of the body (metastasized) have symptoms specific to that part of the body. Some people just have general symptoms of not feeling well. Most people with lung cancer don’t have symptoms until the cancer is advanced. ")
        st.write("  ")
        st.write("Lung cancer symptoms may include---")
        st.write("  ")
        st.write("- Coughing that gets worse or doesn’t go away. ")
        st.write("- Chest pain. ")
        st.write("- Shortness of breath.  ")
        st.write("- Wheezing.  ")
        st.write("- Coughing up blood.  ")
        st.write("- Feeling very tired all the time.  ")
        st.write("- Weight loss with no known cause.  ")
        st.write("  ")
        st.write(" Other changes that can sometimes occur with lung cancer may include repeated bouts of pneumonia and swollen or enlarged lymph nodes (glands) inside the chest in the area between the lungs. ")
        st.write("  ")
        st.write(" These symptoms can happen with other illnesses, too. If you have some of these symptoms, talk to your doctor, who can help find the cause. ")

        with right_column:
            st_lottie(lottie_coding6, height= 350, key="Lung6")
            st_lottie(lottie_coding7, height= 350, key="Lung7")


elif choice == "Prediction":
    with st.container():
        st.header(" Prediction For Lung Cancer")
        st.write("---")
        st.subheader(" ")

    df = pd.read_csv("Data.csv")

    X  = df[["GENDER","AGE","SMOKING","YELLOW FINGERS","ANXIETY","PEER PRESSURE","CHRONIC DISEASE","FATIGUE","ALLERGY","WHEEZING","ALCOHOL CONSUMPTION","COUGHING","SHORTNESS OF BREATH","SWALLOWING DIFFICULTY","CHEST PAIN"]]
    y = df["DETECTION RESULT"]

    clf = LogisticRegression()
    clf.fit(X, y)
    joblib.dump(clf, "model.pkl")

    a = st.number_input("GENDER: Enter 1 for Male and 0 for Female", min_value=0, max_value=1)
    b = st.slider("AGE: Enter your Age", min_value=1, max_value=100)
    c = st.number_input("SMOKING: Enter 1 if you smoke or 0 if you don't smoke", min_value=0, max_value=1)
    d = st.number_input("YELLOW FINGERS: Enter 1 if you have yellow fingers or 0 if you don't", min_value=0, max_value=1)
    e = st.number_input("ANXIETY: Enter 1 if you have anxiety and 0 if you don't", min_value=0, max_value=1)
    f = st.number_input("PEER PRESSURE: Enter 1 if you feel you suffer from peer pressure or 0 if you don't", min_value=0, max_value=1)
    g = st.number_input("CHRONIC DISEASE: Enter 1 if you suffer from a chronic disease or O if you don't", min_value=0, max_value=1)
    h = st.number_input("FATIGUE: Enter 1 if you have fatigue or 0 if you don't", min_value=0, max_value=1)
    i = st.number_input("ALLERGY: Enter 1 if you have some sort of allergy or 0 if you don't", min_value=0, max_value=1)
    j = st.number_input("WHEEZING: Enter 1 if you wheeze or 0 if you don't", min_value=0, max_value=1)
    k =  st.number_input("ALCOHOL CONSUMPTION: Enter 1 if you consume alcohol or 0 if you don't", min_value=0, max_value=1)
    l = st.number_input("COUGHING: Enter 1 if you cough a lot or 0 if you don't", min_value=0, max_value=1)
    m = st.number_input("SHORTNESS OF BREATH: Enter 1 if you suffer from shortness of breath or 0 if you don't", min_value=0, max_value=1)
    n =  st.number_input("SWALLOWING DIFFICULTY: Enter 1 if you have difficulty swallowing or 0 if you don't", min_value=0, max_value=1)
    o =  st.number_input("CHEST PAIN: Enter 1 if you have chest pain or 0 if you don't", min_value=0, max_value=1)

    if st.button("Submit"):
        # Unpickle classifier
        clf = joblib.load("model.pkl")
        
        # Store inputs into dataframe
        X = pd.DataFrame([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]],
                        columns = ["GENDER","AGE","SMOKING","YELLOW_FINGERS","ANXIETY","PEER_PRESSURE","CHRONIC_DISEASE","FATIGUE","ALLERGY","WHEEZING","ALCOHOL_CONSUMPTION","COUGHING","SHORTNESS_OF_BREATH","SWALLOWING_DIFFICULTY","CHEST_PAIN"])
        
        # Get Prediction 
        prediction = clf.predict(X)[0]
        
        # Output Prediction
        st.text(f"{prediction}")