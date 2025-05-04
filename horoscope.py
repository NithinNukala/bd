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
    
    "Aquarius": "Your brain is a buzzing idea factory today. One of those ideas involves starting a podcast for pets—and honestly, it might just work. Let your weird brilliance shine and don't be afraid to wear mismatched socks; it’s part of the creative process.",
    
    "Pisces": "You’re riding a wave of dreamy vibes today. Don’t be surprised if you start a deep conversation with your houseplant or write a poem about cereal. Your imagination is a gift—just maybe avoid adopting another imaginary pet (you’re already booked).",
    
    "Aries": "Energy: high. Patience: low. Passion: maximum. You’re ready to conquer the world—or at least your laundry pile. If someone challenges you to a game of rock-paper-scissors today, go full champion mode. Victory is practically written in the stars.",
    
    "Taurus": "Comfort is your superpower today. Your couch has never looked more inviting, and snacks taste 30% better than usual. It’s okay to indulge—luxury is a mindset, and you're living your best cozy life like a soft blanket in human form.",
    
    "Gemini": "Your thoughts are bouncing around like popcorn in a microwave. You’ll start five conversations, invent three nicknames, and somehow get very passionate about penguins. Embrace the chaos—you’re charming, unpredictable, and probably late for something.",
    
    "Cancer": "Today you’re in full nurturing mode—you might bake cookies for your neighbors, give advice to a squirrel, or cry during a detergent commercial. Your heart is huge and your vibes are warm enough to toast marshmallows.",
    
    "Leo": "You’re the main character today, and the universe is your spotlight. Expect compliments, dramatic hair flips, and at least one slow-motion walk. Even your coffee cup wants your autograph. Own it—you’re fabulous and you know it.",
    
    "Virgo": "You woke up ready to fix things—typos, crooked paintings, possibly the economy. While others are winging it, you’re out here with a spreadsheet and a mission. Just don’t forget to have fun—perfection is cool, but confetti is cooler.",
    
    "Libra": "You’ll be caught in an intense decision today: pancakes or waffles? Just know that whatever you choose, your taste is flawless. You’re radiating charm, grace, and a strong desire to rearrange your furniture for “aesthetic balance.”",
    
    "Scorpio": "Today your aura is mysterious… mostly because you forgot where you put your keys. Still, your intense vibe will have people wondering if you’re a superhero in disguise. Keep them guessing—and maybe check your coat pockets again.",
    
    "Sagittarius": "Adventure is calling—but so is your bed. Today, you’ll explore bold new frontiers like trying a weird flavor of chips or watching a documentary about goats. Life is exciting when you’re curious, caffeinated, and slightly impulsive."
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
