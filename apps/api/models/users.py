import enum
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Boolean, DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class UserRole(str, enum.Enum):
    OWNER = "owner"
    ADMIN = "admin"
    VIEWER = "viewer"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.VIEWER, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", cascade="all, delete-orphan", uselist=False)
    workflow_runs: Mapped[List["WorkflowRun"]] = relationship("WorkflowRun", back_populates="user")
    decided_approvals: Mapped[List["Approval"]] = relationship("Approval", back_populates="decided_by_user")

    def __repr__(self) -> str:
        return f"<User(email={self.email}, role={self.role})>"
