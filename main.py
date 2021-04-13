import streamlit as st
from aitextgen import aitextgen


st.title("AI TextGen App(Bala)")
# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model
ai = aitextgen()

#prompt_text = "Machine Learning is awesome"
prompt_text = st.text_input(label="Enter input text", value="Machine learning is Beautiful")

@st.cache()
def spinner():
    with st.spinner("AI is on force........."):
        gpt_text = ai.generate_one(prompt=prompt_text, max_length=200)
    return gpt_text

# #st.balloons()
st.success("Machine Learning Generated the text")
st.text(spinner())
