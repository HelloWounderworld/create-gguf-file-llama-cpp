# Create GGUF file using Llama CPP
This project is aim to create gguf file to make possible its utilization to the ollama framework.

    https://huggingface.co/docs/transformers/main/gguf

    https://github.com/ggerganov/llama.cpp.git

    https://qiita.com/hudebakononaka/items/ca295eae60231d7d025f

    https://qiita.com/kyotoman/items/5d460708d798a6f26cf0

    https://www.reddit.com/r/LocalLLaMA/comments/1amjx77/how_to_convert_my_finetuned_model_to_gguf/?rdt=56046

    https://github.com/ggerganov/llama.cpp/discussions/4997

    https://github.com/ggerganov/llama.cpp/discussions/2948

    https://medium.com/@qdrddr/the-easiest-way-to-convert-a-model-to-gguf-and-quantize-91016e97c987

## Step by Step to create

    docker compose up -d --build

    docker compose ps

    docker ps | grep <container name>

    docker exec -it <container id> /bin/bash

    huggingface-cli --help

    huggingface-cli login

    python download_model.py

    python check.py

    python testing_cuda_gpu.py

    GGML_CUDA=1 make

    git git@github.com:ggerganov/llama.cpp.git

    pip install -r requirements/requirements-convert-hf-to-gguf.txt

    python llama.cpp/convert_hf_to_gguf.py ./modelfile --outtype q8_0 --outfile ./name-fine-tuned-llm.gguf
