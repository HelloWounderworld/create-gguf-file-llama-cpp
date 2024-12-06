# Create GGUF file using Llama CPP
This project is aim to create gguf file to make possible its utilization to the ollama framework.

## Step by Step to create

    docker compose up -d --build

    docker compose ps

    docker ps | grep <container name>

    docker exec -it <container id> /bin/bash

    huggingface-cli --help

    huggingface-cli login

    python modelfile_download.py

    python testing_cuda_gpu.py

    GGML_CUDA=1 make

    git git@github.com:ggerganov/llama.cpp.git

    pip install -r requirements/requirements-convert-hf-to-gguf.txt

    python llama.cpp/convert_hf_to_gguf.py ./modelfile --outtype q8_0 --outfile ./name-fine-tuned-llm.gguf
