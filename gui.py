import os
import webview
import requests
import openpyxl
import pandas as pd
import concurrent.futures
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from flair.data import Sentence
from urllib.parse import urlparse
from flair.models import SequenceTagger
from openpyxl.utils import get_column_letter
import time
from llama_index.llms.huggingface import HuggingFaceInferenceAPI
from llama_index.core import PromptTemplate
HF_token = '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'

llm = HuggingFaceInferenceAPI(model_name="mistralai/Mixtral-8x7B-Instruct-v0.1", token=HF_token)


tagger = SequenceTagger.load('ner')
def extract_person_names(text,company,url):
    try:
        template = """
        Question: {question}
        Context: {context_str}
        Answer: Let's think step by step.
        """
        prompt_template = PromptTemplate(template=template, input_variables="question, context_str")
        
        question = f"Make a list of the names of people who are being interviewed or are giving testimonials of their experience and how they got in the company {company}. Do not say anything else. Keep in mind that there may not be a single one that have given an interview- if that it is the case, do not return any names. Only those people (if there is any) who are of {company} and are telling about their experience in that job, and how they applied, prepared, etc. "
        
        response = llm.complete(prompt_template.format(question=question, context_str=text))
        response_text = response.text
        sentence = Sentence(response_text)
        tagger.predict(sentence)
        person_names = set(entity.text for entity in sentence.get_spans('ner') if entity.tag == 'PER')
        print(f'Done for company {company} and webpage {url}')
        ans =  list(person_names)

        ans = [s.replace(company, "") for s in ans]
        return ans
    except Exception as e:
        print(e)

        return []

def extract_text(web_url, company):
    try:
        if web_url.lower().endswith('.pdf'):
            pdf_filename = os.path.basename(urlparse(web_url).path)
            
            if not os.path.exists('documents'):
                os.makedirs('documents')
            
            pdf_filepath = os.path.join('documents', pdf_filename)
            
            response = requests.get(web_url)
            with open(pdf_filepath, 'wb') as f:
                f.write(response.content)
            
            with open(pdf_filepath, 'rb') as f:
                reader = PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            
            print(f'Done for {web_url}')
            return text

        else:
            response = requests.get(web_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            print(f'Done for {web_url}')
            return text

    except Exception as e:
        print(f'Failed at {web_url} and {company}: {str(e)}')




def google_search(query,num):
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}?num={num}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for item in soup.find_all('div', class_='yuRUbf'):
        a_tag = item.find('a')
        if a_tag and a_tag.get('href'):
            links.append(a_tag['href'])

    return links
def fetch_details(company_name):
    try:
        if company_name==None:
            return 'Please Enter Company Name'

        company = company_name
        query = f'{company} UK Career Stories -client -customer'

        try:
            company_testimonials = google_search(query,1)
        except Exception as e:
            print(e)
            print("")
            
            
            
            
            


        company_testimonials = [{
            'company':company,
            'web_url': company_testimonials
        }]
        def process_testimonial(comp):
            company = comp['company']
            web_sites = []
            for url in comp['web_url']:
                text = extract_text(url, company) 

                if text:
                    web_sites.append({'company': company, 'web_content': str(text),'url':url})
            return web_sites

        all_web_sites = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(process_testimonial, company_testimonials)

            for result in results:
                all_web_sites.extend(result)


        row_list = []

        def process_website(part):
            try:
                text = part['web_content']
                company = part['company']
                url = part['url']
                names = extract_person_names(text,company,url)
                
                return [{'Name': name, 'Company': company,'Testimonial Page':url} for name in names]
            except:
                print(names)
                return []

        for web_site in all_web_sites:
            result = process_website(web_site)
            row_list.extend(result)       


        file_name = f'{company_name}_list.xlsx'
        df = pd.DataFrame(row_list)
        df.to_excel(file_name,index=False)


        update_file(file_name)
        return f'Successfully done for {file_name}'
    except Exception as e:
        print(e)
        print('Something went wrong!')


