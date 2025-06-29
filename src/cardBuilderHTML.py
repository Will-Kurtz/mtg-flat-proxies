from src.utils import Utils
from html2image import Html2Image
from PIL import Image, ImageChops, ImageDraw, ImageFont


class HtmlCardBuilder:
    def getManaCostImage(card, manaCostFileName):
        try:
            hti = Html2Image(size=(1024, 1024))
            manaCost = card.mana_cost()
            htmlManaCost= HtmlCardBuilder.buildManaCostHTML(card=card)
            hti.screenshot(html_str=htmlManaCost, css_file='css/main.css', save_as=manaCostFileName)
            manaCostTextImage = Image.open(manaCostFileName).convert('RGBA')
            return Utils.trimImage(manaCostTextImage)
        except Exception as e:
            return None
        
    def getOracleAndFlavorTextImage(card, oracleFlavorFileName):
        hti = Html2Image(size=(1024, 1024))

        htmlOracleAndFlavorText= HtmlCardBuilder.buildOracleAndFlavorHTML(card)
        hti.screenshot(html_str=htmlOracleAndFlavorText, css_file='css/main.css', save_as=oracleFlavorFileName)
        oracleAndFlavorTextImage = Image.open(oracleFlavorFileName).convert('RGBA')
        return Utils.trimImage(oracleAndFlavorTextImage)




    def getOracleTextHTML(card):
        cardText = card.oracle_text()

        result = Utils.replaceManaAndSymbols(cardText)

        oracleTextStart = """<div class="oracle-text"><span>"""
        oracleTextEnd = """</span></div>"""
        if hasattr(card, 'oracle_text') and callable(getattr(card, 'oracle_text')):
            oracleText = oracleTextStart + result + oracleTextEnd
        else:
            oracleText = "" 

        return oracleText

    def getManaCostTextHTML(card):
        cardText = card.mana_cost()

        result = Utils.replaceManaAndSymbolsLarge(cardText)

        oracleTextStart = """<div class="oracle-text"><span>"""
        oracleTextEnd = """</span></div>"""
        if hasattr(card, 'oracle_text') and callable(getattr(card, 'oracle_text')):
            oracleText = oracleTextStart + result + oracleTextEnd
        else:
            oracleText = "" 

        return oracleText

    def buildManaCostHTML(card):
        firstPart = """<head>
        <link rel="stylesheet" href="css/main.css"/>
        <link href="css/mana.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        <div class="bg-image">
            <div class="card-containers">
                <div class="base-card-rule-container">
                    <div class="base-card-rule-box">"""
        lastPart = """</div>
                </div>
            </div>
        </div>
        </body>"""
        return firstPart + HtmlCardBuilder.getManaCostTextHTML(card) + lastPart

    def buildOracleAndFlavorHTML(card):
        firstPart = """<head>
        <link rel="stylesheet" href="css/main.css"/>
        <link href="css/mana.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        <div class="bg-image">
            <div class="card-containers">
                <div class="base-card-rule-container">
                    <div class="base-card-rule-box">
                        <div class="base-card-oracle-and-flavor-box">"""
        lastPart = """</div>
                    </div>
                </div>
            </div>
        </div>
        </body>"""
        divider = """<div class="oracle-flavor-spacer"></div>"""
        flavorStart = """<div class="oracle-text-flavor">"""
        flavorEnd = """</div>"""
        try:
            return firstPart + HtmlCardBuilder.getOracleTextHTML(card) + divider + flavorStart + card.flavor_text() + flavorEnd + lastPart 
        except Exception as e:
            print(f"An error occurred: {e}")

        return firstPart + HtmlCardBuilder.getOracleTextHTML(card) + lastPart