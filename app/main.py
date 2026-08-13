from fastapi import FastAPI

from app.routers import admin, contact, courses

app = FastAPI(
    title="JP Solutions DevOps Lab",
    description="Laboratório educacional de práticas DevOps",
    version="1.0.0",
)

app.include_router(courses.router)
app.include_router(contact.router)
app.include_router(admin.router)


@app.get("/health")
def health():
    # BUG INTENCIONAL SUTIL:
    # A rota responde 200, porém o corpo contradiz o estado esperado.
    return {"status": "offline"}
