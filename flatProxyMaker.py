import argparse
from PIL import ImageFont
from src.cardBuilder import CardBuilder
from src.decklistReader import DecklistReader

def save_strings_to_file(string_array, output_file):
    if len(string_array) <= 0:
        return
    try:
        with open(f"decklists/{output_file}.txt", 'w') as file:
            for string in string_array:
                file.write(string + '\n')  # Adds a newline after each string
        print(f"Successfully saved strings to '{output_file}'")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main(deckpath=None, showCards=None, lang=None, original_art=1):
    # Custom font style and font size
    belerenBold28 = ImageFont.truetype('./fonts/BelerenBold.ttf', 28)
    belerenBold32 = ImageFont.truetype('./fonts/BelerenBold.ttf', 32)
    belerenBold36 = ImageFont.truetype('./fonts/BelerenBold.ttf', 36)
    belerenBold44 = ImageFont.truetype('./fonts/BelerenBold.ttf', 42)


    decklistFileNamePath = deckpath
    if deckpath is None:
        decklistFileNamePath = "./decklists/example_deck.txt"

    showCard = showCards
    if showCards is None:
        showCard = False

    # listCards = DecklistReader.readFile(decklistFileNamePath)
    listLines = DecklistReader.read_file_to_list(decklistFileNamePath)

    processedCards = [] 
    errorCards = []
    print("original_art " + str(original_art))
    for line in listLines:
        cardStatus = CardBuilder.buildCard(line, belerenBold28, belerenBold32, belerenBold36, belerenBold44, lang, showCard, original_art)
        if cardStatus is True:
            processedCards.append(line)
        else:
            errorCards.append(line)

    save_strings_to_file(processedCards, "success/downloaded")
    save_strings_to_file(errorCards, "failed/failed_download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MTG Minimalist proxy maker.")
    parser.add_argument('--deck', type=str, help='Optional argument 1')
    parser.add_argument('--showCards', type=bool, help='Show Cards Preview')
    parser.add_argument('--lang', type=str, help='Card language 2 char word as described on scryfall api')
    parser.add_argument('--original_art', type=int, help='Should the program print the original card art or a B&W Line Art')
    args = parser.parse_args()
    main(args.deck, args.showCards, args.lang, args.original_art)