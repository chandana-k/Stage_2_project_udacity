# empty blanks
blanks = ["___1___", "___2___", "___3___", "___4___"]

# Game level
# Easy
easy_level = '''A ___1___ is created with the def keyword. You specify the inputs
a ___1___ takes by adding ___2___ separated by commas between the parentheses.
___1___s by default return ___3___ if you don't specify the value to return.
___2___ can be standard data types such as string, number, dictionary, tuple,
and ___4___ or can be more complicated such as objects and lambda functions.'''


# Medium
medium_level = ''' Python is one of the only ___1___ known in which there exist
an ___2___ clause for For loops. It's a special type of ___3___ that executes
only if the for loop exits naturally, without any ___4___ statements. The
___4___ statement stops the execution of the innermost loop and start executing
the next line of code which in this case is the ___2___ clause.'''

# Difficult
hard_level = '''A ___1___ is created with the def keyword. You specify the inputs
a ___1___ takes by adding ___2___ separated by commas between the parentheses.
___1___s by default return ___3___ if you don't specify the value to return.
___2___ can be standard data types such as string, number, dictionary, tuple,
and ___4___ or can be more complicated such as objects and lambda functions.'''


# Game Answer
easy_level_answer = ["function", "parameters", "none", "list"]
medium_level_answer = ["languages", "else", "syntax", "break"]
hard_level_answer = ["function", "parameters", "none", "list"]

print "Welcome!"


def select_level():
    """
    Prompts the user to input the desired difficulty level
    :inputs: None
    :outputs: play_game() function call
    """
    while True:
        level = raw_input("Please select a game level: easy, medium, hard: ")
        count = 3
        level = level
        while (level not in ["easy", "medium", "hard"]) and count > 1:
            print("\n wrong or misspelled level, please try again!")
            trials = int(count) - 1
            print "You have " + str(trials) + " more trials remaining"
            level = raw_input("Select a game level: easy, medium, hard: ")
            count -= 1
            if (level not in ["easy", "medium", "hard"]) and count == 1:
                print ("\n wrong or misspelled level\n") + "You have " \
                    + str(0) + " trials remaining\n" + game_over
                sys.exit()
        else:
            if level == "easy":
                return play_game(easy_level, easy_level_answer)
            elif level == "medium":
                return play_game(medium_level, medium_level_answer)
            else:
                return play_game(hard_level, hard_level_answer)


def validate_answer(user_answer, answer, game_answer_index, empty_blank):
    """
    Validate if user's answer matches the game's answer
    :inputs: user_answer : user's answer; answer: game answer;
            game_answer_index : game answer's index
    :output: user_answer
    """
    if user_answer == answer[game_answer_index]:
        return user_answer
    else:
        count = 3
        while user_answer != answer[game_answer_index] and count > 1:
            print "\nYour entered: " + user_answer + \
                "\nWrong or misspelled answer!"
            trials = int(count) - 1
            print "You have " + str(trials) + " more trials remaining"
            user_answer = raw_input("What goes in blank " + empty_blank + "?")
            count -= 1
            if user_answer != answer[game_answer_index] and count == 1:
                print "Your entered: " + user_answer + "\nWrong or misspelled"\
                    " answer!\n" + "You have " + str(0) +  \
                    " trials remaining\n" + "You lost! \n" + game_over
                sys.exit()
        if user_answer == answer[game_answer_index]:
            return user_answer


def validate_blank(level, blanks):
    """
     Validate empty blank exist to be filled
     :return : None.
    """
    for blank in blanks:
        if blank in level:
            return blank
    return None


def play_game(level, answer):
    """
    prompt player to select a game difficulty level: easy, medium, hard
    when player guesses correctly, new prompt shows with correct answer
    in the previous blanks and a new prompt for the next blank.
    when player guesses incorrectly, they are prompted to try again
    """
    if level == easy_level:
        print "\n You chose the EASY level game. \n\n" + level
    elif level == medium_level:
        print "\n You chose the MEDIUM level game. \n\n" + level
    elif level == hard_level:
        print "\n You chose the HARD level game. \n\n" + level

    blanks_index = 0
    game_answer_index = 0
    while blanks_index < len(blanks):
        empty_blank = validate_blank(level, blanks)
        user_answer = raw_input("\nWhat goes in blank " + empty_blank + "?")
        valid_answer = validate_answer(
            user_answer, answer, game_answer_index, empty_blank)
        if valid_answer == answer[game_answer_index]:
            # print "\n Your answer is correct! \n"
            level = level.replace(empty_blank, valid_answer)
            print "\n Your answer is correct! \n\n" + level
            game_answer_index += 1
            blanks_index += 1

    print "\n Congratulations, You won the game!!! "
    sys.exit()

game_over = "Game Over!!"
print play_game(select_level())