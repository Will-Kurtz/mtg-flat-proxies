from PIL import Image
import numpy as np
import cv2
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../linedraw')))
import linedraw
import pygame

def clean_dithering(image_path, output_dir='temp'):
    """Process an image through the full Photoshop effects pipeline"""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Load original image
    print("Loading original image...")
    original = Image.open(image_path)
    original.save(f"{output_dir}/1_original.png")
    original_arr = np.array(original)
    
    # 2. Remove dither with median filter
    print("Removing dithering artifacts...")
    cleaned_arr = cv2.medianBlur(original_arr, 5)  # Kernel size 5 works well for most cases
    cleaned = Image.fromarray(cleaned_arr)
    cleaned.save(f"{output_dir}/1_cleaned_dither.png")
    
    # 3. Convert to black & white
    print("Converting to black and white...")
    bw = cleaned.convert('L')
    bw_arr = np.array(bw)
    bw.save(f"{output_dir}/2_black_white.png")
    
    # 4. Vectorize with 5 colors (K-means quantization)
    print("Vectorizing with 5 colors...")
    # Convert back to RGB for quantization
    rgb_arr = cv2.cvtColor(cleaned_arr, cv2.COLOR_RGB2BGR)
    bw_levels_arr = cv2.cvtColor(np.stack([bw_arr]*3, axis=2), cv2.COLOR_RGBA2BGR)
    pixels = rgb_arr.reshape((-1, 3)).astype(np.float32)
    
    # K-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 5
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    labels = labels.reshape(rgb_arr.shape[:2])
    # Define a custom black and white palette (as BGR format)
    bw_palette = np.array([
        
        [255, 255, 255],    # White
        [223, 223, 223],    # Light Gray
        [64, 64, 64],       # Dark Gray
        [0, 0, 0],           # Black
        [192, 192, 192],    # Gray
        
        
    ], dtype=np.uint8)
    # Create quantized image by mapping labels to palette
    quantized_bw = np.zeros_like(rgb_arr)
    for i in range(k):
        quantized_bw[labels == i] = bw_palette[i]
    cv2.imwrite(f"{output_dir}/3_quantized__bw_5colors.png", quantized_bw)
    
    return cleaned, bw, quantized_bw



if __name__ == '__main__':
    # Example usage
    input_image = 'renew.jpg'
    clean_dithering(input_image)
    linedraw.sketch("output/2_black_white.png")
    surface = pygame.image.load("output/out.svg")
    pygame.image.save(surface, "shrubbery.png")

class Test():
    def convertImageToLineArtPng(cardName):
        clean_dithering("temp/"+cardName+".png")
        # linedraw.sketch("temp/2_black_white.png")
        linedraw.sketch("temp/3_quantized__bw_5colors.png")
        surface = pygame.image.load("temp/out.svg")
        pygame.image.save(surface, "temp/"+cardName+"_lines.png")

        return
                            

    
