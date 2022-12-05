from Question import Question # importing the question class

question_prompts = {
    "What color are apples?\n(a) Red/Green/n(b) Purple/(c) Orange/n/n",
    "What color are Bananas?/n(a) Teal/n(b) Magenta/n(c) yellow/n/n",
    "What color are strawberries?/n(a) Yellow/n(b) Red/n(c) Blue/n/n"
}

#creating an array of questions and their objective answers(a,b ,c )
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions): #creating a run test function
    score = 0
    for question in questions: #creating a for loop
        answer = input(question.prompt)
        if answer == question.answer: # using an if statement to check the correctness of the quiz
            score += 1
    print('YOu got ' + str(score) + "/" + str(len(questions)) + ' Correct') # a print statement telling how many questions the user got right
    run_test(questions)