# Langchain chat-csv bot with HuggingFace 

This Python application allows you to load a CSV file and ask questions about its contents using natural language. The application leverages models to generate responses based on the CSV data.

## Installation 
To install the repository, follow these steps: 
1. Clone this repo to your local machine
2. Intall the necessary dependancies bu running the following command

   `pip install -r requirements.txt`
4. Additionally, you need to obtain an API key from Hugging Face and add it to the .env file.


## Usage 
To use the appication, execute the main.py file using the streamlit CLI 
  
  `python -m streamlit run main.py`

## iFood specific dataset 
The data_cleaning.py script was used to clean the dataset to remove missing values and outliers, and replace them with the mode or mean.



![image](https://github.com/geenievuong/csv_chatbot/assets/113995902/597530cf-6b97-4e5c-af33-c80272e0f2db)
![image](https://github.com/geenievuong/csv_chatbot/assets/113995902/73a1cad4-d7ef-4dca-b1b0-6ec98d6ac29e)


