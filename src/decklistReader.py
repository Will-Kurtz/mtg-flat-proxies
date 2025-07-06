class DecklistReader:
    def read_file_to_list(filename):
        with open(filename, 'r') as file:
            content = file.read()
            return content.splitlines()  # Split into lines
        