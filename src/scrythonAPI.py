import scrython
import scrython.cards
import time
import json

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
    def getCardInfo(name):
        time.sleep(0.1)
        print("getCardInfo")
        card = scrython.cards.Named(exact=name)
        obj = json.loads(card)
        json_formatted_str = json.dumps(obj, indent=0)
        print(json_formatted_str)
        return card
    def tryGetCard(line):
        print("line"+str(line))
        try:
            card = parse_card_line(line)
            search = scrython.cards.Search(q="set:"+ card["set"] + " number:"+str(card["number"])+"", pretty=True)
            # print("JSON representation:")
            # print(json.dumps(search.data(), indent=4))
            # print(search.data()[0]["name"])
            # print(search.data()[0]["layout"])
            return search.data()[0], card["quantity"]
        except scrython.ScryfallError as e:
            print(str(e.error_details['status']) + ' ' + e.error_details['code'] + ': ' + e.error_details['details'])

        return
    def tryGetMoreInfoAboutCard(name):
        time.sleep(0.1)
        # print("tryGetMoreInfoAboutCard")
        # card = scrython.cards.search(name=name)
        # print
        # obj = json.loads(card)
        # json_formatted_str = json.dumps(obj, indent=0)
        # print(json_formatted_str)
        # print("tried")

        # return card
        try:
            search = scrython.cards.Search(q="set:fic number:173", pretty=True)
            print("tried")
            # print(dir(search))
            # print(dir(search.dict.values))
            print("JSON representation:")
            print(json.dumps(search.data(), indent=4))
            return search
        except scrython.ScryfallError as e:
            print(str(e.error_details['status']) + ' ' + e.error_details['code'] + ': ' + e.error_details['details'])

        # results = scrython.cards.Search(name='Hildibrand Manderville', mode='fuzzy')
        # print(results)
        # # Check if any results were found
        # if results:
        #     for card in results:
        #         print(f"Name: {card['name']}, Set: {card['set']}, ID: {card['id']}")
        # else:
        #     print("No cards found with that name.")
    
    def getCardAlternateArtInfo(code, collectorNumber, lang):
        time.sleep(0.1)
        print("getCardAlternateArtInfo")

        if lang is None:
            card = scrython.cards.Collector(code=code, collector_number=collectorNumber)
            obj = json.loads(card)
            json_formatted_str = json.dumps(obj, indent=0)
            print(json_formatted_str)
            return card
        return scrython.cards.Collector(code=code, collector_number=collectorNumber, lang=lang)
