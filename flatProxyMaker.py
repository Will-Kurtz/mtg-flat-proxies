import argparse
from PIL import ImageFont
from src.cardBuilder import CardBuilder
from src.decklistReader import DecklistReader
from src.utils import Utils

def main(deckpath=None, lang=None, image_filter=1):
    # Custom font style and font size
    beleren_bold_28 = ImageFont.truetype('./fonts/BelerenBold.ttf', 28)
    beleren_bold_32 = ImageFont.truetype('./fonts/BelerenBold.ttf', 32)
    beleren_bold_36 = ImageFont.truetype('./fonts/BelerenBold.ttf', 36)
    beleren_bold_44 = ImageFont.truetype('./fonts/BelerenBold.ttf', 42)

    decklist_filename = deckpath
    if deckpath is None:
        decklist_filename = "./decklists/example_deck.txt"

    list_lines = DecklistReader.read_file_to_list(decklist_filename)

    processed_cards = [] 
    failed_cards = []
    print("image_filter " + str(image_filter))
    for line in list_lines:
        is_success = CardBuilder.buildCard(line, beleren_bold_28, beleren_bold_32, beleren_bold_36, beleren_bold_44, lang, image_filter)
        if is_success is True:
            processed_cards.append(line)
            return
        failed_cards.append(line)

    Utils.save_strings_to_file(processed_cards, "success/downloaded")
    Utils.save_strings_to_file(failed_cards, "failed/failed_download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MTG Minimalist proxy maker.")
    parser.add_argument('--deck', type=str, help='Optional argument 1')
    parser.add_argument('--lang', type=str, help='Card language 2 char word as described on scryfall api')
    parser.add_argument('--image_filter', type=int, help='Should the program print the original card art or a B&W Line Art')
    args = parser.parse_args()
    main(args.deck, args.lang, args.image_filter)