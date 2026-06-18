import streamlit as st


st.title("Welcome to streamlit")

if st.checkbox("Show/Hide"):
   
  # display the text if the checkbox returns True value
  st.text("Showing the widget")


status = st.radio("Select Gender: ", ('Male', 'Female'))
 
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")


# Create a button, that when clicked, shows a text
if(st.button("Click me")):
    st.text("button click")


def sqr(num):
	
	return num*num


num = st.number_input('Insert a number')
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button("Calculate Square")):
    result = sqr(num)
    st.text(result)


