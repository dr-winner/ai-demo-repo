from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import health, users, workflows

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.APP_VERSION,
    description="Life OS — AI-powered workflow orchestration API",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router)
app.include_router(users.router, prefix="/api/v1")
app.include_router(workflows.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
