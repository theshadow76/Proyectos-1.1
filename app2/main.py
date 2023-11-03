import requests
import json
from transformers import BertTokenizer, BertModel
import requests
from bs4 import BeautifulSoup
import re
from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import RobertaTokenizer, RobertaForSequenceClassification

data = []

class GithubCodeSearcher:
    def __init__(self, token):
        self.api_url = "https://api.github.com"
        self.headers = {'Authorization': 'token {}'.format(token)}
        self.tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base')
        self.model = RobertaForSequenceClassification.from_pretrained('microsoft/codebert-base')

    def search_code(self, query, language=None, sort="indexed", order="desc"):
        code_list = []
        if language:
            query += f' language:{language}'
        url = "{}/search/code?q={}&sort={}&order={}".format(self.api_url, query, sort, order)
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            result = json.loads(response.text)
            for item in result['items']:
                code_list.append(item)
        else:
            print("Error occurred: ", response.status_code)

        return code_list
    
    def extract_text_by_class(self, url):
        global texts
        texts = None
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all("div", class_="Box-sc-g0xbh4-0")
        for element in elements:
            texts = element
            data.append(texts)
        if texts is not None:
            return texts
    
    def extract_code(self, url):
        headers = {"Accept": "application/vnd.github.VERSION.raw"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            code = response.text
            data.append(code)
            return code
        else:
            print("Error occurred: ", response.status_code)
            return None
    
    def convert_to_raw_url(self, html_url):
        # split the URL into components
        parts = html_url.split('/')
        
        # replace 'github.com' with 'raw.githubusercontent.com'
        parts[2] = 'raw.githubusercontent.com'
        
        # remove 'blob' from the URL
        parts.remove('blob')
        
        # join the components back into a URL
        raw_url = '/'.join(parts)
        
        return raw_url
    
    def understand_code(self, code):
        # Ensure the code is not empty or null
        if not code:
            print("Warning: empty code provided.")
            return None

        # Tokenize the code, truncating if necessary
        inputs = self.tokenizer(code[:512], return_tensors="pt")

        # Pass the tokenized input to the model
        try:
            outputs = self.model(**inputs)
        except Exception as e:
            print(f"Error occurred while processing code: {e}")
            return None

        return outputs



def process_results(results, searcher):
    try:
        urls = [item['html_url'] for item in results]
        for url in urls:
            raw_url = searcher.convert_to_raw_url(url)
            code = searcher.extract_code(raw_url)
            # print(code)
            if code is not None:
                outputs = searcher.understand_code(code)
                with open('data.txt', 'a') as f:  # using 'a' instead of 'w' to append to the file instead of overwriting it
                    f.write("Data: " + str(outputs))
                print("output: " + str(outputs))
    except Exception as e:
        print(f"Error occurred while processing results: {e}")

def main():
    searcher = GithubCodeSearcher('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')
    results = searcher.search_code('import requests', 'python')
    process_results(results, searcher)
    print("Done!!!")

if __name__ == '__main__':
    main()