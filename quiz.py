"""Logique du quiz culture générale."""

import json
from pathlib import Path


def load_questions(path: str = "questions.json") -> list[dict]:
    """Charge les questions depuis un fichier JSON."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    with file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data:
        raise ValueError("Le fichier questions.json doit contenir une liste non vide.")

    return data


def display_question(question: dict) -> None:
    """Affiche une question et ses choix numérotés."""
    print()
    print(question["question"])
    print("-" * len(question["question"]))

    for index, choice in enumerate(question["choices"]):
        print(f"  {index + 1}. {choice}")


def ask_question(question: dict) -> bool:
    """
    Pose une question et retourne True si la réponse est correcte.

    Semaine 2 : tu utiliseras cette fonction dans une boucle de partie.
    """
    display_question(question)

    while True:
        raw = input("\nTa réponse (numéro 1-4) : ").strip()

        if not raw.isdigit():
            print("Entre un numéro entre 1 et 4.")
            continue

        choice = int(raw) - 1
        if choice < 0 or choice >= len(question["choices"]):
            print("Choix invalide. Réessaie.")
            continue

        correct_index = question["answer"]
        is_correct = choice == correct_index

        if is_correct:
            print("Bonne réponse !")
        else:
            correct_text = question["choices"][correct_index]
            print(f"Mauvaise réponse. La bonne réponse était : {correct_text}")

        return is_correct
