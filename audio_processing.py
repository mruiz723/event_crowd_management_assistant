import librosa
from IPython.display import Audio, display
from openai import OpenAI
import uuid
import os
import numpy as np
from pydub import AudioSegment

class AudioProcessor:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)

    def voice_input_to_text(self, audio_path):
        """Transcribes an audio file using the Whisper model."""
        try:
            with open(audio_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text",
                    language="en"
                )
            return transcription  # Return only the transcribed text
        except FileNotFoundError:
            print(f"Error: Audio file not found at {audio_path}")
            return None
        except Exception as e:
            print(f"Error during transcription: {e}")
            return None

    def play_speech(self, file_path):
        """Plays an audio file."""
        try:
            data, rate = librosa.load(file_path)
            audio = Audio(data=data, rate=rate, autoplay=True)
            display(audio)
        except FileNotFoundError:
            print(f"Error: Audio file not found at {file_path}")
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    def text_to_voice(self, text, voice="alloy"):
        """Converts text to speech using the specified voice."""
        try:
            with self.client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice=voice,
                input=text    
            ) as response:
                speech_file_path = self._generate_unique_audio_path() 
                response.stream_to_file(speech_file_path)
                return speech_file_path
        except Exception as e:
            print(f"Error during text-to-speech conversion: {e}")
    
    def get_openai_response(self, query):
        """
        Queries the OpenAI API with the specified text and returns the response.

        Args:
            query: The text query to send to the OpenAI API.

        Returns:
            The text response from the OpenAI API, or None if an error occurs.
        """
        try:
            response = self.client.chat.completions.create(
                model = "gpt-4o",
                messages=[
                    { "role": "system", "content": "You are an event organizer. Please summarize the response in 50 words or less." },
                    { "role": "user", "content": query }
                ],
                #max_tokens = 100,  
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return None
    
    def save_audio(self, audio_input):
        """Saves raw audio to an MP3 file and returns the file path."""
        try:
            if isinstance(audio_input, tuple) and len(audio_input) == 2:
                sample_rate, audio_data = audio_input  # Extract data

                # Convert NumPy array to int16 format (required for pydub)
                audio_data = np.int16(audio_data)

                # Convert NumPy array to an AudioSegment
                audio_segment = AudioSegment(
                    audio_data.tobytes(), 
                    frame_rate=sample_rate, 
                    sample_width=2,  # 16-bit PCM
                    channels=1  # Mono audio
                )
                audio_path = self._generate_unique_audio_path()
                # Export as MP3
                audio_segment.export(audio_path, format="mp3")
                print(f"Audio saved at: {audio_path}")
                return audio_path
            else:
                raise ValueError("Invalid audio input format")
        except Exception as save_err:
            print(f"Error saving audio: {save_err}") 
            return None
        
    def get_audio_input_file(self, audio_input):
        print(f"type(audio_input): {type(audio_input)}")
        """Extracts only the file path from the Gradio audio input."""
        if isinstance(audio_input, tuple) and len(audio_input) == 2:
            print(f"audio_input[0]: {audio_input[0]}")
            print(f"audio_input[1]: {audio_input[1]}")
            audio_path = audio_input[0]  # Extract only the file path
            return audio_path
        return "Invalid audio input"
    
    def _generate_unique_audio_path(self):
        unique_id = uuid.uuid4()
        file_path = f"audios/audio-{unique_id}.mp3"
        return file_path


