"""Point d'entrée du quiz culture générale."""

from quiz import display_question, load_questions


def main() -> None:
    """Semaine 1 : charger les questions et afficher la première."""
    questions = load_questions()

    print("=== Quiz Culture Generale ===")
    print(f"{len(questions)} question(s) chargee(s).")

    # Semaine 1 : afficher une seule question (sans verifier la reponse pour l'instant)
    first = questions[0]
    print("\n[Semaine 1] Apercu de la premiere question :")
    display_question(first)

    # Semaine 2 : decommenter et completer pour jouer toute la partie
    # from quiz import ask_question
    # score = 0
    # for q in questions:
    #     if ask_question(q):
    #         score += 1
    # print(f"\nScore final : {score}/{len(questions)}")


if __name__ == "__main__":
    main()
