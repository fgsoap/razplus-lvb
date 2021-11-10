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

    def get_audio(self):
        pass

    def get_image(self):
        rs = self.session.get('https://www.raz-plus.com/projectable/' +
                              'book.php?id=2879&lang=1&type=book')
        page_number_list = re.findall(
            r"var displayPages = \[.*\]",
            rs.text)[0].split('= ')[-1].strip('[').strip(']').split(',')[3:-1]
        for i in page_number_list:
            r = self.session.get(
                'https://cf.content.raz-plus.com/raz_book_image/' +
                '2879/projectable/large/1/book/page-{}.jpg'.format(i),
                stream=True)
            if r.status_code == 200:
                with open('{}.jpg'.format(i), 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

    def concat_audios_and_images(self):
        pass

    def concat_videos(self):
        pass


if __name__ == '__main__':
    razplus = RazPlus('nutrokalmu', 'xZtDcCsP')
    s = razplus.login()

    lvb = LVB(s, 2879)
    lvb.get_image()
