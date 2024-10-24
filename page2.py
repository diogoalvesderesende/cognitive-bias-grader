import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 2")
    st.write("""
    **Considering the specific requirements of Project Aurora, what are the potential benefits and drawbacks of selecting either Thaynara or João as the Lead Developer?**
    """)

    # Initialize session state for Question 2 answer and feedback if not already set
    if 'answer_q2' not in st.session_state:
        st.session_state['answer_q2'] = ""
        
    if 'feedback_q2' not in st.session_state:
        st.session_state['feedback_q2'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q2'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q2'] = answer

        # Get feedback from the AI agent and save it to session state
        feedback = get_feedback(answer, 2)
        st.session_state['feedback_q2'] = feedback

        # Display the feedback
        st.write("**AI Feedback:**")
        st.write(feedback)

    # If feedback was already generated earlier, display it again
    if st.session_state['feedback_q2']:
        st.write("**Previous AI Feedback:**")
        st.write(st.session_state['feedback_q2'])
