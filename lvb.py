import re
import shutil

import requests


class RazPlus(object):
    def __init__(self, username, password):
        self.username = username
        self.passowrd = password

    def login(self):
        s = requests.Session()
        r = s.post('https://www.raz-plus.com/auth/login.php',
                   data={
                       'username': self.username,
                       'password': self.passowrd
                   },
                   allow_redirects=True)
        if r.status_code == 200:
            return s
        else:
            raise Exception('Bad Response!')


class LVB(object):
    def __init__(self, session, id):
        self.session = session
        self.id = id

    def get_images_and_audios(self):
        rs = self.session.get(
            'https://www.raz-plus.com/projectable/book.php?id={}&lang=1&type=book'
            .format(self.id))
        page_number_list = re.findall(
            r"var displayPages = \[.*\]",
            rs.text)[0].split('= ')[-1].strip('[').strip(']').split(',')[3:-1]
        download(
            'https://cf.content.raz-plus.com/raz_book_image/{}/projectable/large/1/book/page-{}.jpg',
            page_number_list, self.session, self.id, 'jpg')
        download(
            'https://cf.content.raz-plus.com/audio/{}/raz_afterschool_lb65_p{}_text.mp3',
            page_number_list, self.session, self.id, 'mp3')

    def concat_audios_and_images(self):
        pass

    def concat_videos(self):
        pass


def download(url, list, session, id, type):
    for i in list:
        r = session.get(url.format(id, i), stream=True)
        if r.status_code == 200:
            with open('{}.{}'.format(i, type), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)


if __name__ == '__main__':
    razplus = RazPlus('lirdorogni', 'OMBlvqdI')
    s = razplus.login()

    lvb = LVB(s, 2879)
    lvb.get_images_and_audios()
