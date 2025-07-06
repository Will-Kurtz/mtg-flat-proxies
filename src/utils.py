from markupsafe import Markup
from PIL import Image, ImageChops
import requests
from io import BytesIO
import argparse

class Utils:
    def str_to_bool(v):
        if v.lower() in ('yes', 'true', 't', '1', "True"):
            return True
        elif v.lower() in ('no', 'false', 'f', '0', "False"):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
        
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
        replacementWU = """<i class="ms ms-cost ms-wu ms-shadow mana-size"></i>"""
        replacementWB = """<i class="ms ms-cost ms-wb ms-shadow mana-size"></i>"""
        replacementUB = """<i class="ms ms-cost ms-ub ms-shadow mana-size"></i>"""
        replacementUR = """<i class="ms ms-cost ms-ur ms-shadow mana-size"></i>"""
        replacementBR = """<i class="ms ms-cost ms-br ms-shadow mana-size"></i>"""
        replacementBG = """<i class="ms ms-cost ms-bg ms-shadow mana-size"></i>"""
        replacementRG = """<i class="ms ms-cost ms-rg ms-shadow mana-size"></i>"""
        replacementRW = """<i class="ms ms-cost ms-rw ms-shadow mana-size"></i>"""
        replacementGW = """<i class="ms ms-cost ms-gw ms-shadow mana-size"></i>"""
        replacementGU = """<i class="ms ms-cost ms-gu ms-shadow mana-size"></i>"""
        replacementCW = """<i class="ms ms-cost ms-cw ms-shadow mana-size"></i>"""
        replacement2W = """<i class="ms ms-cost ms-2w ms-shadow mana-size"></i>"""
        replacementCU = """<i class="ms ms-cost ms-cu ms-shadow mana-size"></i>"""
        replacement2U = """<i class="ms ms-cost ms-2u ms-shadow mana-size"></i>"""
        replacementCB = """<i class="ms ms-cost ms-cb ms-shadow mana-size"></i>"""
        replacement2B = """<i class="ms ms-cost ms-2b ms-shadow mana-size"></i>"""
        replacementCR = """<i class="ms ms-cost ms-cr ms-shadow mana-size"></i>"""
        replacement2R = """<i class="ms ms-cost ms-2r ms-shadow mana-size"></i>"""
        replacementCG = """<i class="ms ms-cost ms-cg ms-shadow mana-size"></i>"""
        replacement2G = """<i class="ms ms-cost ms-2g ms-shadow mana-size"></i>"""
        replacementRGP = """<i class="ms ms-cost ms-rgp ms-shadow mana-size"></i>"""
        replacementGWP = """<i class="ms ms-cost ms-gwp ms-shadow mana-size"></i>"""
        replacementRWP = """<i class="ms ms-cost ms-rwp ms-shadow mana-size"></i>"""
        replacementGUP = """<i class="ms ms-cost ms-gbp ms-shadow mana-size"></i>"""
        
        #  Phyrexian Mana
        replacementWP = """<i class="ms ms-cost ms-wp ms-shadow mana-size"></i>"""
        replacementUP = """<i class="ms ms-cost ms-up ms-shadow mana-size"></i>"""
        replacementBP = """<i class="ms ms-cost ms-bp ms-shadow mana-size"></i>"""
        replacementRP = """<i class="ms ms-cost ms-rp ms-shadow mana-size"></i>"""
        replacementGP = """<i class="ms ms-cost ms-gp ms-shadow mana-size"></i>"""

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
        #Phyrexian mana
        result = result.replace("{W/P}", replacementWP)
        result = result.replace("{U/P}", replacementUP)
        result = result.replace("{B/P}", replacementBP)
        result = result.replace("{R/P}", replacementRP)
        result = result.replace("{G/P}", replacementGP)
        # Color Pairs
        result = result.replace("{W/U}", replacementWU)
        result = result.replace("{W/B}", replacementWB)
        result = result.replace("{U/B}", replacementUB)
        result = result.replace("{U/R}", replacementUR)
        result = result.replace("{B/R}", replacementBR)
        result = result.replace("{B/G}", replacementBG)
        result = result.replace("{R/G}", replacementRG)
        result = result.replace("{R/W}", replacementRW)
        result = result.replace("{G/W}", replacementGW)
        result = result.replace("{G/U}", replacementGU)
        # Monocolored
        result = result.replace("{2/W}", replacement2W)
        result = result.replace("{2/U}", replacement2U)
        result = result.replace("{2/B}", replacement2B)
        result = result.replace("{2/R}", replacement2R)
        result = result.replace("{2/G}", replacement2G)
        result = result.replace("{C/W}", replacementCW)
        result = result.replace("{C/U}", replacementCU)
        result = result.replace("{C/B}", replacementCB)
        result = result.replace("{C/R}", replacementCR)
        result = result.replace("{C/G}", replacementCG)
        # Dual Color Phyrexian
        result = result.replace("{R/G/P}", replacementRGP)
        result = result.replace("{G/W/P}", replacementGWP)
        result = result.replace("{R/W/P}", replacementRWP)
        result = result.replace("{G/U/P}", replacementGUP)
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
        replacementWU = """<i class="ms ms-cost ms-wu ms-shadow mana-size-large"></i>"""
        replacementWB = """<i class="ms ms-cost ms-wb ms-shadow mana-size-large"></i>"""
        replacementUB = """<i class="ms ms-cost ms-ub ms-shadow mana-size-large"></i>"""
        replacementUR = """<i class="ms ms-cost ms-ur ms-shadow mana-size-large"></i>"""
        replacementBR = """<i class="ms ms-cost ms-br ms-shadow mana-size-large"></i>"""
        replacementBG = """<i class="ms ms-cost ms-bg ms-shadow mana-size-large"></i>"""
        replacementRG = """<i class="ms ms-cost ms-rg ms-shadow mana-size-large"></i>"""
        replacementRW = """<i class="ms ms-cost ms-rw ms-shadow mana-size-large"></i>"""
        replacementGW = """<i class="ms ms-cost ms-gw ms-shadow mana-size-large"></i>"""
        replacementGU = """<i class="ms ms-cost ms-gu ms-shadow mana-size-large"></i>"""
        replacementCW = """<i class="ms ms-cost ms-cw ms-shadow mana-size-large"></i>"""
        replacement2W = """<i class="ms ms-cost ms-2w ms-shadow mana-size-large"></i>"""
        replacementCU = """<i class="ms ms-cost ms-cu ms-shadow mana-size-large"></i>"""
        replacement2U = """<i class="ms ms-cost ms-2u ms-shadow mana-size-large"></i>"""
        replacementCB = """<i class="ms ms-cost ms-cb ms-shadow mana-size-large"></i>"""
        replacement2B = """<i class="ms ms-cost ms-2b ms-shadow mana-size-large"></i>"""
        replacementCR = """<i class="ms ms-cost ms-cr ms-shadow mana-size-large"></i>"""
        replacement2R = """<i class="ms ms-cost ms-2r ms-shadow mana-size-large"></i>"""
        replacementCG = """<i class="ms ms-cost ms-cg ms-shadow mana-size-large"></i>"""
        replacement2G = """<i class="ms ms-cost ms-2g ms-shadow mana-size-large"></i>"""
        replacementRGP = """<i class="ms ms-cost ms-rgp ms-shadow mana-size-large"></i>"""
        replacementGWP = """<i class="ms ms-cost ms-gwp ms-shadow mana-size-large"></i>"""
        replacementRWP = """<i class="ms ms-cost ms-rwp ms-shadow mana-size-large"></i>"""
        replacementGUP = """<i class="ms ms-cost ms-gbp ms-shadow mana-size-large"></i>"""
        
        #  Phyrexian Mana
        replacementWP = """<i class="ms ms-cost ms-wp ms-shadow mana-size-large"></i>"""
        replacementUP = """<i class="ms ms-cost ms-up ms-shadow mana-size-large"></i>"""
        replacementBP = """<i class="ms ms-cost ms-bp ms-shadow mana-size-large"></i>"""
        replacementRP = """<i class="ms ms-cost ms-rp ms-shadow mana-size-large"></i>"""
        replacementGP = """<i class="ms ms-cost ms-gp ms-shadow mana-size-large"></i>"""

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
        #Phyrexian mana
        result = result.replace("{W/P}", replacementWP)
        result = result.replace("{U/P}", replacementUP)
        result = result.replace("{B/P}", replacementBP)
        result = result.replace("{R/P}", replacementRP)
        result = result.replace("{G/P}", replacementGP)
        # Color Pairs
        result = result.replace("{W/U}", replacementWU)
        result = result.replace("{W/B}", replacementWB)
        result = result.replace("{U/B}", replacementUB)
        result = result.replace("{U/R}", replacementUR)
        result = result.replace("{B/R}", replacementBR)
        result = result.replace("{B/G}", replacementBG)
        result = result.replace("{R/G}", replacementRG)
        result = result.replace("{R/W}", replacementRW)
        result = result.replace("{G/W}", replacementGW)
        result = result.replace("{G/U}", replacementGU)
        # Monocolored
        result = result.replace("{2/W}", replacement2W)
        result = result.replace("{2/U}", replacement2U)
        result = result.replace("{2/B}", replacement2B)
        result = result.replace("{2/R}", replacement2R)
        result = result.replace("{2/G}", replacement2G)
        result = result.replace("{C/W}", replacementCW)
        result = result.replace("{C/U}", replacementCU)
        result = result.replace("{C/B}", replacementCB)
        result = result.replace("{C/R}", replacementCR)
        result = result.replace("{C/G}", replacementCG)
        # Dual Color Phyrexian
        result = result.replace("{R/G/P}", replacementRGP)
        result = result.replace("{G/W/P}", replacementGWP)
        result = result.replace("{R/W/P}", replacementRWP)
        result = result.replace("{G/U/P}", replacementGUP)
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

    def save_strings_to_file(string_array, output_file):
        if len(string_array) <= 0:
            return
        try:
            with open(f"decklists/{output_file}.txt", 'w') as file:
                for string in string_array:
                    file.write(string + '\n')  # Adds a newline after each string
            print(f"Successfully saved strings to '{output_file}'")
        except Exception as e:
            print(f"Error saving to file: {e}")