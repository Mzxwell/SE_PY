import openai

var = openai.api_key

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="text to table: "
           "The Brooklyn Nets (37 - 42) defeated the Washington Wizards(45 - 34) 117 - 80 on Friday"
           "in Brooklyn. The Nets seized control of this game from the very start, opening up a 31 - 14 lead after "
           "the first quarter. They also ended the contest on a very strong note, winning the fourth quarter 42 - 18. "
           "Brook Lopez once again led the way for the Nets, as he continues to play his best basketball of the "
           "season. He had 26 points (12 - 22 FG) and nine rebounds, and in his last five games is averaging 25 "
           "points and 10 rebounds in his last five games. Bojan Bogdonavic was not far behind, scoring 22 points (7 "
           "- 12 FG, 6 - 6 3Pt) in 30 minutes off the bench. Jarrett Jack (14) and Thaddeus Young (10) were the only "
           "other Brooklyn players to score in double figures, and while he did not reach double figure scoring, "
           "Deron Williams still put together a solid stat line of nine points (3 - 11 FG, 2 - 4 3Pt), nine assists "
           "and seven rebounds in 31 minutes. The win, along with a Celtics win, leaves the Nets in a tie for the "
           "final playoff spot in the Eastern Conference, but they are losing the tiebreaker to Boston. They "
           "currently hold a 2 - game lead over the Pacers for that position with just three games left to play in "
           "the regular season. The Wizards rested John Wall for the second night in a row, as they do not have much "
           "to play for as the season winds down. Bradley Beal played well in the losing effort, scoring a team - "
           "high 24 points (10 - 19 FG, 3 - 4 3Pt), while Marcin Gortat recorded a monster double - double of 21 "
           "points (9 - 11 FG) and 16 rebounds. Ramon Sessions filled in for Wall once again, but struggled shooting "
           "the ball, going 1 - for - 7 from the field for two points to go along with 10 assists and seven rebounds. "
           "Even with the loss, Washington is sitting comfortably in fifth place in the East, and since they are "
           "unable to move up or down in the standings regardless of the outcomes for these final three games in the "
           "regular season. Up next, the Nets will head to Milwaukee Sunday to take on the Bucks, while the Wizards "
           "head home Sunday and play the East-leading Hawks.\n\nTeam | Score | FG | 3Pt | Min\n\nand Player | Points | FG | 3Pt | Reb | Ast | Min",
    temperature=0.5,
    max_tokens=2000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
strs = str(response["choices"][0]["text"]).split('\n\n')
with open('file0.csv', 'w') as f0:
    f0.write(strs[0])
with open('file1.csv', 'w') as f1:
    f1.write(strs[1])
