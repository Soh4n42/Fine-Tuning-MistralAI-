# 🏟️ Sports Headline Generator using Mistral-7B + LoRA

This project fine-tunes [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) using Low-Rank Adaptation (LoRA) to generate **catchy and realistic sports news headlines** from a simple instruction prompt.
The main aim of this project is to understand about the steps involved in fine tuning a llm models such as choosing a model, bits and bytes configuration, loading the model, tokenization, lora weight adaptation, training the model and inferencing to check the results
---

## 📦 Project Structure
.
├── data_collection/   # Scripts and data for scraping & preparing the dataset

│   ├── scrape.py                   # Script to scrape sports news headlines from the web
│   ├── prompt_formatting.py        # Script to convert scraped data into prompt-response format
│   ├── train.txt                   # Raw headlines (optional intermediate file)
│   ├── train.json                  # Final training dataset in prompt-response JSON format

├── ft_mistral.ipynb               # Notebook to fine-tune Mistral-7B using LoRA (PEFT + TRL)

├── README.md                      # Project documentation with instructions and usage

├── pyproject.toml                 # Python dependencies and project metadata

├── .gitignore                     # Git ignored files (e.g., checkpoints, logs, cache)



---

## 📊 Dataset

You create a custom dataset of sports news headlines extracted from sources like:

- Espn
- Fox Sports
- BBC
- CNN

### 🔧 Format: `train.json`

```json
{"prompt": "Generate a sports news headline.", "response": "Spain begin Euro 2025 campaign by thrashing Portugal"}
{"prompt": "Generate a sports news headline.", "response": "Can Raducanu bridge gap to world's best Sabalenka?"}
```


🧠 Model & Training
✅ Base model: mistralai/Mistral-7B-Instruct-v0.1

✅ Quantization: 4-bit using bitsandbytes

✅ PEFT: LoRA for memory-efficient fine-tuning

✅ Frameworks: transformers, trl, peft, datasets

🏋️ Training Objective
To teach the model to generate well-formed, realistic headlines from a fixed instruction prompt.


### 🔍 Inference Example

```python
from transformers import pipeline

generator = pipeline("text-generation", model="your-model", tokenizer="your-tokenizer")

prompt = "Generate a sports news headline."
output = generator(prompt, max_new_tokens=30)
print(output[0]["generated_text"])

