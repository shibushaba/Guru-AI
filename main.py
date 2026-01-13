import streamlit as st
from agent import agent_execute

st.set_page_config(page_title="Guru-AI", page_icon="🦾")
st.title("Guru-AI — gambare gambare")

# -----------------------
# 🧠 SESSION STATE
# -----------------------

if "step" not in st.session_state:
    st.session_state.step = "mode"

if "mode" not in st.session_state:
    st.session_state.mode = None

if "domain" not in st.session_state:
    st.session_state.domain = None

if "topic" not in st.session_state:
    st.session_state.topic = None

if "chat" not in st.session_state:
    st.session_state.chat = []


# -----------------------
# 💬 CHAT HISTORY
# -----------------------

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


def guru_say(text):
    st.session_state.chat.append({"role": "Guru", "content": text})
    st.rerun()


# -----------------------
# 🧑‍🏫 STEP 1 — MODE
# -----------------------

if st.session_state.step == "mode":

    guru_say("Choose your style...")

    c1, c2 = st.columns(2)

    if c1.button("Fast !"):
        st.session_state.mode = "fast"
        st.session_state.chat.append({"role": "user", "content": "Fast"})
        st.session_state.step = "domain"
        st.rerun()

    if c2.button("Deep :)"):
        st.session_state.mode = "deep"
        st.session_state.chat.append({"role": "user", "content": "Deep"})
        st.session_state.step = "domain"
        st.rerun()


# -----------------------
# 🧑‍🏫 STEP 2 — DOMAIN
# -----------------------

elif st.session_state.step == "domain":

    guru_say("Which domain are we conquering?")

    d1, d2, d3, d4 = st.columns(4)

    if d1.button("Tech"):
        st.session_state.domain = "tech"

    if d2.button("Science"):
        st.session_state.domain = "science"

    if d3.button("Business"):
        st.session_state.domain = "business"

    if d4.button("General"):
        st.session_state.domain = "general"

    if st.session_state.domain:
        st.session_state.chat.append(
            {"role": "user", "content": st.session_state.domain}
        )
        st.session_state.step = "topic"
        st.rerun()


# -----------------------
# 🧑‍🏫 STEP 3 — TOPIC
# -----------------------

elif st.session_state.step == "topic":

    guru_say("What do you want to SMASH today...?")

    topic = st.chat_input(placeholder="Anything on Earth...")

    if topic:
        st.session_state.topic = topic
        st.session_state.chat.append({"role": "user", "content": topic})
        st.session_state.step = "execute"
        st.rerun()


# -----------------------
# 🤖 STEP 4 — EXECUTE
# -----------------------

elif st.session_state.step == "execute":

    with st.chat_message("Guru"):
        with st.spinner("Guru is cooking..."):

            result = agent_execute(
                st.session_state.topic,
                st.session_state.mode,
                st.session_state.domain
            )

            reply = f"""
### 🎯 Topic: {result['topic']}
**Mode:** {result['mode']}  
**Category:** {result['domain']}

{result['message']}

### 🎥 Best Video
[{result['video']['title']}]({result['video']['url']})

### 📘 Reading
[{result['reading']['title']}]({result['reading']['url']})

### 📝 Notes
"""

            st.markdown(reply)

            for n in result["notes"]:
                st.write("•", n)

            st.subheader("🛠 Practice")
            for p in result["practice"]:
                st.write("👉", p)

    # Save to chat history
    st.session_state.chat.append(
        {"role": "Guru", "content": "Lets do this! what you want SMASH next...?"}    )

    # Reset flow
    st.session_state.step = "mode"
    st.session_state.mode = None
    st.session_state.domain = None
    st.session_state.topic = None

    st.rerun()
