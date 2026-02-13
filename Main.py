import streamlit as st
from openai import OpenAI
from elevenlabs import generate

# --- CONFIGURATION ---
# ⚠️ Dhayan dein: Nayi key use karein agar purani block ho gayi ho
OPENAI_KEY = "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"
ELEVENLABS_KEY = "1e37b5a3eaa843eca05f3d2b82a7cafa"

st.title("Edith AI 👓")

client = OpenAI(api_key=OPENAI_KEY)
user_input = st.text_input("Hello Sir, I am Edith. Command me:")

if st.button("Activate Edith ⚡"):
    if user_input:
        try:
            # Brain (OpenAI)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are Edith, a loyal Indian assistant. Speak in Hinglish. Call the user Sir."},
                          {"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content
            st.success(f"Edith: {reply}")

            # Voice (ElevenLabs)
            audio = generate(api_key=ELEVENLABS_KEY, text=reply, voice="Mimi", model="eleven_multilingual_v2")
            st.audio(audio, format='audio/mp3')
        except Exception as e:
            st.error(f"Error: {e}")
                            