def update_file(file_name):
    if not os.path.isfile(file_name):
        print(f"File with the name '{file_name}' not found.")
        return 'File Name not found!'
    df = pd.read_excel(file_name)

    if not 'Linkedin Profile' in df.columns:
        df['Linkedin Profile'] = ''

    for index, row in df.iterrows():
        if 'Link' in str(row['Linkedin Profile']):
            continue
        try:
            name = row['Name']
            company_name = row['Company']
            query = f'{name} UK {company_name} profile linkedin'
            link = google_search(query, 10)[0]
            df.at[index, 'Linkedin Profile'] = link
            print(f'Done for index {index}')
        except Exception as e:
            
            print("Max attempts reached")
            print(e)
            df.at[index, 'Linkedin Profile'] = 'IP BLOCKED'
            pass
    df.to_excel(file_name, index=False)

    def convert_urls_to_hyperlinks(excel_file, sheet_name, url_column):
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook[sheet_name]

        col_letter = get_column_letter(url_column)

        for row in range(2, sheet.max_row + 1):
            cell = sheet[f"{col_letter}{row}"]
            if isinstance(cell.value, str) and cell.value.startswith("http"):
                sheet[f"{col_letter}{row}"].hyperlink = cell.value
                sheet[f"{col_letter}{row}"].value = 'Link'
                sheet[f"{col_letter}{row}"].style = "Hyperlink"

        workbook.save(excel_file)

    excel_file = file_name
    sheet_name = "Sheet1"
    url_column = 3

    convert_urls_to_hyperlinks(excel_file, sheet_name, url_column)
    url_column = 4
    convert_urls_to_hyperlinks(excel_file, sheet_name, url_column)
    return f'Successfully updated data to {excel_file}'


  


class API:
    def check_data(self, name):
        return fetch_details(name)
    def update_data(self,name):
        return update_file(name)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scrape Web</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { text-align: center; margin-top: 50px; }
        .timer { font-size: 14px; margin-top: 20px; }
        .result { font-size: 16px; color: green; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h4>Enter Company Name</h4>
        <input type="text" id="nameInput" placeholder="Enter name">
        <button onclick="startProcess()">Start Scraping</button>
        
        <h4>Enter File Name</h4>
        <input type="text" id="fileNameInput" placeholder="Enter File Name">
        
        <button onclick="startUpdate()">Update File</button>
        <div class="timer">
            <p><span id="timerDisplay">0m 0.0s</span> (expected 15-20m)</p>
        </div>
        <div class="result" id="resultDisplay">
            <!-- The result will be displayed here -->
        </div>
    </div>
    
    <script>
        let timer;
        let startTime;

        async function startProcess() {
            startTimer();
            const name = document.getElementById('nameInput').value;
            const result = await pywebview.api.check_data(name);
            stopTimer();
            document.getElementById('resultDisplay').textContent = result;
        }

        async function startUpdate() {
            startTimer();
            const name = document.getElementById('fileNameInput').value;
            const result = await pywebview.api.update_data(name);
            stopTimer();
            document.getElementById('resultDisplay').textContent = result;
        }

        function startTimer() {
            startTime = Date.now();
            timer = setInterval(updateTimer, 100);
        }

        function updateTimer() {
            let elapsed = (Date.now() - startTime) / 1000; // elapsed time in seconds
            let minutes = Math.floor(elapsed / 60);
            let seconds = (elapsed % 60).toFixed(1);
            document.getElementById('timerDisplay').textContent = `${minutes}m ${seconds}s elapsed`;
        }

        function stopTimer() {
            clearInterval(timer);
        }
    </script>
</body>
</html>
"""

def start_gui():
    api = API()
    window = webview.create_window('Timer App', html=html_content, width=400, height=300, js_api=api)
    webview.start(gui='winforms')  # Use the CEF (Chromium) renderer for better compatibility

if __name__ == '__main__':
    start_gui()
