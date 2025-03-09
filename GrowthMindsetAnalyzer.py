import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

@st.cache_data
def load_data(uploaded_file):
    """Loads CSV file with caching to prevent reloading delays."""
    return pd.read_csv(uploaded_file)

def plot_numeric_analysis(df, numeric_cols):
    selected_col = st.selectbox("Select a numerical column for analysis", numeric_cols, key="numeric")
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"], key="chart")
    
    if st.button("Generate Chart"):
        fig, ax = plt.subplots(figsize=(8, 5))
        if chart_type == "Line Chart":
            sns.lineplot(data=df, x=df.index, y=selected_col, marker='o', ax=ax)
        elif chart_type == "Bar Chart":
            sns.barplot(x=df.index[:50], y=df[selected_col].head(50), ax=ax)  
        elif chart_type == "Histogram":
            sns.histplot(df[selected_col], kde=True, bins=20, ax=ax)  
        
        plt.xlabel("Entries (Time-based)")
        plt.ylabel(selected_col)
        plt.title(f"{chart_type}: {selected_col}")
        st.pyplot(fig, clear_figure=True) 

def plot_effort_vs_outcome(df, numeric_cols):
    x_col = st.selectbox("Select Effort Column", numeric_cols, key="effort")
    y_col = st.selectbox("Select Outcome Column", numeric_cols, key="outcome")
    chart_type = st.selectbox("Select Chart Type", ["Scatter Plot", "Line Chart"], key="effort_chart")
    
    if st.button("Show Effort vs Outcome Analysis"):
        fig, ax = plt.subplots(figsize=(6, 4))
        sample_df = df.sample(min(500, len(df))) 
        
        if chart_type == "Scatter Plot":
            sns.scatterplot(data=sample_df, x=x_col, y=y_col, hue=y_col, size=y_col, sizes=(20, 200), ax=ax)
        elif chart_type == "Line Chart":
            sns.lineplot(data=sample_df, x=x_col, y=y_col, marker='o', ax=ax)
        
        plt.title("Effort vs Outcome Relationship")
        st.pyplot(fig, clear_figure=True)

def generate_wordcloud(df, text_cols):
    selected_text_col = st.selectbox("Select a text column", text_cols, key="wordcloud")
    if st.button("Generate Word Cloud"):
        text_data = " ".join(df[selected_text_col].dropna().astype(str))
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        plt.title("Most Frequent Words in Reflections")
        st.pyplot(fig, clear_figure=True)

def main():
    st.title("Growth Mindset Data Analyzer")
    st.write("Upload your progress data to visualize your learning journey and mindset growth!")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head(10)) 

        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        text_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        if numeric_cols:
            st.write("## Numeric Data Analysis")
            plot_numeric_analysis(df, numeric_cols)
        
        if len(numeric_cols) >= 2:
            st.write("## Effort vs Outcome Analysis")
            plot_effort_vs_outcome(df, numeric_cols)
        
        if text_cols:
            st.write("## Growth Mindset Word Cloud")
            generate_wordcloud(df, text_cols)
        
        st.success("Data analysis complete! Explore your insights and keep growing!")

if __name__ == "__main__":
    main()
