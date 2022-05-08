import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0
name_of_player = input("Write your name: ")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    # print("Top scores: " + str(score_list))

current_time = datetime.datetime.now()
# print(current_time)

score_data = {"attempts": attempts,
              "date": str(datetime.datetime.now()),
              "name": name_of_player
              }

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1


    if guess == secret:
        score_list.append(score_data)

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
            # score_file.write("\n With kind regards...")

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")

    elif guess < secret:
        print("Your guess is not correct... try something bigger")
