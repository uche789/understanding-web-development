import io

# To use this script, run it in the root of the project.
# It will read the frontend.md file and generate a table of contents based on the headings in the file.
# Command to run: python generate-table-contents.py

file_name = input("Enter the name of the markdown file (default: frontend.md): ") or "frontend.md"

allLines = io.open('./' + file_name, 'r', encoding='utf-8').readlines();

result=[]

for line in allLines:
    clean_line = line.strip().replace('\n', '').replace('\r', '').replace('\t', '');
    if line.startswith('## '):
        result.append({
            'element': 'h2',
            'text': clean_line.replace('## ', '')
        })
    if line.startswith('### '):
        result.append({
            'element': 'h3',
            'text': clean_line.replace('### ', '')
        })
    if line.startswith('#### '):
        result.append({
            'element': 'h4',
            'text': clean_line.replace('#### ', '')
        })
    # print(line)

allLines.clear()

fileString = "";
for r in result:
    # clean_text = str(r['text']).replace('\s', '-').lower().replace('?', '');
    clean_text = '-'.join((str(r['text']).replace('?', '').lower().split()));
    text = '[' +  r['text'] + '](#' + clean_text + ')\n';
    element = r["element"];

    if element == 'h2':
        fileString = fileString + '- ' + text;
    elif element == 'h3':
        fileString = fileString + '  - ' + text;
    elif element == 'h4':
        fileString = fileString + '    - ' + text;

print(fileString)
# io.open('output-table-contents.md', 'w', encoding='utf-8').write(fileString);