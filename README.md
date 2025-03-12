# xGradio-based CSV Question Answering and Visualization Application

This project aims to create an application based on Gradio, wherein users can upload
a CSV file, query it about its contents, including numerical questions, and get
responses produced by a local Large Language Model (LLM). The app should also accommodate
graph plotting, with all the visualizations presented in the Gradio interface.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.


```bash
pip install -r requirements.txt
```
Requirement files Incudes: gradio, pandas, matplotlib, ollama, pydantic-ai.



## Running the App

```bash
python app.py


```
## Project Structure

#### Description of Key Files:  
- **`app.py`** – Main file to run the Gradio application.  
- **`file_handler.py`** – Manages CSV file parsing and error handling.  
- **`llm_integration.py`** – Connects to the Ollama 3.0-based local LLM for processing queries.  
- **`query_processor.py`** – Handles logic for extracting relevant insights from data.  
- **`visualization.py`** – Generates appropriate charts/graphs based on queries.  
- **`test_file_handler.py`** – Unit test file for ensuring the file handler works correctly.  

This modular structure ensures clean code organization, making it easier to maintain and expand. 

## Landing Page Layout Overview

![Graph Example](/docs/cardekho_1.png)


The landing page of the CSV Question Answering and Visualization Application is divided into two main sections:

🔹 Left Section (User Input Panel)

1. CSV Upload: Users can upload a CSV file (size < 25MB) through a drag-and-drop interface or by clicking to browse files.

2. Query Input: A text box allows users to enter questions related to the uploaded dataset.

3. Graph Inputs: Two fields for selecting X-axis and Y-axis attributes for graph generation.

4. Generate Button: A button labeled "Generate Response" triggers the AI-based analysis and visualization.

🔹 Right Section (AI Output Panel)

1. AI-Generated Response: Displays the AI-generated answer based on the user's query and uploaded CSV data.
2. Graph Output: A dedicated space for displaying the generated graph within the application interface.

This structured layout ensures a user-friendly experience, keeping inputs on the left and outputs on the right for clarity and ease of use. 

## Upload CSV File
On clicking Upload file here a file manager is open, now you can upload CSV from your local computer.
![Graph Example](/docs/cardekho_2.png)



## Example Usage
![Graph Example](/docs/cardekho_3.png)
#### 1️⃣ Enter Your Query  
- In the **"Ask a Question"** section, type your query.  
- Example:
What is the maximum and minimum price of the house?



#### 2️⃣ Set Graph Inputs  
- Choose the columns for visualization:  
- **X-Axis:** `area`  
- **Y-Axis:** `price`  

#### 3️⃣ Generate Response  
- Click the **"Generate Response"** button to get:  
- A **textual answer** to your query.  
- A **graph** plotting **house area vs. price** based on the dataset.

## Output Page Overview  

Once the **"Generate Response"** button is clicked, the application provides:  
![Graph Example](/docs/cardekho_4.png)
#### 1️⃣ AI-Generated Text Response  
- The AI extracts and displays relevant insights from the dataset.  
- Based on the provided context, the **maximum price of a house is 
13,300,000** and **the minimum price of a house is 6,300,000.**



#### 2️⃣ Graph Visualization  
- A **scatter plot** (or another relevant graph) is generated based on the selected columns.  
- Example: A **price vs. area** graph shows how house prices vary with area.  
- The graph helps visualize trends and relationships in the dataset.  

This structured output provides both **numerical insights and graphical representations** to help users interpret data effectively. 

## Combined Preview
Both Input and Output pages simultaneously.
![Graph Example](/docs/cardekho_5.png)


## Conclusion  

This project implements an Ollama 3.0 with Pydantic AI integration to enable effortless interaction with tabular data using features like intelligent query processing and an interactive UI that uses dynamic graph generation which simplifies data probing for users with no advanced technical skills. This project builds a smart and interactive Gradio-based CSV question-answering and Visualization Application.

Future work might support more visualization types, optimize LLM response time, and improve the efficiency of parsing the CSV for complicated datasets. This project is open for contributions and comments for further improvements. 

For further questions and suggestions, don’t hesitate to contact me or open a Pull request!
