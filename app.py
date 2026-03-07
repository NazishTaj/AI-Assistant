<<<<<<< HEAD
import streamlit as st
import pandas as pd
from ai_sql import generate_sql
from database import run_query

st.title("Universal AI Data Analyst")

question = st.text_input("Ask your data")

if question:

    # AI se SQL generate karo
    sql = generate_sql(question)

    st.write("Generated SQL:")
    st.code(sql)

    # SQL run karo
    rows, columns = run_query(sql)

    df = pd.DataFrame(rows, columns=columns)

    st.write("Result:")
=======
import streamlit as st
import pandas as pd
from ai_sql import generate_sql
from database import run_query

st.title("Universal AI Data Analyst")

question = st.text_input("Ask your data")

if question:

    # AI se SQL generate karo
    sql = generate_sql(question)

    st.write("Generated SQL:")
    st.code(sql)

    # SQL run karo
    rows, columns = run_query(sql)

    df = pd.DataFrame(rows, columns=columns)

    st.write("Result:")
>>>>>>> 7e05642f3959b3c581d2fd2943756d244a019264
    st.dataframe(df)