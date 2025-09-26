## characters.rpy
define narrator = Character(None)               # narrator
define ranger = Character("Ranger", what_prefix="“", what_suffix="”")
define player = Character("You")              

# Shared defaults (variables everyone can use)
default ranger_trust = 0                  # grows/shrinks across interactions
default ranger_secrets = []                 # list of strings students append
