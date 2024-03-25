import pandas as pd

foot_ball = pd.read_csv("c:/Users/Gumede/Downloads/dataset - 2020-09-24.csv")

print(foot_ball.tail(7))

print(foot_ball[["Nationality", "Club"]].head())

print(foot_ball.iloc[9])

print(foot_ball.loc[100:110, ["Goals", "Appearances"]])

foot_ball["Goals per Appearance"] = foot_ball["Goals"] / foot_ball["Appearances"]
print(foot_ball.head())

arsenal_players = foot_ball[foot_ball["Club"] == "Arsenal"]
print(arsenal_players)

high_scorers = foot_ball[foot_ball["Goals"] > 5]
print(high_scorers)

#!pip install --upgrade pandas

# Assuming git is used:
# git add .
# git commit -m "Pushing changes for question 3"
# git push origin master
# Collaborator should be added through the repository settings.
