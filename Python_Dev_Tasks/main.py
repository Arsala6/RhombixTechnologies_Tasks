import streamlit as st
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="Hangman Elite", page_icon="🎨", layout="centered")

# --- CUSTOM DESIGNER CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .stApp { background: #f0f2f6; }
    
    /* Main Card styling */
    .game-card {
        background: white; padding: 30px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1); border-top: 10px solid #0D47A1;
        text-align: center; margin-bottom: 20px;
    }
    
    /* Word display styling */
    .word-display {
        font-size: 60px; font-weight: 700; letter-spacing: 12px;
        color: #0D47A1; margin: 20px 0; border-bottom: 3px dashed #FFD700;
    }
    
    /* Category tag */
    .category-tag {
        background: #FFD700; color: #0D47A1; padding: 5px 15px;
        border-radius: 50px; font-weight: bold; font-size: 14px;
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 10px; font-weight: bold; height: 3em;
        transition: 0.3s; border: 1px solid #0D47A1;
    }
    .stButton>button:hover { background: #FFD700; border-color: #0D47A1; color: #0D47A1; }
    </style>
    """, unsafe_allow_html=True)

# --- GAME DATA ---
DATA = {
    "Programming": ["PYTHON", "FLUTTER", "JAVASCRIPT", "STREAMLIT", "FIREBASE"],
    "Design": ["TYPOGRAPHY", "AESTHETIC", "GRADIENT", "MINIMALISM", "PORTFOLIO"],
    "Pakistan": ["KARACHI", "ISLAMABAD", "KHANJPUR", "MARKHOR", "HIMALAYAS"]
}

# --- STATE MANAGEMENT ---
if 'game_active' not in st.session_state:
    st.session_state.game_active = False

def start_new_game(category):
    st.session_state.word = random.choice(DATA[category]).upper()
    st.session_state.guessed = set()
    st.session_state.attempts = 6
    st.session_state.category = category
    st.session_state.game_active = True

# --- SIDEBAR (Settings) ---
with st.sidebar:
    st.title("⚙️ Game Settings")
    cat_choice = st.selectbox("Choose Category", list(DATA.keys()))
    if st.button("New Game", use_container_width=True):
        start_new_game(cat_choice)
        st.rerun()
    st.divider()
    st.info("Goal: Guess the word before the man is fully hung!")

# --- UI CONTENT ---
if not st.session_state.game_active:
    st.title("💎 Welcome to Hangman")
    st.write("Please select a category from the sidebar and click **New Game** to begin.")
else:
    # Header Area
    st.markdown(f"<span class='category-tag'>CATEGORY: {st.session_state.category}</span>", unsafe_allow_html=True)
    
    # Hangman Visual Progress (Emojis as "Images")
    stages = [
        "💀 (Game Over)", "😨 (1 Life)", "😟 (2 Lives)", 
        "😐 (3 Lives)", "🙂 (4 Lives)", "😊 (5 Lives)", "😇 (Perfect)"
    ]
    current_stage = stages[st.session_state.attempts]
    
    # Main Dashboard
    st.markdown("<div class='game-card'>", unsafe_allow_html=True)
    
    # Display the visual state
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.header(current_stage)
        st.write(f"Health: {'❤️' * st.session_state.attempts}")
    
    with col_b:
        display_word = "".join([c if c in st.session_state.guessed else "_" for c in st.session_state.word])
        st.markdown(f"<div class='word-display'>{display_word}</div>", unsafe_allow_html=True)

    # Check Game End
    if "_" not in display_word:
        st.balloons()
        st.success("✨ YOU WON! Excellent Designing Skills.")
        st.session_state.game_active = False
        if st.button("Play Again"): start_new_game(st.session_state.category)
    
    elif st.session_state.attempts <= 0:
        st.error(f"💀 Out of Lives! The word was: {st.session_state.word}")
        st.session_state.game_active = False
        if st.button("Try Again"): start_new_game(st.session_state.category)
    
    else:
        # Keyboard Grid
        st.write("### Choose a Letter")
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rows = [abc[i:i+9] for i in range(0, len(abc), 9)]
        
        for row in rows:
            cols = st.columns(len(row))
            for i, letter in enumerate(row):
                is_guessed = letter in st.session_state.guessed
                if cols[i].button(letter, key=letter, disabled=is_guessed, use_container_width=True):
                    st.session_state.guessed.add(letter)
                    if letter not in st.session_state.word:
                        st.session_state.attempts -= 1
                    st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Footer progress bar (Dynamic Color)
    p_color = "green" if st.session_state.attempts > 3 else "orange" if st.session_state.attempts > 1 else "red"
    st.markdown(f"<p style='text-align:center; color:{p_color};'><b>Survival Chances</b></p>", unsafe_allow_html=True)
    st.progress(st.session_state.attempts / 6)