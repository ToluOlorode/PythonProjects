questions = [
    {
        "question": "Which skill allows Sims to create video games and mobile apps?",
        "options": ["A) Cooking", "B) Programming", "C) Writing", "D) Logic", "Q) Quit"],
        "answer": "B"
    },
    {
        "question": "Which expansion pack introduced the 'City Living' theme?",
        "options": ["A) Get to Work", "B) Seasons", "C) City Living", "D) Cats & Dogs", "Q) Quit"],
        "answer": "C"
    },
    {
        "question": "What is the default lifespan of a Sim in The Sims 4?",
        "options": ["A) Short", "B) Normal", "C) Long", "D) Infinite", "Q) Quit"],
        "answer": "B"
    },
    {
        "question": "Which career path is NOT available in The Sims 4 base game?",
        "options": ["A) Astronaut", "B) Doctor", "C) Painter", "D) Secret Agent", "Q) Quit"],
        "answer": "B"
    },
    {
        "question": "What is the highest level of the 'Cooking' Skill?",
        "options": ["A) 5", "B) 7", "C) 10", "D) 15", "Q) Quit"],
        "answer": "C"
    }
    
]

print("Welcome to the Sims 4 Quiz")
print("Answer these questions and see just how much you know about Sims 4!")
print("You can quit at any time by typing 'Q'\n")

def sims_quiz(questions):
    score = 0
    
    for i in questions:
        print(i["question"])
        for option in i["options"]:
            print(option)
        answer = input("Enter the Letter of your Answer: ").upper()
        if answer == i["answer"]:
            print("That's Correct!\n")
            score += 1
        elif answer == "Q":
            print("Quiz Cancelled")
            break
        else:
            print(f"That's Incorrect! The correct answer was", i["answer"], "\n")
    
    print(f"You got {score} out of {len(questions)}.")
    
sims_quiz(questions) 
    
    
