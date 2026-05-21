# quiz culture générale

petit quiz en python pour réviser un peu (culture générale, pas que de l'info).  
c'est mon premier projet du défi "un projet par mois" que je fais pour avoir un portfolio plus tard.

compte github : [YoussDem](https://github.com/YoussDem)

## comment lancer

le plus simple sur windows : double-clic sur `lancer-quiz.bat`

sinon en terminal :

```
cd quiz-culture-generale
py main.py
```

(faut python installé, j'utilise la 3.13 chez moi)

## fichiers

- `main.py` → démarre le programme
- `quiz.py` → les fonctions du quiz
- `questions.json` → les questions (c'est là que j'en rajoute)
- `scores.json` → pour garder les scores plus tard (pas encore utilisé)
- `lancer-quiz.bat` → pour lancer sans galérer avec le terminal qui se ferme

## où j'en suis

pour l'instant ça affiche une question avec les 4 réponses. la semaine prochaine je veux faire le truc où on répond à tout le quiz et on a un score à la fin.

## questions.json

chaque question ressemble à ça :

```json
{
  "question": "exemple ?",
  "choices": ["a", "b", "c", "d"],
  "answer": 0
}
```

`answer` c'est le numéro de la bonne réponse dans la liste mais en partant de 0 (donc 0 = la première).

## notes perso

- j'ai appris à charger un fichier json et à séparer le code en plusieurs fichiers
- aide ia pour la structure du projet au début, après je modifie moi-même
