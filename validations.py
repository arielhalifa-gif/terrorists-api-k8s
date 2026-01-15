from models import Terrorists as Terr
import pandas as pd

class Functions:

    @staticmethod
    def validating_terr(top5):
        terr_list = []
        for terr in top5:
            terr_list.append(Terr(terr["name"], terr["location"], terr["danger_rate"]).__dict__())
        
        return terr_list