import streamlit as st
from langchain_ollama import OllamaLLM

# -------------------------------
# AI MODEL
# -------------------------------
llm = OllamaLLM(model="llama3.2")

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="AI Career Guidance Chatbot",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🎓 AI Career Guidance Chatbot")

st.write(
    "Get personalized career guidance based on your education, "
    "skills, interests and career goals."
)

st.divider()

# -------------------------------
# STUDENT INFORMATION
# -------------------------------
st.header("👩‍🎓 Student Information")

education = st.text_input(
    "Education",
    placeholder="Example: B.Tech 2nd Year ECE"
)

skills = st.text_input(
    "Your Skills",
    placeholder="Example: Python, C, HTML, Communication"
)

interests = st.text_input(
    "Your Interests",
    placeholder="Example: AI, Electronics, Web Development"
)

goal = st.text_input(
    "Career Goal",
    placeholder="Example: Software Engineer"
)

# -------------------------------
# CAREER RECOMMENDATION
# -------------------------------
if st.button("🚀 Get Career Guidance"):

    if not education or not skills or not interests or not goal:
        st.warning("Please fill in all the fields.")

    else:

        prompt = f"""
You are an AI Career Guidance Assistant.

Analyze the following student information:

Education: {education}

Skills: {skills}

Interests: {interests}

Career Goal: {goal}

Give simple and practical career guidance.

Provide the answer in this format:

1. Recommended Career Paths
- Give 3 suitable career paths.

2. Best Career Choice
- Select the most suitable career and explain why.

3. Required Skills
- List the important technical and soft skills.

4. Learning Roadmap
- Give a step-by-step roadmap for the student.

5. Recommended Projects
- Suggest 3 beginner-friendly projects.

6. Job Roles
- Mention suitable job roles.

7. Final Advice
- Give short motivational advice.

Use simple English suitable for a college student.
"""

        with st.spinner("🤖 AI is analyzing your profile..."):

            try:
                response = llm.invoke(prompt)

                st.success("Career guidance generated successfully!")

                st.subheader("🎯 Your Career Guidance")

                st.write(response)

            except Exception as e:

                st.error(
                    "Unable to connect to Ollama. "
                    "Please make sure Ollama is running."
                )

# -------------------------------
# CHATBOT
# -------------------------------
st.divider()

st.header("💬 Ask the Career Chatbot")

question = st.text_input(
    "Ask a career-related question",
    placeholder="Example: What should I learn to become an AI Engineer?"
)

if st.button("💡 Ask AI"):

    if not question:
        st.warning("Please enter a question.")

    else:

        chat_prompt = f"""
You are a friendly AI Career Guidance Chatbot.

Answer the student's question clearly and simply.

Student question:
{question}

Give:
- Direct answer
- Skills to learn if relevant
- Practical steps
- Suitable resources or project ideas if useful

Do not use complicated language.
"""

        with st.spinner("🤖 Thinking..."):

            try:
                answer = llm.invoke(chat_prompt)

                st.subheader("🤖 AI Response")

                st.write(answer)

            except Exception:

                st.error(
                    "Ollama is not running. Please start Ollama "
                    "and try again."
                )

# -------------------------------
# FOOTER
# -------------------------------
st.divider()

st.caption("AI Career Guidance Chatbot | Python + Streamlit + Ollama")