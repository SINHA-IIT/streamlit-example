!pip install streamlit
import streamlit as st

def find_largest_number(n1, n2, n3):
    """
    Find the largest number among three values
    """
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

# Set the title of the app
st.title("Find the largest number among three values")

# Create input fields for the three numbers
number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")
number3 = st.number_input("Enter the third number")

# Find the largest number
largest_number = find_largest_number(number1, number2, number3)

# Display the largest number to the user
st.write("The largest number is:", largest_number)
