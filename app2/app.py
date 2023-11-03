# !pip install transformers
from transformers import BertTokenizer, BertModel
import requests
from bs4 import BeautifulSoup
import re
from transformers import BartForConditionalGeneration, BartTokenizer
import requests
import json
from transformers import RobertaTokenizer, RobertaForSequenceClassification

CodePattern = ['Search this code', "make me", "generate me", "generate code", "generate code for me", "generate code for this", "generate code for this code", "generate code for this snippet", "generate code for this code snippet", "generate code for this code snippet for me", "Code me", "Code this", "Code this for me", "Code this code", "Code this code for me", "Code this code snippet", "code me"]

class CodeSearcher:
    def __init__(self):
        self.url = 'https://api.github.com/search/code'
        self.headers = {'Accept': 'application/vnd.github.v3.text-match+json', 'Authorization' : 'token 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'}
        self.tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base')
        self.model = RobertaForSequenceClassification.from_pretrained('microsoft/codebert-base')
        self.base_url = 'https://api.stackexchange.com/2.3/'
        
    def search_github(self, query):
        try:
            params = {'q': query}
            response = requests.get(self.url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error occurred while searching Github: {e}")
            return None
    
    def search_advanced(self, query, tagged=None, nottagged=None, sort='relevance', order='desc'):
        url = self.base_url + 'search/advanced'
        params = {
            'q': query,
            'tagged': tagged,
            'nottagged': nottagged,
            'sort': sort,
            'order': order,
            'site': 'stackoverflow'
        }
        response = requests.get(url, params=params)
        return response.json()
    
    def search_and_understand(self, query):
        results = self.search_github(query)
        urls = []  # initialize urls as an empty list
        try: 
            print("Trying")
            try:
                # print(results)
                for result in results['items']:
                    urls.append(result['html_url'])  # directly append url to list
                    # print("link added: " + str(result['html_url']))
            except:
                results2 = self.search_advanced(query, None, None, 'relevance', 'desc')
                print("data: " + str(results2))
        except:
            print('No results found')
        return urls  # return the list of urls

    def extract_text_by_class(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(class_="react-blob-print-hide")
        texts = [element.text for element in elements]
        return texts
    
    def understand_code(self, code):
        inputs = self.tokenizer(code, return_tensors="pt")
        outputs = self.model(**inputs)
        return outputs

class TextSummarizer:
    def __init__(self):
        self.subscription_key = 'aab5d93e331f44a3b7a15b71356cc064'
        self.endpoint = 'https://api.bing.microsoft.com' + "/v7.0/search"
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    def search_articles(self, query):
        headers = {"Ocp-Apim-Subscription-Key" : self.subscription_key}
        params  = {"q": query, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(self.endpoint, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        urls = [result['url'] for result in search_results['webPages']['value']]
        return urls

    def get_webpage_text(self, urls):
        texts = []
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            texts.append(text)
        return texts

    def preprocess_text(self, text):
        text = re.sub(r'\W', ' ', text)
        text = re.sub(r'\d', ' ', text)
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
        text = re.sub(r'\s+', ' ', text, flags=re.I)
        text = text.lower()
        return text

    def generate_summary(self, input_text):
        encoded_input = self.tokenizer(input_text, truncation=True, max_length=1024, return_tensors='pt')
        summary_ids = self.model.generate(encoded_input['input_ids'], num_beams=4, max_length=100, early_stopping=True)
        summary = [self.tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
        return summary

    def summarize_articles(self, query):
        urls = self.search_articles(query)
        text = self.get_webpage_text(urls)
        preprocessed_text = self.preprocess_text(str(text))
        summary = self.generate_summary(preprocessed_text)
        return summary

def main():
    # Create a CodeSearcher object
    searcher = CodeSearcher()

    # Define the query
    prompt = "Code me a function in python that prints hello world"
    
    # Search for the query in Github and understand the results
    github_results = searcher.search_github(prompt)
    if github_results is not None:
        process_results(github_results, searcher)

def process_results(results, searcher):
    try:
        urls = [item['html_url'] for item in results['items']]
        for url in urls:
            texts = searcher.extract_text_by_class(url)
            for text in texts:
                outputs = searcher.understand_code(text)
                with open('data.txt', 'a') as f:  # using 'a' instead of 'w' to append to the file instead of overwriting it
                    f.write("Data: " + str(outputs))
                print("output: " + str(outputs))
    except Exception as e:
        print(f"Error occurred while processing results: {e}")

if __name__ == "__main__":
    main()
