from data import *
from linkedlist import LinkedList

print("Welcome to the Recommender, Enter in a genre of game to see the list of games")


#data for the game types listed in data.py which will be used sorted by linkedlist
def insert_game_types():
    game_type_list = LinkedList()
    for game_type in genre:
        game_type_list.insert_beginning(game_type)
    return game_type_list

def insert_game_series_data():
    series_data_list = LinkedList()
    for game_type in genre:
        series_sublist = LinkedList()  # Create a new sublist for each game type
        for series in game_data:
            if series[0] == game_type:
                series_sublist.insert_beginning(series)  # Add the series data to the sublist
        series_data_list.insert_beginning(series_sublist)  # Add the sublist to the main list
    return series_data_list


my_game_list = insert_game_types()
my_series_list = insert_game_series_data()

selected_series = ""

#interaction code goes here
while len(selected_series) == 0:
    user_input = str(input(
        "\nWhat type of game would you like to play? \nType the beginning of the game genre and press enter to see if it's here.\n")).lower()
    
    matching_types = []
    type_list_head = my_game_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()


    #displays the game type in console to finish it out
    for game in matching_types:
        print(game)

    if len(matching_types) == 1:
        selected_type = str(input("\nThe only matching type for the specified input is " + matching_types[0] +
                                ". \nDo you want to look at " + matching_types[0] + " genre? Enter y for yes and n for no\n")).lower()

        if selected_type == 'y':
            selected_series = matching_types[0]
            print("Selected Game Type: " + selected_series)
            game_list_head = my_series_list.get_head_node()
            while game_list_head is not None:
                sublist = game_list_head.get_value()
                if sublist is not None and sublist.get_head_node() and sublist.get_head_node().get_value()[0] == selected_series:
                    sublist_head = sublist.get_head_node()
                    while sublist_head is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2])
                        print("Company: " + sublist_head.get_value()[3])
                        print("Rating: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                    break  # Exit the loop after displaying the selected genre's games
                game_list_head = game_list_head.get_next_node()

        repeat_loop = str(input("\nDo you want to find another game? Enter y for yes and n for no.\n")).lower()
        if repeat_loop == 'y':
            selected_series = ""