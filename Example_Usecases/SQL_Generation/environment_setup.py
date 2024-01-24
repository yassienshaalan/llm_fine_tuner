# environment_setup.py

import subprocess

def install_packages():
    packages = [
        "torch==2.1.2",
        "transformers==4.36.2",
        "datasets==2.16.1",
        "accelerate==0.26.1",
        "evaluate==0.4.1",
        "bitsandbytes==0.42.0",
        "flash-attn",
        "huggingface_hub"
    ]
    
    for package in packages:
        subprocess.run(["pip", "install", package])

if __name__ == "__main__":
    install_packages()
