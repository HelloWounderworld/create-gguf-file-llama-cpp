import os

model_path = "./modelfile"
required_files = [
    "config.json", 
    "generation_config.json", 
    "pytorch_model.bin",  # ou model.safetensors
    "pytorch_model.bin.index.json",  
    "special_tokens_map.json",  
    "tokenizer_config.json",
    "tokenizer.json",
    "tokenizer.model"
]

# Verificar arquivos essenciais
missing_files = [f for f in required_files if not os.path.exists(os.path.join(model_path, f))]

if missing_files:
    print("Arquivos faltando:", missing_files)
else:
    print("Estrutura do modelo parece estar completa!")