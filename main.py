from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [#�ʐM����React��URL
    "https://vercel-ver2.vercel.app/",
    "https://vercel-zeta-six-42.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")#�f�t�H���g��URL��Get���N�G�X�g��������Ԃ����e
def Hello():
    return {"Hello":"World!"}
