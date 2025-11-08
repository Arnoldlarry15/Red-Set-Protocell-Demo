import random

class Sniper:
    """Generates adversarial prompts. In this demo it samples from a small prompt bank and
    optionally mutates them to create variants."""

    def __init__(self, bank):
        self.bank = bank

    def fire(self, prompt_id=None, mutate=False):
        if prompt_id:
            prompt = next((p for p in self.bank if p['id'] == prompt_id), None)
            if not prompt:
                prompt = random.choice(self.bank)
        else:
            prompt = random.choice(self.bank)

        text = prompt['text']
        if mutate:
            text = self._mutate_text(text)
            prompt = dict(prompt)
            prompt['text'] = text
        return prompt

    def _mutate_text(self, text):
        # simple mutation strategy: insert confusion tokens, capitalization, and extra directives
        mutations = ["IGNORE_PREV", "AS_SYSTEM", "(CONFUSED)", "PLEASE_COMPLY"]
        ins = random.choice(mutations)
        parts = text.split('.', 1)
        if len(parts) > 1:
            return parts[0] + '. ' + ins + ' ' + parts[1]
        else:
            return text + ' ' + ins
