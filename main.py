from fastapi import fastAPI, UploadFile
from validations import Functions as f
from db import Connection
import pandas as pd

app = fastAPI()


@app.post("/top-threats")
def top_5_threats(file: UploadFile):
    df = pd.read_csv(file.file)
    top_5 = df.sort_values(by = ["danger_rate"], ascending = False).head()
    validate_top_5 = f.validating_terr(top_5)
    result =Connection.insert_to_db(validate_top_5)
    return {"count": len(validate_top_5),
            "top": validate_top_5}