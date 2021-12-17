import PySimpleGUI as sg

# Should use YML

# Character states:
charStates_dict = {"Player": 6, "Ghost": 3.6, "Default beefalo": 7,
                   "Ornery beefalo": 7, "Rider beefalo": 8,
                   "Pudgy beefalo": 6.5}

charMult_dict = {"Other characters": 1, "WX-78 overcharge": 1.5,
                 "Wormwood bloom": 1.2, "Woodie beaver": 1.1,
                 "Woodie goose": 1.4, "Woodie moose": 0.9}

# Items
handItems_dict = {"Empty": 1, "Thulicite club": 1.1,
                  "Walking cane": 1.25, "Lazy explorer": 1.25}
headItems_dict = {"Empty": 1, "Ice cube": 0.9}
chestItems_dict = {"Empty": 1, "Marble armor": 0.7,
                   "Piggy back": 0.9, "Magiluminecense": 1.2,
                   "Sculpture": 0.15}

exoticMults_dict = {"stormCheck": 0.4, "roadCheck": 1.3,
                    "webbingCheck": 0.6, "AntlionCheck": 0.3,
                    "honeyCheck": 0.4}

saddles_dict = {"Default": 1.4, "Glossomor": 1.55, "WarSaddle": 1.25}

# The six didgets in order mean if the following should be disabled:
# - state
# - character
# - head
# - chest
# - hand
# - saddle.
# **0** means they shall not be touched, 1 means they should be off.

exceptions_list = [["stateInput", "Player", 0, 0, 0, 0, 0, 1],
                   ["chestInput", "Sculpture", 0, 0, 1, 0, 1, 1],
                   ["charInput", "Woodie beaver", 0, 0, 1, 1, 1, 1],
                   ["charInput", "Woodie goose", 0, 0, 1, 1, 1, 1],
                   ["charInput", "Woodie moose", 0, 0, 1, 1, 1, 1],
                   ["stateInput", "Ghost", 0, 1, 1, 1, 1, 1],
                   ["stateInput", "Default beefalo", 0, 1, 1, 1, 1, 0],
                   ["stateInput", "Ornery beefalo", 0, 1, 1, 1, 1, 0],
                   ["stateInput", "Rider beefalo", 0, 1, 1, 1, 1, 0],
                   ["stateInput", "Pudgy beefalo", 0, 1, 1, 1, 1, 0]]

# Layout

charStates_names = list(charStates_dict)  # This is to get the keys
# vals = list(exoticMults_dict.values()) # This is to get the values

charMult_names = list(charMult_dict)
headItems_names = list(headItems_dict)
chestItems_names = list(chestItems_dict)
handItems_names = list(handItems_dict)
saddles_names = list(saddles_dict)
exoticMults_names = list(exoticMults_dict)

layout = [
    # Character state : in other words, dead, alive, or is a beefalo
    [sg.Text("Choose your state:")],
    [sg.InputCombo(charStates_names, key="stateInput",
                   enable_events=True, default_value="Player")],

    # Character buff
    [sg.Text("Choose your character:")],
    [sg.InputCombo(charMult_names, key="charInput",
                   default_value="Other characters",
                   enable_events=True, disabled=False, visible=True)],

    # Head slot
    [sg.Text("Choose your head item:")],
    [sg.InputCombo(headItems_names, key="headInput", default_value="Empty",
                   enable_events=True, disabled=False, visible=True)],

    # Chest items
    [sg.Text("Choose your chest item:")],
    [sg.InputCombo(chestItems_names, key="chestInput", default_value="Empty",
                   enable_events=True, disabled=False, visible=True)],

    # Hand slot
    [sg.Text("Choose your hand item:")],
    [sg.InputCombo(handItems_names, key="handInput", default_value="Empty",
                   enable_events=True, disabled=False, visible=True)],

    # Saddle
    [sg.Text("Choose your saddle")],
    [sg.InputCombo(saddles_names, key="saddlesInput", default_value="Default",
                   enable_events=True, disabled=True, visible=True)],


    # Checkboxes
    [sg.Checkbox("Storm", key="stormCheck"),
     sg.Checkbox("Road", key="roadCheck"),
     sg.Checkbox("Webbing", key="webbingCheck"),
     sg.Checkbox("Antlion sinkhole", key="AntlionCheck"),
     sg.Checkbox("Honey trail", key="honeyCheck")],

    # Output text
    [sg.Text(size=(60, 1), key="output0")],

    # Buttons
    [sg.Button("Calculate"), sg.Button("Exit"), sg.Button("Copy to clipboard")]
]