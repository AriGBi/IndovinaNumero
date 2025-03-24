import random
#si parte dal modello --> deve contenere la logica del gioco e basta
class Model(object):
    def __init__(self):
        self._NMAx=100 #numero massimi
        self._TMax=6 #numero di vite massimo
        self._T=self._TMax #T è il numero di vite rimanenti, quando inizio il gioco è uguale a Tmax
        self._segreto=None #è il numero segreto, quando creo il modello non so quanto vale

   #siccome nel controller chiamo NMax e Tmax (che però sono private), creo il getter
    @property
    def NMax(self):
     return self._NMAx

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

    #la classe modello ha bisogno di:
    #1) metodo che dice cosa succede quando inizio a giocare (reset)
    #2) metodo che uso quando gioco
    def reset(self):
        """
        questo metodo resetta il gioco in qualsiasi momento
        """
        self._segreto=random.randint(0,self._NMAx) #quando inizio a giocare setto il numero segreto
        self._T = self._TMax #setto le vite rimanenti al numero di vite MAX
        print(self._segreto)

    def play(self, guess):
        """Funzione che esegue uno step del gioco:da fuori ci arriva un tentativo (guess), confrontiamo il tentativo con il numero segreto. Il metodo deve dire: se ho vinto/perso/posso ancora giocare
        :param guess:int
        :return: ritorna 0 se ho vinto, -1 se il numero segreto è piu piccolo, 1 se il numero segreto è piu grande, 2 se ho finito le vite
        """
        self._T-=1 #per prima cosa decremento il numero di vite (a prescindere da se il numero è giusto o no)
        if self._segreto == guess:
            return 0 #scelgo di returnare 0 se ho vinto (scelta del programmatore)
        if self._T==0: #non ho vinto perchè non sono entrato nell'if precedente e non ho piu vite --> HO PERSO
            return 2 #ho perso definitivamente (scelta del programmatore)
        #se arrivo qui vuol dire che ho ancora tentativi e allora deve darmi degli inidizi
        if guess>self._segreto:
            return -1 #il numero segreto è piu piccolo del guess
        if guess<self._segreto:
            return 1 #il numero segreto è piu grande del guess


#provo a testare la classe
if __name__ == "__main__":
    #cioè se sto eseguendo la classe in modo stand alone
    m=Model()
    m.reset()
    print(m.play(80))
    print(m.play(10))

