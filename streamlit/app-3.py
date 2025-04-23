import streamlit as st
import matplotlib.pyplot as plt

st.title("Data Visualization with Matplotlib")

#Dictionary
data={
    "Python": 50,
    "Java": 30,
    "C": 20
}
# display
st.write("Courses:",data)

#update dictionary
key=st.text_input("enter new course")
value=st.text_input("Enter new course value")

if st.button("Add Course"):
    data[key]=int(value)
    st.write("Updated Courses:",data)
    
#plot a barchar

st.header("Bie Chart of course")
fig, ax = plt.subplots() # 'fig' is the figure object, 'ax' is the axes (the actual plot area)
ax.bar(data.keys(), data.values())
ax.set_xlabel("Courses")
ax.set_ylabel("Values")
ax.set_title("Bar Chart of Courses")
st.pyplot(fig)  # Displays the matplotlib figure in the Streamlit app
st.write("Bar chart of courses is displayed above.")
