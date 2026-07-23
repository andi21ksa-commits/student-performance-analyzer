import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Student Performance Analyzer", page_icon="🎓", layout="wide")

st.title("🎓 Student Performance Analyzer")
st.write("Analyze student marks using Python, NumPy, Pandas and Streamlit.")


if "students" not in st.session_state:
    st.session_state.students = []


menu = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Add Student",
        "View Students",
        "Analytics",
        "Grade Report",
        "Search Student",
        "Top 3 Students"
    ]
)


if menu == "Home":

    st.header("Welcome 👋")

    st.info("This project demonstrates NumPy and Pandas operations.")

    st.write("### Features")

    st.write("✅ Add Student")
    st.write("✅ View Students")
    st.write("✅ Analytics")
    st.write("✅ Grade Report")
    st.write("✅ Search Student")
    st.write("✅ Top 3 Students")


elif menu == "Add Student":

    st.header("➕ Add Student")

    name = st.text_input("Student Name")

    marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        step=1
    )

    if st.button("Add Student"):

        st.session_state.students.append({
            "Name": name,
            "Marks": marks
        })

        st.success("Student Added Successfully!")


elif menu == "View Students":

    st.header("📋 Student List")

    if len(st.session_state.students) == 0:
        st.warning("No students added.")

    else:

        df = pd.DataFrame(st.session_state.students)

        st.dataframe(df, use_container_width=True)


elif menu == "Analytics":

    st.header("📊 Analytics")

    if len(st.session_state.students) == 0:

        st.warning("No data available.")

    else:

        df = pd.DataFrame(st.session_state.students)

        marks = df["Marks"].to_numpy()

        col1, col2, col3 = st.columns(3)

        col1.metric("Average", round(np.mean(marks),2))
        col2.metric("Highest", np.max(marks))
        col3.metric("Lowest", np.min(marks))

        st.write("### More Statistics")

        st.write("Median :", np.median(marks))
        st.write("Standard Deviation :", round(np.std(marks),2))


elif menu == "Grade Report":

    st.header("🎓 Grade Report")

    if len(st.session_state.students) == 0:

        st.warning("No data available.")

    else:

        df = pd.DataFrame(st.session_state.students)

        grades = []

        for mark in df["Marks"]:

            if mark >= 90:
                grades.append("A")

            elif mark >= 80:
                grades.append("B")

            elif mark >= 70:
                grades.append("C")

            elif mark >= 60:
                grades.append("D")

            elif mark >= 40:
                grades.append("E")

            else:
                grades.append("F")

        df["Grade"] = grades

        st.dataframe(df, use_container_width=True)


elif menu == "Search Student":

    st.header("🔍 Search Student")

    if len(st.session_state.students) == 0:

        st.warning("No data available.")

    else:

        search = st.text_input("Enter Student Name")

        if search:

            df = pd.DataFrame(st.session_state.students)

            result = df[df["Name"].str.lower() == search.lower()]

            if len(result) == 0:

                st.error("Student Not Found")

            else:

                st.success("Student Found")

                st.dataframe(result, use_container_width=True)


elif menu == "Top 3 Students":

    st.header("🏆 Top 3 Students")

    if len(st.session_state.students) == 0:

        st.warning("No data available.")

    else:

        df = pd.DataFrame(st.session_state.students)

        top = df.sort_values("Marks", ascending=False).head(3)

        st.dataframe(top, use_container_width=True)
