from flask import Flask
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class stocklist(Resource):
    def get(self):
        stockdict = []
        for i in df.values:
            if i[1]<1200:
                if i[11]>8 and i[11]<16:
                    if(abs(i[9])<abs(i[10])):
                        stockdict.append([f"{i[0]}:Buy"])                        
                    else:
                        stockdict.append([f"{i[0]}:Sell"])
                       
        return {"List":stockdict} 

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1s13ccrWmW_i-Rj5njxJypSXpUY70pDtgJc1S8_6085o/export?format=csv")
stockdict = []; 
       

api.add_resource(stocklist,"/stocklist")

if __name__ == "__main__":
    app.run(debug=True)
