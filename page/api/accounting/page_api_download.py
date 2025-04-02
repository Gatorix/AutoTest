import requests

from utils.file_utils import get_project_path


class PageApiDownload:
    @staticmethod
    def page_api_download(links: str, path=rf'{get_project_path()}\download_tmp', specific_filename=None):
        res = requests.get(links)

        filename = specific_filename or links.split('/')[-1]

        with open(rf'{path}\{filename}',
                  'wb') as download_file:
            for bl in res.iter_content(chunk_size=1024):
                if all([
                    bl,
                    '"status":402' not in str(bl),
                    '502 Bad Gateway' not in str(bl)
                ]):
                    download_file.write(bl)
                else:
                    raise Exception(f'下载失败: {bl.decode("utf-8")}')
