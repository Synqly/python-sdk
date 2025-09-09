#!/bin/bash

# Setup script for Synqly Organization Webhook Demo
echo "🚀 Setting up Synqly Organization Webhook Demo"
echo "=============================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found. Please install Python 3."
    exit 1
fi

echo "✅ Python 3 found"

# Check if pip is available
if ! command -v pip3 &> /dev/null && ! python3 -m pip --version &> /dev/null; then
    echo "❌ pip is required but not found. Please install pip."
    exit 1
fi

echo "✅ pip found"

# Install required packages
echo ""
echo "📦 Installing required packages..."
echo "   Installing Flask..."
python3 -m pip install flask

echo "   Installing pyngrok..."
python3 -m pip install pyngrok

echo ""
echo "✅ Dependencies installed successfully!"

# Check for ngrok
if ! command -v ngrok &> /dev/null; then
    echo ""
    echo "⚠️  ngrok not found. Please install ngrok:"
    echo "   macOS: brew install ngrok/ngrok/ngrok"
    echo "   Or download from: https://ngrok.com/download"
    echo ""
    echo "   After installation, authenticate with:"
    echo "   ngrok authtoken YOUR_NGROK_AUTH_TOKEN"
    echo "   (Get token from: https://dashboard.ngrok.com/get-started/your-authtoken)"
else
    echo "✅ ngrok found"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your Synqly organization token:"
echo "   export SYNQLY_ORG_TOKEN='your-token-here'"
echo ""
echo "2. If not already done, authenticate ngrok:"
echo "   ngrok authtoken YOUR_NGROK_AUTH_TOKEN"
echo ""
echo "3. Run the webhook demo:"
echo "   python3 webhook_example.py"
