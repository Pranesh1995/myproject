
import streamlit as st
import pandas as pd
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

# Initialize session storage
if "students" not in st.session_state:
    st.session_state.students = []

# Grade calculation function
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Needs Improvement"


# Application heading
st.title("📊 Student Performance Analyzer")
st.write("Manage, analyze and track student academic performance.")

st.divider()

# Student entry section
st.header("➕ Add Student")

with st.form("student_form"):

    name = st.text_input("Student Name")

    col1, col2 = st.columns(2)

    with col1:
        python_marks = st.number_input(
            "Python Marks", 0, 100, 0
        )

        statistics_marks = st.number_input(
            "Statistics Marks", 0, 100, 0
        )

    with col2:
        java_marks = st.number_input(
            "Java Marks", 0, 100, 0
        )

        ml_marks = st.number_input(
            "Machine Learning Marks", 0, 100, 0
        )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if not name.strip():
            st.warning("Please enter student name.")

        else:

            total = (
                python_marks + java_marks
                + statistics_marks + ml_marks
            )

            percentage = total / 4
            average = percentage

            grade = calculate_grade(percentage)

            student = {
                "Name": name.strip(),
                "Python": python_marks,
                "Java": java_marks,
                "Statistics": statistics_marks,
                "Machine Learning": ml_marks,
                "Total": total,
                "Average": average,
                "Percentage": percentage,
                "Grade": grade
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# Display records
st.divider()
st.header("📋 Student Records")

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    # Summary metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", len(df))

    col2.metric(
        "Class Average",
        f"{df['Percentage'].mean():.2f}%"
    )

    col3.metric(
        "Highest Percentage",
        f"{df['Percentage'].max():.2f}%"
    )

    # Display table
    st.subheader("All Student Records")
    st.dataframe(df, use_container_width=True)

    # Leaderboard
    st.subheader("🏆 Student Leaderboard")

    leaderboard = df.sort_values(
        by="Percentage",
        ascending=False
    )

    st.dataframe(
        leaderboard[["Name", "Percentage", "Grade"]],
        use_container_width=True
    )

    # Performance chart
    st.subheader("📈 Student Performance Chart")

    st.bar_chart(
        leaderboard.set_index("Name")["Percentage"]
    )

    # Excel download
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Student Report"
        )

    st.download_button(
        label="📥 Download Excel Report",
        data=output.getvalue(),
        file_name="Student_Performance_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Clear records
    if st.button("Clear All Student Records"):
        st.session_state.students = []
        st.rerun()

else:

    st.info("No student records available. Add your first student!")
