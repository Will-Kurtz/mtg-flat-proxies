from markupsafe import Markup
from PIL import Image, ImageChops
import requests
from io import BytesIO

class Utils:
    def sanitizeString(string):
        return string.replace(" ", "_").replace("'", "")
    
    def getCardImage(url):
        response = requests.get(url)
        if response.status_code == 200:
            # Open the image using PIL
            return Image.open(BytesIO(response.content))


    def replaceManaAndSymbols(string):
        replacementTap = """<i class="ms ms-cost ms-tap ms-shadow mana-size"></i>"""
        replacementColorLess = """<i class="ms ms-c ms-cost ms-shadow mana-size"></i>"""
        replacementWhite = """<i class="ms ms-cost ms-w ms-shadow mana-size"></i>"""
        replacementGreen = """<i class="ms ms-cost ms-g ms-shadow mana-size"></i>"""
        replacementBlack = """<i class="ms ms-cost ms-b ms-shadow mana-size"></i>"""
        replacementRed = """<i class="ms ms-cost ms-r ms-shadow mana-size"></i>"""
        replacementBlue = """<i class="ms ms-cost ms-u ms-shadow mana-size"></i>"""
        replacement0 = """<i class="ms ms-cost ms-0 ms-shadow mana-size"></i>"""
        replacement1 = """<i class="ms ms-cost ms-1 ms-shadow mana-size"></i>"""
        replacement2 = """<i class="ms ms-cost ms-2 ms-shadow mana-size"></i>"""
        replacement3 = """<i class="ms ms-cost ms-3 ms-shadow mana-size"></i>"""
        replacement4 = """<i class="ms ms-cost ms-4 ms-shadow mana-size"></i>"""
        replacement5 = """<i class="ms ms-cost ms-5 ms-shadow mana-size"></i>"""
        replacement6 = """<i class="ms ms-cost ms-6 ms-shadow mana-size"></i>"""
        replacement7 = """<i class="ms ms-cost ms-7 ms-shadow mana-size"></i>"""
        replacement8 = """<i class="ms ms-cost ms-8 ms-shadow mana-size"></i>"""
        replacement9 = """<i class="ms ms-cost ms-9 ms-shadow mana-size"></i>"""
        replacementX = """<i class="ms ms-cost ms-x ms-shadow mana-size"></i>"""

        result = string.replace("{T}", replacementTap)
        result = result.replace("{C}", replacementColorLess)
        result = result.replace("{W}", replacementWhite)
        result = result.replace("{G}", replacementGreen)
        result = result.replace("{B}", replacementBlack)
        result = result.replace("{R}", replacementRed)
        result = result.replace("{U}", replacementBlue)
        result = result.replace("{0}", replacement0)
        result = result.replace("{1}", replacement1)
        result = result.replace("{2}", replacement2)
        result = result.replace("{3}", replacement3)
        result = result.replace("{4}", replacement4)
        result = result.replace("{5}", replacement5)
        result = result.replace("{6}", replacement6)
        result = result.replace("{7}", replacement7)
        result = result.replace("{8}", replacement8)
        result = result.replace("{9}", replacement9)
        result = result.replace("{X}", replacementX)
        return result 

    def replaceManaAndSymbolsLarge(string):
        replacementTap = """<i class="ms ms-cost ms-tap ms-shadow mana-size-large"></i>"""
        replacementColorLess = """<i class="ms ms-c ms-cost ms-shadow mana-size-large"></i>"""
        replacementWhite = """<i class="ms ms-cost ms-w ms-shadow mana-size-large"></i>"""
        replacementGreen = """<i class="ms ms-cost ms-g ms-shadow mana-size-large"></i>"""
        replacementBlack = """<i class="ms ms-cost ms-b ms-shadow mana-size-large"></i>"""
        replacementRed = """<i class="ms ms-cost ms-r ms-shadow mana-size-large"></i>"""
        replacementBlue = """<i class="ms ms-cost ms-u ms-shadow mana-size-large"></i>"""
        replacement0 = """<i class="ms ms-cost ms-0 ms-shadow mana-size-large"></i>"""
        replacement1 = """<i class="ms ms-cost ms-1 ms-shadow mana-size-large"></i>"""
        replacement2 = """<i class="ms ms-cost ms-2 ms-shadow mana-size-large"></i>"""
        replacement3 = """<i class="ms ms-cost ms-3 ms-shadow mana-size-large"></i>"""
        replacement4 = """<i class="ms ms-cost ms-4 ms-shadow mana-size-large"></i>"""
        replacement5 = """<i class="ms ms-cost ms-5 ms-shadow mana-size-large"></i>"""
        replacement6 = """<i class="ms ms-cost ms-6 ms-shadow mana-size-large"></i>"""
        replacement7 = """<i class="ms ms-cost ms-7 ms-shadow mana-size-large"></i>"""
        replacement8 = """<i class="ms ms-cost ms-8 ms-shadow mana-size-large"></i>"""
        replacement9 = """<i class="ms ms-cost ms-9 ms-shadow mana-size-large"></i>"""
        replacementX = """<i class="ms ms-cost ms-x ms-shadow mana-size-large"></i>"""

        result = string.replace("{T}", replacementTap)
        result = result.replace("{C}", replacementColorLess)
        result = result.replace("{W}", replacementWhite)
        result = result.replace("{G}", replacementGreen)
        result = result.replace("{B}", replacementBlack)
        result = result.replace("{R}", replacementRed)
        result = result.replace("{U}", replacementBlue)
        result = result.replace("{0}", replacement0)
        result = result.replace("{1}", replacement1)
        result = result.replace("{2}", replacement2)
        result = result.replace("{3}", replacement3)
        result = result.replace("{4}", replacement4)
        result = result.replace("{5}", replacement5)
        result = result.replace("{6}", replacement6)
        result = result.replace("{7}", replacement7)
        result = result.replace("{8}", replacement8)
        result = result.replace("{9}", replacement9)
        result = result.replace("{X}", replacementX)
        return result 
    
    
    def get_mana_cost_object(mana_cost):
        segments = list(filter(bool, re.split(r'(?<=})|(?={)', mana_cost)))
        clean_segments = [segment.replace('{', '').replace('}', '').lower() for segment in segments]
        html_output = '<span>'
        for index, cost in enumerate(clean_segments):
            html_output += f'<i key="cost-index{index}" class="ms ms-cost ms-{cost} ms-shadow"></i>'
        html_output += '</span>'
        print(Markup(html_output))
        return Markup(html_output)
    
    def trimImage(image):
        bg = Image.new(image.mode, image.size, image.getpixel((0,0)))
        diff = ImageChops.difference(image, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return image.crop(bbox)
