import streamlit as st
from agent import agent_execute

st.set_page_config(page_title="Guru-AI", page_icon="🦾")

st.markdown("## Guru-AI — Learn with Focus")

# -----------------------
# SESSION STATE
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
# CHAT HISTORY
# -----------------------

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# -----------------------
# STEP 1 — MODE
# -----------------------

if st.session_state.step == "mode":

    with st.chat_message("assistant"):
        st.markdown("Choose your learning style:")

        if st.button("Fast", key="fast_mode"):
            st.session_state.mode = "fast"
            st.session_state.chat.append({"role": "user", "content": "Fast"})
            st.session_state.step = "domain"
            st.rerun()

        if st.button("Deep", key="deep_mode"):
            st.session_state.mode = "deep"
            st.session_state.chat.append({"role": "user", "content": "Deep"})
            st.session_state.step = "domain"
            st.rerun()


# -----------------------
# STEP 2 — DOMAIN
# -----------------------

elif st.session_state.step == "domain":

    with st.chat_message("assistant"):
        st.markdown("Which domain do you want to study?")

        if st.button("Tech", key="dom_tech"):
            st.session_state.domain = "tech"

        if st.button("Science", key="dom_science"):
            st.session_state.domain = "science"

        if st.button("Business", key="dom_business"):
            st.session_state.domain = "business"

        if st.button("General", key="dom_general"):
            st.session_state.domain = "general"

    if st.session_state.domain:
        st.session_state.chat.append(
            {"role": "user", "content": st.session_state.domain.capitalize()}
        )
        st.session_state.step = "topic"
        st.rerun()


# -----------------------
# STEP 3 — TOPIC
# -----------------------

elif st.session_state.step == "topic":

    with st.chat_message("assistant"):
        st.markdown("What topic do you want to learn?")

    topic = st.chat_input("Type your topic here...")

    if topic:
        st.session_state.topic = topic
        st.session_state.chat.append({"role": "user", "content": topic})
        st.session_state.step = "execute"
        st.rerun()


# -----------------------
# STEP 4 — EXECUTE
# -----------------------

elif st.session_state.step == "execute":

    with st.chat_message("assistant"):
        with st.spinner("Preparing your learning pack..."):

            result = agent_execute(
                st.session_state.topic,
                st.session_state.mode,
                st.session_state.domain
            )

            reply = f"""
**Topic:** {result['topic']}  
**Mode:** {result['mode']}  
**Category:** {result['domain']}

{result['message']}

**Video**  
[{result['video']['title']}]({result['video']['url']})

**Reading**  
[{result['reading']['title']}]({result['reading']['url']})

**Notes**
"""
            st.markdown(reply)

            for n in result["notes"]:
                st.write("-", n)

            st.markdown("**Practice Tasks**")
            for p in result["practice"]:
                st.write("-", p)

    # Save full pack into chat
    full_pack = reply + "\n\n**Practice Tasks**\n"
    for p in result["practice"]:
        full_pack += f"- {p}\n"

    st.session_state.chat.append({"role": "assistant", "content": full_pack})
    st.session_state.chat.append({"role": "assistant", "content": "What would you like to learn next?"})

    # RESET FLOW
    st.session_state.step = "mode"
    st.session_state.mode = None
    st.session_state.domain = None
    st.session_state.topic = None

    st.rerun()
