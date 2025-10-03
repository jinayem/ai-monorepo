# backend/scripts/torch_test.py
import torch
from transformers import pipeline

def main():
    print("✅ PyTorch version:", torch.__version__)
    x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    print("✅ Tensor test:", x)

    # Tiny model test (CPU-friendly)
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier("AI is amazing!")
    print("✅ Hugging Face pipeline result:", result)

if __name__ == "__main__":
    main()