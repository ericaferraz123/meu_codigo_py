import tkinter as tk  # noqa: F403
from telas.app_gui import ClienteApp # type: ignore

if __name__ == "__main__":
    janela = tk.Tk()  # noqa: F405
    app = ClienteApp (janela)
    janela.mainloop()