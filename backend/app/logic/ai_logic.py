import torch

def get_device():
    """Return GPU if available, otherwise CPU."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_dummy_inference(input_data: list):
    """
    Run a dummy model that just multiplies input tensor by 2.
    Simulates inference for now.
    """
    device = get_device()
    tensor = torch.tensor(input_data, dtype=torch.float32).to(device)
    result = tensor * 2 # Simple operation simulating model output
    return {
        "device": str(device),
        "input": input_data,
        "output": result.tolist(),
    }
