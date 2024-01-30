import streamlit as st 
import pandas as pd
import os
from getpass import getpass
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain_community.llms import HuggingFaceHub


def main():

    st.title("Hello bestie")
    st.text("Let me know what you'd like to know about the ifood dataset :)")

    uploaded_file = st.file_uploader("Upload your file here")

    if uploaded_file:
        st.header("Data Statistics")
        df = pd.read_csv(uploaded_file)
        st.write(df.describe)

        st.header("Data Header")
        st.write(df.head())

    if uploaded_file is not None:
        user_question = st.text_input("Ask a question about your CSV: ")

        llm = "HuggingFaceH4/zephyr-7b-beta"

        HUGGINGFACEHUB_API_TOKEN = getpass()
        os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

        conv_model = HuggingFaceHub(huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"], task="text-generation",
                                    repo_id=llm, model_kwargs={"temperature":0})
        uploaded_file.seek(0)
        agent = create_csv_agent(conv_model, uploaded_file, verbose=True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question) 
            st.write(response)

            

if __name__ == "__main__":
    main()
