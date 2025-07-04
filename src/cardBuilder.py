import os
from src.scrythonAPI import ScrythonApi
from src.utils import Utils
from src.cardBuilderHTML import HtmlCardBuilder
from src.cardBuilderPNG import PNGCardBuilder

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
class CardBuilder:
    def buildCard(line, font32, font36, font44, lang, show = False, originalArt = 1):
        # TODO enable search by card lang
        print("Downloading info for: " + line)
        card, quantity =  ScrythonApi.tryGetCard(line)
        print(f"Card Layout {card["layout"]}")
        if card["layout"] == "normal":
            print(f"Card layout is Normal - Quantity {str(quantity)}")
            cardName = card["name"]
            type_line = card["type_line"]
            mana_cost = card["mana_cost"]
            if mana_cost != "":
                print(f"Mana Cost: |{mana_cost}|")
                manaCostFileName = "mana_cost"+Utils.sanitizeString(cardName)+".png"
                manaCostTextImage = HtmlCardBuilder.getManaCostImage(mana_cost, manaCostFileName)
            else: 
                manaCostTextImage = None
            try:
                oracle_text = card["oracle_text"]
            except:
                oracle_text = ""
            try: 
                flavor_text = card["flavor_text"]
            except:
                flavor_text = ""
            try: 
                power = card["power"]
            except:
                power = ""
            try: 
                toughness = card["toughness"]
            except:
                toughness = ""
            
            print(f"Oracle text: |{oracle_text}|")
            print(f"Flavor text: |{flavor_text}|")
            oracleFlavorFileName = "oracle_and_flavor"+Utils.sanitizeString(cardName)+".png"
            oracleAndFlavorTextImage = HtmlCardBuilder.getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName)

            art_crop_url = card["image_uris"]["art_crop"]
            completedCard = PNGCardBuilder.generateCardPNG(cardName, power, toughness, type_line, art_crop_url, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage, originalArt)

            if(show is True):
                completedCard.show()

            for x in range(quantity):
                completedCard.save("cards/"+Utils.sanitizeString(cardName)+"_"+card["set"]+"_"+card["collector_number"]+"_"+str(x+1)+".png")
        if card["layout"] == "adventure":

            # print(f"CardFaces {card["card_faces"]}")
            cardNameFirst, type_lineFirst, manaCostFirst, powerFirst, toughnessFirst, oracle_textFirst, flavor_textFirst = getInfoForCardFace(card["card_faces"][0])
            cardNameSecond, type_lineSecond, manaCostSecond, powerSecond, toughnessSecond, oracle_textSecond, flavor_textSecond = getInfoForCardFace(card["card_faces"][1])
            
            # print(f"Mana Cost: |{manaCostFirst}|")
            manaCostFileNameFirst = "mana_cost"+Utils.sanitizeString(cardNameFirst)+".png"
            manaCostTextImageFirst = HtmlCardBuilder.getManaCostImage(manaCostFirst, manaCostFileNameFirst)

            # print(f"Oracle text: |{oracle_textFirst}|")
            # print(f"Flavor text: |{flavor_textFirst}|")
            oracleFlavorFileNameFirst = "oracle_and_flavor"+Utils.sanitizeString(cardNameFirst)+".png"
            oracleAndFlavorTextImageFirst = HtmlCardBuilder.getOracleAndFlavorTextImageForAdventure(oracle_textFirst, flavor_textFirst, oracleFlavorFileNameFirst)

            art_crop_url = card["image_uris"]["art_crop"]
            completedCard = PNGCardBuilder.generateAdventureCardPNG(cardNameFirst, powerFirst, toughnessFirst, type_lineFirst,
                                                                    
                                                                     art_crop_url, font32, font36, font44, manaCostTextImageFirst, oracleAndFlavorTextImageFirst, originalArt)
            if(show is True):
                completedCard.show()

            for x in range(quantity):
                completedCard.save("cards/"+Utils.sanitizeString(cardNameFirst)+"_"+card["set"]+"_"+card["collector_number"]+"_"+str(x+1)+".png")
        return
