import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.team import Base as TeamBase
from app.models.pack import Base as PackBase
from app.models.word import Base as WordBase
from app.models.settings import Base as SettingsBase
from app.api.v1.teams import router as teams_router
from app.api.v1.packs import router as packs_router
from app.api.v1.settings import router as settings_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TeamBase.metadata.create_all(bind=engine)
PackBase.metadata.create_all(bind=engine)
WordBase.metadata.create_all(bind=engine)
SettingsBase.metadata.create_all(bind=engine)

os.makedirs('static/avatars', exist_ok=True)
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(
    teams_router,
    prefix='/api/v1/teams',
    tags=['teams']
    )
app.include_router(
    packs_router,
    prefix='/api/v1/packs',
    tags=['packs']
    )
app.include_router(
    settings_router,
    prefix='/api/v1/settings',
    tags=['settings']
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
