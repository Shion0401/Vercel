from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [#�ʐM����React��URL
    "http://localhost:3001",
    "https://dashboard.heroku.com/apps/serene-bastion-94289",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")#�f�t�H���g��URL��Get���N�G�X�g��������Ԃ����e
def Hello():
    return {"Hello":"World!"}
