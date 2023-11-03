# !pip install transformers
from transformers import RobertaForSequenceClassification, RobertaTokenizer
from transformers import AdamW, get_linear_schedule_with_warmup
import torch
from torch.utils.data import Dataset, DataLoader
import json
import glob
import os
from torch.nn.utils.rnn import pad_sequence

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# load the model
model = RobertaForSequenceClassification.from_pretrained('microsoft/codebert-base')
tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base')
model = model.to(device)

# Load the previously saved progress if available
progress_file = 'data.json'
last_file = None
if os.path.exists(progress_file):
    with open(progress_file, 'r') as f:
        last_file = json.load(f).get('last_file')

# Find all the .jsonl files in the directory
file_names = sorted(glob.glob('C:/Users/vigop/OneDrive/backup 1/coding/python/awdad/Cleaned_CodeSearchNet/CodeSearchNet/python/chunks/*.jsonl'))

start = file_names.index(last_file) + 1 if last_file in file_names else 0

class MyDataset(Dataset):
    def __init__(self, sentences, labels, tokenizer):
        self.sentences = sentences
        self.labels = labels
        self.tokenizer = tokenizer

    def __getitem__(self, idx):
        sentence = self.sentences[idx]
        label = self.labels[idx]
        inputs = self.tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
        item = {key: val[0] for key, val in inputs.items()}
        item['labels'] = torch.tensor(label)
        return item

    def __len__(self):
        return len(self.labels)

epochs = 1
optimizer = AdamW(model.parameters(), lr=1e-5)

def collate_fn(batch):
    input_ids = pad_sequence([item['input_ids'] for item in batch], batch_first=True, padding_value=tokenizer.pad_token_id)
    attention_mask = pad_sequence([item['attention_mask'] for item in batch], batch_first=True, padding_value=0)
    labels = torch.stack([item['labels'] for item in batch])
    return {'input_ids': input_ids, 'attention_mask': attention_mask, 'labels': labels}

for file_name in file_names[start:]:
    # Load the model from the last checkpoint if it exists
    model_path = './model' + '_' + os.path.basename(file_name).split('.')[0]
    if os.path.exists(model_path):
        model = RobertaForSequenceClassification.from_pretrained(model_path)
        model = model.to(device)

    # Load the data from the file
    with open(file_name, 'r') as f:
        data = [json.loads(line) for line in f]
    # Extract the sentences and labels
    sentences = [item['code'] for item in data]
    labels = [1 if item['partition'] == 'train' else 0 for item in data]

    # Tokenize the sentences and create the dataset
    dataset = MyDataset(sentences, labels, tokenizer)
    train_dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

    total_steps = 10
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=10)
    print(f"Training started for {file_name}!")
    # print(total_steps)
    for epoch in range(epochs):
        for batch in train_dataloader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
          # print(f"Epoch: {epoch} finished in {file_name}")
    model_path = './model' + '_' + os.path.basename(file_name).split('.')[0]
    model.save_pretrained(model_path)
    os.makedirs('./model', exist_ok=True)
    base_file_name = os.path.basename(file_name).split('.')[0]
    torch.save(model, f'./model/model_{base_file_name}.pt')

    # Save the progress
    with open(progress_file, 'w') as f:
        json.dump({'last_file': file_name}, f)
    print(f"Training done for {file_name}!")