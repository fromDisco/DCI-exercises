import json
import os
os.chdir("/home/michel/Dokumente/coding/python/DCI-exercises/exercises/ex6.5")

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


def room_loop(story, room):
    print(story[room]["description"])
    story_room_actions = story[room]
    actual_path = [room]
    actual_room = room 
    remaining_time = 20
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
        pass
    

def take(pocket, item):
    pocket.append(item)
    return pocket

story = open_database("get-out-of-your-home-db.json")
room_loop(story, "sleeping-room")
