import json

# Define a function to parse each line into an object
def parse_line(line):
    parts = line.split(' ')
    quantity = int(parts[0])
    # Join the name parts until the set identifier
    name_parts = []
    i = 1
    while not parts[i].startswith('('):
        name_parts.append(parts[i])
        i += 1
    name = ' '.join(name_parts)
    
    # Extract set and collector number
    set_info = parts[i][1:-1]  # Remove parentheses
    collector_number = parts[i + 1]
    
    return {
        'quantity': quantity,
        'name': name,
        'set': set_info,
        'collectorNumber': collector_number
    }

class DecklistReader:
    def readFile(filename):
        # Read the file and transform each line
        objects = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line:  # Check if the line is not empty
                    obj = parse_line(line)
                    objects.append(obj)

        # Print the resulting list of objects
        # print(json.dumps(objects, indent=2))
        return objects
