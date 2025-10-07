quiz = [
    ("Capital of France?", ["Paris","London","Berlin","Rome"], 0),
    ("Language for web apps?", ["Python","Java","HTML","C++"], 2),
    ("Who developed Python?", ["Ritchie","Gosling","Guido","Stroustrup"], 2)
]

score, answers = 0, []
for q, opts, ans in quiz:
    print("\n"+q)
    for i,o in enumerate(opts): print(f"{i+1}. {o}")
    c = int(input("Choice: "))-1
    answers.append(c)
    score += (c==ans)
print(f"\nFinal Score: {score}/{len(quiz)}")
for i,(q,opts,ans) in enumerate(quiz):
    print(f"{q}\n Your: {opts[answers[i]]}, Correct: {opts[ans]}")
