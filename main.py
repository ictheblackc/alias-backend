import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.teams import router as teams_router
from app.database import engine
from app.models.team import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

os.makedirs('static/avatars', exist_ok=True)
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(teams_router, prefix='/api/v1/teams')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
