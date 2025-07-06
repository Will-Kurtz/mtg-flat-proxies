import os
from src.scrythonAPI import ScrythonApi
from src.utils import Utils
from src.cardBuilderHTML import HtmlCardBuilder
from src.cardBuilderPNG import PNGCardBuilder
from src.debug import Debug
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

def process_normal_card(card, font32, font36, font44, originalArt):
    cardName = card["name"]
    type_line = card["type_line"]
    mana_cost = card["mana_cost"]
    
    if mana_cost != "":
        manaCostFileName = "mana_cost" + Utils.sanitizeString(cardName) + ".png"
        manaCostTextImage = HtmlCardBuilder.getManaCostImage(mana_cost, manaCostFileName)
    else: 
        manaCostTextImage = None
    oracle_text = card.get("oracle_text", "")
    flavor_text = card.get("flavor_text", "")
    power = card.get("power", "")
    toughness = card.get("toughness", "")
    
    oracleFlavorFileName = "oracle_and_flavor" + Utils.sanitizeString(cardName) + ".png"
    oracleAndFlavorTextImage = HtmlCardBuilder.getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName)
    art_crop_url = card["image_uris"]["art_crop"]
    completedCard = PNGCardBuilder.generateCardPNG(cardName, power, toughness, type_line, art_crop_url, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage, originalArt)
    return completedCard

def merge_dual_faced_card(front_face, back_face):
    width = 718
    height = 1000
    scale = width/height
    combined_image = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    front_face = front_face.resize((new_width, new_height), Image.Resampling.LANCZOS)
    front_face = front_face.rotate(270, expand=True)
    back_face = back_face.resize((new_width, new_height), Image.Resampling.LANCZOS)
    back_face = back_face.rotate(90, expand=True)

    combined_image.paste(front_face, (0, 0), front_face)
    combined_image.paste(back_face, (0, 484), back_face)

    return combined_image

def save_card(card_name, card_set, card_collector_number, cardImage, quantity):
    for x in range(quantity):
        cardImage.save("cards/"+Utils.sanitizeString(card_name)+"_"+Utils.sanitizeString(card_set)+"_"+Utils.sanitizeString(card_collector_number)+"_"+str(x+1)+".png")

def download_default_card(url, originalArt):
    downloaded_image = Utils.getCardImage(url).convert("RGBA")
    overlay_template = Image.open("arts/base_template.png").convert("RGBA")
    composite_image = downloaded_image.resize((718,1000), Image.Resampling.LANCZOS).copy()
    composite_image.alpha_composite(overlay_template, (0, 0))
    if originalArt == 2:
        return PNGCardBuilder.enhance_image(composite_image.convert('L'), 0.9, 1.5)
    return downloaded_image

class CardBuilder:
    def build_card(line, font28, font32, font36, font44, image_filter = 1):
        # TODO enable search by card lang
        card, quantity, is_error =  ScrythonApi.try_get_card(line)

        if is_error:
            return False

        card_layout = card["layout"]        

        if card_layout == "normal":
            if "planeswalker" in card["type_line"].lower():
                art_url = card["image_uris"]["large"]
                downloaded_image = download_default_card(art_url, image_filter)
                save_card(card["name"], card["set"], card["collector_number"], downloaded_image, quantity)
                return False
            
            card_image = process_normal_card(card, font32, font36, font44, image_filter)
            save_card(card["name"], card["set"], card["collector_number"], card_image, quantity)
            return True
        
        if card_layout == "modal_dfc":
            card_front = card["card_faces"][0]
            card_back = card["card_faces"][1]
            card_image_front = process_normal_card(card_front, font32, font36, font44, image_filter)
            card_image_back = process_normal_card(card_back, font32, font36, font44, image_filter)
            combined_card = merge_dual_faced_card(card_image_front, card_image_back)
            save_card(f"{card_front["name"]}_x_{card_back["name"]}", card["set"], card["collector_number"], combined_card, quantity)
            return True
        
        if card_layout == "adventure":
            cardNameFirst, type_lineFirst, manaCostFirst, powerFirst, toughnessFirst, oracle_textFirst, flavor_textFirst = getInfoForCardFace(card["card_faces"][0])
            cardNameSecond, type_lineSecond, manaCostSecond, powerSecond, toughnessSecond, oracle_textSecond, flavor_textSecond = getInfoForCardFace(card["card_faces"][1])
            
            manaCostFileNameFirst = "mana_cost"+Utils.sanitizeString(cardNameFirst)+".png"
            manaCostTextImageFirst = HtmlCardBuilder.getManaCostImage(manaCostFirst, manaCostFileNameFirst)

            manaCostFileNameSecond = "mana_cost"+Utils.sanitizeString(cardNameSecond)+".png"
            manaCostTextImageSecond = HtmlCardBuilder.getManaCostImageAdventure(manaCostSecond, manaCostFileNameSecond)

            oracleFlavorFileNameFirst = "oracle_and_flavor"+Utils.sanitizeString(cardNameFirst)+".png"
            oracleAndFlavorTextImageFirst = HtmlCardBuilder.getOracleAndFlavorTextImageForAdventure(oracle_textFirst, flavor_textFirst, oracleFlavorFileNameFirst)

            oracleFlavorFileNameSecond = "oracle_and_flavor"+Utils.sanitizeString(cardNameSecond)+".png"
            oracleAndFlavorTextImageSecond = HtmlCardBuilder.getOracleAndFlavorTextImageForAdventure(oracle_textSecond, flavor_textSecond, oracleFlavorFileNameSecond)

            art_url = card["image_uris"]["art_crop"]
            completedCard = PNGCardBuilder.generateAdventureCardPNG(cardNameFirst, powerFirst, toughnessFirst, type_lineFirst, manaCostTextImageFirst, oracleAndFlavorTextImageFirst,
                                                                    cardNameSecond, powerSecond, toughnessSecond, type_lineSecond, manaCostTextImageSecond, oracleAndFlavorTextImageSecond,
                                                                    art_url, font28, font32, font36, font44, image_filter)
            
            save_card(f"{cardNameFirst}_x_{cardNameSecond}", card["set"], card["collector_number"], completedCard, quantity)
            return True

        Debug.log(f"Card Error {line}")
        Debug.log(f"Card Layout {card["layout"]}")
        art_url = card["image_uris"]["large"]
        downloaded_image = download_default_card(art_url, image_filter)
        save_card(card["name"], card["set"], card["collector_number"], downloaded_image, quantity)
        return False
