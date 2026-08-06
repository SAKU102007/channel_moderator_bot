import asyncpg
from config.bot_config import HOST, PASSWORD, USER, DB


async def create_admin(user_id, user_name):
    conn = await asyncpg.connect(host=HOST, password=PASSWORD, user=USER, database=DB)
    await conn.execute('''INSERT INTO users(user_id, user_role, user_name) VALUES($1, $2, $3)''',
                       user_id, 'admin', user_name)
    await conn.close()
    