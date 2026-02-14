import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import String, ForeignKey, JSON, DateTime, Enum, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class ToolCallStatus(str, enum.Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class ToolCall(Base):
    __tablename__ = "tool_calls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("workflow_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    step_id: Mapped[int] = mapped_column(ForeignKey("workflow_steps.id", ondelete="CASCADE"), nullable=False)
    
    connector: Mapped[str] = mapped_column(String(255), nullable=False)
    action: Mapped[str] = mapped_column(String(255), nullable=False)
    
    args_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    result_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    status: Mapped[ToolCallStatus] = mapped_column(Enum(ToolCallStatus), default=ToolCallStatus.PENDING, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    run: Mapped["WorkflowRun"] = relationship("WorkflowRun", back_populates="tool_calls")
    step: Mapped["WorkflowStep"] = relationship("WorkflowStep", back_populates="tool_calls")

    def __repr__(self) -> str:
        return f"<ToolCall(id={self.id}, connector={self.connector}, status={self.status})>"
