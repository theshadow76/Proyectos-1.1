import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
import json
import os
from transformers.data.datasets import LineByLineTextDataset
from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from torch.utils.data import ConcatDataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # Use CUDA if available, otherwise use CPU

tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base')
model = RobertaForSequenceClassification.from_pretrained('microsoft/codebert-base')
tokenizer.add_special_tokens({'pad_token': '[PAD]'}) 

def chunkify(file_path, chunk_size=1000):
    with open(file_path, 'r') as f:
        chunk = []
        for i, line in enumerate(f):
            chunk.append(json.loads(line))
            if (i + 1) % chunk_size == 0:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

def save_chunks(input_file_path, output_file_base_path, chunk_size=1000):
    for i, chunk in enumerate(chunkify(input_file_path, chunk_size)):
        output_file_path = f"{output_file_base_path}_{i}.json"
        with open(output_file_path, 'w') as f:
            json.dump(chunk, f)

# Use the function to save the dataset into smaller chunks
# save_chunks('python100k_train.json', 'python_train_chunk', chunk_size=1000)

# Define a data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False,
)

# Define the training arguments
training_args = TrainingArguments(
    output_dir="./model",  # The output directory
    overwrite_output_dir=True,  # overwrite the content of the output directory
    num_train_epochs=3,  # number of training epochs
    per_device_train_batch_size=32,  # batch size for training
    save_steps=10_000,  # after # steps model is saved
    save_total_limit=2,  # delete old checkpoints; only the last # are saved
    
)

dataset_dir = 'C:\\Users\\vigop\\OneDrive\\backup 1\\coding\\python\\awdad' 

combined_dataset = ConcatDataset(dataset_dir)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=combined_dataset
)

for file_name in os.listdir(dataset_dir):
    if file_name.startswith('python_train_chunk'):  # replace with the prefix of your chunked dataset files
        dataset_path = os.path.join(dataset_dir, file_name)
        dataset = LineByLineTextDataset(
            tokenizer=tokenizer,
            file_path=dataset_path,
            block_size=128  # Specify the appropriate block size for your dataset
        )
        trainer.train_dataset = dataset
        trainer.train()
        print("Trained")

# Save the model
trainer.save_model()
