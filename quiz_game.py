#Messi Quiz Game

questions = (" In which country was Lionel Messi born?:",
             "Which club did Messi join at a very young age?:",
             "How many Ballon d'Or awards has Lionel Messi won?:",
             "What is Messi's current club after leaving FC Barcelona?:",
             "How many UEFA Champions League titles has Messi won with FC Barcelona?:",
             "What is Lionel Messi's all-time leading goal-scoring record for FC Barcelona?:",
             "How many world-cup titles has Lionel Messi won with Argentina?:",
             "Which player has been a long-time rival of Messi throughout his career?:",
             "What is Messi's preferred playing position on the field?:",
             "What is the name of Lionel Messi's charity foundation?:",)

options = (("A. Argentina", "B. Spain", "C. Brazil", "D. Portugal"),
           ("A. Real Madrid", "B. Benfica", "C. Liverpool", "D. Barcelona"),
           ("A. 3", "B. 5", "C. 7", "D. 1"),
           ("A. PSG", "B. Real Madrid", "C. Atletico Madrid", "D. Levski Sofiq"),
           ("A. 7", "B. 6", "C. 5", "D. 4"),
           ("A. 300", "B. 250", "C. 600", "D. 400"),
           ("A. 3", "B. 5", "C. 2", "D. 1"),
           ("A. Neymar", "B. Cristiano Ronaldo", "C. Luis Suarez", "D. Jorge Masvidal"),
           ("A. CB", "B. ST", "C. LW", "D. GK"),
           ("A. Leo Messi Fundation", "B. Child-Support", "C. Help the Poor", "D. Talant Fundation"))

answers = ("A", "D", "C", "A", "D", "C", "D", "B", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("..................................")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter(A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 100
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")


    question_num += 1

print("--------------------------------------------")
print("                  RESULT                    ")
print("--------------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="|")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="|")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")