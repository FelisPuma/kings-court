#! /usr/bin/env python3

from emailSender import create_service, create_message, send_message
from rules import Standard
import re

def load_players(filename):
    """Loads player emails from file. Lines with # are comments.

    Args:
        filename: Name of player file

    Returns:
        A list of player emails.
    """

    players = []

    try:
        with open(filename) as playerfile :
            for line in playerfile :
                # Check for lines that don't start with # and have an @ then a .
                if re.match(r"^\s*[^#][^@]*@[^@]+\.", line) :
                    players.append(line.strip())
    except IOError as e:
        print("I/O ERROR({0}): {1}".format(e.errno, e.strerror))

    return players

def main():
    players = load_players("playeremails.txt")
    print("Players are: {}".format(", ".join(players)))
    
    rules = Standard()
    assignments = rules.assignRoles(players)
    print(assignments)

    # Generate the messages and send to players
    service = create_service()
    for pairs in assignments:
        message = create_message("B3 MTG", pairs[0], "Manifest Roltiny", pairs[1].emailBody())
        send_message(service, "me", message)

if __name__ == '__main__':
    main()