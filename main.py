from fastapi import FastAPI, UploadFile
from validations import Functions as f
from db import Connection
import pandas as pd
import uvicorn

app = FastAPI()


@app.post("/top-threats")
def top_5_threats(file: UploadFile):
    df = pd.read_csv(file.filename)
    top_5 = df.sort_values(by = ["danger_rate"], ascending = False).head()
    # validate_top_5 = f.validating_terr(top_5.to_dict)
    result =Connection.insert_to_db(top_5)
    return {"count": len(top_5),
            "top": [top_5.to_json]}


if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = "8000")