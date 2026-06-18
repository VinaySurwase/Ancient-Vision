# Ancient Vision

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/react-18.0+-61dafb.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

> Transform any image into authentic traditional art styles—including Japanese Ukiyo-e and Indian folk/temple art—using state-of-the-art AI technology.

Ancient Vision bridges the gap between modern photography and traditional art, allowing users to experience the timeless beauty of both Japanese and Indian heritage styles through cutting-edge artificial intelligence.

## Features

### **Artistic Transformation**

- **Authentic Traditional Styles**: Transform images into Japanese Ukiyo-e and a wide range of Indian folk and temple art styles
- **ControlNet Integration**: Structural guidance while maintaining artistic style
  - **Canny Edge Detection**: Preserves edges and outlines (automatically applied)
  - **Depth Estimation**: Maintains spatial relationships and depth
  - **Pose Detection**: Preserves human poses and body structure
- **Smart Prompting**: Default prompt with optional user additions
  - Each style has a unique, culturally accurate prompt for best results
  - User prompts are appended to the default for enhanced results
- **Optimized Parameters**: Pre-configured settings for best results
  - Strength: 0.75
  - Guidance Scale: 8.5
  - Inference Steps: 25
  - Resolution: 512x512

#### Supported Art Styles

- **Japanese Ukiyo-e** (classic, landscape, portrait, nature, urban, seasonal)
- **Indian Traditional Styles:**
  - **Gond Art**: Tribal art with dot patterns, nature, and storytelling
  - **Kalighat Painting**: Bengali folk art, bold lines, mythological themes
  - **Kangra Miniature**: Himalayan miniature, delicate brushwork, court scenes
  - **Kerala Mural**: South Indian temple art, mythological scenes, vibrant colors
  - **Madhubani Art**: Bihar folk art, geometric designs, ritualistic motifs
  - **Mandana Art**: Rajasthani wall art, geometric and auspicious patterns
  - **Pichwai Painting**: Nathdwara temple art, Krishna themes, devotional motifs

### **Modern Input Methods**

- **File Upload**: Standard drag-and-drop or click-to-browse functionality
- **Real-time Camera Capture**:
  - Direct photo capture within the application
  - Front/back camera switching for mobile devices
  - High-definition capture (1280x720 resolution)
  - Mobile-first responsive design
  - Secure permission-based camera access

### **User Experience**

- **Intuitive Interface**: Clean, minimalist design focused on the art creation process
- **Instant Results**: Fast processing with optimized AI pipeline
- **Cross-platform**: Works seamlessly on desktop and mobile browsers

## Repository Structure

```text
Ancient-Vision/
├── docs/                   # Auxiliary documentation
├── frontend/               # React frontend application
├── models/                 # AI models and weights
├── modules/                # Core Python modules
├── notebooks/              # Jupyter notebooks for research
├── scripts/                # Utility scripts
├── tests/                  # Automated test scripts
├── app.py                  # Main Flask backend application
└── run.sh                  # Quickstart script
```

## Tech Stack

| Component            | Technology                     | Purpose                                     |
| -------------------- | ------------------------------ | ------------------------------------------- |
| **Backend**          | Flask + PyTorch                | AI model serving and API endpoints          |
| **Frontend**         | React + Material-UI            | Modern, responsive user interface           |
| **AI Models**        | Stable Diffusion + Custom LoRA | Traditional art style transformation engine |
| **ControlNet**       | Multiple ControlNet Models     | Structural guidance and preservation        |
| **Image Processing** | Canvas API + WebRTC            | Real-time camera capture and processing     |

## Quick Start

### Automated Setup (Recommended)

```bash

# Clone the repository
git clone https://github.com/VinaySurwase/Ancient-Vision.git
cd Ancient-Vision

# Make the run script executable and start everything
chmod +x run.sh
./run.sh
```

### Access Points

- **Frontend Application**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Documentation**: http://localhost:5000/docs

## Usage Guide

### Image Input Methods

#### Traditional Upload

1. Click **"Choose File"** or drag and drop images into the upload area
2. Supported formats: JPEG, PNG, WebP (max 10MB)

#### Camera Capture

1. Click **"Take Photo"** button
2. Grant camera permissions when prompted by your browser
3. Use the live preview to frame your subject
4. Toggle between front/back cameras using the switch button
5. Click **"Capture Photo"** to take the picture
6. Your image is immediately ready for transformation

### Transformation Workflow

