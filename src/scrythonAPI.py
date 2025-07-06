import scrython
import scrython.cards
import time
import json
from src.debug import Debug

def parse_card_line(line):
    # Split the line into tokens
    tokens = line.split()
    
    # The first token is always quantity
    quantity = int(tokens[0])
    
    # Initialize variables
    name_parts = []
    set_abbr = ""
    card_num = None
    
    i = 1  # Start after quantity
    while i < len(tokens):
        token = tokens[i]
        
        # Check for set abbreviation in parentheses
        if token.startswith('('):
            set_abbr = token.strip('()')
            i += 1
            # Next token might be number
            if i < len(tokens):
                num_token = tokens[i]
                if num_token.isdigit():
                    card_num = int(num_token)
                    i += 1
            break
        
        # Add to name parts
        name_parts.append(token)
        i += 1
    
    # Join the name parts and clean up slashes
    name = ' '.join(name_parts).replace(' / / ', ' // ')
    
    # Create the card object
    card = {
        'quantity': quantity,
        'name': name,
        'set': set_abbr,
        'number': card_num
    }
    
    return card

class ScrythonApi:
    def try_get_card(line):
        Debug.log(line)
        try:
            card = parse_card_line(line)
            search = scrython.cards.Search(q="set:"+ card["set"] + " number:"+str(card["number"])+"", pretty=True)
            Debug.log("Card info from Scryfall =====================")
            Debug.log(json.dumps(search.data(), indent=4))
            Debug.log("End =========================================")
            return search.data()[0], card["quantity"], False
        except scrython.ScryfallError as e:
            print(str(e.error_details['status']) + ' ' + e.error_details['code'] + ': ' + e.error_details['details'])
            return None, None, True