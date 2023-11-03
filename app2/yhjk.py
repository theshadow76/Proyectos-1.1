import json
import os

def split_jsonl(file_name, chunk_size=1000, output_dir=''):
    with open(file_name, 'r') as f:
        chunk = []
        for i, line in enumerate(f):
            chunk.append(line)
            if (i + 1) % chunk_size == 0:
                output_file = os.path.join(output_dir, f'{os.path.basename(file_name)}_chunk_{i // chunk_size + 1}.jsonl')
                with open(output_file, 'w') as chunk_file:
                    chunk_file.writelines(chunk)
                chunk = []
        if chunk:  # write the remaining lines in the last chunk
            output_file = os.path.join(output_dir, f'{os.path.basename(file_name)}_chunk_{i // chunk_size + 1}.jsonl')
            with open(output_file, 'w') as chunk_file:
                chunk_file.writelines(chunk)

output_dir = 'C:/Users/vigop/OneDrive/backup 1/coding/python/awdad/Cleaned_CodeSearchNet/CodeSearchNet/python/chunks/'
input_file = 'C:/Users/vigop/OneDrive/backup 1/coding/python/awdad/Cleaned_CodeSearchNet/CodeSearchNet/python/train.jsonl_chunk_26.jsonl'
split_jsonl(input_file, chunk_size=100, output_dir=output_dir)
