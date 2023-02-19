"""
A BARD DAY'S NIGHT
a.k.a. BARD ROCK CAFE
a.k.a. THE SCHOOL OF BARD KNOCKS
a.k.a. A BARD RAIN'S A-GONNA FALL
"""

# Imports

from typing import Optional, TextIO  # Specific annotations

from math import ceil  # For stats

# Constants

# Minimum number of songs for a villager to be promoted to a bard
BARD_THRESHOLD = 10

# Number of songs for the billboard_top statistic
BILLBOARD_N = 10

# Maps from {name: songs that this person knows}
villagers_type = dict[str, set[str]]

bards_type = set[str]

# Maps from {song name: names of people that know this song}
songs_type = dict[str, set[str]]

# A list of parties; each party is a set of the attendee names
parties_type = list[set[str]]


def read_input(
        f: TextIO,
) -> tuple[villagers_type, bards_type, songs_type, parties_type]:
    """
    Read the given file and return the villagers, bards, songs, and parties.

    f is an open file containing VILLAGERS and bards, SONGS, and PARTIES,
    in that order. One villager or bard per line;
    one song per line; one party per line, consisting of attendees
    separated by commas. The parties are given in the order they're held.

    """
    villagers = {}
    bards = set()
    songs = {}
    parties = []
    section = ''

    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        if line == 'VILLAGERS':
            section = line
            continue
        elif line == 'SONGS':
            section = line
            continue
        elif line == 'PARTIES':
            section = line
            continue
        elif line == '':
            continue

        if section == 'VILLAGERS':
            if line.endswith('*'):
                line = line.replace('*', '')
                bards.add(line)
            else:
                villagers.update({line: set()})
        elif section == 'SONGS':
            songs.update({line: set()})
        elif section == 'PARTIES':
            parties.append(set(line.split(',')))

    return villagers, bards, songs, parties


def sing_at_party(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        party: set[str]
) -> None:
    """
    A bard sings if present, otherwise the villagers sing.
    """
    villagers_knows_songs = set()

    if len(party & bards) > 0:
        for villager_knows_songs in villagers.values():
            villagers_knows_songs |= villager_knows_songs
        all_songs = set(songs.keys())
        songs_list = sorted(all_songs - villagers_knows_songs)
        for attendee in party - bards:
            attendee_knows_songs = villagers[attendee]
            if len(songs_list) > 0:
                attendee_knows_songs.add(songs_list[0])

    elif len(party - bards) > 0:
        attendees_knows_songs = set()
        for party_attendee in party:
            for attendee_knows_song in villagers[party_attendee]:
                attendees_knows_songs.add(attendee_knows_song)
        for party_attendee in party:
            villagers[party_attendee] |= attendees_knows_songs


def update_bards_after_party(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        party: set[str]
) -> None:
    """
    Promote attendees who have learned enough songs to bards,
    iff there is another bard present at the party.
    """
    for party_attendee in party - bards:
        knows_songs = villagers[party_attendee]
        all_songs = set(songs.keys())
        if knows_songs == all_songs or len(knows_songs) >= BARD_THRESHOLD:
            bards.add(party_attendee)


def unheard_songs(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> set[str]:
    """
    Return a set of songs that have never been heard by non-bards.
    (This means that only the bards know it.)
    """
    villagers_knows_songs = set()
    for villager_knows_songs in villagers.values():
        villagers_knows_songs |= villager_knows_songs

    all_songs = set()
    for song in songs.keys():
        all_songs.add(song)

    only_bards = all_songs - villagers_knows_songs
    return only_bards


def billboard_top(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> list[str]:
    """
    Return a list of the BILLBOARD_N most popular songs by number of people
    who know them, in descending order. Break ties alphabetically.
    """
    billboard = dict()
    for song in songs:
        billboard[song] = 0

    for knows_songs in villagers.values():
        for song in knows_songs:
            if song in billboard:
                billboard[song] += 1
            else:
                billboard[song] = 0

    sorted_billboard = sorted(billboard.items(), key=lambda item: item[1], reverse=True)

    ret_billboard = []
    if len(sorted_billboard) > BILLBOARD_N:
        for i in range(0, BILLBOARD_N):
            ret_billboard.append(sorted_billboard[i][0])
    else:
        for i in range(0, len(sorted_billboard)):
            ret_billboard.append(sorted_billboard[i][0])

    return ret_billboard


def all_bards(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> set[str]:
    """Return the set of the village's bards."""
    # villager_bards = set()

    # orig_villagers = set(villagers.keys())
    # villagers_bards = bards & orig_villagers

    # return villagers_bards
    return bards


def average_attendees(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> int:
    """
    Return the average number of attendees at parties in the village.
    Round up to the nearest integer.
    """
    no_parties = 0
    no_attendees = 0

    for party in parties:
        if len(party) > 0:
            no_parties += 1
            no_attendees += len(party)

    if no_parties > 0 and no_attendees > 0:
        return ceil(no_attendees / no_parties)
    else:
        return 0


# Main process

def run(filename: str) -> dict[str, object]:
    """
    Run the program: Create a village, read the input, host the parties,
    and return a dictionary of resulting statistics keyed by name:
    unheard_songs, billboard_top, all_bards, average_attendees

    filename is the name of an input file.
    """
    ret = dict()

    f = open(filename)
    villagers, bards, songs, parties = read_input(f)
    f.close()

    for party in parties:
        sing_at_party(villagers, bards, songs, party)
        update_bards_after_party(villagers, bards, songs, party)

    ret['unheard_songs'] = unheard_songs(villagers, bards, songs, parties)
    ret['billboard_top'] = billboard_top(villagers, bards, songs, parties)
    ret['all_bards'] = all_bards(villagers, bards, songs, parties)
    ret['average_attendees'] = average_attendees(villagers, bards, songs, parties)

    return ret


# Run program

if __name__ == "__main__":

    # Sample input from the handout -- you can tweak this if you like
    stats_handout = run("handout_example.txt")
    print("Results of handout sample input")
    for key, value in stats_handout.items():
        print(f"{key}: {value}")

    print()

    # Sample bigger input -- you can tweak this if you like
    stats_bigger = run("bigger_example.txt")
    print("Results of bigger sample input")
    for key, value in stats_bigger.items():
        print(f"{key}: {value}")
