import os
import webview
import requests
import openpyxl
import pandas as pd
import concurrent.futures
import time
import random
import threading
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from flair.data import Sentence
from urllib.parse import urlparse
from flair.models import SequenceTagger
from openpyxl.utils import get_column_letter
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Initialize the NER tagger once
tagger = SequenceTagger.load('ner')

# Create a session for making HTTP requests
session = requests.Session()

# Set up retries with exponential backoff
retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Update headers to mimic a real browser
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.121 Safari/537.36"
})

def extract_person_names(text, company, url):
    try:
        sentence = Sentence(text)
        tagger.predict(sentence)
        person_names = set(entity.text for entity in sentence.get_spans('ner') if entity.tag == 'PER')
        print(f'Done extracting names for company {company} and webpage {url}')
        ans = list(person_names)
        ans = [s.replace(company, "").strip() for s in ans]
        return ans
    except Exception as e:
        print(f'Error extracting names from {url}: {e}')
        return []

def extract_text(web_url, company):
    try:
        # Random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))

        if web_url.lower().endswith('.pdf'):
            pdf_filename = os.path.basename(urlparse(web_url).path)

            if not os.path.exists('documents'):
                os.makedirs('documents')

            pdf_filepath = os.path.join('documents', pdf_filename)

            response = session.get(web_url, timeout=10)
            with open(pdf_filepath, 'wb') as f:
                f.write(response.content)

            with open(pdf_filepath, 'rb') as f:
                reader = PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

            print(f'Done extracting text from {web_url}')
            return text

        else:
            response = session.get(web_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            print(f'Done extracting text from {web_url}')
            return text

    except Exception as e:
        print(f'Failed to extract text from {web_url} for {company}: {str(e)}')
        return ""

def google_search(query, num):
    try:
        # Random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))

        query = query.replace(' ', '+')
        url = f"https://www.google.com/search?q={query}&num={num}"

        response = session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for item in soup.find_all('div', class_='yuRUbf'):
            a_tag = item.find('a')
            if a_tag and a_tag.get('href'):
                links.append(a_tag['href'])

        return links
    except Exception as e:
        print(f'Error during Google search: {e}')
        return []

def fetch_details(company_name):
    try:
        if not company_name:
            return 'Please enter a company name.'

        company = company_name.strip()
        query = f'{company} UK Career Stories -client -customer'

        try:
            company_testimonial_links = google_search(query, 10)
            if not company_testimonial_links:
                return 'No results found or IP blocked during Google search.'
        except Exception as e:
            print(f'Google search failed: {e}')
            return 'IP BLOCKED or error during Google search.'

        # Process each URL individually
        all_web_sites = []

        def process_url(url):
            text = extract_text(url, company)
            if text:
                return {'company': company, 'web_content': str(text), 'url': url}
            return None

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(process_url, company_testimonial_links)

        for result in results:
            if result:
                all_web_sites.append(result)

        row_list = []

        def process_website(part):
            try:
                text = part['web_content']
                company = part['company']
                url = part['url']
                names = extract_person_names(text, company, url)
                return [{'Name': name, 'Company': company, 'Testimonial Page': url} for name in names]
            except Exception as e:
                print(f'Error processing website {url}: {e}')
                return []

        for web_site in all_web_sites:
            result = process_website(web_site)
            row_list.extend(result)

        if not row_list:
            return 'No data extracted.'

        file_name = f'{company_name}_list.xlsx'
        df = pd.DataFrame(row_list)
        df.to_excel(file_name, index=False)

        update_file(file_name)
        return f'Successfully done for {file_name}'
    except Exception as e:
        print(f'Error in fetch_details: {e}')
        return 'Something went wrong!'

def update_file(file_name):
    try:
        if not os.path.isfile(file_name):
            print(f"File '{file_name}' not found.")
            return 'File not found!'

        df = pd.read_excel(file_name)

        if 'Linkedin Profile' not in df.columns:
            df['Linkedin Profile'] = ''

        for index, row in df.iterrows():
            if 'Link' in str(row.get('Linkedin Profile', '')):
                continue
            try:
                name = row['Name']
                company_name = row['Company']
                query = f'{name} UK {company_name} profile linkedin'
                links = google_search(query, 10)
                if links:
                    link = links[0]
                    df.at[index, 'Linkedin Profile'] = link
                    print(f'Done fetching LinkedIn profile for index {index}')
                else:
                    df.at[index, 'Linkedin Profile'] = 'No profile found'
                    print(f'No LinkedIn profile found for index {index}')
                # Random delay to mimic human behavior
                time.sleep(random.uniform(1, 3))
            except Exception as e:
                print(f'Error fetching LinkedIn profile for index {index}: {e}')
                df.at[index, 'Linkedin Profile'] = 'Error fetching profile'
                continue  # Ensure the loop continues

        df.to_excel(file_name, index=False)

        # Convert URLs to hyperlinks in Excel
        convert_urls_to_hyperlinks(file_name, 'Sheet1', 3)
        convert_urls_to_hyperlinks(file_name, 'Sheet1', 4)
        return f'Successfully updated data in {file_name}'
    except Exception as e:
        print(f'Error in update_file: {e}')
        return 'Something went wrong during file update.'

def convert_urls_to_hyperlinks(excel_file, sheet_name, url_column):
    try:
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
    except Exception as e:
        print(f'Error converting URLs to hyperlinks: {e}')

class API:
    def check_data(self, name):
        threading.Thread(target=self._check_data, args=(name,)).start()
        return 'Process started'

    def _check_data(self, name):
        result = fetch_details(name)
        # Send result back to webview
        escaped_result = result.replace('"', '\\"').replace('\n', '\\n')
        script = f'document.getElementById("resultDisplay").textContent = "{escaped_result}"; stopTimer();'
        webview.evaluate_js(script)

    def update_data(self, name):
        threading.Thread(target=self._update_data, args=(name,)).start()
        return 'Process started'

    def _update_data(self, name):
        result = update_file(name)
        # Send result back to webview
        escaped_result = result.replace('"', '\\"').replace('\n', '\\n')
        script = f'document.getElementById("resultDisplay").textContent = "{escaped_result}"; stopTimer();'
        webview.evaluate_js(script)

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

        function startProcess() {
            startTimer();
            const name = document.getElementById('nameInput').value;
            pywebview.api.check_data(name);
            // The result will be updated by the Python code via evaluate_js
        }

        function startUpdate() {
            startTimer();
            const name = document.getElementById('fileNameInput').value;
            pywebview.api.update_data(name);
            // The result will be updated by the Python code via evaluate_js
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
    window = webview.create_window('Scrape Web', html=html_content, width=400, height=300, js_api=api)
    webview.start(gui='winforms')

if __name__ == '__main__':
    start_gui()
