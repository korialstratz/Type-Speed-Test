from tkinter import *
from words import word_list
import random
import time
from threading import *

font = ("Raleway", 14, "bold")


class App:

    def __init__(self):
        self.window = Tk()
        self.window.title("Type Speed Test")
        self.window.iconbitmap("images/speed.ico")

        self.window.config(padx=30, pady=30, bg="#3E497A")
        self.canvas = Canvas(width=600, height=400)

        def start():
            self.text_label.config(state="normal")
            selected_word = random.choice(word_list)
            self.test_text = selected_word
            self.text_label.delete(1.0, END)
            self.text_label.insert(1.0, selected_word)
            self.text_label.config(state="disabled")

        def get_user_text():
            print("getting user values")
            time.sleep(60)
            user_text = self.user_entry.get(1.0, END)
            user_text_length = len(user_text)
            gross_wpm = int(user_text_length/5)
            text_list = self.test_text.split(" ")
            user_list = user_text.split(" ")
            n = 0
            for i in range(len(user_list)):
                if user_list[i] != text_list[i]:
                    n += 1
            net_wpm = gross_wpm - n
            if net_wpm > 41:
                speed = "Your are a fast !!"
            else:
                speed = "You can do better than that keep practicing"

            user_result = f"Gross WPM: {gross_wpm}, Net WPM: {net_wpm} {speed}"
            self.result_label.config(text=user_result)
            self.test_button.config(text="Test Ended")
            time.sleep(5)
            self.text_label.config(state="normal")
            self.text_label.delete(1.0, END)
            self.text_label.config(state="disabled")
            self.result_label.config(text=self.test_result)
            self.test_button.config(text=self.test_status)
            self.user_entry.delete(1.0, END)

        def thread():
            self.test_button.config(text="Test Started")
            t1 = Thread(target=start)
            t1.start()
            t2 = Thread(target=get_user_text)
            t2.start()

        # Labels

        self.logo = PhotoImage(file="images/speed.png")
        self.image_label = Label(image=self.logo, bg="#3E497A")
        self.image_label.grid(column=0, row=0, columnspan=2, sticky="w")

        self.test_text = ""
        self.text_label = Text(font=font, height=5, width=100)
        self.text_label.grid(column=0, row=1, sticky="news", columnspan=2, pady=5)
        self.text_label.insert(1.0, self.test_text)

        self.user_entry = Text(font=font, height=5, width=100)
        self.user_entry.grid(column=0, row=2, columnspan=2, sticky="news", pady=5)

        self.test_status = "Start Test"
        self.test_button = Button(text=self.test_status, font=font, height=2, width=20, bg="#20bebe", fg="white",
                                  command=thread)
        self.test_button.grid(column=0, row=3, sticky="w", padx=5)

        self.test_result = "Learn your Gross WPM and Net WPM"
        self.result_label = Label(text=self.test_result, font=font, height=2, width=75, bg="#20bebe", fg="white")
        self.result_label.grid(column=1, row=3, sticky="w")

        self.window.mainloop()


if __name__ == '__main__':
    App()
