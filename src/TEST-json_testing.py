import json
import os
import class_exit
import class_item
import dungeon
import character
import room
import adventure_loader
os.chdir("..\\")
core_chars = "                              core Characteristics                              "
char_table_bar = "+-----"
char_table_top = " "*17+"|  WS |  BS | Str | Tgh |  Ag | Int | Per |  WP | Chr |"

def print_char(char):
    if len(str(char)) == 2:
        char = str(char)
    else:
        char = " "+str(char)
    return char
def character_sheet(character):
    print("                              "+character["name"]+"                              ")
    print(f"{core_chars}")
    print((" "*17)+(char_table_bar*9)+"+")
    print(char_table_top)
    print((" "*17)+(char_table_bar*9)+"+")
    ws = print_char(character["weapon skill"])
    bs = print_char(character["ballistic skill"])
    s = print_char(character["strength"])
    t = print_char(character["toughness"])
    ag = print_char(character["agility"])
    Int = print_char(character["intelligence"])
    per = print_char(character["perception"])
    fell = print_char(character["fellowship"])
    will = print_char(character["will power"])
    print(" "*17+"|  "+ws+" |  "+bs+" |  "+s+" |  "+t+" |  "+ag+" |  "+Int+" |  "+per+" |  "+will+" |  "+fell+" |")
    print((" "*17)+(char_table_bar*9)+"+")

def exit_builder(exit):
    direction = exit["direction"]
    source_room = exit["source room"]
    destination_room = exit["destination room"]
    return class_exit.Exit(direction,source_room,destination_room)

def room_builder(room):
    name = room["name"]
    desc = room["desc"]
    return room.Room(name,desc)
def dungeon_builder(dungeon):
    pass
def adventur_builder(adv_info):
    fileName = adv_info["file name"]
    name = adv_info["name"]
    desc = adv_info["desc"]


adv_info = {
	"name": "Price of Hubris v.01",
	"description": " +++To: Lord GeneraL CasTus IaCTon+++\n+++From: Keybor Tayne, PrImary LexoGraPher+++\n+++subjeCT: ConTaCT hIsTory wITh aurum+++\nas requested, I have compiled a chronological account of our attempts to establish relations with the natives of the planet designated: aurum. The following shows a repeated pattern of rejecting diplomats, supporting your assessment that military envoys may be better received.\n+++The emperor Protects+++",
	"version": 0.01,
	"npcs": [{
			"name": "Alkedre FireStalker",
			"ballistic skill": 55,
			"weapon skill": 32,
			"strength": 50,
			"Toughness": 45,
			"Agility": 48,
			"Intelligence": 46,
			"Perception": 52,
			"Will Power": 45,
			"Fellowship": 44,
			"Home world": "Aurum",
			"motivation": "protection",
			"Gender": "Female",
			"Wounds": 26,
			"skills": "Awareness(perception),climb(strength),command(fellowship),Concealment (Agility), Dodge (Agility) +20, Intimidate (Strength) +10,Scrutiny (perception) +20, Silent Move (Agility), Survival (Intelligence) +10,Swim (Strength), Tracking (Intelligence), Wrangling (Intelligence) +10",
			"traits": "Basic Weapon Training (Primitive), Counter Attack,Crushing Blow, Lightning Attack, Melee Weapon Training(Primitive), Swift Attack, Wall of Steel."
		},
		{
			"name": "Diaz Lan",
			"ballistic skill": 38,
			"weapon skill": 52,
			"strength": 35,
			"Toughness": 41,
			"Agility": 44,
			"Intelligence": 52,
			"Perception": 43,
			"Will Power": 39,
			"Fellowship": 47,
			"Home world": "Devo Sierra",
			"motivation": "profit",
			"Gender": "Male",
			"Wounds": 17,
			"skills": "Awareness (perception), Carouse (toughness), Charm (fellowship) +20,Command (fellowship) +10, Common Lore (Imperium), Common Lore (Jericho Reach), Common Lore (Koronus Expanse),  Common Lore (Rogue Traders), Deceive (fellowship),Dodge (Agility), Evaluate (Intelligence) +10, Forbidden Lore (Xenos), Literacy (Intelligence) +10, Pilot (Space Craft) +20,Scholastic Lore (Astromancy), Scrutiny (Perception), SpeakLanguage (Low Gothic, High Gothic, Eldar), Tactics (Intelligence), Tech-Use (intelligence)",
			"traits": "Air of Authority, Ambidextrous, Deadeye Shot, Master Orator, Melee Weapon Training (Universal), Mighty Shot, Peer (Imperial Navy), Pistol Weapon Training (Universal), Nerves of Steel, Quick Draw, Step Aside, Touched by the Fates (2), Two-Weapon Wielder (Ballistic)."
		}
	],
	"items": [{
			"name": "Apple",
			"description": "A red Fuji Apple",
			"weight": 0.2,
			"actions": {
				"eat": "consume-You eat the apple",
				"examine": "It's a red apple. It looks really tasty.",
				"throw": "destroy-You hurl the apple agaisnt the wall. It smashes agaisnt it with a splat."
			}
		},
		{
			"name": "Spoon",
			"description": "A metal spoon",
			"weight": 0.1,
			"actions": {
				"examine": "examine-The spoon is made of some form of lite metal, perhaps tin.",
				"throw": "remove-You hurl the spoon agaisnt the wall. It clashes against the wall with a clatter."
			}
		}
	],
	"rooms": [{
			"name": "Room One",
			"desc": "Room one of the maze",
			"inventory": ["Apple", "Spoon"]
		},
		{
			"name": "Room Two",
			"desc": "Room Two of the maze",
			"inventory": []
		},
		{
			"name": "Room Three",
			"desc": "Room Three of the maze",
			"inventory": []
		},
		{
			"name": "Room Four",
			"desc": "Room Four of the maze",
			"inventory": []
		}

	],
	"exits": [{
			"direction": "w",
			"source room": "Room one",
			"destination room": "Room two"
		},
		{
			"direction": "e",
			"source room": "Room two",
			"destination room": "Room one"
		},
		{
			"direction": "n",
			"source room": "Room four",
			"destination room": "Room two"
		},
		{
			"direction": "s",
			"source room": "Room two",
			"destination room": "Room four"
		},
		{
			"direction": "w",
			"source room": "Room four",
			"destination room": "Room three"
		},
		{
			"direction": "e",
			"source room": "Room three",
			"destination room": "Room four"
		},
		{
			"direction": "n",
			"source room": "Room three",
			"destination room": "Room one"
		},
		{
			"direction": "s",
			"source room": "Room one",
			"destination room": "Room three"
		}
	]

}

with open("test_file.adv", "w") as write_file:
    json.dump(data, write_file)

with open("test_file.adv",'r') as adv:
    module = json.load(adv)

print(module["name"])
print(module["description"])
print(module["version"])
adv_data ={"file name":"test_file.adv", "name":module["name"], "desc":module["description"]}
adventur_builder(adv_data)

for value in module['items']:
    print(module['items']['name'])
for value in module['npcs']:
    print("Character info:")
    character_sheet(value)


