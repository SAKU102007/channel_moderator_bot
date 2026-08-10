import asyncpg
from config.bot_config import HOST, PASSWORD, USER, DB


async def create_post(post_name, post_description, post_image, post_tag, user_name, create_date, create_time):
    conn = await asyncpg.connect(user=USER, database=DB, password=PASSWORD, host=HOST)
    await conn.execute(
        '''INSERT INTO posts(post_name, post_description, post_image, post_tag, user_name, create_date, create_time)
        VALUES($1, $2, $3, $4, $5, $6, $7)''',
        post_name, post_description, post_image, post_tag, user_name, create_date, create_time
    )
    await conn.close()
