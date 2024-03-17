import os
import re

from tika import parser

pdf_folder_path = "questions"
question_pattern = "/ \b[Qq][Ee][Tt][Oo]:?\s + (\d+)\b / g"
for file in os.listdir(pdf_folder_path):
    if file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder_path, file)
        print('PDF path: ', pdf_path)
        parsed_pdf = parser.from_file(pdf_path)
        data = parsed_pdf['content']
        data_clean = data.replace("\n", "")
        print('data:', data_clean)

        #matches = re.split(r"(...)", data)

        #print('matches:', matches)

        #for match in matches:
        #    print('printing match')
        #    print(match)



