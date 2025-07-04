import os
from src.scrythonAPI import ScrythonApi
from src.utils import Utils
from src.cardBuilderHTML import HtmlCardBuilder
from src.cardBuilderPNG import PNGCardBuilder
from PIL import Image

def getInfoForCardFace(cardFace):
    cardName = cardFace["name"]
    type_line = cardFace["type_line"]
    try: 
        power = cardFace["power"]
    except:
        power = ""
    try: 
        toughness = cardFace["toughness"]
    except:
        toughness = ""
    try:
        mana_cost = cardFace["mana_cost"]        
    except:
        ""
    else: 
        manaCostTextImage = None
    try:
        oracle_text = cardFace["oracle_text"]
    except:
        oracle_text = ""
    try: 
        flavor_text = cardFace["flavor_text"]
    except:
        flavor_text = ""

    return cardName, type_line, mana_cost, power, toughness, oracle_text, flavor_text

def process_normal_card(card, quantity, font32, font36, font44, originalArt):
    # print(f"Card layout is Normal - Quantity {str(quantity)}")
    cardName = card["name"]
    type_line = card["type_line"]
    mana_cost = card["mana_cost"]
    
    if mana_cost != "":
        # print(f"Mana Cost: |{mana_cost}|")
        manaCostFileName = "mana_cost" + Utils.sanitizeString(cardName) + ".png"
        manaCostTextImage = HtmlCardBuilder.getManaCostImage(mana_cost, manaCostFileName)
    else: 
        manaCostTextImage = None
    oracle_text = card.get("oracle_text", "")
    flavor_text = card.get("flavor_text", "")
    power = card.get("power", "")
    toughness = card.get("toughness", "")
    
    # print(f"Oracle text: |{oracle_text}|")
    # print(f"Flavor text: |{flavor_text}|")
    
    oracleFlavorFileName = "oracle_and_flavor" + Utils.sanitizeString(cardName) + ".png"
    oracleAndFlavorTextImage = HtmlCardBuilder.getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName)
    art_crop_url = card["image_uris"]["art_crop"]
    completedCard = PNGCardBuilder.generateCardPNG(cardName, power, toughness, type_line, art_crop_url, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage, originalArt)
    return completedCard

def merge_dual_faced_card(front_face, back_face):
    # Define the dimensions
    width = 718
    height = 1000
    # Create a black image with RGBA mode
    background_image = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    scale = 0.718
    original_width = 718
    original_height = 1000
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    
    # Resize with anti-aliasing for better quality
    front_face = front_face.resize((new_width, new_height), Image.Resampling.LANCZOS)
    front_face = front_face.rotate(270, expand=True)

    # Resize with anti-aliasing for better quality
    back_face = back_face.resize((new_width, new_height), Image.Resampling.LANCZOS)
    back_face = back_face.rotate(90, expand=True)

    combined_image = background_image.copy()
    combined_image.paste(front_face, (0, 0), front_face)
    combined_image.paste(back_face, (0, 484), back_face)

    return combined_image

def save_card(card_name, card_set, card_collector_number, cardImage, quantity):
    for x in range(quantity):
        cardImage.save("cards/"+Utils.sanitizeString(card_name)+"_"+Utils.sanitizeString(card_set)+"_"+Utils.sanitizeString(card_collector_number)+"_"+str(x+1)+".png")

class CardBuilder:
    def buildCard(line, font28, font32, font36, font44, lang, show = False, originalArt = 1):
        # TODO enable search by card lang
        # print("Downloading info for: " + line)
        card, quantity =  ScrythonApi.tryGetCard(line)
        card_layout = card["layout"]
        if card_layout == "modal_dfc":
            card_front = card["card_faces"][0]
            card_back = card["card_faces"][1]
            card_image_front = process_normal_card(card_front, quantity, font32, font36, font44, originalArt)
            card_image_back = process_normal_card(card_back, quantity, font32, font36, font44, originalArt)
            combined_card = merge_dual_faced_card(card_image_front, card_image_back)
            save_card(f"{card_front["name"]}_x_{card_back["name"]}", card["set"], card["collector_number"], combined_card, quantity)
            return True
        if card_layout == "normal":
            card_image = process_normal_card(card, quantity, font32, font36, font44, originalArt)
            save_card(card["name"], card["set"], card["collector_number"], card_image, quantity)
            return True
        if card_layout == "adventure":
            # print(f"CardFaces {card["card_faces"]}")
            cardNameFirst, type_lineFirst, manaCostFirst, powerFirst, toughnessFirst, oracle_textFirst, flavor_textFirst = getInfoForCardFace(card["card_faces"][0])
            cardNameSecond, type_lineSecond, manaCostSecond, powerSecond, toughnessSecond, oracle_textSecond, flavor_textSecond = getInfoForCardFace(card["card_faces"][1])
            
            # print(f"Mana Cost: |{manaCostFirst}|")
            manaCostFileNameFirst = "mana_cost"+Utils.sanitizeString(cardNameFirst)+".png"
            manaCostTextImageFirst = HtmlCardBuilder.getManaCostImage(manaCostFirst, manaCostFileNameFirst)

            manaCostFileNameSecond = "mana_cost"+Utils.sanitizeString(cardNameSecond)+".png"
            manaCostTextImageSecond = HtmlCardBuilder.getManaCostImageAdventure(manaCostSecond, manaCostFileNameSecond)

            # print(f"Oracle text: |{oracle_textFirst}|")
            # print(f"Flavor text: |{flavor_textFirst}|")
            oracleFlavorFileNameFirst = "oracle_and_flavor"+Utils.sanitizeString(cardNameFirst)+".png"
            oracleAndFlavorTextImageFirst = HtmlCardBuilder.getOracleAndFlavorTextImageForAdventure(oracle_textFirst, flavor_textFirst, oracleFlavorFileNameFirst)

            oracleFlavorFileNameSecond = "oracle_and_flavor"+Utils.sanitizeString(cardNameSecond)+".png"
            oracleAndFlavorTextImageSecond = HtmlCardBuilder.getOracleAndFlavorTextImageForAdventure(oracle_textSecond, flavor_textSecond, oracleFlavorFileNameSecond)

            art_crop_url = card["image_uris"]["art_crop"]
            completedCard = PNGCardBuilder.generateAdventureCardPNG(cardNameFirst, powerFirst, toughnessFirst, type_lineFirst, manaCostTextImageFirst, oracleAndFlavorTextImageFirst,
                                                                    cardNameSecond, powerSecond, toughnessSecond, type_lineSecond, manaCostTextImageSecond, oracleAndFlavorTextImageSecond,
                                                                    art_crop_url, font28, font32, font36, font44, originalArt)
            
            save_card(f"{cardNameFirst}_x_{cardNameSecond}", card["set"], card["collector_number"], completedCard, quantity)

            return True


        print(f"Card Error {line}")
        print(f"Card Layout {card["layout"]}")
        return False
