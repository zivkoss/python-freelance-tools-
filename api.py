from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import pandas as pd
import io
import tempfile
import os

app = FastAPI()

def clean_csv(df, sort_col="price"):
    """Inline CSV cleaner функција"""
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.sort_values(by=sort_col)
    return df

@app.get("/")
def home():
    return {"message": "🚀 API ради! POST /clean-csv"}

@app.post("/clean-csv")
async def clean_csv_api(file: UploadFile = File(...), sort_col: str = Form("price")):
    # Чита CSV
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    
    # ЧИСТИ
    df_clean = clean_csv(df, sort_col)
    
    # Креира CSV у меморији
    output = io.StringIO()
    df_clean.to_csv(output, index=False)
    output.seek(0)
    
    # Враћа фајл
    return FileResponse(
        io.BytesIO(output.getvalue().encode()),
        filename=f"cleaned_{file.filename}",
        media_type='text/csv'
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
