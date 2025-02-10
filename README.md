# Event Crowd Management Assistant

## 📌 Project Overview

This project provides a Python-based Event Crowd Management Assistant. It analyzes images to estimate crowd density and generates images using AI.  In addition to image processing and crowd analysis via the OpenAI API, this application also features an interactive voice interface. Users can record audio, which is then transcribed into a text-based question. This question is processed, and the system's text response is then converted to speech using Text-to-Speech (TTS) functionality, providing an audio response to the user.

## 🚀 Features

*   **Intelligent Crowd Analysis:**  Accurately estimates crowd density in images and provides alerts based on user-defined thresholds, enabling proactive event management.
*   **Flexible Image Input:** Supports a wide range of image sources, including local file paths, base64 encoded strings, URLs, and direct image objects, offering seamless integration with various systems.
*   **AI-Powered Image Generation:** Leverages OpenAI's DALL-E model to generate custom images from text prompts, facilitating creative content generation and visualization.
*   **Efficient Image Management:**  Automatically saves processed images locally with unique, timestamped filenames for easy organization and retrieval.
*   **Interactive Voice Interface:** Enables hands-free interaction through voice commands. Users can record audio queries, which are transcribed, processed, and responded to via text-to-speech, enhancing accessibility and convenience.

## 🛠️ Setup Instructions

This guide provides step-by-step instructions for setting up the Event Crowd Management Assistant.

### 1️⃣ **System Dependencies**

Before proceeding, ensure you have the following system dependencies installed:

*   **Python:** Version 3.12.7 is recommended.  Use a version manager like `pyenv` (recommended) to manage multiple Python versions. See the Python Version Management section below for details.
*   **FFmpeg:** Required for audio processing.

    *   **macOS (Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    *   **Linux (apt):**
        ```bash
        sudo apt-get update
        sudo apt-get install ffmpeg
        ```
    *   **Linux (yum):**
        ```bash
        sudo yum install ffmpeg
        ```
    *   **Windows:** Download the appropriate FFmpeg build from a reputable source (e.g., gyan.dev/ffmpeg/) and add the `bin` directory to your system's PATH environment variable.  See the Windows PATH Setup section below for details.

Windows PATH Setup (for FFmpeg):
1. Download the FFmpeg build.
2. Extract the archive.
3. Locate the bin directory within the extracted folder.
4. Search for "environment variables" in the Windows search bar.
5. Click on "Edit the system environment variables."
6. Click "Environment Variables..."
7. Under "System variables," select "Path" and click "Edit..."
8. Click "New" and add the full path to the FFmpeg bin directory.
9. Click "OK" on all dialog boxes to save the changes.
10. Restart your terminal or VS Code for the changes to take effect.

### 2️⃣ **Python Version Management (Recommended)**

Using `pyenv` is highly recommended for managing Python versions.

*   **Install pyenv:** Follow the instructions on the pyenv GitHub page: [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
*   **Install Python 3.12.x:**
    ```bash
    pyenv install 3.12.7  # Or your preferred 3.12.x version
    ```
*   **Set Local Python Version:**
    ```bash
    pyenv local 3.12.7
    pyenv rehash  # Important!
    ```

### 3️⃣ **Clone the Repository**

```bash
git clone git@github.com:mruiz723/event_crowd_management_assistant.git
cd event_crowd_management_assistant
```

### 4️⃣ **Activate the Virtual Environment**

python -m venv .venv  # Ensure Python 3.12 is selected (see above)

```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```

### 6️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 7️⃣ **Set Up OpenAI API Key**

Create a .env file in the project root directory and add your API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

### 8️⃣ **Run the Application**

Open `event_crowd_management_assistant.ipynb` in VS Code or Jupyter Lab.  

Make sure the correct Python interpreter (from your virtual environment) is selected in VS Code.

## 🎮 Usage see the Demo Video 📹

🔗 [Watch Demo](https://www.loom.com/share/edd708ebfc3240118b23c17b0a76ad87?sid=d1125763-8ff9-46ae-99eb-fa070c5b7215)

## 🔗 Important Links

*   **GitHub Repository:** [https://github.com/mruiz723/event_crowd_management_assistant](https://github.com/mruiz723/event_crowd_management_assistant)  *(Source Code)*
*   **Pyenv Repository:** [https://github.com/pyenv/pyenv/#installation] (https://github.com/pyenv/pyenv/#installation)


## 🛠️ Dependencies

- `Python 3.12`
- `See the requirements.txt`
- `ffmpeg`

## 👨‍💻 Author

**Marlon Ruiz Arroyave**

Feel free to contribute by creating issues or pull requests! 🚀

