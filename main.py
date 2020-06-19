from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.loader import Loader
from kivy.uix import screenmanager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineListItem, OneLineListItem, OneLineAvatarListItem, ImageLeftWidget
import sqlite3
from datetime import datetime
from kivy.uix.image import Image

dataconnection = sqlite3.connect('remedios.db')
cursor = dataconnection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS LEMBRAIME (data TEXT, tomado INTEGER)')
dataconnection.commit()
tudo = cursor.execute('''
SELECT * FROM LEMBRAIME
''').fetchall()

dataconnection.close()

lista_remedios = []
comprimidos_tomados = []
lista_remedios = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-feira", "Sábado", "Domingo"]

switcher = {
            1: "Segunda-Feira",
            2: "Terça-Feira",
            3: "Quarta-Feira",
            4: "Quinta-Feira",
            5: "Sexta-feira",
            6: "Sábado",
            7: "Domingo"
        }

class Main(Screen):

    def on_enter(self):
        Clock.schedule_once(self.verificar_tomado)


    def verificar_tomado(self,dt):

        try:
            for i in tudo:
                for e in self.ids.dias.children:
                    # print(e.children[0].text)
                    if i[0] == e.children[0].text:
                        e.children[1].icon = 'img/remedio tomado.jpg'

        except Exception as e:
            print(e)


    def remedio_tomado(self,dia):

        try:
            dataconnection1 = sqlite3.connect('remedios.db')
            cursor1 = dataconnection1.cursor()
            cursor1.execute('''
            INSERT INTO LEMBRAIME VALUES (?,?)
            ''',(dia,1))
            dataconnection1.commit()
            dataconnection1.close()

        except Exception as e:
            dataconnection = sqlite3.connect('remedios.db')
            cursor = dataconnection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS LEMBRAIME (data TEXT, tomado INTEGER)')
            dataconnection.commit()
            dataconnection.close()

    def resetar_semana(self):
        dataconnection1 = sqlite3.connect('remedios.db')
        cursor1 = dataconnection1.cursor()
        cursor1.execute('DROP TABLE LEMBRAIME')
        dataconnection1.commit()
        dataconnection1.close()
        print('Semana Resetada')


class AddPills(Screen):
    pass


class Remedios(Screen):
    def lista_remedios(self):
        pass

class LembreimeApp(MDApp):
    def build(self):
        KV = Builder.load_file('lembrei.kv')
        return KV

    # def on_start(self):
    #     Main.verificar_tomado(Main)
if __name__ == '__main__':
    LembreimeApp().run()


