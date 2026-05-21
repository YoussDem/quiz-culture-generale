"""Point d'entrée du quiz culture générale."""

from quiz import ask_question, load_questions


def main() -> None:
    """Charge les questions et lance le quiz."""
    questions = load_questions()

    print("=== Quiz Culture Générale ===")
    print(f"{len(questions)} question(s) en banque.")
    print("C'est parti !\n")

    score = 0
    total = len(questions)

    for numero, question in enumerate(questions, start=1):
        print(f"--- Question {numero}/{total} ---")
        if ask_question(question):
            score += 1

    print(f"\nScore final : {score}/{total}")


if __name__ == "__main__":
    main()
