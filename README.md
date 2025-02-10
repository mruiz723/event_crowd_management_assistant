# Event Crowd Management Assistant

## 📌 Project Overview

This project provides a Python-based Event Crowd Management Assistant. It analyzes images to estimate crowd density and generates images using AI. The application utilizes OpenAI's API for image processing and crowd analysis.

## 🚀 Features

- **Crowd Detection & Analysis**: Estimates the number of people in an image and provides warnings based on a defined threshold.
- **Image Display & Processing**: Supports different image sources (file path, base64, URL, or direct image objects).
- **AI Image Generation**: Uses OpenAI's DALL-E model to generate images based on text prompts.
- **Image Saving & Management**: Saves processed images locally with unique filenames.

---

## 🛠️ Setup Instructions

### 1️⃣ **Clone the Repository**

```bash
git clone git@github.com:mruiz723/event_crowd_management_assistant.git
cd event_crowd_management_assistant
```

### 2️⃣ **Create a Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate  # MacOS/Linux
# or
.venv\Scripts\activate  # Windows
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up OpenAI API Key**

Create a `.env` file in the project root directory and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Alternatively, you can export it as an environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here  # MacOS/Linux
set OPENAI_API_KEY=your_api_key_here  # Windows
```

### 5️⃣ **Run the Application**

```bash
Open event_crowd_management_assistant.ipynb in vscode or jupyter lab
```

---

## 🎮 Usage see the Demo Video 📹

🔗 [Watch Demo](https://www.loom.com/share/edd708ebfc3240118b23c17b0a76ad87?sid=d1125763-8ff9-46ae-99eb-fa070c5b7215)

---

## 🛠️ Dependencies

- `Python 3.12`
- `See the requirements.txt`

---

## 👨‍💻 Author

**Marlon Ruiz Arroyave**

Feel free to contribute by creating issues or pull requests! 🚀

