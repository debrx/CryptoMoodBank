import pandas as pd
import numpy as np
import random

# Function to simulate random coin rewards
def generate_random_rewards():
    return random.randint(5, 20)

# Function to log daily mood and calculate weekly/monthly stats
def mood_tracker():
    print("\nWelcome to the Mood Tracker!")
    days_in_month = 30
    moods = []  # Stores the user's mood for each day
    rewards = []  # Stores weekly coin rewards

    # Daily mood input for a month
    for day in range(1, days_in_month + 1):
        while True:
            mood = input(f"Enter your mood for Day {day} (Happy/Sad/Neutral): ").strip().lower()
            if mood in ["happy", "sad", "neutral"]:
                moods.append(mood)
                break
            else:
                print("Invalid input! Please enter 'Happy', 'Sad', or 'Neutral'.")

    # Convert moods to a DataFrame
    mood_data = pd.DataFrame({
        'Day': list(range(1, days_in_month + 1)),
        'Mood': moods
    })

    # Calculate weekly stats and assign coin rewards
    for week in range(4):
        start_day = week * 7
        end_day = start_day + 7

        weekly_moods = mood_data.iloc[start_day:end_day]
        happy_days = weekly_moods[weekly_moods['Mood'] == 'happy'].shape[0]
        sad_days = weekly_moods[weekly_moods['Mood'] == 'sad'].shape[0]
        neutral_days = weekly_moods[weekly_moods['Mood'] == 'neutral'].shape[0]

        print(f"\nStats for Week {week + 1}:")
        print(f"  Happy Days: {happy_days}")
        print(f"  Sad Days: {sad_days}")
        print(f"  Neutral Days: {neutral_days}")

        # Assign random coin reward for the week
        weekly_reward = generate_random_rewards()
        rewards.append(weekly_reward)
        print(f"  Coin Reward: {weekly_reward} coins")

    # Monthly stats
    print("\nMonthly Stats:")
    print(mood_data['Mood'].value_counts())

    total_rewards = sum(rewards)
    print(f"Total Coin Rewards for the Month: {total_rewards} coins")

# Run the mood tracker
mood_tracker()
