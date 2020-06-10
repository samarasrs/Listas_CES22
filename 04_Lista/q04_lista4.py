import tkinter as tk


class Conta():
    def __init__(self, saldo, limite=1000):
        self.saldo = saldo
        self.limite = limite
        self.historico = ''

    def mod_saldo(self, valor):
        self.saldo = self.saldo + valor

    def verifica_saldo(self, valor):
        if (self.saldo + self.limite) >= valor:
            return True
        else:
            return False

    def saque(self, valor):
        if valor > 0:
            if self.verifica_saldo(valor):
                self.mod_saldo(-valor)

                self.historico = self.historico + 'saque: '+ str(valor)+"\n"

            else:
                self.historico = self.historico + 'saque - operação cancelada (saldo insuficiente)\n'
        else:
            self.historico = self.historico + 'saque - operação cancelada (valor inserido inválido)\n'

    def deposito(self, valor):
        if valor > 0:
            self.mod_saldo(valor)
            self.historico = self.historico + 'deposito:' +str(valor)+"\n"
        else:
            self.historico = self.historico + 'deposito - operação cancelada (valor inserido inválido)\n'

    def transferencia(self, valor):
        if valor > 0:
            if (self.saldo + self.limite) >= valor:
                self.mod_saldo(-valor)
                self.historico = self.historico + 'transferencia: '+ str(valor) +"\n"
            else:
                self.historico = self.historico +'transferencia - operação cancelada (saldo insuficiente)\n'
        else:
            self.historico = self.historico +'transferencia - operação cancelada (valor inserido inválido)\n'

    def mostrar_historico(self):
        return self.historico



class Saldo():
    def __init__(self, cliente):
        self.cliente = cliente

    def acao(self):
        return self.cliente.saldo


class Saque():
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def acao(self):
        return self.cliente.saque(self.valor)


class Deposito():
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def acao(self):
        return self.cliente.deposito(self.valor)

class Historico():
    def __init__(self, cliente):
        self.cliente = cliente

    def acao(self):
        return self.cliente.mostrar_historico()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_tela1()


    def create_tela1(self):
        # Campo
        self.ed1 = tk.Entry(self)
        self.ed1.insert(0, "Insira o valor")
        self.ed1.pack(pady=40)
        # Botao Saldo
        self.lb1 = tk.Label(self, text=' ')
        self.lb2 = tk.Label(self, text=' ')

        self.lb1.pack()
        self.lb2.pack()

        self.buttom_saldo = tk.Button(self, text="SALDO", command=self.get_saldo)
        self.buttom_saldo.pack(pady=10)
        # botao Saque
        self.buttom_saque = tk.Button(self, text="SAQUE", command=self.sacar)
        self.buttom_saque.pack(pady=10)
        # botao Deposito
        self.buttom_deposito = tk.Button(self, text="Deposito", command=self.deposito)
        self.buttom_deposito.pack(pady=10)
        self.buttom_historico = tk.Button(self, text=' ** Historico ** ', command=self.historico)
        self.buttom_historico.pack(pady=10)
        self.lb5 = tk.Label(self, text=' ')
        self.lb5.pack()
        # botao quit
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(pady=10)

    def get_saldo(self):
        self.lb1['text'] = "Valor do Saldo"
        self.num = Saldo(cliente).acao()
        self.lb2['text'] = self.num
        self.historico()

    def sacar(self):
        valor = int(self.ed1.get())
        Saque(cliente, valor).acao()
        if valor != "Insira o valor":
            self.ed1.delete(0, "end")
            self.ed1.insert(0, "Insira o valor")
        self.get_saldo()
        self.historico()

    def deposito(self):
        valor = int(self.ed1.get())
        Deposito(cliente, valor).acao()
        if valor != "Insira o valor":
            self.ed1.delete(0, "end")
            self.ed1.insert(0, "Insira o valor")
        self.get_saldo()
        self.historico()

    def historico(self):
        self.lb5['text'] = Historico(cliente).acao()



conta1 = Conta(1500)
cliente = conta1
root = tk.Tk()
root.geometry("800x600")
app = Application(master=root)
app.mainloop()
