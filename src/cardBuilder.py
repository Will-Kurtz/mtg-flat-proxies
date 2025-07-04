import os
from src.scrythonAPI import ScrythonApi
from src.utils import Utils
from src.cardBuilderHTML import HtmlCardBuilder
from src.cardBuilderPNG import PNGCardBuilder

class CardBuilder:
    def buildCard(line, font32, font36, font44, lang, show = False, originalArt = 1):
        # TODO enable search by card lang
        print("Downloading info for: " + line)
        card, quantity =  ScrythonApi.tryGetCard(line)
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
        
        return

        # try:
        #     cardName = card.printed_name()
        # except Exception as e:
        #     cardName = card.name()

        # try:
        #     type_line = card.printed_type_line()
        # except Exception as e:
        #     type_line = card.type_line()
        
        # try:
        #     oracle_text = card.printed_text()
        # except Exception as e:
        #     oracle_text = card.oracle_text()
        
        # try:
        #     flavor_text = card.flavor_text()
        # except Exception as e:
        #     flavor_text = ""

        # manaCostFileName = "mana_cost"+Utils.sanitizeString(cardName)+".png"
        # manaCostTextImage = HtmlCardBuilder.getManaCostImage(card, manaCostFileName)

        # oracleFlavorFileName = "oracle_and_flavor"+Utils.sanitizeString(cardName)+".png"
        # oracleAndFlavorTextImage = HtmlCardBuilder.getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName)

        # completedCard = PNGCardBuilder.generateCardPNG(card, cardName, type_line, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage, originalArt)
        # os.remove(oracleFlavorFileName)
        # os.remove(manaCostFileName)
        # os.remove("temp/"+Utils.sanitizeString(cardName)+".png")
        # if(show is True):
        #     completedCard.show()

        # for x in range(cardObject["quantity"]):
        #     completedCard.save("cards/"+Utils.sanitizeString(cardName)+"_"+cardObject["set"]+"_"+cardObject["collectorNumber"]+"_"+str(x+1)+".png")