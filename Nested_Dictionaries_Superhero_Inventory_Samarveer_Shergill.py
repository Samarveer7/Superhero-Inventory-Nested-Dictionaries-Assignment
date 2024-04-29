#Superhero Inventory - Samarveer Shergill
#April 25, 2024


#Listed below are a few characters from The Avengers along with their home bases, 
#true identity, potential threats and inventories!

# Characters and traits
characters = {                                                        #Defines a dictionary 'chracters' containing information about different characters                  
    "Spiderman": {                                                    #A dictionary that gives information about spiderman          
        "secret_identity": "Peter Parker",                            
        "super_power": "Spider sense and superhuman strength",
        "health_points": 150
    },
    "Iron Man": {                                                     #A dictionary that gives information about Iron Man
        "secret_identity": "Tony Stark",
        "super_power": "Powered armor suit",
        "health_points": 200
    },
    "Captain America": {                                              #A dictionary that gives information about Captain America
        "secret_identity": "Steve Rogers",
        "super_power": "Super soldier serum",
        "health_points": 180
    }
}

# Locations and descriptions
locations = {                                                                            #Defines a dictionary 'locations' containing information about the home bases of the chracters
    "New York City": "Spiderman's hometown and main patrol area.",                       #Spiderman's home base
    "Stark Tower": "Iron Man's headquarters and technology hub.",                        #Iron Man's home base
    "The Avengers Compound": "Home base for the Avengers, including Captain America."    #Captain America's home base
}

# Additional location descriptions
additional_descriptions = {                                                                                                         #Defines a dictionary 'additional descriptions' containing some extra information
    "New York City": "You are on a bustling city street. Watch out for criminals!",                                                 #Additional description about New York City
    "Stark Tower": "You are in the heart of advanced technology. Various suits and gadgets are being developed here.",              #Additional description about Stark tower
    "The Avengers Compound": "You are in a high-security facility. Training sessions and strategy meetings are common here.",       #Additional description about th Avengers compound
    "Supply Depot": "You have found a supply depot. It contains valuable items for your mission. Choose wisely!",                   #Additional description about Supply depot
    "Empty Alley": "You have reached an empty alley. Take a moment to rest and plan your next move."                                #additional description about Empty alley
}

# Inventory and characteristics
inventory = {                                                                                                  #Defines a dictionary 'inventory' containing information about the inventories of the Avengers
    "Spiderman's Inventory": [                                                                                 #dictionary conataining Spiderman's inventory
        {
            "item": "Web shooters",
            "description": "Devices that shoot synthetic webbing for swinging and trapping enemies.",
            "damage": 10,
            "protection": 0
        },
        {
            "item": "Spider-Tracer",
            "description": "Tracking device used to trace objects or individuals.",
            "damage": 5,
            "protection": 0
        }
    ],
    "Iron Man's Inventory": [                                                                                 #dictionary conataining Iron man's inventory
        {
            "item": "Mark LXXXV Suit",
            "description": "Advanced powered armor suit equipped with various weapons and flight capabilities.",
            "damage": 100,
            "protection": 100
        },
        {
            "item": "Repulsor Beams",
            "description": "Energy blasts emitted from Iron Man's palms.",
            "damage": 50,
            "protection": 0
        }
    ],
    "Captain America's Inventory": [                                                                          #dictionary conataining Captain America's inventory
        {
            "item": "Vibranium Shield",
            "description": "Nearly indestructible shield made of vibranium.",
            "damage": 50,
            "protection": 150
        },
        {
            "item": "Mjolnir",
            "description": "Thor's enchanted hammer, wielded by Captain America in certain situations.",
            "damage": 200,
            "protection": 100
        }
    ]
}

# Printing out the information
for character, traits in characters.items():                                                     
    print(f"{character}'s secret identity is {traits['secret_identity']}.")                   #prints the characters' seceret identity
    print(f"{character}'s super power is {traits['super_power']}.")                           #prints the characters' super powers
    print(f"{character} has {traits['health_points']} health points.\n")                      #prints characters' health points


print("Locations:")                                                                           #prints the locations
for location, description in locations.items():
    print(f"- {location}: {description}")
    
print("\nAdditional Descriptions:")                                                           #prints the additional descriptions
for location, description in additional_descriptions.items():
    print(f"{location} - {description}")
    

for inventory_type, items in inventory.items():                                               #prints each character's inventory 
    print(f"{inventory_type}:")
    for item in items:
        print(f"* {item['item']}")
        print(f"description: {item['description']}")
        print(f"damage: {item['damage']}")
        print(f"protection: {item['protection']}\n")

