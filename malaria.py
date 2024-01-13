<<<<<<< HEAD
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import streamlit as st
import base64
import pickle as pk
import base64
from sklearn import svm
#import seaborn as sns
import altair as alt
import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64



st.set_page_config(page_title='Mycobacterium Drug prediction',layout='centered')




# Call the function






def execute_bash_script():
    bashCommand = "bash padel.sh"

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    print("Command Output:", output)
    print("Command Error:", error)

    if process.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed with return code:", process.returncode)

# Call the function to execute the bash script

namer=[]

def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms1G -Xmx1G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')

def multi(input_data):
    load_model = pk.load(open('MalariaBioinformatics.sav', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(namer, name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

       
# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download your Predictions</a>'
    return href


st.markdown("""
# Malaria Drug discovery Prediction App (Mycobacterium)

This app allows you to predict the bioactivity towards inhibting the `Mycobacterium` enzyme. `Mycobacterium` is a drug target for Tuberculosis disease.

**Credits**
- App built in `Python` + `Streamlit` by [Group 7)
- Descriptor calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
---
""")





with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['csv'])

if uploaded_file:
    load_data = pd.read_csv(uploaded_file)
    load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False)

    st.header('**Original input data**')
    st.dataframe(load_data)

if st.sidebar.button('Predict'):
    
    with st.spinner("Calculating descriptors..."):
        desc_calc()


    # Read in calculated descriptors and display the dataframe
    st.header('**Calculated molecular descriptors**')
    desc = pd.read_csv('descriptors_output.csv')
    namer=desc["Name"]
    st.write(desc)
    st.write(desc.shape)

    # # Read descriptor list used in previously built model
    st.header('**Subset of descriptors from previously built models**')
    Xlist = list(pd.read_csv('descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # # Apply trained model to make prediction on query compounds
    desc_subset.columns = range(desc_subset.shape[1])

    multi(desc_subset)
# else:
#     st.info('Upload input data in the sidebar to start!')
    
=======
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import streamlit as st
import base64
import pickle as pk
import base64
from sklearn import svm
#import seaborn as sns
import altair as alt
import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64



st.set_page_config(page_title='Malaria Drug prediction',layout='centered')




# Call the function






def execute_bash_script():
    bashCommand = "bash padel.sh"

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    print("Command Output:", output)
    print("Command Error:", error)

    if process.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed with return code:", process.returncode)

# Call the function to execute the bash script

namer=[]

def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms1G -Xmx1G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')

def multi(input_data):
    load_model = pk.load(open('MalariaBioinformatics.sav', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(namer, name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

       
# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download your Predictions</a>'
    return href


st.markdown("""
# Malaria Drug discovery Prediction App (Plasmodium falciparum)

This app allows you to predict the bioactivity towards inhibting the `Plasmepsin 2` enzyme. `Plasmepsin 2` is a drug target for Malaria SIckness.

#**Credits**
#- App built in `Python` + `Streamlit` by [Group 7)
#- Descriptor calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
#---
#""")





with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['csv'])

if uploaded_file:
    load_data = pd.read_csv(uploaded_file)
    load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False)

    st.header('**Original input data**')
    st.dataframe(load_data)

if st.sidebar.button('Predict'):
    
    with st.spinner("Calculating descriptors..."):
        desc_calc()


    # Read in calculated descriptors and display the dataframe
    st.header('**Calculated molecular descriptors**')
    desc = pd.read_csv('descriptors_output.csv')
    namer=desc["Name"]
    st.write(desc)
    st.write(desc.shape)

    # # Read descriptor list used in previously built model
    st.header('**Subset of descriptors from previously built models**')
    Xlist = list(pd.read_csv('descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # # Apply trained model to make prediction on query compounds
    desc_subset.columns = range(desc_subset.shape[1])

    multi(desc_subset)
# else:
#     st.info('Upload input data in the sidebar to start!')
    
>>>>>>> 39a91be2cb568c6f414864d31f4ee89b263eea9e
