import asyncpg
from config.bot_config import HOST, PASSWORD, DB, USER

async def get_post_name(post_id):
    conn = await asyncpg.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
    row = await conn.fetchrow("SELECT post_name FROM posts WHERE id = $1", post_id)
    await conn.close()

    if row is None:
        return 'None'
    else:
        return row
