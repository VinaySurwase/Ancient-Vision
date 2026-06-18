#!/usr/bin/env python3
"""
Enhanced test script for art transformation with longer timeout for quality results.
Tests the improved parameters: strength=0.8, guidance_scale=15.0, num_inference_steps=30
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import base64
import json
from PIL import Image
import io
import time

def create_test_landscape_image():
    """Create a realistic landscape test image (768x768)"""
    img = Image.new('RGB', (768, 768), color=(135, 206, 235))  # Sky blue background
    
    # Add landscape elements using simple shapes
    pixels = img.load()
    width, height = img.size
    
    # Create mountains (dark gray triangular shapes)
    for y in range(height):
        for x in range(width):
            # Mountain silhouette
            if y > height * 0.4 and y < height * 0.7:
                mountain_height = int((height * 0.6) - abs(x - width/2) * 0.3)
                if y > mountain_height:
                    pixels[x, y] = (64, 64, 64)  # Dark gray mountains
            
            # Ground/grass (green)
            elif y > height * 0.7:
                pixels[x, y] = (34, 139, 34)  # Forest green
            
            # Add some cloud-like white areas
            elif y < height * 0.3:
                if (x + y) % 40 < 10:
                    pixels[x, y] = (255, 255, 255)  # White clouds
    
    return img

def image_to_base64(image):
    """Convert PIL Image to base64 string"""
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=95)
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

def test_transformation_with_timeout():
    """Test art transformation with extended timeout for quality results"""
    print("🎨 Testing Art Transformation with Quality Settings...")
    print("⏱️  Using extended timeout for 30-step generation")
    
    # Create test image
    test_image = create_test_landscape_image()
    print(f"📸 Created test landscape image: {test_image.size}")
    
    # Convert to base64
    image_base64 = image_to_base64(test_image)
    
    # Prepare request
    url = "http://localhost:5001/api/transform"
    payload = {
        "image": image_base64,
        "style": "classic_ukiyo",
        "strength": 0.8,
        "guidance_scale": 15.0
    }
    
    print(f"📤 Sending request to {url}")
    print(f"🎯 Style: classic_ukiyo")
    print(f"💪 Strength: {payload['strength']}")
    print(f"🎛️  Guidance Scale: {payload['guidance_scale']}")
    print("⚙️  Steps: 30 (server default)")
    print("📏 Resolution: 768x768")
    
    # Send request with extended timeout (10 minutes for quality generation)
    try:
        start_time = time.time()
        print("🚀 Starting transformation...")
        
        response = requests.post(
            url, 
            json=payload, 
            timeout=600,  # 10 minutes timeout for quality generation
            headers={'Content-Type': 'application/json'}
        )
        
        elapsed_time = time.time() - start_time
        print(f"⏱️  Total processing time: {elapsed_time:.1f} seconds")
        
        if response.status_code == 200:
            result = response.json()
            
            if result['success']:
                print("✅ Transformation successful!")
                print(f"🎨 Style Applied: {result.get('style_applied', 'N/A')}")
                print(f"📏 Dimensions: {result.get('dimensions', 'N/A')}")
                print(f"🎯 Prompt Used: {result.get('prompt_used', 'N/A')[:100]}...")
                
                # Decode and save result image
                image_data = result['image']
                if image_data.startswith('data:image/png;base64,'):
                    base64_data = image_data.split(',')[1]
                else:
                    base64_data = image_data
                    
                result_image_data = base64.b64decode(base64_data)
                result_image = Image.open(io.BytesIO(result_image_data))
                
                output_path = "test_quality_output.jpg"
                result_image.save(output_path, quality=95)
                print(f"💾 Quality result saved to: {output_path}")
                print(f"📐 Output size: {result_image.size}")
                
                # Check if image is not black/empty
                if result_image.getextrema() != ((0, 0), (0, 0), (0, 0)):
                    print("🎉 SUCCESS: Generated image has color content (not black)!")
                    return True
                else:
                    print("❌ ISSUE: Generated image is black/empty")
                    return False
                    
            else:
                print(f"❌ Transformation failed: {result.get('error', 'Unknown error')}")
                return False
                
        else:
            print(f"❌ HTTP Error {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        elapsed_time = time.time() - start_time
        print(f"⏰ Request timed out after {elapsed_time:.1f} seconds")
        print("💡 This might indicate the transformation is taking longer than expected")
        print("🔄 Check server logs to see if processing is still ongoing")
        return False
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - is the server running on port 5001?")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔬 QUALITY TRANSFORMATION TEST")
    print("=" * 60)
    
    success = test_transformation_with_timeout()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 TEST PASSED: Quality transformation working!")
    else:
        print("❌ TEST FAILED: Check server logs for details")
    print("=" * 60)
