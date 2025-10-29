import streamlit as st
import time

# --- Page Style ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffcccc, #ccffff);
        color: #333333;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Session State Setup ---
for key, default in {
    "loaded": False,
    "show_birthday": None,
    "show_surprise": None,
    "loading": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# --- Intro Loading Animation ---
if not st.session_state.loaded:
    st.markdown("<h1 style='text-align:center;'>🎉 Loading ...</h1>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    for percent in range(100):
        time.sleep(0.03)
        progress_bar.progress(percent + 1)
    st.session_state.loaded = True
    st.rerun()

# --- Main Content ---
st.title("🎂 🎊 🎁")
st.header("Happy Bats Appreciation Week! 🦇")
st.image(
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2twYzU0ZGRxb3FyMWg4bDkxenB5ZjFpZ3c4MzQydGxxNWl4bWhnbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10I2yiQCXk4aaI/giphy.gif",
    width=700
)

# --- Name Gate ---
name = st.text_input("Enter your name to continue 👇")

if name:
    if name.strip().lower() == "suheila":
        st.success("Welcome, Suheila! 💖")
        time.sleep(1)

        st.header("You also want to know what happens on the same week coincidentally?")
        time.sleep(1)

        # --- Second Loading ---
        with st.spinner("🤔 Thinking... let's find out!"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)
        st.success("Okay, now choose below 👇")

        # --- Buttons ---
        col1, col2 = st.columns(2)
        with col1:
            if st.button("YES!!! 😛😛", key="yes_button"):
                st.session_state.show_birthday = True
        with col2:
            if st.button("NO 😞", key="no_button"):
                st.session_state.show_birthday = False

        # --- Only react AFTER a button is pressed ---
        if st.session_state.show_birthday is True:
            loading_messages = [
                "🦇 Counting all the bats in the sky...",
                "🎂 Checking birthday calendar...",
                "🎈 Blowing up balloons...",
                "💌 Writing your surprise message...",
                "✨ Almost ready!"
            ]
            progress = st.progress(0)
            status = st.empty()

            for i, msg in enumerate(loading_messages):
                status.write(msg)
                progress.progress(int((i + 1) / len(loading_messages) * 100))
                time.sleep(1.2)

            st.subheader("Someone's Birthday happens to fall on the same week! 🤩😝")
            st.image("https://media1.giphy.com/media/KYElw07kzDspaBOwf9/giphy.gif", width=700)
            st.subheader("Happy Birthday!! 🎉")
            st.subheader("Do you want to see your surprise?")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("YES!!! 🎉", key="yes_surprise"):
                    st.session_state.show_surprise = True
            with col2:
                if st.button("NO!!! 😟", key="no_surprise"):
                    st.session_state.show_surprise = False

            # --- Surprise ---
            if st.session_state.show_surprise:
                st.success("Ta-da!!")
                st.image("sleep.jpeg", width=700)
                
                st.balloons()
                st.markdown("""
                <iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/track/5a8z2vyIDKMh5qcRG6w9wu?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                """, unsafe_allow_html=True)
                st.write("""
                Jokes aside though, Happy Birthday!  
                Najua nimekua nikitroll hii app mzima but I wanted to make something memorable.  
                Hope you like it — and that I survive your ragebait for one more year 😂😂  
                **Happy Birthday Suheila 🫶**
                """)
            elif st.session_state.show_surprise is False:
                st.subheader("Wdym no? 😟")
                st.image("https://media2.giphy.com/media/W0c3xcZ3F1d0EYYb0f/giphy.gif")

        elif st.session_state.show_birthday is False:
            # 👇 Only show this AFTER pressing a button
            st.subheader("Unasema 'no' kama hujui ni birthday yako 🙄")
            st.image("https://media2.giphy.com/media/y9QemIlaYYWdi/giphy.gif", width=700)
            st.warning("Toka hapa!")

        # --- Confetti ---
        st.markdown("""
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>setTimeout(() => { confetti(); }, 1000);</script>
        """, unsafe_allow_html=True)

    else:
        st.error("🚫 Access Denied! This app is not for you 💅")
        st.stop()





