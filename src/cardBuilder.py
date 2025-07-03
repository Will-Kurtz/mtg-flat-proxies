import os
from src.scrythonAPI import ScrythonApi
from src.utils import Utils
from src.cardBuilderHTML import HtmlCardBuilder
from src.cardBuilderPNG import PNGCardBuilder

class CardBuilder:
    def buildCard(cardObject, font32, font36, font44, lang, show = False, originalArt = 1):
        # TODO enable search by name or set collector number
        # card = ScrythonApi.getCardInfo(cardObject["name"])
        print("Downloading info for: " + cardObject["name"])
        try:
            card = ScrythonApi.getCardAlternateArtInfo(cardObject["set"], cardObject["collectorNumber"], lang)
        except:
            try:
                card = ScrythonApi.getCardInfo(cardObject["name"])
            except:
                print("Card not found " + cardObject["name"] + " for selected edition/language")
                return

        try:
            cardName = card.printed_name()
        except Exception as e:
            cardName = card.name()

        try:
            type_line = card.printed_type_line()
        except Exception as e:
            type_line = card.type_line()
        
        try:
            oracle_text = card.printed_text()
        except Exception as e:
            oracle_text = card.oracle_text()
        
        try:
            flavor_text = card.flavor_text()
        except Exception as e:
            flavor_text = ""

        manaCostFileName = "mana_cost"+Utils.sanitizeString(cardName)+".png"
        manaCostTextImage = HtmlCardBuilder.getManaCostImage(card, manaCostFileName)

        oracleFlavorFileName = "oracle_and_flavor"+Utils.sanitizeString(cardName)+".png"
        oracleAndFlavorTextImage = HtmlCardBuilder.getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName)

        completedCard = PNGCardBuilder.generateCardPNG(card, cardName, type_line, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage, originalArt)
        os.remove(oracleFlavorFileName)
        os.remove(manaCostFileName)
        if(show is True):
            completedCard.show()

        for x in range(cardObject["quantity"]):
            completedCard.save("cards/"+Utils.sanitizeString(cardName)+"_"+cardObject["set"]+"_"+cardObject["collectorNumber"]+"_"+str(x+1)+".png")