# Camera Import Feature

This document describes the new camera import functionality added to UkiyoeFusion.

## Overview

The camera import feature allows users to capture photos directly within the application instead of having to upload existing files. This is particularly useful for:

- Quick transformations of real-world objects or scenes
- Mobile users who want to take photos on the spot
- Testing the Ukiyo-e transformation with immediate visual feedback

## Features

### Camera Access

- Automatically requests camera permissions when "Take Photo" button is clicked
- Handles permission errors gracefully with user-friendly error messages
- Uses the device's back camera by default (better for capturing objects/scenes)

### Camera Controls

- **Switch Camera**: Toggle between front and back cameras (if available)
- **High Quality**: Captures at 1280x720 resolution by default
- **Mobile Optimized**: Uses `playsInline` and proper video constraints for mobile devices

### User Interface

- **Modal Dialog**: Camera interface opens in a clean modal dialog
- **Live Preview**: Real-time video preview before capturing
- **Capture Button**: Large, prominent button to take the photo
- **Close/Cancel**: Easy to close the camera without taking a photo

## Technical Implementation

### Browser Compatibility

- Uses `navigator.mediaDevices.getUserMedia()` API
- Requires HTTPS in production (browsers block camera access on HTTP)
- Fallback error handling for unsupported browsers

### Image Processing

- Captures images as JPEG with 80% quality for optimal file size
- Converts to base64 data URL for immediate processing
- Maintains aspect ratio and original resolution

### Camera Constraints

```javascript
{
  video: {
    width: { ideal: 1280 },
    height: { ideal: 720 },
    facingMode: 'environment' // or 'user' for front camera
  }
}
```

## Usage Instructions

1. **Access Camera**: Click the "Take Photo" button in the image upload area
2. **Grant Permissions**: Allow camera access when prompted by the browser
3. **Position Subject**: Frame your subject in the camera preview
4. **Switch Camera** (optional): Use the switch button to toggle between cameras
5. **Capture**: Click "Capture Photo" to take the picture
6. **Automatic Processing**: The captured image is immediately ready for transformation

## Browser Requirements

- **Chrome**: Version 53+
- **Firefox**: Version 36+
- **Safari**: Version 11+
- **Edge**: Version 12+

## Security Considerations

- Camera access requires user permission
- No images are stored on servers during capture
- Camera stream is properly terminated when dialog is closed
- Works only on HTTPS in production environments

## Mobile Considerations

- Responsive design adapts to smaller screens
- Touch-friendly button sizes
- Proper handling of device orientation
- Battery-efficient video streaming

## Error Handling

The feature includes comprehensive error handling for:

- Camera permission denied
- No camera available
- Camera already in use by another application
- Browser compatibility issues

## Future Enhancements

Potential improvements for future versions:

- Manual focus controls
- Flash/torch toggle
- Image resolution selection
- Multiple photo capture
- Basic image filters before transformation
