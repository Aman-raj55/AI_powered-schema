from fastapi import FastAPI
from pydantic import BaseModel
from schema_loader import load_schema
from query_processor import process_query

app = FastAPI()
schema = load_schema("data/database_schema.json")

class QueryRequest(BaseModel):
    query: str

@app.post("/filter-tables/")
async def filter_tables(request: QueryRequest):
    selected_tables = process_query(request.query, schema)
    return {"filtered_schema": selected_tables}

# Run with: uvicorn main:app --reload