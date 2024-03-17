from api_chat import get_query_response


def get_api_query_response(query):
    """Function to fetch response for API query"""

    year = query['reportYear']
    input_question = query['inputQuestion']

    print('year: ', year)
    print('Input Question: ', input_question)

    query_response = get_query_response(report_year=year, user_input=input_question)
    return query_response
