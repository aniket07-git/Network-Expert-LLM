
tune validate configs/1B_qlora_single_device_custom.yaml

tune run lora_finetune_single_device --config configs/llama_instruction_tune.yaml
