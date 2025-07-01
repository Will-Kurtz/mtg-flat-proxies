
from PIL import Image, ImageChops, ImageDraw, ImageFont
from src.utils import Utils

class PNGCardBuilder:
    

    def generateCardPNG(card, cardName, type_line, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage):
        baseCard = PNGCardBuilder.getBaseCardBackground(card).convert("RGBA")
        baseCardWithText = ImageDraw.Draw(baseCard)

        # Add Card Name to image
        baseCardWithText.text((55, 62), cardName, font=font36, fill =('#000000'))
        # Add Line Type to image
        baseCardWithText.text((55, 581), type_line, font=font32, fill =('#000000'))
        try:
            baseCardWithText.text((585, 905), str(card.power())+"/"+str(card.toughness()), font=font44, fill =('#000000'))
        except Exception as e:
            print(f"An error occurred: {e}")

        oracleFlavorwidth, oracleFlavorHeight = oracleAndFlavorTextImage.size
        oracleAndFlavorPosition = (68, int(628 +(306 - oracleFlavorHeight) / 2))
        baseCard.paste(oracleAndFlavorTextImage, oracleAndFlavorPosition, oracleAndFlavorTextImage)

        if(manaCostTextImage is not None):
            manaCostWidth, manaCostHeight = manaCostTextImage.size
            baseCard.paste(manaCostTextImage, (int(665 - manaCostWidth), int(57)), manaCostTextImage)

        cropeedImageZX = Utils.getCardImage(card.image_uris()["art_crop"]).convert("RGBA")
        cropeedImage = cropeedImageZX.crop((0,0, 612, 446))
        baseCard.paste(cropeedImage, (53,112), cropeedImage)
        return baseCard


    def getBaseCardBackground(card):
        try:
            isCreature = card.power()
            return Image.open('./arts/base_creature_template.png')
        except Exception as e:
            return Image.open('./arts/base_non_creature_template.png')
