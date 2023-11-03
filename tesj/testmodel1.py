import torch
from transformers import BertTokenizer, BertForMaskedLM

def generate_code(prompt, model, tokenizer, max_length=50):
    model.eval()

    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    input_length = input_ids.shape[1]

    # Generate code
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=max_length,
            do_sample=True,
            top_p=0.9,
            top_k=0,
            num_return_sequences=1
        )

    # Decode the generated tokens to text
    generated_code = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Remove the input prompt from the generated code
    generated_code = generated_code[input_length:].strip()

    return generated_code

# Load the saved model and tokenizer
model = BertForMaskedLM.from_pretrained("trained_model")
if torch.cuda.device_count() > 1:
    model = model.module
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Set your desired prompt
prompt = "create a function that adds two numbers"

# Generate Python code using the saved model
generated_code = generate_code(prompt, model, tokenizer)
print(generated_code)
