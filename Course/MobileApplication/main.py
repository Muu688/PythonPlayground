from datetime import datetime
import imp
import pathlib
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class LoginScreen(Screen): # LoginScreen inherits from Screen
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        if username in users and users[username]['password'] == password:
            self.manager.transition.direction = 'left'
            self.manager.current = 'login_success_screen'
        else:
            self.ids.loginfailed.text = "Username or Password Incorrect!"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        users[username] = {'username' : username, 'password' : password,
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        # print(users)

        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = 'sign_up_success_screen'

class SignUpSuccessScreen(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class LoginSuccessScreen(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob('quotes/*.txt')
        print(available_feelings)

        available_feelings = [Path(filename).stem for filename in available_feelings]
        print(available_feelings)

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling..."            

class ImageButton(HoverBehavior, Image, ButtonBehavior):
    pass

class MainApp(App):
    def build(self):
        return RootWidgeqt()

if __name__ == "__main__":
    MainApp().run()