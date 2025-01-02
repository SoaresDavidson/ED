import tkinter as tk
from tkinter import ttk
import binarytree
from tkinter import messagebox


def draw_tree(canvas, tree, node, x, y, offset_x, offset_y):
    if node is not None:
        radius = 20
        death_left = 0 if node.left is None else node.left.height()
        death_right = 0 if node.right is None else node.right.height()
        canvas.create_text(x, y - 10, text=str(node.key), font=('Arial', 14, 'bold'), fill='darkgreen')
        canvas.create_text(x+30, y + 10, text=f"{death_right - death_left}", font=('Arial', 12, 'bold'), fill='darkblue')
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='lightgreen', outline='green', width=0.8)
        canvas.create_text(x, y, text=str(node.key), font=('Arial', 14, 'bold'), fill='darkgreen')


        if node.left:
            canvas.create_line(x, y + radius, x - offset_x, y + offset_y, arrow=tk.LAST, fill='lightgreen', width=1)
            draw_tree(canvas, tree, node.left, x - offset_x, y + offset_y, offset_x // 1.25, offset_y)

        if node.right:
            canvas.create_line(x, y + radius, x + offset_x, y + offset_y, arrow=tk.LAST, fill='lightgreen')
            draw_tree(canvas, tree, node.right, x + offset_x, y + offset_y, offset_x // 1.25, offset_y)



def main():
    def mostrar_messagebox_personalizada(titulo, mensagem,cor):
        messagebox_personalizada = tk.Toplevel(root)
        messagebox_personalizada.title(titulo)
        messagebox_personalizada.geometry("400x200")
        messagebox_personalizada.configure(bg=cor)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = 50
        position_right = 70
        messagebox_personalizada.geometry(f"400x200+{position_right}+{position_top}")

        label = ttk.Label(messagebox_personalizada, text=mensagem, font=("Arial", 12), background=cor, justify="left")
        label.pack(pady=20)
        btn_ok = ttk.Button(messagebox_personalizada, text="OK", command=messagebox_personalizada.destroy, style="TButton")
        btn_ok.pack(pady=5)
        style = ttk.Style()
        style.configure("TButton",
                        padding=6,
                        relief="flat",
                        background="lightgreen",
                        font=("Arial", 10),
                        width=10)
        messagebox_personalizada.transient(root)
        messagebox_personalizada.grab_set()
    def inserir_valor():
        try:
            valor = int(entry_valor.get())
            tree.insert(valor)
            messagebox.showinfo("Sucesso", f"Valor {valor} inserido com sucesso!")
            entry_valor.delete(0, tk.END)
            atualizar_canvas()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
            entry_valor.delete(0, tk.END)

    def verificar_balanceamento():
        balanced = binarytree.isAVL(tree.root)
        if balanced:
            messagebox.showinfo("Árvore Balanceada", "A árvore está balanceada!")
        else:
            messagebox.showwarning("Árvore Não Balanceada", "A árvore não está balanceada!")
    def mostrar_informacoes():
        try:
            altura = tree.heightT()-1
            menor = tree.min()
            maior = tree.max()
            comprimento_interno = tree.internalPathLength()
            tamanho = tree.sizes()
            info = f"Tamanho: {tamanho}\nAltura: {altura}\nMenor elemento: {menor}\nMaior elemento: {maior}\nComprimento Interno: {comprimento_interno}"
            mostrar_messagebox_personalizada("Informações da Árvore", info,'lightblue')
        except Exception as e:
            mostrar_messagebox_personalizada("Erro", "A árvore está vazia!",'lightcoral')

    def mostrar_percursos():
        try:
            percursos = (
                f"Em Ordem: {'=>'.join(map(str,tree.emOrdem()))}",
                f"Pós Ordem: {'=>'.join(map(str,tree.posOrdem()))}",
                f"Pré Ordem: {'=>'.join(map(str,tree.preOrdem()))}",
                f"Busca em Largura: {'=>'.join(map(str,tree.levelOrder()))}"
            )
            mostrar_messagebox_personalizada("Percursos da Árvore", "\n".join(percursos),'lightblue')
        except Exception as e:
            mostrar_messagebox_personalizada("Erro", "A árvore está vazia!",'lightcoral')
        

    def atualizar_canvas():
        canvas.delete("all")
        draw_tree(canvas, tree, tree.root, 640, 20, 125, 60)
        altura = tree.heightT()
        novo_altura_canvas = max(400, altura * 65)  
        canvas.config(scrollregion=(0, 0, 600, novo_altura_canvas))
        
        root.geometry(f"700x{max(novo_altura_canvas + 100, 500)}") 

    
    root = tk.Tk()
    root.title("Árvore Binária")
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", root.attributes("-fullscreen", True))
    largura = root.winfo_screenwidth()
    altura = root.winfo_screenheight()
    root.state('iconic')
    root.geometry(f"{altura}x{largura}")
    root.configure(bg='lightblue')
    #imagem = tk.PhotoImage(file='C:/Users/kauan/Documents/Code/mytkinter/exemplos/icons/download.png')

    tree = binarytree.BinaryTree()

 
    frame_entrada = tk.Frame(root, bg='lightblue')
    frame_entrada.pack(pady=20)

    label_valor = tk.Label(frame_entrada, text="Insira um valor:", bg='lightblue', font=('Arial', 12))
    label_valor.grid(row=0, column=0, padx=5)

    entry_valor = tk.Entry(frame_entrada, font=('Arial', 12))
    entry_valor.grid(row=0, column=1, padx=5)

    btn_inserir = tk.Button(frame_entrada, text="Inserir", command=inserir_valor, bg='lightgreen', font=('Arial', 12))
    btn_inserir.grid(row=0, column=2, padx=5)

    def press_button(event):
        btn_inserir.invoke()

    entry_valor.bind('<Return>', press_button)    

    btn_verificar_balanceamento = tk.Button(root, text="Verificar Balanceamento", command=verificar_balanceamento, bg='lightyellow', font=('Arial', 12))
    btn_verificar_balanceamento.pack(pady=10)
    btn_mostrar_info = tk.Button(root, text="Mostrar Informações", command=mostrar_informacoes, bg='lightyellow', font=('Arial', 12))
    btn_mostrar_info.pack(pady=10)

    btn_mostrar_percursos = tk.Button(root, text="Mostrar Percursos", command=mostrar_percursos, bg='lightyellow', font=('Arial', 12))
    btn_mostrar_percursos.pack(pady=10)
    frame_canvas = tk.Frame(root)
    frame_canvas.pack(pady=10)

    canvas = tk.Canvas(frame_canvas, width=1280,height=720,bg='white')
    #canvas.create_image(0, 0, anchor="nw", image=imagem)
    canvas.grid(row=0, column=0)

    scrollbar = tk.Scrollbar(frame_canvas, orient='vertical', command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')

    canvas.config(yscrollcommand=scrollbar.set)
    
    canvas.config(scrollregion=canvas.bbox("all"))
    def scroll_canvas(event):
        if event.delta > 0: 
            canvas.yview_scroll(-1, "units")
        else:  
            canvas.yview_scroll(1, "units")

    root.bind("<MouseWheel>", scroll_canvas)
    canvas.config(scrollregion=canvas.bbox("all"))
    atualizar_canvas()
    label_instrucoes = tk.Label(frame_entrada, text="Digite um número e clique em 'Inserir' para adicionar à árvore.", bg='lightblue', font=('Arial', 10))
    label_instrucoes.grid(row=1, column=1, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
