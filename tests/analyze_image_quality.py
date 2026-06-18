#!/usr/bin/env python3
"""
Check the quality of the generated image to validate our fix for black results.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PIL import Image
import numpy as np

def analyze_image_quality():
    """Analyze the generated image to check if it has proper content"""
    try:
        # Load the generated image
        img = Image.open('test_quality_output.jpg')
        print(f"📐 Image size: {img.size}")
        print(f"🎨 Image mode: {img.mode}")
        
        # Convert to numpy array for analysis
        img_array = np.array(img)
        print(f"📊 Array shape: {img_array.shape}")
        
        # Get basic statistics
        mean_val = np.mean(img_array)
        std_val = np.std(img_array)
        min_val = np.min(img_array)
        max_val = np.max(img_array)
        
        print(f"📈 Statistics:")
        print(f"   Mean: {mean_val:.2f}")
        print(f"   Std: {std_val:.2f}") 
        print(f"   Min: {min_val}")
        print(f"   Max: {max_val}")
        
        # Check if image is mostly black (all values near 0)
        black_pixels = np.sum(img_array < 10)  # Very dark pixels
        total_pixels = img_array.size
        black_ratio = black_pixels / total_pixels
        
        print(f"⚫ Black analysis:")
        print(f"   Black pixels: {black_pixels:,}")
        print(f"   Total pixels: {total_pixels:,}")
        print(f"   Black ratio: {black_ratio:.3f}")
        
        # Check color distribution
        if len(img_array.shape) == 3:  # Color image
            r_mean = np.mean(img_array[:,:,0])
            g_mean = np.mean(img_array[:,:,1])
            b_mean = np.mean(img_array[:,:,2])
            print(f"🌈 Color channels:")
            print(f"   Red mean: {r_mean:.2f}")
            print(f"   Green mean: {g_mean:.2f}")
            print(f"   Blue mean: {b_mean:.2f}")
        
        # Determine if image has meaningful content
        is_black = black_ratio > 0.9  # More than 90% black
        is_low_variance = std_val < 5  # Very low variance
        is_empty = mean_val < 15 and std_val < 10  # Low mean and variance
        
        print(f"\n🔍 Quality Assessment:")
        print(f"   Is mostly black: {is_black}")
        print(f"   Is low variance: {is_low_variance}")
        print(f"   Is empty: {is_empty}")
        
        if is_black or is_empty:
            print("❌ RESULT: Image appears to be black/empty")
            print("🔧 This indicates the black result issue is NOT fixed")
            return False
        else:
            print("✅ RESULT: Image has meaningful content!")
            print("🎉 The black result issue appears to be FIXED!")
            return True
            
    except Exception as e:
        print(f"❌ Error analyzing image: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔬 IMAGE QUALITY ANALYSIS")
    print("=" * 60)
    
    success = analyze_image_quality()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 ANALYSIS: Generated image has proper content!")
        print("✅ BLACK RESULT ISSUE FIXED!")
    else:
        print("❌ ANALYSIS: Image quality issues detected")
        print("🔧 May need further parameter tuning")
    print("=" * 60)
