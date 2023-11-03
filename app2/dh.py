from transformers import RobertaForSequenceClassification, RobertaTokenizer
from transformers import AdamW, get_linear_schedule_with_warmup
import torch
from torch.utils.data import Dataset, DataLoader
import json
import glob

# load the model
model = RobertaForSequenceClassification.from_pretrained('microsoft/codebert-base')
tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base')

# a list of code snippets
# Load the data from a .jsonl file
# Find all the .jsonl files in the directory
file_names = glob.glob('C:/Users/vigop/OneDrive/backup 1/coding/python/awdad/Cleaned_CodeSearchNet/CodeSearchNet/python/*.jsonl')

sentences = []
labels = []

# Loop over the files and load the data from each file
for file_name in file_names:
    with open(file_name, 'r') as f:
        data = [json.loads(line) for line in f]
    # Extract the sentences and labels and add them to the lists
    sentences.extend([item['code'] for item in data])
    labels.extend([1 if item['partition'] == 'train' else 0 for item in data])


# assuming `sentences` is a list of your code snippets and `labels` is a list of corresponding labels
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
inputs["labels"] = torch.tensor(labels)

class MyDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# create the dataset
dataset = MyDataset(inputs, labels)
train_dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

epochs = 3

optimizer = AdamW(model.parameters(), lr=1e-5)
total_steps = len(train_dataloader) * epochs  # assuming `train_dataloader` is your PyTorch DataLoader
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

model.train()
print("Training started!")
for epoch in range(epochs):
    for batch in train_dataloader:
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()
    print(f"Epoch {epoch} done!")

# save the model
model.save_pretrained('./model')