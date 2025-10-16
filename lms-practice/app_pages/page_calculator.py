# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
    
import streamlit as st

def calculator_body():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("Enter first number", value=0)
    with col2:
        num2 = st.number_input("Enter second number", value=0)
    with col3:
        operation = st.selectbox(label="Select operation", 
                                 options=["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Click here for the maths"):
        if num2 == 0 and operation == "Divide":
            st.write("Cannot divide by zero. Try again.")
        else:
            calculator_function(num1, num2, operation)
            
def calculator_function(num1, num2, operation):
    """
    Performs a basic arithmetic operation (addition, subtraction, multiplication, or division) 
    on two numbers and displays the result using Streamlit.

    Args:
        num1 (float or int): The first number.
        num2 (float or int): The second number.
        operation (str): The operation to perform. Should be one of "Add", "Subtract", "Multiply", or "Divide".

    Returns:
        None: The function displays the result using Streamlit's st.success or st.error, and does not return a value.

    Raises:
        None: The function handles division by zero and invalid operations internally.
    """
    if operation == "Add":
        result = num1 + num2
        st.success(f"The sum of {num1} and {num2} is: **{result}**")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The difference of {num1} and {num2} is: **{result}**")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The product of {num1} and {num2} is: **{result}**")
    elif operation == "Divide":
        result = num1 / num2
        st.success(f"The quotient of {num1} and {num2} is: **{result}**")
    else:
        st.error("Invalid operation selected.")
