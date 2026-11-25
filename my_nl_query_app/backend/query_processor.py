import openai

openai.api_key = "your_openai_api_key"

def extract_keywords(nl_query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Extract table names from query."},
                  {"role": "user", "content": nl_query}]
    )
    return response["choices"][0]["message"]["content"].split()

def find_relevant_tables(schema, keywords):
    relevant_tables = []
    for table, details in schema.items():
        if any(keyword.lower() in table.lower() for keyword in keywords):
            relevant_tables.append(table)
    return relevant_tables

def process_query(nl_query, schema):
    keywords = extract_keywords(nl_query)
    return find_relevant_tables(schema, keywords)