import json

# Mapping von Hidden Power Codes zu Typen
hidden_power_map = {
    "2": "Rock",
    "3": "Electric",
    "4": "Dragon",
    "5": "Water",
    "6": "Bug",
    "7": "Dark",
    "8": "Ghost",
    "9": "Fighting",
    "10": "",  # Leerer Wert, keine Typenzuordnung
    "11": "Grass",
    "12": "Ice",
    "13": "Ground",
    "14": "Steel",
    "15": "Poison",
    "16": "Flying",
    "17": "Fire"
}

# Öffnen der JSON-Datei
with open('calc.json', encoding="utf8") as calc:
    # JSON-Daten als Dictionary laden
    data = json.load(calc)

# Liste der Trainer-IDs im Spiel
number_of_ingame_trainers = [9,325,232,654,470,190,28,404,264,270,732,24,35,719,90,11,746,656,204,804,244,720,728,754,72,107,271,469,591,408,401,108,596,731,704,89,597,416,596,724,321,704,16,579,268,244,108,472,589,731,617,419,514,601,470,804,724,320,269,572,109,28,712,538,397,545,190,604,621,227,621,37,512,94,343,584,525,534,6,261,204,601,524,525,533,534,726,128,73,201,108,19,8,729,705,763,189,266,621,191,635,603,573,78,247,143,720,501,746,19,472,586,712,729,10,615,747,616,262,404,94,201,268,597,522,531,233,588,628,728,254,699,194,212,767,803,204,804,591,23,596,116,579,729,705,107,553,193,589,287,90,245,145,17,5,545,632,571,744,19,212,654,343,804,44,27,718,74,26,128,404,11,71,743,3,760,728,729,16,89,114,701,109,635,603,573,408,654,202,338,701,211,11,632,655,3,338,268,270,109,5,6,756,402,71,627,203,269,469,109,5,143,590,72,107,235,567,727,621,227,179,196,700,191,196,522,525,528,531,534,537,143,338,586,726,649,267,732,34,654,732,521,524,527,530,533,536,244,514,732,435,234,567,724,196,17,7,628,731,74,604,263,522,531,579,194,601,435,116,212,261,116,719,212,522,525,528,531,534,537,20,27,31,146,719,322,569,11,262,582,597,235,247,416,262,270,601,602,591,28,214,717,635,234,17,236,206,745,699,28,364,677,216,340,235,190,27,559,501,627,469,579,588,727,339,244,760,574,553,245,236,35,146,321,734,425,582,35,718,335,343,339,583,270,286,17,23,416,8,205,89,202,266,572,193,19,590,731,16,763,648,261,583,631,586,716,179,179,179,35,270,803,91,584,268,597,214,724,727,339,648,233,589,726,802,72,755,263,569,335,71,267,233,400,4,731,404,218,584,522,525,528,531,534,537,245,321,803,44,18,193,763,261,583,2,214,501,754,30,32,128,264,28,552,7,574,145,20,400,756,419,10,335,334,655,247,3,263,23,2,567,538,602,34,802,323,320,216,654,74,136,30,425,335,73,109,21,23,2,6,761,270,743,235,720,321,20,189,74,584,254,266,116,472,717,426,574,626,757,202,265,338,579,590,718,179,11,203,707,204,326,191,189,91,583,26,628,720,728,287,762,508,204,235,712,205,715,757,655,145,247,400,596,7,700,767,626,631,746,206,716,408,404,617,7,211,767,471,320,763,425,271,244,24,31,629,757,426,649,128,525,534,245,190,2,34,263,271,804,744,718,265,271,271,16,20,552,569,73,263,233,4,90,762,469,552,6,729,404,89,584,203,472,588,726,340,35,559,114,538,202,560,319,21,24,5,760,617,218,107,732,744,334,538,211,90,767,265,435,724,10,615,402,73,584,265,470,521,524,527,530,533,536,804,73,269,244,628,591,17,416,32,128,234,31,4,232,91,109,21,232,145,193,754,34,73,261,269,602,19,571,268,234,629,211,72,483,627,654,335,89,271,236,3,559,189,648,602,655,247,26,4,146,729,745,571,5,589,32,569,280,615,227,21,590,335,527,528,536,537,89,206,719,753,701,753,425,803,91,269,597,7,262,340,560,18,193,24,2,604,37,747,648,254,746,201,514,586,724,753,37,747,402,726,648,262,732,528,537,116,206,716,767,649,26,91,655,234,567,596,716,677,30,32,569,334,94,262,601,528,537,233,18,236,760,8,586,716,483,747,268,524,527,533,536,116,731,280,201,145,629,727,802,700,194,267,16,803,582,18,190,193,35,762,23,31,4,572,616,128,582,401,145,2,567,326,343,521,524,530,533,744,3,472,719,318,213,245,280,755,574,203,302,233,19,5,718,616,756,72,401,471,245,108,143,143,728,364,74,743,560,23,326,319,34,323,318,512,613,115,502,301,130,614,129,118,272,79,96,80,540,546,97,99,82,83,417,98,38,324]

