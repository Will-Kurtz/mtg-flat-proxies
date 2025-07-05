
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageEnhance
from src.utils import Utils
from src.test import Test
import cv2
import numpy as np

def enhance_image(image, brightness_factor, contrast_factor):
    # Load the image
    # Enhance brightness
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    return image

def reduce_colors(base_image, num_colors):
    # Load the image
    # image = Image.open(image_path)
    # Convert the image to P mode which is a palette-based image
    return base_image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)

def reduce_dither(base_image, kernel_size = 5):
    # 2. Remove dither with median filter
    print("Removing dithering artifacts...")
    original_arr = np.array(base_image)
    cleaned_arr = cv2.medianBlur(original_arr, kernel_size)  # Kernel size 5 works well for most cases
    return Image.fromarray(cleaned_arr)
    cleaned.save(f"{output_dir}/1_cleaned_dither.png")

class PNGCardBuilder:
    def generateCardPNG(cardName, power, toughness, type_line, art_crop_url, font32, font36, font44, manaCostTextImage, oracleAndFlavorTextImage, originalArt=1):
        baseCard = PNGCardBuilder.getBaseCardBackground(power).convert("RGBA")
        baseCardWithText = ImageDraw.Draw(baseCard)

        # Add Card Name to image
        baseCardWithText.text((55, 62), cardName, font=font36, fill =('#000000'))
        # Add Line Type to image
        baseCardWithText.text((55, 581), type_line, font=font32, fill =('#000000'))
        if(power != ""):
            baseCardWithText.text((585, 905), str(power)+"/"+str(toughness), font=font44, fill =('#000000'))

        if(oracleAndFlavorTextImage is not None):
            oracleFlavorwidth, oracleFlavorHeight = oracleAndFlavorTextImage.size
            oracleAndFlavorPosition = (68, int(628 +(306 - oracleFlavorHeight) / 2))
            baseCard.paste(oracleAndFlavorTextImage, oracleAndFlavorPosition, oracleAndFlavorTextImage)

        if(manaCostTextImage is not None):
            manaCostWidth, manaCostHeight = manaCostTextImage.size
            baseCard.paste(manaCostTextImage, (int(665 - manaCostWidth), int(57)), manaCostTextImage)

        # card.image_uris()["art_crop"]
        cropeedImageZX = Utils.getCardImage(art_crop_url).convert("RGBA")
        # cropeedImageZX.save("temp/"+Utils.sanitizeString(cardName)+".png")
        brightness_factor = 1.25  # Increase brightness (1.0 means no change)
        contrast_factor = 1.25  

        if originalArt == 1:
            print("originalArt " + str(originalArt))
            cropeedImage = cropeedImageZX.crop((0,0, 612, 446))
            baseCard.paste(cropeedImage, (53,112), cropeedImage)
            return baseCard
        if originalArt == 2:
            baseCopy = cropeedImageZX.copy()
            noDither = reduce_dither(baseCopy, 3)
            bwNoDither = noDither.copy().convert('L')
            enhancedImage = enhance_image(bwNoDither, brightness_factor, contrast_factor)
            num_colors = 8  # Specify the number of colors you want
            reduced_image = reduce_colors(enhancedImage, num_colors).copy().convert('RGBA')
            cropeedImage = reduced_image.crop((0,0, 612, 446))
            baseCard.paste(cropeedImage, (53,112), cropeedImage)
            return baseCard
        if originalArt == 3:
            baseCopy = cropeedImageZX.copy()
            noDither = reduce_dither(baseCopy, 5)
            num_colors = 16 # Specify the number of colors you want
            reduced_image = reduce_colors(noDither, num_colors).copy().convert('RGBA')
            cropeedImage = reduced_image.crop((0,0, 612, 446))
            baseCard.paste(cropeedImage, (53,112), cropeedImage)
            return baseCard


        print(cardName)
        cropeedImageZX.save("temp/"+Utils.sanitizeString(cardName)+".png")
        Test.convertImageToLineArtPng(cardName)

        line_art = Image.open("temp/"+cardName+"_lines.png")
        line_art = line_art.resize((626, 457)).crop((0,0, 612, 446))
        baseCard.paste(line_art, (53,112), line_art)
        return baseCard
    
    def generateAdventureCardPNG(cardNameFirst, powerFirst, toughnessFirst, type_lineFirst, manaCostTextImageFirst, oracleAndFlavorTextImageFirst,
                                 cardNameSecond, powerSecond, toughnessSecond, type_lineSecond, manaCostTextImageSecond, oracleAndFlavorTextImageSecond, 
                                 art_crop_url, font28, font32, font36, font44, originalArt=1):
        baseCard = PNGCardBuilder.getBaseAdventureCardBackground(powerFirst).convert("RGBA")
        baseCardWithText = ImageDraw.Draw(baseCard)

        # Add Card Name to image
        baseCardWithText.text((55, 62), cardNameFirst, font=font36, fill =('#000000'))
        # Add Line Type to image
        baseCardWithText.text((55, 581), type_lineFirst, font=font32, fill =('#000000'))
        # Add Card Name to image
        baseCardWithText.text((60, 638), cardNameSecond, font=font28, fill =('#000000'))
        baseCardWithText.text((60, 684), type_lineSecond, font=font28, fill =('#000000'))

        try:
            baseCardWithText.text((585, 905), str(powerFirst)+"/"+str(toughnessFirst), font=font44, fill =('#000000'))
        except Exception as e:
            print(f"An error occurred: {e}")

        if(oracleAndFlavorTextImageFirst is not None):
            oracleFlavorwidth, oracleFlavorHeight = oracleAndFlavorTextImageFirst.size
            oracleAndFlavorPosition = (370, int(628 +(306 - oracleFlavorHeight) / 2))
            baseCard.paste(oracleAndFlavorTextImageFirst, oracleAndFlavorPosition, oracleAndFlavorTextImageFirst)

        if(oracleAndFlavorTextImageSecond is not None):
            oracleFlavorwidth, oracleFlavorHeight = oracleAndFlavorTextImageSecond.size
            oracleAndFlavorPosition = (68, int(720 +(213 - oracleFlavorHeight) / 2))
            baseCard.paste(oracleAndFlavorTextImageSecond, oracleAndFlavorPosition, oracleAndFlavorTextImageSecond)

        if(manaCostTextImageFirst is not None):
            manaCostWidth, manaCostHeight = manaCostTextImageFirst.size
            baseCard.paste(manaCostTextImageFirst, (int(665 - manaCostWidth), int(57)), manaCostTextImageFirst)

        
        if(manaCostTextImageSecond is not None):
            manaCostWidth, manaCostHeight = manaCostTextImageSecond.size
            baseCard.paste(manaCostTextImageSecond, (int(352 - manaCostWidth), int(634)), manaCostTextImageSecond)

        # card.image_uris()["art_crop"]
        cropeedImageZX = Utils.getCardImage(art_crop_url).convert("RGBA")
        # cropeedImageZX.save("temp/"+Utils.sanitizeString(cardName)+".png")
        brightness_factor = 1.25  # Increase brightness (1.0 means no change)
        contrast_factor = 1.25  

        if originalArt == 1:
            print("originalArt " + str(originalArt))
            cropeedImage = cropeedImageZX.crop((0,0, 612, 446))
            baseCard.paste(cropeedImage, (53,112), cropeedImage)
            return baseCard
        if originalArt == 2:
            baseCopy = cropeedImageZX.copy()
            noDither = reduce_dither(baseCopy, 3)
            bwNoDither = noDither.copy().convert('L')
            enhancedImage = enhance_image(bwNoDither, brightness_factor, contrast_factor)
            num_colors = 8  # Specify the number of colors you want
            reduced_image = reduce_colors(enhancedImage, num_colors).copy().convert('RGBA')
            cropeedImage = reduced_image.crop((0,0, 612, 446))
            baseCard.paste(cropeedImage, (53,112), cropeedImage)
            return baseCard
        if originalArt == 3:
            baseCopy = cropeedImageZX.copy()
            noDither = reduce_dither(baseCopy, 5)
            num_colors = 16 # Specify the number of colors you want
            reduced_image = reduce_colors(noDither, num_colors).copy().convert('RGBA')
            cropeedImage = reduced_image.crop((0,0, 612, 446))
            baseCard.paste(cropeedImage, (53,112), cropeedImage)
            return baseCard


        print(cardNameFirst)
        cropeedImageZX.save("temp/"+Utils.sanitizeString(cardNameFirst)+".png")
        Test.convertImageToLineArtPng(cardNameFirst)

        line_art = Image.open("temp/"+cardNameFirst+"_lines.png")
        line_art = line_art.resize((626, 457)).crop((0,0, 612, 446))
        baseCard.paste(line_art, (53,112), line_art)
        return baseCard



    def getBaseCardBackground(power):
        if power == "":
            return Image.open('./arts/base_non_creature_template.png')
        return Image.open('./arts/base_creature_template.png')
    
    def getBaseAdventureCardBackground(power):
        if power == "":
            return Image.open('./arts/base_adventure_non_creature_template.png')
        return Image.open('./arts/base_adventure_creature_template.png')
