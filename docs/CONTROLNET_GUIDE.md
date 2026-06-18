# ControlNet Integration with UkiyoeFusion

## Overview

UkiyoeFusion now supports ControlNet integration to provide structural guidance while maintaining the authentic Ukiyo-e artistic style. This allows you to preserve specific structural elements like edges, depth, and poses while applying the traditional Japanese woodblock print aesthetic.

## Features

### Supported ControlNet Models

1. **Canny Edge Detection**

   - Preserves edge structure and outlines
   - Best for: Architectural elements, object boundaries, geometric shapes
   - Parameters: Low/High thresholds for edge sensitivity

2. **Depth Estimation**

   - Maintains depth and spatial relationships
   - Best for: Landscapes, scenes with foreground/background separation
   - Automatic depth map generation

3. **Pose Detection**
   - Preserves human pose and body structure
   - Best for: Portrait work, figure studies, traditional poses
   - Detects key body joints and maintains pose structure

## API Usage

### New Endpoints

#### GET `/api/controlnet`

Returns available ControlNet options and their status.

**Response:**

```json
{
  "controlnet_options": {
    "canny": {
      "name": "Canny Edge Detection",
      "description": "Preserves edge structure and outlines",
      "available": true
    },
    "depth": {
      "name": "Depth Estimation",
      "description": "Maintains depth and spatial relationships",
      "available": true
    },
    "openpose": {
      "name": "Pose Detection",
      "description": "Preserves human pose and body structure",
      "available": false
    }
  }
}
```

### Enhanced Transform Endpoint

#### POST `/api/transform`

**New Parameters:**

- `control_type` (string, optional): Type of ControlNet guidance (`"canny"`, `"depth"`, `"openpose"`, or `null`)
- `controlnet_conditioning_scale` (float, optional): Strength of ControlNet influence (0.0-2.0, default: 1.0)
- `canny_low_threshold` (int, optional): Lower threshold for Canny edge detection (default: 100)
- `canny_high_threshold` (int, optional): Upper threshold for Canny edge detection (default: 200)

**Example Request:**

```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...",
  "prompt": "traditional Japanese temple, cherry blossoms",
  "style": "classic_ukiyo",
  "control_type": "canny",
  "controlnet_conditioning_scale": 1.0,
  "strength": 0.75,
  "guidance_scale": 8.5,
  "num_inference_steps": 25,
  "canny_low_threshold": 100,
  "canny_high_threshold": 200
}
```

## Frontend Usage

### ControlNet Selection

The UI now includes a ControlNet selection dropdown that allows users to choose:

- **None**: Pure style transfer without structural guidance
- **Canny Edge Detection**: Preserves edges and outlines
- **Depth Estimation**: Maintains spatial depth relationships
- **Pose Detection**: Preserves human poses and body structure

### Advanced Settings

When ControlNet is enabled, additional controls become available:

1. **ControlNet Strength**: Controls how strongly the structural guidance influences the generation

   - 0.0: No structural control
   - 1.0: Balanced control (recommended)
   - 2.0: Strong structural preservation

2. **Canny-specific Controls** (when Canny is selected):
   - **Low Threshold**: Sensitivity for weak edges (50-150)
   - **High Threshold**: Sensitivity for strong edges (150-300)

## Technical Implementation

### Model Architecture

```python
# ControlNet + LoRA Pipeline
pipeline = StableDiffusionControlNetImg2ImgPipeline.from_pretrained(
    "path/to/ukiyo_e_lora",  # Your trained LoRA model
    controlnet=controlnet_model,  # Selected ControlNet
    torch_dtype=torch.float16
)

# Image preprocessing for ControlNet
control_image = preprocess_controlnet_input(image, control_type)

# Generation with both style and structure control
result = pipeline(
    prompt=ukiyo_e_prompt,
    image=input_image,
    control_image=control_image,
    strength=0.75,
    controlnet_conditioning_scale=1.0
)
```

### Memory Optimization

- Models are loaded on-demand to conserve memory
- Automatic cleanup of unused pipelines
- Support for CPU, CUDA, and MPS devices
- Memory-efficient attention and VAE slicing

## Best Practices

### When to Use ControlNet

1. **Canny Edge Detection**:

   - Architectural photography → Ukiyo-e buildings/temples
   - Geometric compositions → Traditional patterns
   - Clear object boundaries → Defined artistic elements

2. **Depth Estimation**:

   - Landscape photography → Traditional Japanese scenery
   - Multi-layered compositions → Foreground/background separation
   - Spatial depth preservation → Traditional perspective

3. **Pose Detection**:
   - Portrait photography → Traditional figure studies
   - Human subjects → Kabuki poses, traditional stances
   - Action shots → Dynamic traditional poses

### Parameter Tuning

- **ControlNet Strength**: Start with 1.0, reduce for more artistic freedom
- **Canny Thresholds**: Lower values detect more edges, higher values only strong edges
- **Guidance Scale**: Keep at 8.5 for optimal Ukiyo-e style adherence
- **Strength**: 0.75 provides good balance between original and style

## Installation Requirements

Add these packages to your environment:

```bash
pip install controlnet-aux>=0.0.6
pip install xformers>=0.0.22  # For memory optimization
```

## Troubleshooting

### Common Issues

1. **ControlNet models not loading**: Check internet connection for model downloads
2. **Memory errors**: Reduce image size or use CPU mode
3. **Slow generation**: Reduce inference steps or use attention slicing
4. **Poor structural preservation**: Increase ControlNet conditioning scale

### Performance Tips

- Use CUDA if available for faster processing
- Enable xFormers for memory efficiency
- Cache ControlNet models after first load
- Process images at 512x512 for optimal speed/quality balance

## Example Results

With ControlNet integration, you can now:

- Transform architectural photos while preserving building structure
- Apply Ukiyo-e style to portraits while maintaining pose
- Convert landscapes while keeping depth relationships
- Maintain geometric patterns while applying traditional aesthetics

The combination of your trained Ukiyo-e LoRA with ControlNet provides the best of both worlds: authentic traditional Japanese art style with precise structural control.
