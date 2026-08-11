import asyncpg
from config.bot_config import HOST, PASSWORD, USER, DB


async def change_post(post_name, post_description, post_image, post_tag,
                      change_user_name, change_date, change_time, post_id):
    conn = await asyncpg.connect(user=USER, database=DB, password=PASSWORD, host=HOST)
    await conn.execute('''UPDATE posts SET post_name=$1, post_description=$2, post_image=$3,
                       post_tag=$4, change_user_name=$5, change_data=$6, change_time=$7 WHERE id=$8''',
                       post_name, post_description, post_image, post_tag,
                       change_user_name, change_date, change_time, post_id)
    await conn.close()
