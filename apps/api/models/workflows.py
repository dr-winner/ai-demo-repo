import enum
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, ForeignKey, JSON, DateTime, Enum, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

class RunState(str, enum.Enum):
    QUEUED = "queued"
    PLANNING = "planning"
    WAITING_APPROVAL = "waiting_approval"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"

class StepState(str, enum.Enum):
    PENDING = "pending"
    READY = "ready"
    RUNNING = "running"
    BLOCKED = "blocked"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    SKIPPED = "skipped"

class WorkflowRun(Base):
    __tablename__ = "workflow_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    intent: Mapped[str] = mapped_column(Text, nullable=False)
    risk_level: Mapped[str] = mapped_column(String(10), default="L0")  # L0, L1, L2, L3
    state: Mapped[RunState] = mapped_column(Enum(RunState), default=RunState.QUEUED, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="workflow_runs")
    steps: Mapped[List["WorkflowStep"]] = relationship("WorkflowStep", back_populates="run", cascade="all, delete-orphan")
    approvals: Mapped[List["Approval"]] = relationship("Approval", back_populates="run", cascade="all, delete-orphan")
    tool_calls: Mapped[List["ToolCall"]] = relationship("ToolCall", back_populates="run", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<WorkflowRun(id={self.id}, user_id={self.user_id}, state={self.state})>"

class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("workflow_runs.id", ondelete="CASCADE"), nullable=False, index=True)
    
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    depends_on: Mapped[Optional[list]] = mapped_column(JSON, default=list) # List of step IDs
    tool: Mapped[Optional[str]] = mapped_column(String(255))
    
    state: Mapped[StepState] = mapped_column(Enum(StepState), default=StepState.PENDING, nullable=False)
    attempt: Mapped[int] = mapped_column(Integer, default=0)
    
    result_ref: Mapped[Optional[str]] = mapped_column(String(255))
    error_message: Mapped[Optional[str]] = mapped_column(Text)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    run: Mapped["WorkflowRun"] = relationship("WorkflowRun", back_populates="steps")
    approvals: Mapped[List["Approval"]] = relationship("Approval", back_populates="step")
    tool_calls: Mapped[List["ToolCall"]] = relationship("ToolCall", back_populates="step")

    def __repr__(self) -> str:
        return f"<WorkflowStep(id={self.id}, name={self.name}, state={self.state})>"
