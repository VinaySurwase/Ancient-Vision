# 🎨 UkiyoeFusion - Quick Start Guide

## What is UkiyoeFusion?

UkiyoeFusion is a powerful image-to-image transformation application that uses AI (Stable Diffusion) to transform your images into different artistic styles. Simply upload an image, describe how you want to transform it, choose a style, and let AI do the magic!

## 🚀 Quick Start (One Command)

```bash
git clone <your-repo>
cd UkiyoeFusion
./run.sh
```

That's it! The script will:

- Check prerequisites (Python, Node.js)
- Set up virtual environment
- Install all dependencies
- Start both backend and frontend servers
- Open the app in your browser

## 🎯 Features

### Core Features

- **Image-to-Image Transformation**: Upload any image and transform it with AI
- **Multiple AI Models**: Switch between different Stable Diffusion models
- **8 Art Styles**: Realistic, Anime, Oil Painting, Watercolor, Cyberpunk, Fantasy, Vintage, Minimalist
- **Custom Prompts**: Add your own transformation descriptions
- **Real-time Settings**: Adjust strength, guidance, and quality on the fly
- **Custom Models**: Easy support for your own trained models

### Advanced Features

- **Advanced Settings**: Fine-tune transformation strength, guidance scale, and inference steps
- **Model Management**: Built-in tools to download and manage AI models
- **GPU Acceleration**: Automatic GPU detection and optimization
- **High Quality**: Support for high-resolution image processing
- **Download Results**: Save your transformed images locally

## 🛠️ Manual Setup (if needed)

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm
- (Optional) NVIDIA GPU with CUDA for faster processing

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone <your-repo>
   cd UkiyoeFusion
   ```

2. **Run setup script**

   ```bash
   ./setup.sh
   ```

3. **Start the application**

   ```bash
   ./run.sh
   ```

4. **Open in browser**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

## 📱 How to Use

1. **Upload Image**: Drag and drop or click to select an image
2. **Choose Model**: Select from available AI models
3. **Pick Style**: Choose from 8 predefined art styles
4. **Add Prompt**: Describe your desired transformation
5. **Adjust Settings**: (Optional) Fine-tune advanced parameters
6. **Transform**: Click "Transform Image" and wait for AI magic
7. **Download**: Save your transformed image

## 🤖 Adding Custom Models

### Using the Model Manager

```bash
./scripts/model_manager.sh download username/model-name
```

### Manual Addition

1. Create folder in `models/` directory
2. Add your model files (must include `model_index.json`)
3. Restart the application
4. Your model will appear in the dropdown

## 🔧 Troubleshooting

### Common Issues

- **"No GPU available"**: App works on CPU but will be slower
- **"Model not loading"**: Check internet connection for online models
- **"Out of memory"**: Reduce image size or use smaller model
- **"Port already in use"**: Stop other applications using ports 3000/5000

### Getting Help

1. Check the logs in the terminal
2. Verify all dependencies are installed
3. Run the test script: `./scripts/test_api.sh`
4. Check system requirements

## 📊 System Requirements

### Minimum

- 8GB RAM
- 2GB free disk space
- Python 3.8+
- Node.js 14+

### Recommended

- 16GB+ RAM
- NVIDIA GPU with 8GB+ VRAM
- SSD storage
- Fast internet (for downloading models)

## 🎨 Tips for Best Results

1. **Use clear, descriptive prompts**: "Transform into an oil painting with vibrant colors"
2. **Experiment with strength**: Lower values (0.3-0.5) for subtle changes, higher (0.7-0.9) for dramatic transformations
3. **Try different styles**: Each style has its own character
4. **Quality vs Speed**: More inference steps = better quality but slower processing
5. **Image size**: Larger images take more time and memory

## 🚀 Production Deployment

### Using Docker

```bash
docker-compose up -d
```

### Manual Production Setup

1. Build frontend: `cd frontend && npm run build`
2. Set `FLASK_ENV=production`
3. Use a production WSGI server like Gunicorn
4. Configure reverse proxy (nginx)

## 📝 API Documentation

The app includes a REST API for developers:

- `POST /api/transform` - Transform an image
- `GET /api/models` - List available models
- `GET /api/styles` - List available styles
- `GET /api/health` - Health check

## 🎯 What Makes UkiyoeFusion Special

- **No Authentication Required**: Jump straight into creating
- **Real-time Model Switching**: Change AI models without restarting
- **Custom Model Support**: Use your own trained models easily
- **Beautiful UI**: Clean, intuitive interface built with Material-UI
- **One-Click Setup**: Everything automated for easy deployment
- **Developer Friendly**: Well-documented API and code structure

Happy creating! 🎨✨
