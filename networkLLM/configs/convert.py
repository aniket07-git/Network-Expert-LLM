# from litgpt.scripts.download import convert_safetensors_file
from pathlib import Path
import torch

# def convert_safetensors_file(safetensor_path: Path) -> None:
#     from safetensors import SafetensorError
#     from safetensors.torch import load_file as safetensors_load

#     bin_path = safetensor_path.with_suffix(".bin")
#     # try:
#     result = safetensors_load(safetensor_path)
#     # except SafetensorError as e:
#     #     raise RuntimeError(f"{safetensor_path} is likely corrupted. Please try to re-download it.") from e
#     print(f"{safetensor_path} --> {bin_path}")
#     torch.save(result, bin_path)
#     try:
#         os.remove(safetensor_path)
#     except PermissionError:
#         print(
#             f"Unable to remove {safetensor_path} file. "
#             "This file is no longer needed and you may want to delete it manually to save disk space."
#         )

sf1 = "/home/ayadav/projects/llm/Llama-3.2-1B-Instruct-tuned/hf_model_0001_0.pt"
bin_path = "/home/ayadav/projects/llm/Llama-3.2-1B-Instruct-tuned/hf_model_0001_0.bin"
model = torch.load(sf1)
torch.save(model, bin_path)


# convert_safetensors_file(sf1)