import streamlit as st
import random

def get_random_quote():
    quotes = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Your only limit is your mind.",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Difficulties in life are intended to make us better, not bitter. - Dan Reeves"
    ]
    return random.choice(quotes)

# Streamlit App Layout
st.title("🌱 Growth Mindset Challenge")
st.write("Believe in your ability to grow! Accept challenges and improve every day.")

# Display Random Inspirational Quote
st.header("💡 Inspirational Quote of the Day")
st.success(get_random_quote())

# Daily Challenge Section
st.header("🔥 Today's Growth Challenge")
challenges = [
    "Write down 3 things you learned today.",
    "Step out of your comfort zone and try something new.",
    "Find a positive lesson in a recent failure.",
    "Help someone understand a difficult concept."
]
st.info(random.choice(challenges))

# Reflection Section
st.header("📝 Your Growth Journey")
reflection = st.text_area("What did you learn today?")
if st.button("Submit Reflection"):
    if reflection:
        st.success("Great job! Keep up the habit of self-reflection and learning.")
    else:
        st.warning("Please enter your reflection before submitting.")

# Progress Tracker (Optional - Can be enhanced with a database)
st.header("📊 Your Progress")
progress = st.slider("How much did you push yourself today?", 0, 100, 50)
st.write(f"You rated your effort at {progress}%. Keep going!")

# Footer
st.markdown("---")
st.write("**Developed with ❤️ to encourage a Growth Mindset.**")
