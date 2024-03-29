import psycopg2
from openai import OpenAI
import os
api_key = os.environ.get('OPENAI_API_KEY')
# The api key
key_2 = api_key
client = OpenAI(api_key=key_2)

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    database="YoutubeDB",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
print("Connected to the database!\n")

def execute_sql_query(sql_query):
    try:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)
            
    except Exception as e:
        print("Error executing SQL query:", e)

# Chat with the OpenAI GPT-3.5-turbo API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who knows how to write PostgreSQL SQL queries."},
        {"role": "user", "content": "Generate a SQL query to retrieve all the data in the cities_table_data."},
        {"role":"assistant", "content": "SELECT * FROM cities_table_data"},
        {"role": "user", "content": "write an sql querry to select all tables in the YoutubeDB"}
    ]
)

# Extract the SQL query generated by the assistant
sql_query = response.choices[0].message.content
print("Generated SQL Query:", sql_query)

# Execute the SQL query and print the results
execute_sql_query(sql_query)


