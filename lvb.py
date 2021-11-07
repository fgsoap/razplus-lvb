import requests


class RazPlus(object):
    def __init__(self, username, password):
        self.username = username
        self.passowrd = password

    def login(self):
        r = requests.post('https://www.raz-plus.com/auth/login.php',
                          data={
                              'username': self.username,
                              'password': self.passowrd
                          },
                          allow_redirects=True)
        print(r.status_code)


class LVB(object):
    def get_audio():
        pass

    def get_image():
        pass

    def concat_audios_and_images():
        pass

    def concat_videos():
        pass


if __name__ == '__main__':
    razplus = RazPlus('', '')
    razplus.login()
