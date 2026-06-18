#!/usr/bin/env python3
"""
Test script for ControlNet integration with UkiyoeFusion
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import base64
import json
from PIL import Image
import io

def test_controlnet_api():
    """Test the ControlNet API endpoints"""
    
    # Test base API
    try:
        response = requests.get('http://localhost:5001/api/controlnet')
        if response.status_code == 200:
            data = response.json()
            print("✓ ControlNet API endpoint working")
            print("Available ControlNet options:")
            for name, info in data.get('controlnet_options', {}).items():
                status = "✓" if info['available'] else "✗"
                print(f"  {status} {info['name']}: {info['description']}")
        else:
            print(f"✗ ControlNet API failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Error testing ControlNet API: {e}")

def test_image_transformation():
    """Test image transformation with ControlNet"""
    
    # Create a simple test image
    test_image = Image.new('RGB', (512, 512), color='white')
    
    # Add some basic shapes for ControlNet to detect
    from PIL import ImageDraw
    draw = ImageDraw.Draw(test_image)
    draw.rectangle([100, 100, 400, 400], outline='black', width=5)
    draw.ellipse([200, 200, 300, 300], outline='red', width=3)
    
    # Convert to base64
    buffer = io.BytesIO()
    test_image.save(buffer, format='PNG')
    buffer.seek(0)
    image_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Test without ControlNet
    test_data = {
        'image': f'data:image/png;base64,{image_b64}',
        'prompt': 'mountain temple',
        'style': 'classic_ukiyo',
        'strength': 0.75,
        'guidance_scale': 8.5,
        'num_inference_steps': 10  # Reduced for testing
    }
    
    try:
        print("\nTesting transformation without ControlNet...")
        response = requests.post('http://localhost:5001/api/transform', 
                               json=test_data, 
                               headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✓ Basic transformation successful")
            else:
                print(f"✗ Transformation failed: {result.get('error')}")
        else:
            print(f"✗ API call failed: {response.status_code}")
            
    except Exception as e:
        print(f"✗ Error testing transformation: {e}")
    
    # Test with ControlNet (if available)
    test_data_controlnet = test_data.copy()
    test_data_controlnet.update({
        'control_type': 'canny',
        'controlnet_conditioning_scale': 1.0,
        'canny_low_threshold': 100,
        'canny_high_threshold': 200
    })
    
    try:
        print("\nTesting transformation with Canny ControlNet...")
        response = requests.post('http://localhost:5001/api/transform', 
                               json=test_data_controlnet, 
                               headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✓ ControlNet transformation successful")
                print(f"  Used ControlNet: {result.get('controlnet_used', 'None')}")
            else:
                print(f"✗ ControlNet transformation failed: {result.get('error')}")
        else:
            print(f"✗ ControlNet API call failed: {response.status_code}")
            
    except Exception as e:
        print(f"✗ Error testing ControlNet transformation: {e}")

if __name__ == "__main__":
    print("🎨 Testing UkiyoeFusion ControlNet Integration")
    print("=" * 50)
    
    test_controlnet_api()
    test_image_transformation()
    
    print("\n" + "=" * 50)
    print("Test completed!")
