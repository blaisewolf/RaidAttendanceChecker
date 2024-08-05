from wclogsapi import get_character_list
from spreadsheetsapi import execute
import json

def main():
    #test = []
    #path = Path(input(f"Log path: "))
    #path.replace("\\", "/")
    #with open(path.as_posix().strip("\"\"")) as logfile:
    #    lines = logfile.readlines()
    #    character_ids = collect_player_ids(lines)
    #    character_names = collect_character_names(lines, character_ids)
    #    test = character_names
    #for x in test:
    #    print(x)
    character_list = get_character_list()
    with open("playersCharacters2.json", "r+", encoding="utf-8") as json_file:
        character_to_player = json.load(json_file)
        attended_player_list = [character_to_player.get(character) for character in character_list if character_to_player.get(character) is not None]
    for player in attended_player_list:
        execute(player)





if __name__ == "__main__":
    main()
