quiz_data = {}

def master():
    while True:
        print("\nMENU\n1: Add Questions  2: View Questions  3: Delete Questions  4: Exit")
        operation = input("Select operation: ")

        if operation == '1':
            question_id = input("Enter question ID: ")
            if question_id in quiz_data:
                print("ID exists, try again.")
                continue
            question = input("Question: ")
            option_A = input("Option A: ")
            option_B = input("Option B: ")
            correct_answer = input("Correct answer (A/B): ").upper()

            if correct_answer not in ['A', 'B']:
                print("Invalid answer.")
                continue

            quiz_data[question_id] = {'question': question, 'options': {'A': option_A, 'B': option_B}, 'correct_answer': correct_answer}
            print("Question added!")

        elif operation == '2':
            if not quiz_data:
                print("No questions.")
            else:
                for question_id, data in quiz_data.items():
                    print(f"ID: {question_id}  {data['question']}")
                    for opt, txt in data['options'].items():
                        print(f"{opt}: {txt}")
                    print(f"Correct: {data['correct_answer']}")
                    print()

        elif operation == '3':
            question_id_to_delete = input("Enter question ID to delete: ")
            if question_id_to_delete in quiz_data:
                confirm = input(f"Delete {question_id_to_delete}? (Y/N): ").upper()
                if confirm == 'Y':
                    del quiz_data[question_id_to_delete]
                    print(f"Question {question_id_to_delete} deleted.")
                else:
                    print("Deletion canceled.")
            else:
                print("ID not found.")

        elif operation == '4':
            break
        else:
            print("Invalid option.")

def cracker():
    print("Welcome to Cracker Mode!")
    if not quiz_data:
        print("No questions to answer.")
        return

    score = 0
    for question_id, data in quiz_data.items():
        print(f"\n{data['question']}")
        for opt, txt in data['options'].items():
            print(f"{opt}: {txt}")
        answer = input("Your answer (A/B): ").upper()
        if answer == data['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {data['correct_answer']}")

    print(f"Your score: {score}/{len(quiz_data)}")

print("1: Master  2: Cracker  3: Exit")
while True:
    choice = input("Enter choice: ")
    if choice == '1':
        master()
    elif choice == '2':
        cracker()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
