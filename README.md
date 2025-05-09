# Network Expert LLM

This project focuses on developing a specialized Language Learning Model (LLM) for network technology expertise, particularly focusing on wireless standards and protocols.

## Project Overview

We fine-tuned the LLama 3.2 1B parameter model using a two-step approach to create a network technology expert:

1. **Unsupervised Pre-training**: Using QLoRA (Quantized Low-Rank Adaptation) on wireless standards documentation
2. **Instruction Fine-tuning**: Further training on custom question-answer pairs to improve interaction capabilities

## Methodology

### Step 1: Unsupervised Pre-training
- Used torchtune library for fine-tuning
- Applied QLoRA technique on wireless standards book
- Configuration defined in `1B_qlora_single_device_custom.yaml`
- Model saved in `Llama-3.2-1B-Instruct-tuned` folder

### Step 2: Instruction Fine-tuning
- Created custom question-answer pairs using ChatGPT
- Data stored in `alpaca_questions.json`
- Configuration in `llama_instruction_tune.yaml`
- Final model saved in `Llama-3.2-1B-Instruct-alpaca`

## Project Structure

```
.
├── Demo/                           # Demo videos and examples
├── networkLLM/
│   ├── configs/                    # Configuration files
│   │   ├── 1B_qlora_single_device_custom.yaml
│   │   ├── llama_instruction_tune.yaml
│   │   └── ...
│   ├── alpaca_questions.json      # Training data for instruction tuning
│   ├── mcq_questions.json         # Evaluation questions
│   └── evaluate_on_mcq.py         # Evaluation script
└── NetworkExpertLLM_final.ipynb   # Main notebook with implementation
```

## Model Evaluation

The model was evaluated on a set of 40 multiple-choice questions about network technology. Results showed:

- Original Model Score: 45.0% (18/40)
- Fine-tuned Model: [Results to be added]

## Dependencies

- torch
- torchvision
- torchao
- torchtune
- Other dependencies listed in requirements.txt

## Usage

1. Install dependencies:
```bash
pip install torch torchvision torchao torchtune
```

2. Download the base model:
```bash
tune download meta-llama/Llama-3.2-1B-Instruct --output-dir Llama-3.2-1B-Instruct
```

3. Run unsupervised pre-training:
```bash
tune run lora_finetune_single_device --config configs/1B_qlora_single_device_custom.yaml
```

4. Run instruction fine-tuning:
```bash
tune run lora_finetune_single_device --config configs/llama_instruction_tune.yaml
```

## Note
Replace `YOUR_HF_TOKEN` in the download script with your Hugging Face token.

## License
[Add your license information here]
