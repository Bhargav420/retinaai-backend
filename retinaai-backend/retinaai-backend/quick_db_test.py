from sqlalchemy import create_engine, text

DB_URL = "mysql+pymysql://root:@127.0.0.1:3306/retinaai"

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM user LIMIT 1;"))
        row = result.fetchone()
        if row:
            print("✅ User table is accessible. First user:", row)
        else:
            print("⚠️ User table is empty or not accessible.")
except Exception as e:
    print("❌ Query failed:", e)