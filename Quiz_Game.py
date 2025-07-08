que_ans_dict = {
    "Q1: What is the output of print(2 ** 3)?": "8",
    "Q2: Which of these is a mutable data type in Python?": "list",
    "Q3: What is the output of 'Hello' + 'World'?": "HelloWorld",
    "Q4: What keyword is used to define a function in Python?": "def",
    "Q5: What is the correct file extension for Python files?": ".py",
    "Q6: What will len('Python') return?": "6",
    "Q7: What is the output of print(bool(""))?": "False",
    "Q8: Which one is not a valid Python keyword?": "then",
    "Q9: Which method is used to remove items from a list?": "pop()",
    "Q10: What does str() function do?": "Converts value to string"
}

options = {
    "Q1": {"a": "6", "b": "8", "c": "9", "d": "5"},
    "Q2": {"a": "tuple", "b": "list", "c": "str", "d": "int"},
    "Q3": {"a": "Hello World", "b": "HelloWorld", "c": "Hello+World", "d": "Error"},
    "Q4": {"a": "function", "b": "fun", "c": "define", "d": "def"},
    "Q5": {"a": ".pt", "b": ".python", "c": ".py", "d": ".pyt"},
    "Q6": {"a": "5", "b": "6", "c": "7", "d": "Error"},
    "Q7": {"a": "True", "b": "False", "c": "None", "d": "0"},
    "Q8": {"a": "int", "b": "str", "c": "then", "d": "bool"},
    "Q9": {"a": "remove()", "b": "pop()", "c": "delete()", "d": "clear()"},
    "Q10": {"a": "Converts to int", "b": "Converts to float", "c": "Converts value to string", "d": "Converts to boolean"}
}

def quiz_game(main_dict, option_dict):
    print("\nWelcome to Quiz Game\n")
    i = 0
    re_check = {}
    score = []
    error_message = "\nInvalid Input\nTry Again\n"
    while i < len(main_dict):
        for ques in main_dict:
            print(f"{ques}")
            for option in option_dict[f"Q{i+1}"].keys():
                print(f"{option}) {option_dict[f"Q{i+1}"][option]}")
            while True:
                opt_inp = input("\nEnter your answer : ").lower().strip()
                if opt_inp and opt_inp.isalpha() and opt_inp in "abcd":
                    if option_dict[f"Q{i+1}"][opt_inp] == main_dict[list(main_dict.keys())[i]]:
                        score.append(1)
                        if f"Q{i+1}" not in re_check:
                            re_check[f"Q{i+1}"] = {}
                            re_check[f"Q{i+1}"][f"{opt_inp}"] = list(main_dict.values())[i]
                        i += 1
                        break
                    else:
                        score.append(0)
                        if f"Q{i+1}" not in re_check:
                            re_check[f"Q{i+1}"] = {}
                            re_check[f"Q{i+1}"][f"{opt_inp}"] = list(main_dict.values())[i]
                        i += 1
                        break
                else:
                    print(error_message)

    print("\nYour Result\n")

    j = 0
    while j < len(score):
        for qno in re_check:
            for my_ans in re_check[qno]:
                print(f"{qno}) Your Answer : {option_dict[f'Q{j+1}'][my_ans]} - Correct Answer : {re_check[qno][my_ans]} - Marks : {score[j]}")
            j += 1

    score_obt = sum(score)
    percentage = (score_obt / 10) * 100

    if percentage > 60:
        print(f"\nExcellent Job!!!\nYour Total Marks : {sum(score)}\nAnd Total percentage you got is {(sum(score)/10)*100}\n----x----")
    else:
        print(f"\nNice Try\nYour Total Marks : {sum(score)}\nAnd Total percentage you got is {(sum(score)/10)*100}\n----x----")

quiz_game(que_ans_dict, options)
