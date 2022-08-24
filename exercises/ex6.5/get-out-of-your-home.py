import json
import os
import colorama
import art
# expecting that working directory is ony 3 folders above file
os.chdir("exercises/ex6.5")


def open_database(database):
    ''' 
    open database and return docstring

        Parameters:
            database (string): link to json-database

        Returns:
            story (dict)
    '''
    with open(database) as file:
        story = json.loads(file.read())

    return story


def room_loop(story, room, remaining_time, in_your_pocket, left_house):
    '''
    Navigates throught the actual room

        Parameters:
            story (dict): json-object with story
            room (string): name of actual room
            remaining_time (int): time remaining
            in_your_pocket (list): collected items
            left-house (bool): changed to true, once user leaves house

        Returns:
            story: json-object, can be updated in room, if user picks up elements
            actual_position: string, when user changes room, loop is exited
                         new value is passed to room_selector()
            remaining_time (int): updated time remaining
            in_your_pocket: list (updated?) of picked up objects 
            left_house: bool, can only be set to True in hallway (room)
    '''
    # stepping into a new room, display description
    print(story[room]["description"])
    # actual list of possible actions
    story_room_objects = story[room]
    # save the taken path, moving back is possible
    actual_path = [room]
    # the position of the user
    actual_position = room
    # list items, that were picked up
    in_your_pocket = []
    # input of user, look-around
    user_action = "look-around"

    while actual_position == room:
        # TODO: only one print at the end of the loop. collect data in variables. use format-string
        # TODO: .items()
        try:
            actions = story_room_objects[user_action].keys()
        except AttributeError:
            # if user chooses to change room end this loop and return to room_selector()
            if user_action == "leave-room":
                actual_position = story_room_objects["leave-room"]
                return story, actual_position, remaining_time, in_your_pocket, left_house
            print(eval(story_room_objects[user_action]))
        except KeyError:  # doesn't work. Why?
            print("Na")
        except:
            print("Sorry, don't know what you mean.")
        else:
            story_room_objects = story_room_objects[user_action]
            actual_path.append(user_action)
            print("Your actual position: \n" + " -> ".join(actual_path))

        print("possible actions:")
        print("\n".join(actions))

        # ask user to choose action
        user_action = input("What to do next? ")
        # action adds new element to path
        # story_room_objects = story_room_actions[user_action]


def start_game():
    '''
    Initialize the game: 
        Get json-database. 
        Print the inital story of the game.
        Run room_seletor() for the first time
    '''
    story = open_database("get-out-of-your-home-db.json")
    print(story["story"])
    # all other arguments are optional at first.
    # If in game, the default arguments would srew up the progress
    room_selector(story)


def room_selector(story, actual_position="sleeping-room", remaining_time=20,
                  in_your_pocket=[], left_house=False):
    '''
    Changes the room, if user chooses so.
    Restarts room_loop 
    '''
    while left_house == False:
        story, actual_position, remaining_time, in_your_pocket, left_house = room_loop(
            story, actual_position, remaining_time, in_your_pocket, left_house)


def take(pocket, item):
    '''
    Adds item to pocket-list

        Parameters: 
            pocket: list-item
            item: string

        Returns:
            updated pocket-list
    '''
    pocket.append(item)
    return pocket


def countdown(act_time, reduce_time):
    '''
    Reduces time left to finish the game

        Parameters:
            act_time: int (time left)
            reduce_time: int (time to reduce act_time)

        Returns:
            updated act_time (int)
    '''
    return act_time - reduce_time


def change_json(story_json, element):
    '''
    Change json, if an element was picked up

        Parameters:
            story_json: json-object (complete story)
            element: json-element to be changed

        Returns:
            updated json-object
    '''
    return story_json


def clearscreen():
    '''check the OS and clear the terminal screen'''
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


start_game()
