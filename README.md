# music_quizzes

This project is for those who want to practice on introductory and intermediate music theory.
It includes multiple choice quizzes for preparatory, first, second, and third grade.

The `main.py` contains multiple choice dictionaries for each grade and the functions for generating a quiz.
The rest of the files (`preparatory.csv`, `first_grade.csv`, `second_grade.csv`, and `third_grade.csv`) 
contain the correct answer for every question included in the dictionaries.

In summary, the code in `main.py` does the following:
- prompts the user to select a grade (preparatory, first grade, second grade or third grade),
- generates 10 multiple choice questions,
- prompts the user to answer each question one by one,
- informs the user, after each question, whether he/she answered correctly,
- prints the result at the end of the quiz, and
- asks the user if he/she wants to retake the quiz.
