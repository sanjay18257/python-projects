def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]: 
            print(i)
        guess=input("Enter the answer (A/B/C/D):").upper()
        guesses.append(guess)

        correct_guesses+=check_answer(questions.get(key),guess)
        question_num+=1

    display_score(correct_guesses,guesses)
     
def check_answer(answer,guess):
    if answer==guess:
       print("Correct")
       return 1
    else :
       print("wrong")
       return 0

def  display_score(correct_guesses,guesses):
      print("--------------------------")
      print("Results:")
      print("Answer:" ,end=" ")

      for i in questions:
         print(questions.get(i),end=" ")
      print()
        
      print("Guesses:" ,end=" ")
      for i in guesses:
          print(i,end=" ")
    
      print()
      score=int((correct_guesses/len(questions))*100)
      print("--------------------------")
      print("Your Score: "+str(score)+"%")

def play_again():
    
    response =input("Do you want to play again? (YES or NO): ").upper()

    if response=="YES":
        return True
    else :
        return False

questions={
   "What is a correct syntax to output \"Hello World\" in Python?: ":"A",
   "How do you insert COMMENTS in Python code? ":"A",
   "Which one is NOT a legal variable name?: ":"B",
   "What is the correct file extension for Python files?: ":"C",
}

options=[["A. print(\"Hello World\")","B. echo \"Hello World\" ","C. p(\"Hello World\")","D. echo(\"Hello world\")"],
["A. #This is a comment","B. /*This is a comment*/","C. //This is a comment","D. <!--This is a comment-->"],
["A. my_var","B. _myvar","C. my-var","D. Myvar"],
["A. .pyth","B. .pt","C. .py","D. .pyt"]]

new_game()

while  play_again():
        new_game()

print("Bye! have a nice day!")