1. **Select Input**: Upload a file or capture with camera
2. **Choose Model**: Select your art model (automatic detection of available models)
3. **Add Context** _(Optional)_: Provide additional descriptive prompts that will be added to the default prompt
4. **Configure Settings** _(Optional)_: Adjust advanced parameters if needed (strength, guidance scale, steps)
5. **Transform**: Click transform and let AI create your traditional artwork with automatic ControlNet guidance
6. **Download**: Save your traditional artwork

### Default Configuration

| Parameter       | Value                                                               | Purpose                                  |
| --------------- | ------------------------------------------------------------------- | ---------------------------------------- |
| **Base Prompt** | Each style has a unique, culturally accurate prompt (see below)     | Core traditional style definition        |
| **Negative**    | Each style has a negative prompt to avoid modern/realistic elements | Prevents unwanted modern elements        |
| **Strength**    | 0.75                                                                | Balance between original and transformed |
| **Guidance**    | 8.5                                                                 | Optimal prompt adherence for style       |
| **Steps**       | 25                                                                  | Fast processing with quality results     |
| **Resolution**  | 512x512                                                             | Optimized for model performance          |
| **ControlNet**  | Canny (0.8 strength)                                                | Automatic edge preservation              |

### Camera Feature Requirements

| Requirement      | Details                                      |
| ---------------- | -------------------------------------------- |
| **Protocol**     | HTTPS required in production environments    |
| **Permissions**  | User must explicitly grant camera access     |
| **Connectivity** | Active internet connection for AI processing |
| **Performance**  | Modern device with adequate processing power |

## Manual Setup

### Prerequisites

- Python 3.8 or higher
- Node.js 16.0 or higher
- npm or yarn package manager

### Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the Flask server
python app.py
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### Custom Models

```bash
# Add your custom models to the models directory
cp your_custom_model.safetensors models/
# Models are automatically detected and loaded
```

## API Reference

### Endpoints

| Method | Endpoint          | Description                          | Parameters                                      |
| ------ | ----------------- | ------------------------------------ | ----------------------------------------------- |
| `POST` | `/api/transform`  | Transform image to traditional style | `image`, `prompt`, `style`, `control_type`, etc |
| `GET`  | `/api/models`     | List available AI models             | None                                            |
| `GET`  | `/api/styles`     | List available art styles            | None                                            |
| `GET`  | `/api/controlnet` | List available ControlNet options    | None                                            |
| `GET`  | `/api/health`     | Service health check                 | None                                            |

### Example Request

```bash
curl -X POST http://localhost:5001/api/transform \
  -H "Content-Type: application/json" \
  -d '{
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...",
    "prompt": "lotus flowers, peacocks, or mythological scene",
    "style": "gond",  # or kalighat, kangra, kerala_mural, madhubani, mandana, pichwai, classic_ukiyo, etc.
    "control_type": "canny",
    "controlnet_conditioning_scale": 1.0,
    "strength": 0.75,
    "guidance_scale": 8.5,
    "num_inference_steps": 25
  }'
```

## Development

### Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### Testing

```bash
# Frontend tests
cd frontend
npm test

# Backend tests
python -m pytest tests/

# Run specific test file
npm test -- ImageUpload.test.js
```

### Code Quality

```bash
# Frontend linting
cd frontend
npm run lint

# Python code formatting
black .
flake8 .
```

## Security & Privacy

### Data Protection

- **No Server Storage**: Images are processed in memory and immediately discarded
- **Local Processing**: Camera captures remain on the client until transformation
- **Secure Transmission**: All API communications use HTTPS in production
- **Privacy First**: No user data collection or tracking

### Camera Security

- **Explicit Permissions**: Camera access requires user consent
- **Stream Management**: Automatic cleanup of camera streams after use
- **Browser Security**: Leverages native browser security for camera access
- **HTTPS Requirement**: Camera functionality requires secure connections in production


### Feature Support Notes

- **Camera switching** may be limited on some older mobile devices
- **HTTPS required** for camera access in all modern browsers
- **WebGL support** recommended for optimal performance

## Contributing

We welcome contributions from the community! Please follow these guidelines:

### Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
4. **Make** your changes
5. **Test** thoroughly
6. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
7. **Push** to your branch (`git push origin feature/amazing-feature`)
8. **Submit** a Pull Request

### Code Standards

- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass before submitting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Traditional Ukiyo-e artists who inspired this work
- The Stable Diffusion community for foundational AI models
- Contributors and testers who helped improve the application
- Japanese cultural preservation organizations

## 📞 Support

- **Documentation**: Check this README and inline code comments
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Community**: Join discussions in GitHub Discussions
- **Updates**: Watch the repository for latest releases and updates

---