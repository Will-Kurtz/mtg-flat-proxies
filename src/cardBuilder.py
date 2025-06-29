import os
from src.scrythonAPI import ScrythonApi
from src.utils import Utils
from src.cardBuilderHTML import HtmlCardBuilder
from src.cardBuilderPNG import PNGCardBuilder

class CardBuilder:
    def buildCard(cardObject, font32, font36, font44, show = False):
        # TODO enable search by name or set collector number
        # card = ScrythonApi.getCardInfo(cardObject["name"])
        print("Downloading info for: " + cardObject["name"])
        card = ScrythonApi.getCardAlternateArtInfo(cardObject["set"], cardObject["collectorNumber"])

        manaCostFileName = "mana_cost"+Utils.sanitizeString(card.name())+".png"
        manaCostTextImage = HtmlCardBuilder.getManaCostImage(card, manaCostFileName)

        oracleFlavorFileName = "oracle_and_flavor"+Utils.sanitizeString(card.name())+".png"
        oracleAndFlavorTextImage = HtmlCardBuilder.getOracleAndFlavorTextImage(card, oracleFlavorFileName)

        completedCard = PNGCardBuilder.generateCardPNG(card, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage)
        os.remove(oracleFlavorFileName)
        os.remove(manaCostFileName)
        if(show is True):
            completedCard.show()

        for x in range(cardObject["quantity"]):
            completedCard.save("cards/"+Utils.sanitizeString(card.name())+"_"+cardObject["set"]+"_"+cardObject["collectorNumber"]+"_"+str(x+1)+".png")