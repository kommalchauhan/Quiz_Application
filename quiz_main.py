from quiz_functions import slow_print, clear_screen, save_score, ask_question
from quiz_questions import questions
import time
import random

clear_screen()
slow_print("🎉 Welcome to the Ultimate Quiz Challenge! 🏆")
time.sleep(1)

player_name = input("Enter your name: ").strip().title()
slow_print(f"\nNice to meet you, {player_name}! Let's test your knowledge! 📚\n")
time.sleep(2)

slow_print("🎯 Rules:")
slow_print("✅ You get 1 chance per question.")
slow_print("✅ Type the letter of your answer (a, b, c, or d).")
slow_print("✅ Try to score as high as possible!\n")
time.sleep(2)

slow_print("💡 Choose your difficulty level:")
slow_print("1️⃣ Easy (No time pressure)")
slow_print("2️⃣ Hard (5-second timer per question)")

difficulty = input("\nEnter 1 or 2: ").strip()
hard_mode = difficulty == "2"

score = 0

random.shuffle(questions)
for q in questions:
    score = ask_question(q[0], q[1], q[2], hard_mode, score)

slow_print("\n📊 Calculating your score...", 0.1)
time.sleep(2)

save_score(player_name, score, len(questions))

if score == len(questions):
    slow_print(f"🏆 AMAZING, {player_name}! You got a perfect score: {score}/{len(questions)}! 🎉")
elif score >= len(questions) // 2:
    slow_print(f"👏 Well done, {player_name}! You scored {score}/{len(questions)}! Keep learning! 📚")
else:
    slow_print(f"😅 Better luck next time, {player_name}! You scored {score}/{len(questions)}. Keep practicing! 🚀")

slow_print("\n🌟 Thanks for playing! 🌟")
