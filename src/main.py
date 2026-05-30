from fastapi import FastAPI
import structlog

logger = structlog.get_logger()
app = FastAPI(title="O.N.I.O.N Framework", version="0.1.0")

@app.get("/")
async def root():
    logger.info("system_access", status="active", layer="root")
    return {"status": "O.N.I.O.N Active", "mode": "Zero-Trust Safety-First Integration"}