mon_store = {}
party_order = {}

for trainer in data:
    trainer_num = int(trainer[-3:])
    trainer_name = trainer[:-4]

    # Trainer aussortieren, die nicht in der In-Game-Liste sind
    if trainer_num not in number_of_ingame_trainers:
        continue

    final_party = []
    
    # Die Reihenfolge der Pokémon wie in der calc.json-Datei vorhanden ist
    for dirty_mon_name in data[trainer].keys():
        mon_name = dirty_mon_name[:-2]
        if len([x for x in final_party if x == mon_name]) > 0:
            i = 1
            while f'{mon_name} ({i})' in final_party:
                i += 1
            final_party.append(f'{mon_name} ({i})')
        else:
            final_party.append(mon_name)

    party_order[trainer_name + f' [#{trainer_num}]'] = final_party

    for mon_name in final_party:
        mon_index = final_party.index(mon_name)
        dirty_mon_name = list(data[trainer].keys())[mon_index]
        mon_name_actual = mon_name.split(' (')[0]

        # Mapping von Moves
        for move in data[trainer][dirty_mon_name]["moves"]:
            if "Hidden Power~" in move:
                code = move.split("~")[-1]
                if code in hidden_power_map:
                    # Ersetzen der Hidden Power mit dem korrekten Typ
                    data[trainer][dirty_mon_name]["moves"][
                        data[trainer][dirty_mon_name]["moves"].index(move)
                    ] = f"Hidden Power {hidden_power_map[code]}"
            elif move == "Hidden Power":  # Fall für Hidden Power ohne Zahl
                data[trainer][dirty_mon_name]["moves"][
                    data[trainer][dirty_mon_name]["moves"].index(move)
                ] = "Hidden Power Psychic"
            elif move in ["Weather Ball~2", "Weather Ball~3"]:  # Fall für Weather Ball~2/3
                data[trainer][dirty_mon_name]["moves"][
                    data[trainer][dirty_mon_name]["moves"].index(move)
                ] = "Weather Ball"
        if mon_name_actual not in mon_store:
            mon_store[mon_name_actual] = {}

        if "(" in mon_name:
            mon_store[mon_name_actual][
                trainer_name + ' ' + mon_name.split(" ")[-1] + f' [#{trainer_num}]'
            ] = data[trainer][dirty_mon_name]
        else:
            mon_store[mon_name_actual][
                trainer_name + f' [#{trainer_num}]'
            ] = data[trainer][dirty_mon_name]

# Speichern der angepassten Daten in JSON-Dateien
with open('setdex.json', 'w', encoding="utf8") as f:
    json.dump(mon_store, f, sort_keys=True, indent='\t', separators=(',', ': '), ensure_ascii=False)

with open('party_order.json', 'w', encoding="utf8") as f:
    json.dump(party_order, f, indent='\t', separators=(',', ': '), ensure_ascii=False)
