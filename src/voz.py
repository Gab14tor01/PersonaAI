import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from gtts import gTTS
import os

# carregar modelo Whisper
model = whisper.load_model("base")

def gravar_audio(nome="input.wav", duracao=5, fs=44100):
    print("🎤 Gravando...")
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()
    write(nome, fs, audio)
    print("✅ Áudio gravado!")

def transcrever():
    resultado = model.transcribe("input.wav")
    return resultado["text"]

def falar(texto):
    tts = gTTS(text=texto, lang="pt")
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")  # Windows