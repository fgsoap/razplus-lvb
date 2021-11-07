import requests, shutil


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
        r = self.session.get(
            'https://cf.content.raz-plus.com/raz_book_image/2879/projectable/large/1/book/page-3.jpg',
            stream=True)
        if r.status_code == 200:
            with open('2879.jpg', 'wb') as f:
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
