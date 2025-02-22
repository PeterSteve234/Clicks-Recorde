import tkinter as tk
import time

# variáveis globais
contador = 0 
recorde = 0 
tempo_iniciado = 0 

# Função para iniciar a contagem de tempo
def iniciar_contagem():
    global contador, tempo_iniciado, recorde, botao, label_contador, label_recorde, botao_iniciar

    contador = 0 
    tempo_iniciado = time.time()    # Captura o tempo inicial
    botao.config(state=tk.NORMAL)   # Habilita o botão clique
    label_contador.config(text=f"Cliques: {contador}") # Reseta o contador visível
    label_recorde.config(text=f"Recorde: {recorde} cliques/minuto")  # Exibe o recorde atual

    # Desabilita o botão de iniciar até que o tempo acabe
    botao_iniciar.config(state=tk.DISABLED)

    # Inicia o cronômetro (exemplo de 60 segundos)
    janela.after(60000, finalizar_contagem)

# Função para contar os cliques
def contar_clique():
    global contador, recorde, tempo_iniciado
    contador += 1
    label_contador.config(text=f"Cliques: {contador}")  # Atualiza o contador na interface

    # Calcula os cliques por minuto
    tempo_decorrido = time.time() - tempo_iniciado
    cliques_por_minuto = (contador / tempo_decorrido) * 60

    # Verifica se o novo recorde foi batido
    if cliques_por_minuto > recorde:
        recorde = cliques_por_minuto
        label_recorde.config(text=f"Recorde: {int(recorde)} cliques/minuto")

# Função para finalizar a contagem
def finalizar_contagem():
    botao.config(state=tk.DISABLED)  # Desabilita o botão de clique ao finalizar

# Criando a janela principal
janela = tk.Tk()
janela.title("Contagem de Cliques")

# Configuração dos widgets
label_contador = tk.Label(janela, text=f"Cliques: {contador}", font=("Comic Sans", 15))
label_contador.pack(pady=20)

label_recorde = tk.Label(janela, text=f"Recorde: {recorde} cliques/minuto", font=("Comic Sans", 15))
label_recorde.pack(pady=20)

botao = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), state=tk.DISABLED, command=contar_clique)
botao.pack(pady=20)

botao_iniciar = tk.Button(janela, text="Iniciar", font=("Arial", 14), command=iniciar_contagem)
botao_iniciar.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
