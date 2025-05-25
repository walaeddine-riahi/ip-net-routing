import streamlit as st
from chapters import chapters
from quiz_data import quizzes
from progress import load_progress, save_progress

st.set_page_config(page_title="IPNet Routing Trainer", layout="wide")
st.sidebar.title("📚 Menu")

# Tableau de bord
if st.sidebar.button("📊 Tableau de bord"):
    st.header("📈 Progression des chapitres")
    progress = load_progress()
    if not progress:
        st.info("Aucune tentative enregistrée.")
    else:
        for ch, res in progress.items():
            st.markdown(f"**{ch}** : {res['score']}/{len(quizzes[ch])}")

# Sélection de chapitre
chapter_names = list(chapters.keys())
selected = st.sidebar.selectbox("Sélectionnez un chapitre", chapter_names)
chapter = chapters[selected]

# --- Titre avec lampe pour flashcard chapitre ---
col1, col2 = st.columns([0.95, 0.05])
with col1:
    st.title(selected)
with col2:
    if st.button("💡", key=f"flash_chapter_{selected}"):
        st.session_state[f"show_flash_chapter_{selected}"] = not st.session_state.get(f"show_flash_chapter_{selected}", False)

# Affichage de la flashcard globale du chapitre
if st.session_state.get(f"show_flash_chapter_{selected}", False):
    flashcard_chap = chapter.get("flashcard", "Pas de flashcard disponible pour ce chapitre.")
    st.markdown(
        f"<div style='background-color:#E6F0FF; border-left: 5px solid #3399FF; padding: 15px; margin-bottom: 15px; border-radius: 8px;'>"
        f"💡 <b>Flashcard du chapitre :</b><br>{flashcard_chap}</div>",
        unsafe_allow_html=True,
    )

# Contenu principal du chapitre
st.markdown(chapter["content"], unsafe_allow_html=True)

# Initialiser l'état des flashcards questions si pas encore défini
if "flashcards_visible" not in st.session_state:
    st.session_state.flashcards_visible = {}

# Quiz
st.divider()
st.subheader("🧠 Quiz d'entraînement")
responses = {}

for i, q in enumerate(quizzes[selected]):
    cols = st.columns([0.9, 0.1])
    with cols[0]:
        st.markdown(f"**{i+1}. {q['question']}**")
        responses[i] = st.radio("", q["options"], key=f"{selected}_{i}")
    with cols[1]:
        key_flash = f"flash_{selected}_{i}"
        if st.button("💡", key=key_flash):
            current = st.session_state.flashcards_visible.get(key_flash, False)
            st.session_state.flashcards_visible[key_flash] = not current
    if st.session_state.flashcards_visible.get(key_flash, False):
        explication = q.get("flashcard", "Pas d'explication disponible.")
        st.markdown(
            f"<div style='background-color:#FFF8DC; border-left: 5px solid #FFA500; padding: 10px; margin-top:5px; border-radius:5px;'>"
            f"💡 <b>Explication :</b> {explication}</div>", unsafe_allow_html=True
        )

if st.button("✅ Soumettre mes réponses"):
    score = 0
    total_questions = len(quizzes[selected])
    for i, q in enumerate(quizzes[selected]):
        correct = q["answer"]
        user_ans = responses[i]
        if user_ans == correct:
            score += 1
        st.markdown(
            f"- **Q{i+1}** {'✅' if user_ans == correct else '❌'} : "
            f"Votre réponse : `{user_ans}` | Réponse correcte : `{correct}`"
        )
    st.success(f"🎯 Score : {score}/{total_questions}")
    progress = load_progress()
    progress[selected] = {"score": score}
    save_progress(progress)
