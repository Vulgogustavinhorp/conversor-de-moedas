import tkinter as tk
from tkinter import messagebox
import requests

def converter():
    try:
        valor = float(entry_valor.get())
        moeda_base = "USD"
        moeda_destino = moeda_var.get()

        # Chamada à API pública
        url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_base}&to={moeda_destino}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            convertido = dados['rates'][moeda_destino]
            resultado_label.config(text=f"{valor:.2f} {moeda_base} = {convertido:.2f} {moeda_destino}")
        else:
            messagebox.showerror("Erro", "Não foi possível obter os dados.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

# Interface com tkinter
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("300x200")

tk.Label(janela, text="Valor em USD:").pack(pady=5)
entry_valor = tk.Entry(janela)
entry_valor.pack()

tk.Label(janela, text="Moeda de destino:").pack(pady=5)
moeda_var = tk.StringVar(janela)
moeda_var.set("BRL")
moedas_disponiveis = ['BRL', 'EUR', 'GBP', 'JPY', 'ARS', 'CAD']
tk.OptionMenu(janela, moeda_var, *moedas_disponiveis).pack()

tk.Button(janela, text="Converter", command=converter).pack(pady=10)
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()