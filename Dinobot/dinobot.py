import streamlit as st
import google.generativeai as genai
import base64

def get_image_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# === CONFIG ===
GOOGLE_API_KEY = "AIzaSyCaFkxX3LtZcQ20nEC8wqdT27IS8Gx67Ww"  # Replace this!
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# === PAGE SETTINGS ===
st.set_page_config(page_title="DinoBot Chat 🦖", page_icon="🦖")

# === STYLES ===
st.markdown("""
    <style>
    .stApp {
        background-color: #f6fff8;
        font-family: 'Segoe UI', sans-serif;
    }
    .dino-msg {
        background-color: #e0f7ef;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 1px 1px 4px #c2f0d0;
    }
    .avatar {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# === BIG DINO HEADER (Works for Local Images) ===
st.image("dino.png", width=250)  # Adjust width as needed
st.markdown("## DinoBot")
st.write("Friendly, helpful, and efficient – your dino assistant is here!")

# === SESSION INIT ===
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

# === GEMINI RESPONSE (Semi-Casual) ===
def get_gemini_response(prompt):
    tone_prompt = (
        f"You are DinoBot 🦖 — a helpful assistant with a cheeky, semi-casual tone. "
        f"Respond to: '{prompt}' in a clear, supportive, and professional-friendly way."
    )
    response = model.generate_content(tone_prompt)
    return response.text.strip()


# === MAIN CHAT ===
def main():
    st.title("🦖 DinoBot – Here to Rawwwrrr!")

    initialize_session_state()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f"<div class='dino-msg'>{message['content']}</div>", unsafe_allow_html=True)

    if prompt := st.chat_input("Type your message here..."):
        with st.chat_message("user"):
            st.markdown(f"<div class='dino-msg'>{prompt}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_gemini_response(prompt)
        with st.chat_message("assistant"):
            st.markdown(f"<div class='dino-msg'>{response}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
