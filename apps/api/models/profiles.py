from datetime import datetime
from typing import Optional
from sqlalchemy import String, ForeignKey, JSON, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    
    full_name: Mapped[Optional[str]] = mapped_column(String(255))
    location: Mapped[Optional[str]] = mapped_column(String(255))
    headline: Mapped[Optional[str]] = mapped_column(String(255))
    
    skills: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    experience: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    preferences: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship back to User
    user: Mapped["User"] = relationship("User", back_populates="profile")

    def __repr__(self) -> str:
        return f"<Profile(user_id={self.user_id}, full_name={self.full_name})>"
