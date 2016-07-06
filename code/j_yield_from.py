import os


def main():
    root_dir = '/Users/mkennedy/github/talk-python/transcripts'

    files = get_files(root_dir)
    print("Found these files")
    for f in files:
        print(f)
    print('done')


def get_files(folder):
    for item in os.listdir(folder):
        if item == '.DS_Store':
            continue

        full_item = os.path.join(folder, item)
        if os.path.isfile(full_item):
            yield full_item
        elif os.path.isdir(full_item):
            # NOW WHAT?
            pass
            # TODO: old skool style loop
            # TODO: new recursive yield style


if __name__ == '__main__':
    main()
