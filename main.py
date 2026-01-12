import streamlit as st
from youtube_finder import get_best_video
from docs_finder import get_docs_page
from notes_generator import generate_notes

st.set_page_config(page_title="Guru-AI", page_icon="🦾")

st.title("Guru-AI , gambare gambare")
st.caption("in my theory you need to day+=1% ")

topic = st.text_input("Pick the Topic to SMASH!!", placeholder="anything in the world...")
mode = st.selectbox("Mode", ["fast", "deep"])

if st.button("Let Guru Cookk :)"):

    if not topic:
        st.warning("Enter a topic first.")
    else:
        with st.spinner("study smarter not harder..."):

            video = get_best_video(topic, mode)
            docs = get_docs_page(topic)
            notes = generate_notes(docs) if docs else []

        st.success("Let's SMASH!!")

        st.subheader("Video")
        if video:
            st.markdown(f"**{video['title']}**")
            st.video(video["url"])
        else:
            st.write("Could not find video.")

        st.subheader("Documentation")
        if docs:
            st.markdown(docs)
        else:
            st.write("Docs not found.")

        st.subheader("Notes")
        if notes:
            for i, n in enumerate(notes, 1):
                st.write(f"{i}. {n}")
        else:
            st.write("No notes available.")
