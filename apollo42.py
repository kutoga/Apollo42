#!/usr/bin/env python3
import sys
import re
import inquirer
from mutagen.easyid3 import EasyID3

def remove_duplicates(lst):
    for i in reversed(range(len(lst))):
        remove_duplicate = lst[i] in lst[:i]
        if remove_duplicate:
            lst.pop(i)

def get_candidates_from_name(file):
    artists = []
    titles = []
    low_prio_candidates = []

    # remove extension
    low_prio_candidates.append(file.strip())
    if '.' in file:
        file = '.'.join(file.split('.')[:-1])

    file = file.strip()
    if file:

        # does the name end with \[[a-zA-Z0-9]+\]? we want to ignore that (this was added by youtube-dl)
        parts = file.split()
        if len(parts) > 1 and re.match(r'^\[[0-9a-zA-Z]{5,}\]$', parts[-1]):
            low_prio_candidates.insert(0, file)
            file = file[:-len(parts[-1])].strip()

        for sep in [' - ', '-']:
            parts = file.split(sep)
            if len(parts) <= 1:
                continue

            for i in range(1, len(parts)):
                part1 = ' '.join(parts[:i]).strip()
                part2 = ' '.join(parts[i:]).strip()

                artists.append(part1)
                titles.append(part2)

                low_prio_candidates += [part1, part2]

                # sometimes there are some suffixes like "(official)" => remove that
                if re.match(r'.*\([^)]+\)$', part2):
                    part2 = part2[:part2.rindex('(')].strip()
                    artists.append(part2)
                    titles.append(part2)

        # add full name as candidates
        artists.append(file)
        titles.append(file)

    artists += low_prio_candidates
    titles += low_prio_candidates

    return artists, titles

def choose_candidate(name, candidates):
    theme = inquirer.themes.Default()
    theme.Checkbox.selected_color = theme.Checkbox.unselected_color
    custom_text = 'CUSTOM'
    candidates.append(custom_text)
    selection = inquirer.prompt([inquirer.List(f'items',
        message=f"Please select the {name}",
        choices=candidates,
        default=candidates[0]
    )], theme=theme)['items']
    if selection == custom_text:
        selection = input(f'Input a value for {name}: ')
    return selection

def get_candidates_from_id3(file):
    artists = []
    titles = []

    id3 = EasyID3(file)
    if 'artist' in id3:
        try:
            artists.append(id3['artist'][0])
        except:
            pass
    if 'title' in id3:
        try:
            titles.append(id3['title'][0])
        except:
            pass

    return artists, titles

def add_tags(file):
    artists = []
    titles = []

    def add_candidates(candidates):
        nonlocal artists
        nonlocal titles
        artists += candidates[0]
        titles += candidates[1]

    add_candidates(get_candidates_from_id3(file))
    add_candidates(get_candidates_from_name(file))

    # remove duplicates:
    # note that we still prefer a list, because we need a specific ordering
    remove_duplicates(artists)
    remove_duplicates(titles)

    artist = choose_candidate('artist', artists)
    title = choose_candidate('title', titles)

    id3 = EasyID3(file)
    id3['artist'] = artist
    id3['title'] = title
    id3.save(v2_version=3)

def main():
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} file1.mp3 file2.mp3 ...")
        exit(1)
    
    for i, file in enumerate(sys.argv[1:]):
        if len(sys.argv) > 1:
            if i > 0:
                print('---------------------------')
            print(f'File: {file}')
        add_tags(file)

if __name__ == '__main__':
    main()

