from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

class InvitationBase(BaseModel):
    id: UUID
    inviter_id: UUID
    invitee_email: str
    qr_code_url: str
    status: str

class InvitationCreate(InvitationBase):
    pass

class InvitationRead(InvitationBase):
    
    inviter_id: UUID
    invitee_email: str
    status: str
    id: UUID
    qr_code_url: str

    class Config:
        orm_mode = True
        from_attributes = True

class InvitationEdit(BaseModel):
    status: str
    
class PaginationLinks(BaseModel):
    self: str
    next: Optional[str]
    prev: Optional[str]

class PaginatedInvitations(BaseModel):
    data: List[InvitationRead]
    _links: PaginationLinks