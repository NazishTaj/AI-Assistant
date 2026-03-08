import streamlit as st
import pandas as pd
from ai_sql import generate_sql
from database import run_query
from visual_ai import suggest_chart
from charts import create_chart

st.title("Universal AI Data Analyst")

question = st.text_input("Ask your data")

if question:

   
    sql = generate_sql(question)

    st.write("Generated SQL:")
    st.code(sql)

  
    rows, columns = run_query(sql)

    df = pd.DataFrame(rows, columns=columns)

    st.write("Result:")

    st.dataframe(df)
    if len(df.columns) >= 2:

        chart_type = suggest_chart(question, df.columns.tolist())

        st.write("Suggested Chart:", chart_type)

        chart = create_chart(df, chart_type)

        st.pyplot(chart)