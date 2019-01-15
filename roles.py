#! /usr/bin/env python3

__all__ = ["King", "Royalist", "Traitor", "Usurper", "Parliamentarian", "Jester"]

class Role:

    def __init__(self, title, group, exclude, description):
        self.title = title # The name of the role
        self.group = group # The type of role
        self.exclude = exclude # Other roles to exclude if this one is used
        self.description = description # The text sent to the player

    def isAllowed(self, roletitles, playercount):
        # Check if any excluded roles have been chosen yet
        allowed = True
        #print ("Checking used {1} excluded {0}".format(", ".join(self.exclude), roletitles))
        for excludetitle in self.exclude:
            if excludetitle in roletitles:
                allowed = False
                break # Could just let it go through all of them?
        #print ("Allowed is {}".format(allowed))
        return allowed

    def emailBody(self):
        return "You are the " + self.title + ", a(n) " + self.group + " role.\n\n" + self.description

    def __str__(self):
        return self.title + " (" + self.group + "): " + self.description

# The roles are defined here. Alternatively, these could be loaded from a file.

class King(Role):
    def __init__(self):
        Role.__init__(self, "King", "Ruler", [], "The King picks the format, goes first and starts with 25 life. The King wins if the Usurper, Parliamentarian and Traitor are dead. If there is no Traitor then the King wins if the Usurper and Parliamentarian are dead.")

class Royalist(Role):
    def __init__(self):
        Role.__init__(self, "Royalist", "Support", ["Traitor"], "The Royalist wins if they are still alive when the King wins. Can also win if the Usurper and Parliamentaria are dead.")

class Traitor(Role):
    def __init__(self):
        Role.__init__(self, "Traitor", "Assassin", ["Royalist"], "The Traitor wins by dealing the King the killing blow, like the Usurper, or as the last one standing.")
        
class Usurper(Role):
    def __init__(self):
        Role.__init__(self, "Usurper", "Assassin", [], "The Usurper wins by dealing the killing blow to the King or by being the last one standing.")

class Parliamentarian(Role):
    def __init__(self):
        Role.__init__(self, "Parliamentarian", "Assassin", [], "The Parliamentarian wins if the King and Royalist are dead and the Usurper didn't deal the King the killing blow.")

class Jester(Role):
    def __init__(self):
        Role.__init__(self, "Jester", "Nuetral", [], "The Jester may win only through an alternative victory condition (printed on a card) and only if nobody else has won first. The Jester can also win as last one standing.")
    def isAllowed(self, roles, playercount):
        if Role.isAllowed(self, roles, playercount):
            return playercount > 4
        else:
            return False
