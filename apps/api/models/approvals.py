import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import String, ForeignKey, DateTime, Enum, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class ApprovalStatus(str, enum.Enum):
    REQUIRED = "required"
    APPROVED = "approved"
    REJECTED = "rejected"

class Approval(Base):
    __tablename__ = "approvals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("workflow_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    step_id: Mapped[Optional[int]] = mapped_column(ForeignKey("workflow_steps.id", ondelete="CASCADE"), nullable=True)
    
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[ApprovalStatus] = mapped_column(Enum(ApprovalStatus), default=ApprovalStatus.REQUIRED, nullable=False)
    
    decided_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    decided_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    # Relationships
    run: Mapped["WorkflowRun"] = relationship("WorkflowRun", back_populates="approvals")
    step: Mapped[Optional["WorkflowStep"]] = relationship("WorkflowStep", back_populates="approvals")
    decided_by_user: Mapped[Optional["User"]] = relationship("User", back_populates="decided_approvals")

    def __repr__(self) -> str:
        return f"<Approval(id={self.id}, run_id={self.run_id}, status={self.status})>"
