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
        
    def getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName):
        hti = Html2Image(size=(1024, 1024))

        htmlOracleAndFlavorText= HtmlCardBuilder.buildOracleAndFlavorHTML(oracle_text, flavor_text)
        hti.screenshot(html_str=htmlOracleAndFlavorText, css_file='css/main.css', save_as=oracleFlavorFileName)
        oracleAndFlavorTextImage = Image.open(oracleFlavorFileName).convert('RGBA')
        return Utils.trimImage(oracleAndFlavorTextImage)




    def getOracleTextHTML(oracle_text):
        result = Utils.replaceManaAndSymbols(oracle_text)

        oracleTextStart = """<div class="oracle-text"><span>"""
        oracleTextEnd = """</span></div>"""
        if oracle_text is not "":
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

    def buildOracleAndFlavorHTML(oracle_text, flavor_text):
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
        if flavor_text is not "":
            return firstPart + HtmlCardBuilder.getOracleTextHTML(oracle_text) + divider + flavorStart + flavor_text + flavorEnd + lastPart 

        return firstPart + HtmlCardBuilder.getOracleTextHTML(oracle_text) + lastPart