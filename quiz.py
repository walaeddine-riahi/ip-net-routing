import streamlit as st

quizzes = {
    "Chapitre 1 : Concepts de Routage": [
        {
            "question": "Quelle commande affiche la table de routage ?",
            "options": ["show interfaces", "show running-config", "show ip route"],
            "answer": "show ip route"
        },
        {
            "question": "Quels sont les types d'accès possibles à un routeur ?",
            "options": ["Ethernet, série, console", "Console, Telnet, AUX", "SSH, Telnet, FastEthernet"],
            "answer": "Console, Telnet, AUX"
        }
    ],
    "Chapitre 2 : Routage Statique": [
        {
            "question": "Quelle commande configure une route par défaut ?",
            "options": ["ip route 0.0.0.0 0.0.0.0", "ip default-gateway", "route add default"],
            "answer": "ip route 0.0.0.0 0.0.0.0"
        }
    ],
    "Chapitre 3 : Routage Dynamique": [
        {
            "question": "Quel protocole utilise l’algorithme de Bellman-Ford ?",
            "options": ["OSPF", "RIP", "EIGRP"],
            "answer": "RIP"
        }
    ],
    "Chapitre 4 : OSPF Point-à-Point": [
        {
            "question": "Quel message OSPF est utilisé pour découvrir les voisins ?",
            "options": ["LSU", "Hello", "LSAck"],
            "answer": "Hello"
        }
    ],
    "Chapitre 5 : OSPF Accès Multiple": [
        {
            "question": "Quel routeur devient DR en cas de priorité égale ?",
            "options": ["Celui avec la plus faible IP", "Celui avec l’ID le plus élevé", "Le plus ancien"],
            "answer": "Celui avec l’ID le plus élevé"
        }
    ],
    "Chapitre 6 : NAT IPv4": [
        {
            "question": "Quel type de NAT utilise la surcharge ?",
            "options": ["Statique", "Dynamique", "PAT"],
            "answer": "PAT"
        }
    ]
}


from progress import load_progress, save_progress

def run_quiz(chapter):
    progress = load_progress()

    st.subheader("📝 Quiz d'entraînement")
    score = 0
    total = len(quizzes[chapter])

    for q in quizzes[chapter]:
        st.markdown(f"**{q['question']}**")
        selected = st.radio("Choix :", q["options"], key=q["question"])
        if selected == q["answer"]:
            score += 1

    if st.button("🎯 Obtenir mon score"):

        progress[chapter] = {
            "score": score,
            "total": total
        }
        save_progress(progress)

        st.success(f"Votre score est {score} / {total}")