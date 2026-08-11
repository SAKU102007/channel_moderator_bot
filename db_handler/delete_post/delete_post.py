import asyncpg
from config.bot_config import HOST, PASSWORD, USER, DB


async def delete_post(post_id):
    conn = await asyncpg.connect(host=HOST, password=PASSWORD, user=USER, database=DB)
    await conn.execute('''DELETE FROM posts WHERE id=$1''', post_id)
    await conn.close()
