from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.retrievers import AzureCognitiveSearchRetriever
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def get_query_response(user_input, report_year):
    query_response = ""
    load_dotenv()
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, output_key="answer"
    )

    prompt_template = """You are a helpful assistant for questions about the Wells Fargo Environmental, Social and 
    Governance survey. 
    
    {context}
    
    Question: {question}`
    Answer here:"""
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    retriever = AzureCognitiveSearchRetriever(content_key="chunk", top_k=10)

    llm_chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0),
        memory=memory,
        retriever=retriever,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt},
    )

    if user_input:
        response = llm_chain({"question": user_input}, return_only_outputs=True)
        print('response:', response)
        answer = response['answer']

        print('Answer: ', answer)
        source_documents = response['source_documents']
        # print('Source document: ', source_documents)
        titles = []
        for source_document in source_documents:
            # print('Title: ', source_document.metadata['title'])
            titles.append(source_document.metadata['title'])
            # print('Search score:', source_document.metadata['@search_score'])

        response = bytes(answer, 'utf-8').decode('unicode_escape')
        query_response = {'reportYear': report_year,
                          'questionnaireSummary': {
                              'response': response,
                              'citation': titles
                          }}

    return query_response
