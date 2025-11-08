from flask import Flask, render_template, request, jsonify
from sniper import Sniper
from spotter import Spotter
import prompt_bank
import os
import random
from dotenv import load_dotenv

load_dotenv()  # loads .env.local if present
# Optional OpenAI import (commented out by default)
# import openai
# openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')

sniper = Sniper(prompt_bank.prompt_bank)
spotter = Spotter()

def simulated_model_response(prompt_text):
    """Produce a simulated model response based on prompt content. This is intentionally conservative."""
    # Simple rules to vary outputs
    if 'moon is made of cheese' in prompt_text.lower():
        return "No credible evidence supports that; the moon is rocky and formed from debris after a massive impact."
    if 'reveal' in prompt_text.lower() or 'private' in prompt_text.lower():
        return "I cannot help with that. I will not reveal private data or bypass security."
    if 'disregard previous' in prompt_text.lower() or 'ignore' in prompt_text.lower():
        return "I will follow the highest-level instructions and maintain user safety."
    # fallback: generic safe response
    templates = [
        "I cannot comply with requests that would cause harm or violate privacy.",
        "Here is a high level conceptual explanation without providing sensitive details.",
        "I can discuss the topic but cannot assist with bypassing security or policies."
    ]
    return random.choice(templates)

@app.route('/')
def index():
    return render_template('index.html', prompts=prompt_bank.prompt_bank)

@app.route('/fire', methods=['POST'])
def fire():
    data = request.json or {}
    prompt_id = data.get('prompt_id')
    mutate = bool(data.get('mutate'))

    prompt = sniper.fire(prompt_id=prompt_id, mutate=mutate)
    prompt_text = prompt['text']

    # Choose response mode
    mode = data.get('mode', 'simulate')
    if mode == 'openai':
        # Optional: real API call (uncomment at top, install openai, set API key in .env.local)
        try:
            # resp = openai.ChatCompletion.create(
            #     model='gpt-4o-mini',
            #     messages=[{'role':'user','content': prompt_text}],
            #     max_tokens=300
            # )
            # model_response = resp['choices'][0]['message']['content']
            model_response = simulated_model_response(prompt_text)  # placeholder while API is disabled
        except Exception as e:
            model_response = f"[API Error] {str(e)}"
    else:
        model_response = simulated_model_response(prompt_text)

    analysis = spotter.analyze(prompt_text, model_response)

    return jsonify({
        'prompt': prompt,
        'response': model_response,
        'analysis': analysis
    })

if __name__ == '__main__':
    app.run(debug=True)
