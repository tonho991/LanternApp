from threading import Thread
import time
from tkinter import *

class Lanterna:
  def __init__(self):
    self.estado = "desligado"

  def mudarEstado(self):
    if self.estado == 'desligado':
      self.estado = 'ligado'
    else:
      self.estado = 'desligado'

class Bateria:
  def __init__(self):
    self.carga = 100

  def consumo(self):
    global lb_carga
    while True:
      if lant.estado == 'ligado':
        time.sleep(1)
        if self.carga > 0:
            self.carga -= 1
            lb_carga = Label(janela, text=str(bat.carga) + "%")
            lb_carga.place(x=300, y=100)

  def trocarBateria(self):
    self.carga = 100
    lb_carga = Label(janela, text=str(bat.carga) + "%")
    lb_carga.place(x=300, y=100)

lant = Lanterna()
bat = Bateria()
consumo = Thread(target=bat.consumo)
consumo.start()

janela = Tk()
janela.geometry("500x300")

def bt_est_click():
  lant.mudarEstado()
  if bat.carga == 0 and lant.estado == 'ligado':
      lant.estado = 'desligado'
  lb_estado["text"] = lant.estado

  if lant.estado == "ligado":
    janela["bg"] = "white"
  else:
    janela["bg"] = "blue"

def bt_carg_click():
  bat.trocarBateria()

bt_estado = Button(janela, width=40, text="Ligar/Desligar", command=bt_est_click)
bt_estado.place(x=100, y=50)

bt_carga = Button(janela, width=40, text="Trocar Bateria", command=bt_carg_click)
bt_carga.place(x=100, y=100)

lb_estado = Label(janela, text=lant.estado)
lb_estado.place(x=300, y=50)

janela.title("Lanterna")
janela["bg"] = "blue"
janela.mainloop()
