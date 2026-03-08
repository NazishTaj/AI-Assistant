# AI Data Analyst Assistant

An experimental AI-powered data analyst assistant that allows users to analyze data using natural language instead of writing SQL manually.

This project explores how Large Language Models (LLMs) can assist with data analysis by converting user questions into SQL queries and generating visualizations automatically.

---

# Project Overview

Data analysis usually requires writing SQL queries and manually building dashboards.  
This project attempts to simplify that process by allowing users to interact with the dataset using natural language.

The system converts user questions into SQL queries using an LLM and automatically generates charts based on the results.

Workflow:

User Question  
↓  
LLM generates SQL query  
↓  
SQL executes on the database  
↓  
Results returned as a dataframe  
↓  
System suggests the best chart type  
↓  
Visualization generated automatically

---

# Features

• Natural Language → SQL Query Generation  
• Automatic Chart Selection (Bar / Line / Pie / Scatter)  
• Interactive Data Exploration  
• Visualization using Python libraries  
• Streamlit-based dashboard interface  
• Integration of LLM APIs with SQL analytics  

---

# Example Queries

Users can ask questions like:

• Top 10 cities by revenue  
• Monthly order trend  
• Payment type distribution  
• Top product categories by sales  
• Average delivery time by month  
• Orders by state  

---

# Dataset

This project uses the **Olist E-commerce Dataset**.

The dataset contains information about:

• Customers  
• Orders  
• Products  
• Sellers  
• Payments  
• Reviews  
• Geolocation data  

This dataset is widely used for SQL and data analytics practice.

---

# Tech Stack

Programming & Data

• Python  
• SQL  
• Pandas  

Visualization

• Seaborn  
• Matplotlib  

Application Framework

• Streamlit  

AI Integration

• LLM APIs  
• Prompt Engineering  

---

# System Architecture

Natural Language Question  
↓  
LLM generates SQL query  
↓  
SQL executed on database  
↓  
Results converted to dataframe  
↓  
Chart type selected  
↓  
Visualization generated automatically

---

# Project Structure

```
AI-Assistant/
│
├── app.py              # Streamlit application interface
├── ai_sql.py           # Natural language to SQL generation
├── database.py         # Database connection and query execution
├── charts.py           # Visualization logic
├── visual_ai.py        # Chart selection using LLM
├── requirements.txt    # Project dependencies
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/NazishTaj/AI-Assistant
```

Move into the project folder

```
cd AI-Assistant
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit application

```
streamlit run app.py
```

---

# Future Improvements

Some possible improvements for this project include:

• Improving SQL generation accuracy  
• Adding query validation and correction  
• Supporting multiple datasets  
• Adding more advanced visualizations  
• Implementing smarter chart selection  
• Adding caching for faster performance  

---

# Limitations

This project is an experimental prototype.

Since the SQL queries are generated using an LLM, they may sometimes be inaccurate and require validation.

The goal of this project is to explore how LLMs can assist data exploration rather than replace traditional SQL analysis.

---

# Learning Outcomes

Through this project I explored:

• Integrating LLMs with data pipelines  
• Natural language to SQL conversion  
• Building interactive data apps using Streamlit  
• Automated data visualization  
• Prompt engineering for structured outputs  

---

# Author

MD Nazish Taj

---

# License

This project is for educational and experimental purposes.
