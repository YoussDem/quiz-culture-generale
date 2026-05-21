# Quiz Culture Generale

Quiz en ligne de commande (Python) pour reviser la culture generale.  
Projet **1/12** du defi « un projet par mois » — [YoussDem](https://github.com/YoussDem).

## Statut

| Semaine | Objectif | Etat |
|---------|----------|------|
| S1 | Charger le JSON + afficher une question | En cours |
| S2 | Boucle de partie + score | A faire |
| S3 | Sauvegarder le meilleur score | A faire |
| S4 | README final + polish GitHub | A faire |

## Installation

```bash
git clone https://github.com/YoussDem/quiz-culture-generale.git
cd quiz-culture-generale
python main.py
```

Prerequis : Python 3.10+ (aucune lib externe).

## Structure

```
quiz-culture-generale/
├── main.py           # Lance le programme
├── quiz.py           # Logique (chargement, affichage, reponses)
├── questions.json    # Banque de questions
├── scores.json       # Meilleur score (semaine 3)
└── requirements.txt
```

## Format des questions (`questions.json`)

```json
{
  "question": "Texte de la question",
  "choices": ["A", "B", "C", "D"],
  "answer": 0
}
```

`answer` est l'**index** de la bonne reponse dans `choices` (0 = premiere option).

## Ce que j'apprends (a completer chaque semaine)

- S1 : lecture de JSON avec `json`, structure de projet, fonctions Python
- S2 : ...
- S3 : ...

## Aide utilisee

- IA : structure du projet et relecture du code
- Code ecrit / valide par moi : ...

## Licence

MIT
