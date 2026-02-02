import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="Mind Reading Game", page_icon="🧠")

# ---------- Initialize Session State ----------
if "initialized" not in st.session_state:
    st.session_state.last_1 = 0
    st.session_state.last_2 = 0
    st.session_state.inputs = np.zeros((2, 2, 2), dtype=int)
    st.session_state.scores = [0, 0]  # [computer, player]
    st.session_state.game_over = False
    st.session_state.history = []
    st.session_state.initialized = True


# ---------- AI Prediction Logic ----------
def predict_easy():
    return random.randint(0, 1)


def predict_medium():
    inputs = st.session_state.inputs
    l1 = st.session_state.last_1
    l2 = st.session_state.last_2

    if inputs[l2][l1][1] == 1:
        return inputs[l2][l1][0]
    return random.randint(0, 1)


def predict_hard():
    # Pattern-based prediction
    pattern_pred = predict_medium()

    # Frequency-based prediction
    if len(st.session_state.history) >= 5:
        ones = st.session_state.history.count(1)
        zeros = st.session_state.history.count(0)
        freq_pred = 1 if ones > zeros else 0
    else:
        freq_pred = random.randint(0, 1)

    # Combine both predictions
    return pattern_pred if random.random() < 0.7 else freq_pred


def get_prediction(mode):
    if mode == "Easy":
        return predict_easy()
    elif mode == "Medium":
        return predict_medium()
    else:
        return predict_hard()


# ---------- Game Logic ----------
def update_inputs(current):
    inputs = st.session_state.inputs
    l1 = st.session_state.last_1
    l2 = st.session_state.last_2

    if inputs[l2][l1][0] == current:
        inputs[l2][l1][1] = 1
    else:
        inputs[l2][l1][1] = 0

    inputs[l2][l1][0] = current
    st.session_state.last_2 = l1
    st.session_state.last_1 = current


def update_scores(player_input, predicted):
    if player_input == predicted:
        st.session_state.scores[0] += 1
    else:
        st.session_state.scores[1] += 1


def reset_game():
    st.session_state.last_1 = 0
    st.session_state.last_2 = 0
    st.session_state.inputs = np.zeros((2, 2, 2), dtype=int)
    st.session_state.scores = [0, 0]
    st.session_state.history = []
    st.session_state.game_over = False


# ---------- UI ----------
st.title("🧠 Mind Reading Game (AI Mode)")
st.write("The computer adapts its prediction strategy based on difficulty level.")

difficulty = st.selectbox(
    "🎯 Select AI Difficulty",
    ["Easy", "Medium", "Hard (AI)"],
    disabled=st.session_state.scores != [0, 0]
)

player_choice = st.radio(
    "Your Choice:",
    [0, 1],
    horizontal=True,
    disabled=st.session_state.game_over
)

if st.button("▶️ Play Move", disabled=st.session_state.game_over):
    prediction = get_prediction(difficulty)

    st.session_state.history.append(player_choice)
    update_inputs(player_choice)
    update_scores(player_choice, prediction)

    st.info(f"🤖 AI predicted: **{prediction}**")

    if st.session_state.scores[0] == 20:
        st.error("💻 AI Wins!")
        st.session_state.game_over = True
    elif st.session_state.scores[1] == 20:
        st.success("🎉 You Won!")
        st.session_state.game_over = True


# ---------- Scoreboard ----------
st.subheader("📊 Scoreboard")
col1, col2 = st.columns(2)

with col1:
    st.metric("👤 Player", st.session_state.scores[1])

with col2:
    st.metric("🤖 AI", st.session_state.scores[0])


# ---------- Reset ----------
if st.button("🔄 Reset Game"):
    reset_game()
    st.rerun()
