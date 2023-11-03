import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
import json

with open('data.json', 'r') as file:
    data = json.load(file)

text_data = data[0]  # Access the first string in the list

# Load pre-trained model and tokenizer
model = TFGPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Add padding token to the tokenizer
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Tokenize the data
inputs = tokenizer(text_data, return_tensors="tf", padding=True, truncation=True)

# Create a TextDataset and DataCollator for the tokenized data
dataset = tf.data.Dataset.from_tensor_slices(inputs)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./trained_model",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
)

# Train the model
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()

# Save the model
model.save_pretrained("./trained_model")
