import streamlit as st
from datetime import date
import time

# Background styling
st.markdown("""
<style>
.stApp {
    background: url('https://img.freepik.com/premium-photo/cupcake-with-lighting-happy-birthday-candles-blue_23-2147779141.jpg?semt=ais_hybrid&w=740') no-repeat center center fixed;
    background-size: cover;
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

# Constants
t_date = date.today()
fake_name = "Aishwarya"
birthdate = t_date  # Assume today is their birthday

ZODIAC_SIGNS = {
    (1, 20): "Capricorn", (2, 19): "Aquarius", (3, 20): "Pisces",
    (4, 20): "Aries", (5, 21): "Taurus", (6, 21): "Gemini",
    (7, 23): "Cancer", (8, 23): "Leo", (9, 23): "Virgo",
    (10, 23): "Libra", (11, 22): "Scorpio", (12, 22): "Sagittarius",
    (12, 31): "Capricorn"
}

funny_horoscopes = {
    "Capricorn": "Today, your inner CEO is thriving—you might find yourself organizing your closet, your emails, and possibly a stranger’s shopping cart. The universe respects your hustle, even if it’s just color-coding your snack drawer. Keep climbing, majestic goat!",
    # ... (Include all other zodiac horoscopes as in your original code)
}

def get_zodiac(month, day):
    for (m, d), sign in ZODIAC_SIGNS.items():
        if (month == m and day <= d):
            return sign
    return "Capricorn"

def generate_cake(name):
    return f"""
🎉🎂🎈🎊🎁🎉   Happy Birthday, {name}!   🎉🎁🎊🎈🎂🎉

           🎂   🎂   🎂
         🎉  🍰  🎉  🍰  🎉

     May your day be filled with
     laughter, love, and cake 🍰✨

          🎁   🎈   🎊   🎈   🎁
    """

def generate_funny_horoscope(sign):
    return funny_horoscopes.get(sign, "No stars today. Try again tomorrow!")

# Streamlit config
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bot starts the conversation (once)
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("🎉 Surprise! Nithin sent a sweet birthday message just for you... 🎂🎁")
        time.sleep(2)
        st.code(generate_cake(fake_name), language="text")
        time.sleep(2)
        st.toast("🎉 Nithin is sending birthday joy! 🎉", icon="🎂")
        st.balloons()
        st.markdown("### 🎵 Click play to enjoy your birthday song from Nithin:")
        st.audio("bd.mp3", format="audio/mp3")

    sign = get_zodiac(birthdate.month, birthdate.day)
    st.write(f"🪐 Your zodiac sign is **{sign}**")

    if st.button("🔮 Reveal My Funny Horoscope!"):
        with st.spinner("Consulting the stars... 🌌"):
            result = generate_funny_horoscope(sign)
            time.sleep(2)
        st.success("Here’s your hilarious horoscope!")
        st.markdown(f"**{fake_name}**, here’s your birthday wisdom:")
        st.markdown(result)
