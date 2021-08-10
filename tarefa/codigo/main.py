from os import setxattr
import pickle
from pydantic import BaseModel
from fastapi import FastAPI

class inputs(BaseModel):
    Sex:int
    Age:float
    Lifeboat:int
    Pclass:int

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo 
def titanic(features: inputs,Status:int,Message:str):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)   
    return({"survived":bool(titanic.predict([[features.Sex,features.Age,features.Lifeboat,features.Pclass]])[0]),"status":Status,"message":Message})


@app.get('/model')
def get():
    return {'hello':'test'}


