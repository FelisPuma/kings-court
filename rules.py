#! /usr/bin/env python3

from roles import * 
import random
import sys

class RuleSet:

    def __init__(self, title, roles):
        self.title = title # The name of the rule set
        self.roles = roles # The permitted roles, with their conditions

    def assignRoles(self, players):
        pass

# These are the rule sets. These could also be loaded from a file.

# Standard rules, just King Court v2.0
class Standard(RuleSet):
    def __init__(self):
        RuleSet.__init__(self, "Standard", [King(), Royalist(), Traitor(), Usurper(), Parliamentarian(), Jester()])

    def assignRoles(self, players):
        assignments = [] # Stores the tuples (email, role)
        usedroletitles = [] # Roles that have been selected, this could be computed from assignments
        roles = self.roles
        curplayer = 0

        while len(assignments) < len(players):
            while True: # do-while to find a legal role
                try:
                    temprole = random.choice(roles)
                except IndexError:
                    print("ERROR: Roles are assigned as follows with no valid roles remaing. Emails not sent!")
                    print(assignments)
                    sys.exit()
                if temprole.isAllowed(usedroletitles, len(players)):
                    break
                else: # Remove disallowed role to avoid retry, not really required
                    # If we want to do a good job https://www.oreilly.com/library/view/python-cookbook/0596001673/ch02s09.html
                    roles.remove(temprole)
            # Remove used roles from the list
            roles.remove(temprole)
            # Assign the role, is there a better way than curplayer?
            assignments.append((players[curplayer], temprole))
            curplayer += 1
            usedroletitles.append(temprole.title)

        return assignments