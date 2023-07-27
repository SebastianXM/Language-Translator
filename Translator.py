import googletrans
from googletrans import Translator
import tkinter as tk
from tkinter import StringVar, ttk

class MyGUI:
    def __init__(self):
        self.translator = Translator()

        # Selected language to language code using HashMap
        reversed_dict = {value: key for key, value in googletrans.LANGUAGES.items()}
        def lang_to_code(str) -> str:
           return reversed_dict[str.lower()] 
        
        # Translation Function
        def translateText():
            text = self.textbox1.get("1.0", tk.END)
            src_language = lang_to_code(self.option1.get())
            target_language = lang_to_code(self.option2.get())
            translated_text = self.translator.translate(text, src = src_language, dest= target_language).text
            self.textbox2.delete("1.0", tk.END)
            self.textbox2.insert(tk.END, translated_text)

        # Building GUI
        self.root = tk.Tk()
        self.languages = list(googletrans.LANGUAGES.values())
        self.languages = [language.capitalize() for language in self.languages]

        self.option1 = StringVar()
        self.option1.set(googletrans.LANGUAGES['en'].capitalize())
        self.option2 = StringVar()
        self.option2.set(googletrans.LANGUAGES['es'].capitalize())

        self.root.geometry("1000x500")
        self.root.title("Language Translator")

        self.title = tk.Label(self.root, text = "Language Translator", font=('Arial', 20))
        self.title.pack(padx=20, pady=10)

        self.textbox1 = tk.Text(self.root, font=('Arial', 18), height=4)
        self.textbox1.pack(padx=10)

        self.dropdown1 = ttk.Combobox(self.root, textvariable=self.option1, values= self.languages)
        self.dropdown1.pack(pady=10)

        self.text = tk.Label(self.root, text="to", font = ('Arial', 18))
        self.text.pack()

        self.dropdown2 = ttk.Combobox(self.root, textvariable=self.option2, values= self.languages)
        self.dropdown2.pack(pady=10)

        self.textbox2 = tk.Text(self.root, font=('Arial', 18), height=4)
        self.textbox2.pack(padx=10, pady= 5)

        self.btn = tk.Button(self.root, text = "Translate", font = ('Arial', 20), command=translateText)
        self.btn.pack(pady=10)

        self.root.mainloop()

MyGUI()