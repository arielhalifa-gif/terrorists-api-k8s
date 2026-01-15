from models import Terrorists as Terr
import pandas as pd

class Functions:

    @staticmethod
    def validating_terr(top5: dict):
        terr_list = []
        for terr in top5:
            temp_terrorist = Terr(name=terr["name"], location=terr["location"], danger_rate=terr["danger_rate"])
            terr_list.append(temp_terrorist.__dict__())
        
        return terr_list