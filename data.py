# Dictionary for cows's status
status = {
    "Name": "", 
    "Type": "", 
    "Age": 0, 
    "Hunger": 0,
    "Happiness": 100, 
    "Owned Toys": []
}

# Dictionary for cow's toys
toy_dictionary = {
    "Highland": ["bagpipes", "Loch Ness monster", "rugby ball"], 
    "Texas Longhorn": ["guitar", "Trump", "tumbleweed"], 
    "Limousin": ["bike", "skiis", "Effiel Tower"], 
}

# Dictionary for cow's food
food_dictionary = {
    "Highland": ["haggis", "shortbread", "bacon butty"], 
    "Texas Longhorn": ["barbeque", "chilli", "anything fried"], 
    "Limousin": ["baguette", "cigarette", "croissant"], 
}

# Dictionary for menu options
menu_options = {
    "Q": {"function": quit_app, "text": "Quit the application"},
    "F": {"function": feed_cow, "text": f"Feed {name}"},
    "G": {"function": game, "text": f"Play rock, paper, scissors against {name}"},
    "T": {"function": toy, "text": f"Give {name} a new toy"}
}