from Question import Question


question_prompts = [
    "Welk niveau deed ik op school?\n(a) VMBO\n(b) MAVO\n(c) HAVO/VWO\n(d) Gymnasium\n\n",
    "Hoe oud ben ik?\n(a) 14\n(b) 15\n(c) 16\n(d) 17\n(e) 18\n\n",
    "Waar woon ik?\n(a) Amsterdam\n(b) Zaanstad\n(c) Heerhugowaard\n(d) Den Helder\n(e) Maastricht\n\n"
]
print("Hello You! Ik ben Sil")
print("Wie ben jij?")
username = input("Put your name here ->")
print("Hello " + username)

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)