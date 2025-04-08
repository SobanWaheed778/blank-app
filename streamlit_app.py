import streamlit as st
from collections import Counter

st.set_page_config(page_title="Text Analyzer", layout="centered")
st.title("📝 Text Analyzer App")

text = st.text_area("Enter some text below:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        most_common = Counter(words).most_common(1)[0]

        st.success("✅ Analysis Complete!")
        st.write(f"**Word Count:** {word_count}")
        st.write(f"**Character Count:** {char_count}")
        st.write(f"**Most Frequent Word:** '{most_common[0]}' ({most_common[1]} times)")
