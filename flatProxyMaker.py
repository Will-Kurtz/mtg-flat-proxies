import argparse
from PIL import ImageFont
from src.cardBuilder import CardBuilder
from src.decklistReader import DecklistReader
from src.utils import Utils
from src.debug import Debug

def main(decklist_filename, image_filter, debug_mode):
    Debug.set_debug_enabled(debug_mode)
    # Custom font style and font size
    beleren_bold_28 = ImageFont.truetype('./fonts/BelerenBold.ttf', 28)
    beleren_bold_32 = ImageFont.truetype('./fonts/BelerenBold.ttf', 32)
    beleren_bold_36 = ImageFont.truetype('./fonts/BelerenBold.ttf', 36)
    beleren_bold_44 = ImageFont.truetype('./fonts/BelerenBold.ttf', 42)

    list_lines = DecklistReader.read_file_to_list(decklist_filename)

    processed_cards = [] 
    failed_cards = []

    for line in list_lines:
        is_success = CardBuilder.build_card(line, beleren_bold_28, beleren_bold_32, beleren_bold_36, beleren_bold_44, image_filter)
        if is_success is True:
            processed_cards.append(line)
        else:
            failed_cards.append(line)

    Utils.save_strings_to_file(processed_cards, "success/downloaded")
    Utils.save_strings_to_file(failed_cards, "failed/failed_download")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MTG Flat Proxy Maker.")
    parser.add_argument('--deck', type=str, help='Path and filename of your decklist', default="./decklists/example_deck.txt")
    parser.add_argument('--image_filter', type=int, help='Should the program print the original card art or a B&W Line Art', default=1)
    parser.add_argument('--debug_mode', type=Utils.str_to_bool, help='Should the program print the original card art or a B&W Line Art', default=False)
    args = parser.parse_args()
    main(args.deck, args.image_filter, args.debug_mode)