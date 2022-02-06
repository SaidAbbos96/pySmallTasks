from decoratorio import async_analitic
import asyncio
import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, fumb_url):
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.fumb_url = fumb_url
        self.album_id = album_id

    @classmethod
    def from_json(cls, obj):
        print(obj)
        return Photo(obj["albumId"], obj["id"], obj["title"], obj["url"], obj["thumbnailUrl"])


def print_titles(photos):
    for photo in photos:
        print(f"{photo.title}", end="\n")


async def photos_by_album(task_name, album, session):
    print(f"{task_name=}")
    response = await session.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album}")
    photos_json = await response.json()
    return [Photo.from_json(photo) for photo in photos_json]


@async_analitic
async def main():
    # async with aiohttp.ClientSession() as session:
    #     photos = await photos_by_album("Task 1", 3, session)
    #     print_titles(photos)
    async with aiohttp.ClientSession() as session:
        photos = await asyncio.gather(*(photos_by_album(f"Task {i + 1}", album, session)
                                        for i, album in enumerate(range(2, 50))))
        photos_count = sum([len(list_photos) for list_photos in photos])
        print(photos_count)


if __name__ == "__main__":
    pass
    # asyncio.run(main())
    # xotoni ko'rmaslik uchun'
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()
