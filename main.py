from pathlib import Path

def collect_player_ids(file_line_content):
    character_ids = []
    for line in file_line_content:
        if "COMBATANT_INFO" in line:
            id = line.split(",")[1]
            if id not in character_ids:
                character_ids.append(id)
    return character_ids

def collect_character_names(file_line_content, character_ids):
    character_names = []
    for id in character_ids:
        for line in file_line_content:
            if "SPELL_AURA_APPLIED" in line and id in line and "Player" in line.split(",")[1]:
                name = line.split(",")[2].strip("\"\"")
                if name not in character_names:
                    character_names.append(name)
    return character_names

def main():
    test = []
    path = Path(input(f"Log path: "))
    #path.replace("\\", "/")
    with open(path.as_posix().strip("\"\"")) as logfile:
        lines = logfile.readlines()
        character_ids = collect_player_ids(lines)
        character_names = collect_character_names(lines, character_ids)
        test = character_names
    for x in test:
        print(x)

main()
