import threading
import time
from asyncio import CancelledError, FIRST_EXCEPTION
import asyncio
import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'task_name = {task_name}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = await session.get(url)
    photos_json = await response.json()

    sleeping_period = 3 if task_name == 't3' else 1
    print(f'task name = {task_name} sleeping')
    await asyncio.sleep(sleeping_period)
    print(f'task name = {task_name} finished sleeping')

    print(f'Finished task = {task_name}')
    return [Photo.from_json(photo) for photo in photos_json]


async def main_wait():
    async with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('t3', 3, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t4', 4, session),
        ]

        photos = []
        done_tasks, pending_tasks = await asyncio.wait(tasks)

        for pending_task in pending_tasks:
            print(f'Cancelling {pending_task}')
            print(pending_tasks.cancel())

        for done in done_tasks:
            try:
                result = done.result()
                photos.extend(result)
            except Exception as ex:
                print(repr(ex))

if __name__ == '__main__':
    asyncio.run(main_wait())

    print('main ended')
