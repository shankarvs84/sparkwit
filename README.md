# Team 56 - Sparkwit
## _ESG Survey Automation_


We provide simple API and GUI for getting responses to you ESG related queries.

## Features

- Get response to your ESG related queries through a REST API call
- Access a simple and interactive GUI to upload your training data files
- Chat with ESG survey GPT to get responses to your ESG related queries

### Make queries through API call
#### API details:
> _Request:_
> 
> POST http://[host-name]/ping
> 
> body:
> {
>    "reportYear": "2024",
>    "inputQuestion": "What is wells fargo strategy for inclusion"
>}

> _Response:_
> 
> {
>    "questionnaireSummary": {
>        "citation": [
>            "CO2eMission_Executive_Summary.pdf",
            "2019-ballot-measures.pdf",
            "CO2eMission_Methodology.pdf",
            "CO2eMission_Methodology.pdf",
            "2022-diversity-equity-inclusion-report.pdf",
            "2022-diversity-equity-inclusion-report.pdf",
            "CO2eMission_Executive_Summary.pdf",
            "2022-diversity-equity-inclusion-report.pdf",
            "2022-diversity-equity-inclusion-report.pdf",
            "2022-diversity-equity-inclusion-report.pdf"
>        ],
>        "response": "Wells Fargo's strategy for inclusion focuses on creating a diverse and inclusive workplace where all employees feel valued and respected. This includes promoting diversity in hiring, providing equal opportunities for advancement, and fostering a culture of inclusion where all voices are heard and valued. Wells Fargo also works to support diverse communities through various initiatives and partnerships aimed at promoting economic empowerment and social inclusion."
>    },
>    "reportYear": "2024"
> }

### GUI with chat and file upload features

![img.png](img.png)

#### Chat with our ESG survey GPT:
![img_1.png](img_1.png)

### Upload your PDF training data files:
![img_2.png](img_2.png)

## Powered by
- Python
- Azure Cognitive Search
- Azure OpenAI embedding model - text-embedding-ada-002
- LangChain - an open-source framework designed to simplify the creation of applications using large language models (LLMs).
- Streamlit - an open-source framework to rapidly build and share beautiful machine learning and data science web apps.


