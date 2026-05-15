"""
初始化数据库和预设账户
"""
import sys
sys.path.insert(0, '.')

from app.core.database import Base, engine, SessionLocal, User
from app.core.security import get_password_hash

def init_db():
    """初始化数据库"""
    print("正在创建数据库表...")
    Base.metadata.create_all(bind=engine)
    print("数据库表创建完成")

def create_default_users():
    """创建默认用户"""
    db = SessionLocal()
    
    try:
        # 检查管理员是否已存在
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            admin = User(
                username="admin",
                email="admin@example.com",
                hashed_password=get_password_hash("Admin@123456"),
                is_active=True
            )
            db.add(admin)
            print("✅ 管理员账户已创建: admin / Admin@123456")
        else:
            print("ℹ️  管理员账户已存在")
        
        # 检查普通用户是否已存在
        user = db.query(User).filter(User.username == "testuser").first()
        if not user:
            user = User(
                username="testuser",
                email="test@example.com",
                hashed_password=get_password_hash("Test@123456"),
                is_active=True
            )
            db.add(user)
            print("✅ 普通用户账户已创建: testuser / Test@123456")
        else:
            print("ℹ️  普通用户账户已存在")
        
        db.commit()
        print("\n✅ 所有账户创建完成！")
        
    except Exception as e:
        db.rollback()
        print(f"❌ 创建账户失败: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("=" * 40)
    print("格式转换工具 - 数据库初始化")
    print("=" * 40)
    print()
    
    init_db()
    print()
    create_default_users()
    
    print()
    print("=" * 40)
    print("账户信息:")
    print("-" * 40)
    print("管理员: admin / Admin@123456")
    print("普通用户: testuser / Test@123456")
    print("=" * 40)
