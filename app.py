import streamlit as st

st.title("AI Powered Student Assistant")

st.header("Enter Assignment Information")

assignment = st.text_input("Assignment Name")
deadline = st.text_input("Deadline")
difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
hours = st.slider("Estimated Study Hours", 1, 20)

if st.button("Generate Study Plan"):

    st.subheader("Assignment Summary")
    st.write("Assignment:", assignment)
    st.write("Deadline:", deadline)
    st.write("Difficulty:", difficulty)
    st.write("Estimated Hours:", hours)

    if difficulty == "Hard" or hours > 10:
        st.error("Warning: You may be at risk of falling behind.")
    else:
        st.success("Your workload appears manageable.")

    st.subheader("Suggested Study Plan")

    if hours <= 5:
        st.write("- Study 1 hour per day")
    elif hours <= 10:
        st.write("- Study 2 hours per day")
    else:
        st.write("- Study 3+ hours per day")

    st.subheader("AI Topic Help")

    topic = st.text_input("Enter a topic you need help with")

    if topic:
        st.write(f"Explanation for {topic}:")
        st.write("This is where AI generated explanations would appear.")
