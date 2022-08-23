import json
import os
# expect
os.chdir("exercises/ex6.5")


def open_database(database):
    ''' open database and return docstring

    Parameters:
    database: link to json-database

    Returns:
    dict: story
    '''

    with open(database) as file:
        story = json.loads(file.read())

    return story


def room_loop(story, room, remaining_time, left_house):

    print(story[room]["description"])
    story_room_actions = story[room]
    actual_path = [room]
    actual_room = room
    in_your_pocket = []

    while actual_room == room:
        print("possible actions:")
        # print("\n".join(story_room_actions.keys()))

        # ask user to choose action
        user_action = input("What to do next?")

        try:
            actions = story_room_actions[user_action].keys()
        except AttributeError:
            print(eval(story_room_actions[user_action]))
        except:
            print("Sorry, don't know what you mean.")
        else:
            actual_path.append(user_action)
            print("Your actual position: \n" + " -> ".join(actual_path))
            print("\n".join(actions))

        # action adds new element to path
        story_room_actions = story_room_actions[user_action]
        # actual_room = "sleeping-room"

    return story, actual_room, in_your_pocket, left_house


def room_selector(story, actual_room="living-room", in_your_pocket=[], left_house=False):
    room_loop(story, "sleeping-room", 20, left_house)


def take(pocket, item):
    '''Adds item to pocket-list

    Parameters: 
    pocket: list-item
    item: string

    Returns:
    updated pocket-list
    '''

    pocket.append(item)
    return pocket


def countdown(act_time, reduce_time):
    '''Reduces time left to finish the game

    Parameters:
    act_time: int (time left)
    reduce_time: int (time to reduce act_time)

    Returns:
    updated act_time (int)
    '''

    return act_time - reduce_time


def change_json(story_json, element):
    '''Change json, if an element was picked up

    Parameters:
    story_json: json-object (complete story)
    element: json-element to be changed

    Returns:
    updated json-object
    '''

    return story_json


story = open_database("get-out-of-your-home-db.json")
# all other arguments are optional at first. If in game, the default arguments would srew up the progress
room_selector(story)
