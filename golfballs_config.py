import os 

script_dir = os.path.dirname(os.path.abspath(__file__))

sku_to_image = {
    "UVPCCGNHBTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'golfballs', 'UVPCCGNHBTUVP.png'),
 }

sku_to_font = {
    "UVPCCGNHBTUVP": os.path.join(script_dir, 'fonts', 'AbhayaLibre.ttf'),
}

sku_to_fontsize_placement = {  # (font-size, x, y) 
    
    # Normal
    'UVPCCGNHBTUVP': {     
         1: (280, 920),  2: (280, 920),  3: (280, 920),  4: (280, 920),  5: (280, 920),  
         6: (280, 920),  7: (280, 920),  8: (280, 920),  9: (280, 920), 10: (280, 920),
        11: (270, 920), 12: (240, 930), 13: (220, 940), 14: (200, 950), 15: (200, 950),
    },
}

sku_to_second_fontsize_placement = { # (font-size, x, y)

        'UVPCCGNHBTUVP': {  # out of bounds   
         1: (0, 5000),  2: (0, 5000),  3: (0, 5000),  4: (0, 5000),  5: (0, 5000), 
         6: (0, 5000),  7: (0, 5000),  8: (0, 5000),  9: (0, 5000), 10: (0, 5000), 
        11: (0, 5000), 12: (0, 5000), 13: (0, 5000), 14: (0, 5000), 15: (0, 5000), 
        16: (0, 5000), 17: (0, 5000), 18: (0, 5000), 19: (0, 5000), 20: (0, 5000), 
        21: (0, 5000), 22: (0, 5000), 23: (0, 5000), 24: (0, 5000), 25: (0, 5000), 
        26: (0, 5000), 27: (0, 5000), 28: (0, 5000), 29: (0, 5000), 30: (0, 5000), 
    },
}

sku_to_third_fontsize_placement = {  # (font-size, x, y)
    
        'UVPCCGNHBTUVP': {  # out of bounds   
         1: (0, 5000),  2: (0, 5000),  3: (0, 5000),  4: (0, 5000),  5: (0, 5000), 
         6: (0, 5000),  7: (0, 5000),  8: (0, 5000),  9: (0, 5000), 10: (0, 5000), 
        11: (0, 5000), 12: (0, 5000), 13: (0, 5000), 14: (0, 5000), 15: (0, 5000), 
        16: (0, 5000), 17: (0, 5000), 18: (0, 5000), 19: (0, 5000), 20: (0, 5000), 
        21: (0, 5000), 22: (0, 5000), 23: (0, 5000), 24: (0, 5000), 25: (0, 5000), 
        26: (0, 5000), 27: (0, 5000), 28: (0, 5000), 29: (0, 5000), 30: (0, 5000), 

    },
}

sku_to_four_fontsize_placement = {  # (font-size, x, y)
            
        'UVPCCGNHBTUVP': {  # out of bounds   
         1: (0, None, 5000),  2: (0, None, 5000),  3: (0, None, 5000),  4: (0, None, 5000),  5: (0, None, 5000), 
         6: (0, None, 5000),  7: (0, None, 5000),  8: (0, None, 5000),  9: (0, None, 5000), 10: (0, None, 5000), 
        11: (0, None, 5000), 12: (0, None, 5000), 13: (0, None, 5000), 14: (0, None, 5000), 15: (0, None, 5000), 
        16: (0, None, 5000), 17: (0, None, 5000), 18: (0, None, 5000), 19: (0, None, 5000), 20: (0, None, 5000), 
        21: (0, None, 5000), 22: (0, None, 5000), 23: (0, None, 5000), 24: (0, None, 5000), 25: (0, None, 5000), 
        26: (0, None, 5000), 27: (0, None, 5000), 28: (0, None, 5000), 29: (0, None, 5000), 30: (0, None, 5000), 

    },
}