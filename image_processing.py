# Standard Library Imports
import base64
from io import BytesIO
from enum import Enum
import os
import uuid

# Third-Party Imports
from openai import OpenAI
from PIL import Image
import matplotlib.pyplot as plt
from models.crowd_analysis import CrowdAnalysisResult
import requests

"""
    Crowd Detection and Analysis:
    Develop a Python function that accepts an image file or URL as input.
    Use an image analysis API to estimate the number of people in the image.
    Provide a warning if the space appears too crowded (you define the threshold).
"""

class ImageSource(Enum):
    IMAGE_OBJECT = 1
    FILE_PATH = 2
    BASE64_DATA = 3
    URL = 4 # Add URL as a source type

class ImageProcessor:
    def __init__(self, openai_api_key): 
        self.client = OpenAI(api_key=openai_api_key)  # Store the OpenAI client

    def _encode_image(self, image_path):  # "private" helper method (starts with _)
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
            return None
        except Exception as e:
            print(f"Error encoding image: {e}")
            return None
    
    def show_image(self, image_data, source_type: ImageSource):
        print(image_data)
        match source_type:
            case ImageSource.IMAGE_OBJECT:
                img = Image.open(BytesIO(image_data))
            case ImageSource.FILE_PATH:
                img = Image.open(image_data)
            case ImageSource.BASE64_DATA:
                img = Image.open(BytesIO(base64.b64decode(image_data)))
            case ImageSource.URL:
                response = requests.get(image_data, stream=True) # Stream for large files
                response.raise_for_status()  # Check for HTTP errors (4xx or 5xx)
                img = Image.open(BytesIO(response.content))
            case _:  # Handle unexpected source types
                print("Invalid image source type.")
                return
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    def save_image(self, image_input):
        """Saves a PIL Image object to a file and returns the file path."""
        try:
            image_path = self._generate_unique_image_path()
            image_input.save(image_path)
            return image_path
        except Exception as save_err:
            print(f"Error saving image: {save_err}") 
            return None
    
    def _generate_unique_image_path(self):
        unique_id = uuid.uuid4()
        file_path = f"images/image-{unique_id}.png"
        return file_path

    def analyze_crowd(self, image_path, threshold):
        prompt = f"""
            Analyze the attached image and estimate the number of people. Provide a warning either the space appears too crowded or not. 
            If threshold is not exceeded, provide a joke warning.
            Use a threshold of {threshold}.
        """

        base64_image = self._encode_image(image_path)
        if base64_image is None: # Handle if encoding fails
            return None

        try:
            response = self.client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=[
                    { "role": "system", "content": "You are an event organizer." },
                    {
                        "role": "user",
                        "content": [
                            { "type": "text", "text": prompt },
                            { "type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{base64_image}" } },
                        ],
                    }
                ],
                response_format = CrowdAnalysisResult,
            )

            choice = response.choices[0]
            # print(f"response parsed message: { choice.message.parsed.message }")
            return choice.message.parsed
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return None
    
    # Define a function to generate an image using DALL-E
    def generate_image(self, model: str, prompt, size, quality=None, style=None, response_format='url', n=1):
        # return "https://picsum.photos/id/237/200/300" For testing purposes
        params = {
            'model': model,
            'prompt': prompt,
            'size': size,
            'n': n,
            'response_format': response_format
        }
        if style:
            params['style'] = style
        if quality:
            params['quality'] = quality
        response = self.client.images.generate(**params)
        image_url = response.data[0].url
        # print(f"Generated image URL: {image_url}")
        # print(f"Generated image URL response: {response}")
        return image_url
