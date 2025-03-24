import flet as ft
from controller import Controller
from view import View
#main istanzia la classe view, crea un controller a cui passa la classe View e poi dice alla View qual è il suo controller
#dopodichè runna l'interfaccia grafica
def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c)
    v.caricaInterfaccia()

ft.app(target=main)
