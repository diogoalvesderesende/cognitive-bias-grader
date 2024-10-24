import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 3")
    st.write("""
    **What steps can Patricia take to ensure a fair and unbiased decision-making process in selecting the Lead Developer for Project Aurora?**
    """)

    # Initialize session state for Question 3 answer and feedback if not already set
    if 'answer_q3' not in st.session_state:
        st.session_state['answer_q3'] = ""
        
    if 'feedback_q3' not in st.session_state:
        st.session_state['feedback_q3'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q3'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q3'] = answer

        # Get feedback from the AI agent and save it to session state
        feedback = get_feedback(answer, 3)
        st.session_state['feedback_q3'] = feedback

        # Display the feedback
        st.write("**AI Feedback:**")
        st.write(feedback)

    # If feedback was already generated earlier, display it again
    if st.session_state['feedback_q3']:
        st.write("**Previous AI Feedback:**")
        st.write(st.session_state['feedback_q3'])
