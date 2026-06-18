#!/usr/bin/env python3
"""Simple test for basic art transformation without ControlNet"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import base64
import json
from PIL import Image
import io

def create_simple_test_image():
    """Create a more realistic test image"""
    # Create a 768x768 test image with more interesting content
    img = Image.new('RGB', (768, 768), color='lightblue')
    
    # Add some simple shapes for testing transformation
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    
    # Create a landscape-like scene for better transformation testing
    # Sky gradient
    for y in range(200):
        intensity = int(135 + (y * 120 / 200))  # Gradient from light to darker blue
        draw.line([(0, y), (768, y)], fill=(intensity, intensity + 20, 255))
    
    # Ground
    draw.rectangle([0, 200, 768, 768], fill=(101, 67, 33))  # Brown ground
    
    # Simple mountain silhouettes
    mountain_points = [(0, 200), (200, 100), (400, 150), (600, 80), (768, 200)]
    draw.polygon(mountain_points, fill=(50, 50, 70))
    
    # Simple building/house
    draw.rectangle([300, 120, 450, 200], fill=(139, 90, 43))  # House body
    house_roof = [(280, 120), (375, 60), (470, 120)]
    draw.polygon(house_roof, fill=(160, 82, 45))  # Roof
    
    # Window
    draw.rectangle([320, 140, 360, 180], fill=(100, 100, 150))
    
    # Convert to base64
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_base64}"

def test_simple_transformation():
    """Test basic transformation without ControlNet"""
    print("🧪 Testing Simple Art Transformation (No ControlNet)...")
    
    # Create simple test image
    print("📷 Creating realistic test image (768x768)...")
    test_image = create_simple_test_image()
    
    # Prepare minimal transformation request
    # Prepare transformation request with proper settings for quality results
    payload = {
        "image": test_image,
        "prompt": "traditional portrait",
        "style": "classic_ukiyo",
        "strength": 0.8,  # Higher strength for better transformation
        "guidance_scale": 15.0,  # Higher guidance for stronger style
        "num_inference_steps": 30,  # More steps for better quality
        "model_id": "ukiyo_e_lora"
    }
    
    print("🚀 Sending minimal transformation request...")
    print(f"   - Style: {payload['style']}")
    print(f"   - Steps: {payload['num_inference_steps']}")
    print(f"   - Strength: {payload['strength']}")
    
    try:
        response = requests.post(
            "http://localhost:5001/api/transform",
            json=payload,
            timeout=120
        )
        
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get('success', False):
                print("✅ Basic transformation successful!")
                print(f"   - Style applied: {result.get('style_applied', 'N/A')}")
                return True
            else:
                print(f"❌ Transformation failed: {result.get('error', 'Unknown error')}")
                return False
                
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🎨 Simple Art Transformation Test")
    print("=" * 40)
    
    success = test_simple_transformation()
    
    print("\n" + "=" * 40)
    if success:
        print("✅ Basic model loading WORKS!")
    else:
        print("❌ Basic model loading FAILED")
