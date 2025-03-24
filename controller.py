from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNMax(self):
       return self._model.NMax

    def getTMax(self):
        return self._model.TMax

    def reset(self,e):
        """
        resetta il modello e anche l'interfaccia (metto le vite rimanenti VISUALIZZATE uguali al massimo e tolgo le scritte della lv della aprtita precedente)
        :param e:
        :return:
        """
        self._model.reset()
        self._view._txtOutT.value=self._model.T
        self._view._lv.controls.clear()
        self._view.btnPlay.disabled=False
        self._view._txtIn.disabled=False
        self._view._lv.controls.append(ft.Text("Indovina a quale numero sto pensando!"))
        self._view.update()

    def play(self, e):
        tentativoStr=self._view._txtIn.value #salvo il tentativo che ha fatto l'utente
        self._view._txtIn.value="" #svuoto il punto dove l'utente scrive il numero
        self._view._txtOutT.value=self._model.T -1
        if tentativoStr=="":
            self._view._lv.controls.append(ft.Text("Attenzione, inserisci un valore numerico da testare", color="red"))
            self._view.update()
            return #non ha senso andare avanti
        try:
            tentativoInt= int(tentativoStr) #non funziona se l'utente non mette un numero INTERO
        except ValueError:
            self._view._lv.controls.append(ft.Text("Attenzione, valore inserito non è un intero", color="red"))
            return
        #se va tutto bene, posso giocare e quindi chiamare il play del model
        res= self._model.play(tentativoInt) #in res salvo i return del metodo play
        if res==0: #ho vinto
           self._view._lv.controls.append(ft.Text(f"Fantastico! hai vinto, il segreto era {tentativoInt}", color="green"))
           self._view.btnPlay.disabled = True #se ho vinto, disabilito la possibilità di GIOCARE senza aver resettato
           self._view._txtIn.disabled=True
           self._view.update()
           return
        elif res==2: #ho finito tutte le vite
            self._view._lv.controls.append(
                ft.Text(f"Mi dispiace hai finito le vite. Il numero segreto era {self._model.segreto}"))
            self._view.btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res==-1: #il numero segreto è piu piccolo
            self._view._lv.controls.append(ft.Text(f"Il numero segreto è piu piccolo di {tentativoInt} " ))
            #non disabilito nulla perchè devo contiunare a giocare
            self._view.update()
        else: #il numero segreto è piu grande
            self._view._lv.controls.append(ft.Text(f"Il numero segreto è piu grande di {tentativoInt} "))
            self._view.update()


