
from httpx import AsyncClient
from fastapi import FastAPI
import pytest
from app.main import app  # Import your FastAPI app
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import sessionmaker
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_send_invitation_success(db_session):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        inviter_id = "b077ee0a-6d37-4bc5-b0cc-5aa9f8d9be14"
        invitee_email = "test@example.com"
        response = await ac.post("/send-invitation/", json={"inviter_id": inviter_id, "invitee_email": invitee_email})
        assert response.status_code == 200
        assert response.json() == {"message": "Invitation has been sent successfully!", "qr_code_url": "some_url"}