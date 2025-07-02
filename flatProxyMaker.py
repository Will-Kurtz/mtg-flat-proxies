import argparse
from PIL import ImageFont
from src.cardBuilder import CardBuilder
from src.decklistReader import DecklistReader

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', '1', "True"):
        return True
    elif v.lower() in ('no', 'false', 'f', '0', "False"):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main(deckpath=None, showCards=None, lang=None, original_art=True):
    # Custom font style and font size
    belerenBold32 = ImageFont.truetype('./fonts/BelerenBold.ttf', 32)
    belerenBold36 = ImageFont.truetype('./fonts/BelerenBold.ttf', 36)
    belerenBold44 = ImageFont.truetype('./fonts/BelerenBold.ttf', 42)


    decklistFileNamePath = deckpath
    if deckpath is None:
        decklistFileNamePath = "./decklists/example_deck.txt"

    showCard = showCards
    if showCards is None:
        showCard = False

    listCards = DecklistReader.readFile(decklistFileNamePath)

    print(original_art)
    for card in listCards:
        CardBuilder.buildCard(card, belerenBold32, belerenBold36, belerenBold44, lang, showCard, original_art)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MTG Minimalist proxy maker.")
    parser.add_argument('--deck', type=str, help='Optional argument 1')
    parser.add_argument('--showCards', type=bool, help='Show Cards Preview')
    parser.add_argument('--lang', type=str, help='Card language 2 char word as described on scryfall api')
    parser.add_argument('--original_art', type=str2bool, help='Should the program print the original card art or a B&W Line Art')
    args = parser.parse_args()
    main(args.deck, args.showCards, args.lang, args.original_art)