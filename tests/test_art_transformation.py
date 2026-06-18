#!/usr/bin/env python3
"""Test script to verify art transformation model loading"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import base64
import json
from PIL import Image
import io

def create_test_image():
    """Create a simple test image"""
    # Create a simple 512x512 test image with a pattern
    img = Image.new('RGB', (512, 512), color='white')
    
    # Add some simple shapes for testing
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    
    # Draw a simple face-like pattern
    draw.ellipse([100, 100, 400, 400], fill='lightblue', outline='blue', width=3)
    draw.ellipse([150, 180, 200, 230], fill='black')  # Left eye
    draw.ellipse([300, 180, 350, 230], fill='black')  # Right eye
    draw.arc([200, 280, 300, 350], 0, 180, fill='red', width=5)  # Smile
    
    # Convert to base64
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_base64}"

def test_transformation():
    """Test art transformation with model loading"""
    print("🧪 Testing Art Transformation Model Loading...")
    
    # Create test image
    print("📷 Creating test image...")
    test_image = create_test_image()
    
    # Prepare transformation request with optimized settings for faster testing
    payload = {
        "image": test_image,
        "prompt": "simple portrait",
        "style": "classic_ukiyo",
        "strength": 0.6,  # Reduced for faster processing
        "guidance_scale": 8.0,  # Reduced for faster processing
        "num_inference_steps": 10,  # Much reduced for faster testing
        "model_id": "ukiyo_e_lora"
    }
    
    print("🚀 Sending transformation request...")
    print(f"   - Style: {payload['style']}")
    print(f"   - Model: {payload['model_id']}")
    print(f"   - Strength: {payload['strength']}")
    
    try:
        response = requests.post(
            "http://localhost:5001/api/transform",
            json=payload,
            timeout=300  # 5 minutes timeout for model loading and processing
        )
        
        print(f"📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Transformation successful!")
            print(f"   - Full response: {result}")
            print(f"   - Processing time: {result.get('processing_time', 'N/A')}")
            print(f"   - Style applied: {result.get('style_applied', 'N/A')}")
            print(f"   - Success flag: {result.get('success', 'N/A')}")
            
            # Check if we got a transformed image
            if 'image' in result and result.get('success', False):
                print("🎨 Transformed image received!")
                return True
            else:
                print("❌ No transformed image in response or transformation failed")
                return False
                
        else:
            print(f"❌ Transformation failed with status {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("⏰ Request timed out - model loading might be taking too long")
        return False
    except Exception as e:
        print(f"❌ Request failed: {str(e)}")
        return False

def test_health_after_transformation():
    """Check health status after transformation attempt"""
    print("\n🏥 Checking health status after transformation...")
    
    try:
        response = requests.get("http://localhost:5001/api/health")
        if response.status_code == 200:
            health = response.json()
            print(f"   - Current model: {health.get('current_model', 'None')}")
            print(f"   - Pipeline ready: {health.get('pipeline_ready', False)}")
            print(f"   - Models loaded: {health.get('models_loaded', False)}")
            print(f"   - ControlNet loaded: {health.get('controlnet_loaded', False)}")
            return health
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Health check error: {str(e)}")
        return None

if __name__ == "__main__":
    print("🎨 Art Transformation Model Loading Test")
    print("=" * 50)
    
    # Test transformation
    success = test_transformation()
    
    # Check health after
    health = test_health_after_transformation()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Model loading test PASSED - Art transformation is working!")
    else:
        print("❌ Model loading test FAILED - Issues detected")
        
    print("🔍 Check the Flask server logs for detailed information")
