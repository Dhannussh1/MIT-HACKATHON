import random
import time

class VocabularyGame:
    def __init__(self):
        # Different categories of questions
        self.tense_questions = [
            {
                "question": "Yesterday, I _____ (go) to the store.",
                "answer": "went",
                "options": ["go", "went", "gone", "going"],
                "explanation": "'Went' is the past tense of 'go'."
            },
            {
                "question": "By next month, she _____ (complete) her project.",
                "answer": "will have completed",
                "options": ["completes", "completed", "will complete", "will have completed"],
                "explanation": "'Will have completed' is the future perfect tense, used for actions that will be finished before a point in the future."
            },
            {
                "question": "They _____ (work) on this problem for three hours now.",
                "answer": "have been working",
                "options": ["work", "are working", "have been working", "worked"],
                "explanation": "'Have been working' is the present perfect continuous tense, used for actions that began in the past and continue up to now."
            }
        ]
        
        self.preposition_questions = [
            {
                "question": "The book is _____ the table.",
                "answer": "on",
                "options": ["in", "on", "at", "under"],
                "explanation": "'On' is used when something is positioned on the surface of something else."
            },
            {
                "question": "We arrived _____ the airport at 9pm.",
                "answer": "at",
                "options": ["to", "at", "in", "on"],
                "explanation": "'At' is used for specific points/locations like airports, stations, etc."
            },
            {
                "question": "She's been living in Paris _____ 2020.",
                "answer": "since",
                "options": ["for", "since", "during", "while"],
                "explanation": "'Since' is used with a specific point in time when something began."
            }
        ]
        
        self.phrasal_verb_questions = [
            {
                "question": "Can you _____ (look after) my cat while I'm away?",
                "answer": "look after",
                "options": ["look at", "look for", "look after", "look up"],
                "explanation": "'Look after' means to take care of someone or something."
            },
            {
                "question": "I need to _____ (fill out) this application form.",
                "answer": "fill out",
                "options": ["fill in", "fill out", "fill up", "fill with"],
                "explanation": "'Fill out' means to complete a form or document with the required information."
            },
            {
                "question": "Please _____ (turn off) the lights when you leave.",
                "answer": "turn off",
                "options": ["turn up", "turn down", "turn on", "turn off"],
                "explanation": "'Turn off' means to stop a device from working by operating its switch."
            }
        ]
        
        self.idiom_questions = [
            {
                "question": "Finding that old photo album was a real _____ down memory lane.",
                "answer": "trip",
                "options": ["walk", "journey", "trip", "drive"],
                "explanation": "'A trip down memory lane' is an idiom meaning to remember or reminisce about past experiences."
            },
            {
                "question": "Learning a new language isn't easy, but it's _____ the effort.",
                "answer": "worth",
                "options": ["value", "worth", "deserving", "meriting"],
                "explanation": "'Worth the effort' means something deserves the time and energy invested in it."
            }
        ]
        
        # Combine all question types
        self.all_questions = self.tense_questions + self.preposition_questions + self.phrasal_verb_questions + self.idiom_questions
        
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("\n" + "="*60)
        print("WELCOME TO THE VOCABULARY FILL-IN-THE-BLANKS GAME!")
        print("="*60)
        print("Test your knowledge of English tenses, prepositions, phrasal verbs, and idioms.")
        print("\nInstructions:")
        print("- Read each sentence carefully")
        print("- Choose the correct word to fill in the blank")
        print("- Learn from the explanations after each question")
        print("="*60 + "\n")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        score = 0
        questions = random.sample(self.all_questions, min(10, len(self.all_questions)))
        
        for i, question in enumerate(questions, 1):
            print(f"\nQuestion {i} of {len(questions)}:")
            print(question["question"])
            
            # Display options
            random.shuffle(question["options"])
            for j, option in enumerate(question["options"], 1):
                print(f"{j}. {option}")
            
            # Get user input
            while True:
                try:
                    choice = int(input("\nEnter your choice (1-4): "))
                    if 1 <= choice <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")
            
            user_answer = question["options"][choice-1]
            correct = user_answer == question["answer"]
            
            # Display result
            if correct:
                score += 1
                print("\n✓ Correct! Well done!")
            else:
                print(f"\n✗ Sorry, that's incorrect. The correct answer is: '{question['answer']}'")
            
            print(f"Explanation: {question['explanation']}")
            time.sleep(1)
            
        # Final score
        print("\n" + "="*60)
        print(f"GAME OVER! Your final score: {score}/{len(questions)}")
        percentage = (score / len(questions)) * 100
        
        if percentage >= 90:
            print("Excellent! You have a great command of English vocabulary!")
        elif percentage >= 70:
            print("Good job! You have a solid understanding of English vocabulary.")
        elif percentage >= 50:
            print("Not bad! Keep practicing to improve your vocabulary skills.")
        else:
            print("Keep practicing! You'll get better with time.")
        print("="*60)
        
        return self.play_again()
        
    def play_again(self):
        """Ask if the user wants to play again"""
        while True:
            choice = input("\nWould you like to play again? (yes/no): ").lower()
            if choice in ["yes", "y"]:
                return True
            elif choice in ["no", "n"]:
                print("\nThank you for playing! Goodbye!")
                return False
            else:
                print("Please enter 'yes' or 'no'.")

    def add_custom_question(self, category, question, answer, options, explanation):
        """Add a custom question to the game"""
        new_question = {
            "question": question,
            "answer": answer,
            "options": options,
            "explanation": explanation
        }
        
        if category == "tense":
            self.tense_questions.append(new_question)
        elif category == "preposition":
            self.preposition_questions.append(new_question)
        elif category == "phrasal_verb":
            self.phrasal_verb_questions.append(new_question)
        elif category == "idiom":
            self.idiom_questions.append(new_question)
            
        # Update the combined list
        self.all_questions = self.tense_questions + self.preposition_questions + self.phrasal_verb_questions + self.idiom_questions
        
        print(f"New {category} question added successfully!")

# Main program
if __name__ == "__main__":
    game = VocabularyGame()
    play_again = True
    
    while play_again:
        play_again = game.play_game()
    
    # Example of how to add custom questions:
    # game.add_custom_question(
    #     "tense", 
    #     "She _____ (study) all night for the exam.",
    #     "had been studying",
    #     ["studied", "has studied", "had been studying", "was studying"],
    #     "Past perfect continuous tense is used for actions that continued up until another point in the past."
    # )