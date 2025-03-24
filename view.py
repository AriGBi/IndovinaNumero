import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        #creo tutti gli oggetti grafici che servono
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        self._txtOutNmax= ft.TextField(label="Numero Max", disabled=True, width=200, value=self._controller.getNMax()) #non voglio che venda modificato dallo user --> disabled=True
        self._txtOutTMax= ft.TextField(label="Tentativi Max ", disabled=True, width=200, value=self._controller.getTMax()) #metto le tonde dopo il metodo del controller per SALVARE il return
        self._txtOutT=ft.TextField(label="Tentativi Rimanenti", disabled =True, width=200)

        self._txtIn=ft.TextField(label="Tentativo", width=200)
        self._btnReset= ft.ElevatedButton(text="Nuova Partita", width=200, on_click=self._controller.reset) #non metto le parentesi dopo il metodo del controller perchè voglio semplicemente ESEGIRLO, non salvarmi il return
        self.btnPlay=ft.ElevatedButton(text="Gioca", width=200, on_click=self._controller.play)

        self._lv=ft.ListView(expand=True) #expand permette di scrollare

        #metto gli oggetti in delle righe/container
        row1=ft.Container(self._titolo, alignment=ft.alignment.center) #metto il titolo in un container perchè c'è solo lui nella riga
        row2=ft.Row([self._txtOutNmax, self._txtOutTMax,self._txtOutT], alignment= ft.MainAxisAlignment.CENTER)
        row3=ft.Row([self._btnReset,self._txtIn, self.btnPlay], alignment= ft.MainAxisAlignment.CENTER )

        #aggiungo le righe/container alla pagina
        self._page.add(row1, row2, row3,self._lv)

        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        """
        serve solo per non dover scrivere tutte le volte self._page.update()
        :return:
        """
        self._page.update()
