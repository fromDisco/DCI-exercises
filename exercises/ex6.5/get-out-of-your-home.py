import json

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
    # print(story[room]["description"])
    story_room_actions = story[room]
    actual_room = room 
    while actual_room == room:
        print("possible actions:")
        print("\n".join(story_room_actions.keys()))
        user_choice = input("What to do next?")
        

        try:
            actions = story_room_actions[user_choice].keys()
        except:
            print("Sorry, don't know what you mean.")
        else: 
            print(story_room_actions["look-around"].isin)
            # print("\n".join(actions))

        actual_room = "sleeping-room"
        pass
    

story = open_database("get-out-of-your-home-db.json")
room_loop(story, "living-room")