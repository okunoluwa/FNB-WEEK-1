# high_score_tracker.py

while True:
    score_input = input("Enter your game score (or type 'stop' to exit): ")

    # Clean the input and check if the user wants to stop
    if score_input.strip().lower() == "stop":
        print("Game session ended!")
        break

    # Convert the score to an integer
    score = int(score_input)

    # Check the score
    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")