import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

def create_chart(data, chart_type):

    df = pd.DataFrame(data)

    x = df.iloc[:,0]
    y = df.iloc[:,1]

    plt.figure(figsize=(10,6))

    if chart_type == "bar":
        sns.barplot(x=x, y=y)

    elif chart_type == "line":
        sns.lineplot(x=x, y=y)

    elif chart_type == "pie":
        plt.pie(y, labels=x, autopct='%1.1f%%')

    elif chart_type == "scatter":
        sns.scatterplot(x=x, y=y)

    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt