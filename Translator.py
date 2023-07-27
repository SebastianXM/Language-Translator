import googletrans
from googletrans import Translator
import tkinter as tk
from tkinter import StringVar

class MyGUI:
    def __init__(self):
        self.translator = Translator()

        def translateText():
            text = self.textbox1.get("1.0", tk.END)
            src_language = self.clicked1.get()
            target_language = self.clicked2.get()
            translated_text = self.translator.translate(text, src = src_language, dest= target_language).text
            self.textbox2.delete("1.0", tk.END)
            self.textbox2.insert(tk.END, translated_text)

        self.root = tk.Tk()
        self.languages = ["en", "es", "fr", "it", "ja"]

        self.clicked1 = StringVar()
        self.clicked1.set(self.languages[0])
        self.clicked2 = StringVar()
        self.clicked2.set(self.languages[1])

        self.root.geometry("1000x500")
        self.root.title("RUTranslating")

        self.title = tk.Label(self.root, text = "RUTranslating", font=('Arial', 20))
        self.title.pack(padx=20, pady=10)

        self.textbox1 = tk.Text(self.root, font=('Arial', 18), height=4)
        self.textbox1.pack(padx=10)

        self.dropdown1 = tk.OptionMenu(self.root, self.clicked1, *self.languages)
        self.dropdown1.pack(pady=10)

        self.text = tk.Label(self.root, text="to", font = ('Arial', 18))
        self.text.pack()

        self.dropdown2 = tk.OptionMenu(self.root, self.clicked2, *self.languages)
        self.dropdown2.pack(pady=10)

        self.textbox2 = tk.Text(self.root, font=('Arial', 18), height=4)
        self.textbox2.pack(padx=10, pady= 5)

        self.btn = tk.Button(self.root, text = "Translate", font = ('Arial', 20), command=translateText)
        self.btn.pack(pady=10)

        self.root.mainloop()

MyGUI()