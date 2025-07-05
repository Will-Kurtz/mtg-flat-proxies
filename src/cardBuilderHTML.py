from src.utils import Utils
from html2image import Html2Image
from PIL import Image, ImageChops, ImageDraw, ImageFont
import os

def remove_parentheses(s):
    if s.startswith('('):
        s = s[1:]  # Remove the first character if it's '('
    if s.endswith(')'):
        s = s[:-1]  # Remove the last character if it's ')'
    return s
class HtmlCardBuilder:
    def getManaCostImage(mana_cost, manaCostFileName):
        try:
            hti = Html2Image(size=(1024, 1024))
            htmlManaCost= HtmlCardBuilder.buildManaCostHTML(mana_cost)
            hti.screenshot(html_str=htmlManaCost, css_file='css/main.css', save_as=manaCostFileName)
            manaCostTextImage = Image.open(manaCostFileName).convert('RGBA')
            os.remove(manaCostFileName)
            return Utils.trimImage(manaCostTextImage)
        except Exception as e:
            return None
        
    def getManaCostImageAdventure(mana_cost, manaCostFileName):
        try:
            hti = Html2Image(size=(1024, 1024))
            htmlManaCost= HtmlCardBuilder.buildManaCostHTMLAdventure(mana_cost)
            hti.screenshot(html_str=htmlManaCost, css_file='css/main.css', save_as=manaCostFileName)
            manaCostTextImage = Image.open(manaCostFileName).convert('RGBA')
            os.remove(manaCostFileName)
            return Utils.trimImage(manaCostTextImage)
        except Exception as e:
            return None
        
    def getOracleAndFlavorTextImageForAdventure(oracle_text, flavor_text, oracleFlavorFileName):
        hti = Html2Image(size=(1024, 1024))
        htmlOracleAndFlavorText= HtmlCardBuilder.buildAdventureOracleAndFlavorHTML(oracle_text, flavor_text)
        hti.screenshot(html_str=htmlOracleAndFlavorText, css_file='css/main.css', save_as=oracleFlavorFileName)
        oracleAndFlavorTextImage = Image.open(oracleFlavorFileName).convert('RGBA')
        os.remove(oracleFlavorFileName)
        return Utils.trimImage(oracleAndFlavorTextImage)
    
    def getOracleAndFlavorTextImage(oracle_text, flavor_text, oracleFlavorFileName):
        hti = Html2Image(size=(1024, 1024))
        htmlOracleAndFlavorText= HtmlCardBuilder.buildOracleAndFlavorHTML(oracle_text, flavor_text)
        hti.screenshot(html_str=htmlOracleAndFlavorText, css_file='css/main.css', save_as=oracleFlavorFileName)
        oracleAndFlavorTextImage = Image.open(oracleFlavorFileName).convert('RGBA')
        os.remove(oracleFlavorFileName)
        return Utils.trimImage(oracleAndFlavorTextImage)

    def getOracleTextHTML(oracle_text):
        result = Utils.replaceManaAndSymbols(remove_parentheses(oracle_text))

        oracleTextStart = """<div class="oracle-text"><span>"""
        oracleTextEnd = """</span></div>"""
        if oracle_text is not "":
            oracleText = oracleTextStart + result + oracleTextEnd
        else:
            oracleText = "" 

        return oracleText

    def getManaCostTextHTML(mana_cost):
        result = Utils.replaceManaAndSymbolsLarge(mana_cost)

        oracleTextStart = """<div class="oracle-text"><span>"""
        oracleTextEnd = """</span></div>"""
        return oracleTextStart + result + oracleTextEnd

    def getManaCostTextHTMLAdventure(mana_cost):
        result = Utils.replaceManaAndSymbols(mana_cost)

        oracleTextStart = """<div class="oracle-text"><span>"""
        oracleTextEnd = """</span></div>"""
        return oracleTextStart + result + oracleTextEnd

    def buildManaCostHTML(mana_cost):
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
        return firstPart + HtmlCardBuilder.getManaCostTextHTML(mana_cost) + lastPart
    
    def buildManaCostHTMLAdventure(mana_cost):
        firstPart = """<head>
        <link rel="stylesheet" href="css/main.css"/>
        <link href="css/mana.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        <div class="bg-image">
            <div class="card-containers">
                <div class="base-card-rule-container">
                    <div class="adventure-card-rule-box">"""
        lastPart = """</div>
                </div>
            </div>
        </div>
        </body>"""
        return firstPart + HtmlCardBuilder.getManaCostTextHTMLAdventure(mana_cost) + lastPart

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
    
    def buildAdventureOracleAndFlavorHTML(oracle_text, flavor_text):
        firstPart = """<head>
        <link rel="stylesheet" href="css/main.css"/>
        <link href="css/mana.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        <div class="bg-image">
            <div class="card-containers">
                <div class="base-card-rule-container">
                    <div class="base-card-rule-box">
                        <div class="adventure-card-oracle-and-flavor-box">"""
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