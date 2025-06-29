import argparse
from PIL import ImageFont
from src.cardBuilder import CardBuilder
from src.decklistReader import DecklistReader

def main(deckpath=None, showCards=None):
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

    for card in listCards:
        CardBuilder.buildCard(card, belerenBold32, belerenBold36, belerenBold44, showCard)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MTG Minimalist proxy maker.")
    parser.add_argument('--deck', type=str, help='Optional argument 1')
    parser.add_argument('--showCards', type=bool, help='Show Cards Preview')
    args = parser.parse_args()
    main(args.deck, args.showCards)