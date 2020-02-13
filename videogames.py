# --------------------------------------
# CSCI 127, Program 3                  |
# October 16th, 2019                   |
# Mike Gotta,                          |
# --------------------------------------
def completed_game(file_name):
    input_file = open(file_name, "r")     # opening a file
    input_file.readline()
    game = "Unknown"
    highest_count = 0
    for players in input_file:      # looping through that file
        row = players.split(",")
        completed_game = float((row[24]).split('"')[1])     # trying to find the game most people could complete
        if completed_game >= highest_count:    # the game the most people could complete should take the place of highest count
            highest_count = completed_game
            game = (row[0])

    return game

    input_file.close()




def video_game_main_story_average(file_name):
    input_file = open(file_name, "r")      # opening the file again
    input_file.readline()
    average_time = 0
    count = 0
    hours = []

    for time in input_file:
        time = time.split(",")
        average_time = float(time[31].split('"')[1])     # looping through the index of where the amount of time it takes to complete the game is held
        hours.append(average_time)
    time_sum = 0

    for math in hours:
        count += 1
        time_sum += math
    hours = time_sum / count    # trying to determine the amount of time it takes to complete a game
    print("The average time to complete a game is {:.2f}".format(hours) + " hours")

    return hours

# #  ----------------------------------------------------


def companies(file_name):
    input_file = open(file_name, "r")         # opening the file
    input_file.readline()
    user = input("Please enter a company name: ")    # asking for user input

    count = 0

    for line in input_file:
        row = line.split(",")
        company = (row[-29]).split('"')[1]            # this line in the file is where all the companies are held
        if company.lower() == user or company == user:
            count += 1                        # trying to see how many games the company made
    if count == 0:
        print("They did not make a game")
    else:
        print("They made " + str(count) + " games")

        return count



#  ----------------------------------------------------

def main(file_name):                  # running all the functions
    game = completed_game(file_name)
    print("The game that the most people could complete: " + str((game)))
    video_game_main_story_average(file_name)
    companies(file_name)

# --------------------------------------

main("video_games.csv")

