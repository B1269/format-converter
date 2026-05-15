"""
数据库模型 - 同步版本
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

Base = declarative_base()

# 同步引擎
engine = create_engine(DATABASE_URL.replace("+aiosqlite", ""), connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class User(Base):
    """用户表"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User {self.username}>"


class ConversionRecord(Base):
    """转换记录表"""
    __tablename__ = "conversion_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    file_name = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)
    input_format = Column(String(20))
    output_format = Column(String(20))
    input_size = Column(Integer)
    output_size = Column(Integer)
    status = Column(String(20), default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<ConversionRecord {self.file_name}>"
