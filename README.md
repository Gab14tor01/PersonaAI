# PersonaAI

Um assistente de voz em Python inspirado em conceitos de Black Mirror, capaz de interagir com o usuário através de diferentes “personas”, utilizando reconhecimento de fala, síntese de voz e memória contextual.

---

## Sobre o projeto

O **PersonaAI** simula uma “consciência digital”, permitindo que o usuário converse com versões diferentes de si mesmo — como um crítico, racional, ideal ou pessimista.

A interação acontece por voz: o usuário fala, o sistema transcreve, processa e responde também em áudio.

Atualmente, o projeto utiliza lógica local para simular respostas com base em diferentes personas, sem dependência de APIs externas.

---

## Tecnologias utilizadas

- Python  
- Whisper (reconhecimento de voz)  
- gTTS (síntese de fala)  
- SoundDevice (captura de áudio)  

---

## Funcionalidades

- Conversa por voz com o usuário  
- Transcrição automática de áudio  
- Sistema de personas (crítico, racional, ideal, pessimista)  
- Memória contextual das últimas interações  
- Reset de memória durante execução  
- Respostas em áudio  

---

## Conceito

O projeto explora a ideia de identidade digital e auto-reflexão, simulando como diferentes “versões” de uma pessoa poderiam responder às mesmas situações.
python src/main.py
Inspirado em narrativas de tecnologia e consciência artificial.

---

## Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/Gab14tor01/PersonaAI.git
cd PersonaAI
