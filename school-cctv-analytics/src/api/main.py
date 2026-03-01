from fastapi import FastAPI
from .routes import auth, cameras, alerts, faces

app = FastAPI(title="School CCTV Analytics API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(cameras.router, prefix="/cameras", tags=["Cameras"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(faces.router, prefix="/faces", tags=["Faces"])

@app.get("/")
def read_root():
    return {"message": "Welcome to School CCTV Analytics API"}
