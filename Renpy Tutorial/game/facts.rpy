## facts.rpy
init python:
    def add_secret(new_secret):
        if new_secret not in ranger_secrets:
            ranger_secrets.append(new_secret)

    def change_trust(delta):
        global ranger_trust
        ranger_trust += delta