#!/usr/bin/env python3

""" or use #!/usr/bin/python3 as shebang line  """


round = 0
answer = " "
while round < 3 and answer != "Brian":
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize()
    if answer == 'Brian':
        print("Correct!")
    elif round == 3:
        print("Sorry, the correct answer was Brian")
    else:
        print("Sorry. Please try again!")


