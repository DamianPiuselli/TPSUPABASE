import os
from supabase import create_client, Client
import requests


def create_tables_from_sql_files(
    supabase_url: str, supabase_key: str, sql_file_paths: list
):
    # Function to read the SQL file
    def read_sql_file(file_path: str) -> str:
        with open(file_path, "r") as file:
            return file.read()

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
    }

    for sql_file in sql_file_paths:
        sql_command = read_sql_file(sql_file)
        try:
            response = requests.post(
                f"{supabase_url}/rest/v1/rpc",
                headers=headers,
                json={"sql": sql_command},
            )
            if response.status_code == 200 or response.status_code == 201:
                print(f"Table created successfully from {sql_file}")
            else:
                print(f"Failed to create table from {sql_file}: {response.text}")
        except Exception as e:
            print(f"An error occurred while creating table from {sql_file}: {e}")


# Example usage
if __name__ == "__main__":
    SUPABASE_URL = "https://zqvvljiwpsqzxnabqzdb.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpxdnZsaml3cHNxenhuYWJxemRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTcwMDQ4NjAsImV4cCI6MjAzMjU4MDg2MH0.BmST_0FGsdGcsYSAFVd3y5cCOMaFAE_ythCiAYjsE_o"

    sql_file_paths = [
        rf"sql_queries\dim_category.sql",
        rf"sql_queries\dim_item.sql",
        rf"sql_queries\fact_sales.sql",
        rf"sql_queries\fact_wholesale.sql",
    ]

    create_tables_from_sql_files(SUPABASE_URL, SUPABASE_KEY, sql_file_paths)
