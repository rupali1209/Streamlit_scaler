import streamlit as st

st.header("Trying the first app")
st.write("Hello world")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.header("Bravo! My first app")

st.title("First title of app")

agree = st.checkbox("I agree")
dont_agree = st.checkbox("don't agree")

if agree:
    st.write("Great!")
elif dont_agree:
    st.write("I agree to disagree")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

def sqr(x):
    return x**2

num= st.number_input("Enter a number")
if (st.button("calculate square")):
    result = sqr(num)
    st.text(result)