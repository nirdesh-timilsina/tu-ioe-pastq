from bs4 import BeautifulSoup
import json
import re
import demjson3

with open('index.html','r',encoding='utf-8') as f:
    content = f.read()
print ("file loaded. total characters:", len(content))

soup = BeautifulSoup(content, 'html.parser')
scripts = soup.find_all('script')
full_js=''
for script in scripts:
    if script.string:
        full_js+=script.string
print ("JS extracted. Total characters:", len(full_js))

subjects = {
    'CN': 'computer_networks',
    'COA': 'computer_organization_architecture',
    'PS': 'probability_statistics',
    'DBMS': 'database_management_system',
    'WAP': 'web_application_programming',
    'CD': 'compiler_design',
    'APDS': 'advanced_python_data_science',
    'AI': 'artificial_intelligence',
}

for var_name, file_name in subjects.items():
    match = re.search(rf'const {var_name} = (\[.+?\]);', full_js, re.DOTALL)
    if match:
        raw = match.group(1)
        data = demjson3.decode(raw)
        with open(f'{file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"{var_name} done. Chapters: {len(data)}")
    else:
        print(f"{var_name} not found")