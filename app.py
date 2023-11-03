import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Specify the path to your model weights
model_path = "./gpt2_python/pytorch_model.bin"

# Load the model weights
model_state_dict = torch.load(model_path)

# Initialize a new GPT-2 model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Load the weights into the model
model.load_state_dict(model_state_dict)

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Encode input context
input_context = "for v1 in range(100):"
input_ids = tokenizer.encode(input_context, return_tensors='pt')

# Generate text
output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, temperature=1)

# Decode the output
generated_code = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_code)
