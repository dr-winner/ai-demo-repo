# Life OS API — Operations Manual

This is a production-grade FastAPI backend for the Life OS system.

## Setup Instructions

### 1. Database Setup
Ensure you have a PostgreSQL database running. You can create the database with:
```bash
createdb life_os
```

### 2. Environment Configuration
Create a `.env` file in `apps/api/` (it has been pre-created for you, but adjust as needed):
```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/life_os
REDIS_URL=redis://localhost:6379/0
```

### 3. Run Migrations
Apply the initial migration to create the tables:
```bash
alembic upgrade head
```

### 4. Start the Server
Run the FastAPI application:
```bash
python main.py
```
Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

## API Documentation
Once the server is running, visit:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

## Project Structure
- `main.py`: Application entrypoint.
- `db.py`: Database engine and session management.
- `config.py`: Configuration and environment handling.
- `models/`: SQLAlchemy 2.0 ORM models.
- `routers/`: FastAPI route handlers grouped by domain.
- `migrations/`: Alembic migration history.
