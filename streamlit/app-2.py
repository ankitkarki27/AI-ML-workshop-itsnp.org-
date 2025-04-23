import streamlit as st

st.title("Python Data Structure")

#list
st.header("List")
st.write("A list is a collection of items in a particular order.")

names = ["John", "Jane", "Doe"]
st.write("Original List",names)

# add new items
new_name=st.text_input("Enter new name")
if st.button("Add Name"):
    if new_name:
        names.append(new_name)
        st.write("Updated List",names)
        
    else:
        st.write("Please enter a name to add to the list.")
