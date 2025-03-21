import streamlit as st
import pandas as pd
import openpyxl
import os
from io import BytesIO

# set up our apps

st.set_page_config(page_title="💾 Data Sweeper", layout="wide")
st.title("💾 Data Sweeper")
st.write("Transform Your files between CSV and Excel formats with built-in data"
" cleaning and visualization")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv","xlsx"],
accept_multiple_files= True)

if uploaded_files:
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[-1].lower()

        if file_extension == ".csv":
            data_frame = pd.read_csv(file)
        elif file_extension == ".xlsx":
            data_frame = pd.read_excel(file, engine="openpyxl")
        else:
            st.error(f"Unsupported file type: {file_extension  }")
            continue

        # Display info about the file
        st.write(f"**File Name:**{file.name}")
        st.write(f"**File Size:**{file.size/1024}")

        # Show five rows of our data frames
        st.write("Preview the Head of the Dataframe")
        st.dataframe(data_frame.head())

        # Option for data cleaning
        st.subheader ("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1,col2 = st.columns(2)

            with col1:
                if st.button(f"RemoveDuplicates from {file.name}"):
                    data_frame.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed..!!")

            with col2:
                if st.button(f"Fill Mising values for {file.name}"):
                    numeric_cols = data_frame.select_dtypes(include=['number']).columns
                    data_frame[numeric_cols] = data_frame[numeric_cols].fillna(data_frame[numeric_cols].mean())
                    st.write("Missing Values have been Filled.!")

        
        # choose specefic Colounms to keep or Convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose Coloumns for{file.name}", data_frame.columns, default=data_frame.columns)
        data_frame =data_frame[columns]

        # Creat Visualisations
        st.subheader("📊 Data Visualisation")
        if st.checkbox(f"Show Visualisation for {file.name}"):
            numeric_df = data_frame.select_dtypes(include='number')
    
            if numeric_df.shape[1] < 2:
                st.warning("Not enough numeric columns for visualization.")
            else:
                st.bar_chart(numeric_df.iloc[:, :2])
        


        # Convert the file -> CSV to Excel
        st.subheader("🔁 Conversion Options")
        conversion_types = st.radio(f"Convert {file.name} to:",["CSV","Excel"],key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_types == "CSV":
                data_frame.to_csv(buffer,index=False)
                file_name = file.name.replace(file_extension,".csv")
                mime_type = "txt/csv"

            elif conversion_types =="Excel":
                data_frame.to_excel(buffer,index=False)
                file_name = file.name.replace(file_extension,".xlsx")
                mime_type = "application/vnd.openxmlformats-0fficedocument.spresdsheetml.sheet"
            buffer.seek(0)


            # Download Button
            st.download_button(
                label = f"⬇ Download {file.name} as {conversion_types}",
                data = buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("🎉 All files processed")