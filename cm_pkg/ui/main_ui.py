import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Python UI example")
    window.geometry("500x200")

    label = tk.Label(text="Python rocks!", font=("Arial 16"))
    label.place(relx=0.15, rely=0.1, anchor="nw")
    entry = tk.Entry()
    entry.place(relx=0.15, rely=0.25, anchor="nw")

    def change_label():
        label.config(text=entry.get(), font=("Helvetica 30"))

    button = tk.Button(text="Change label", command=change_label)
    button.place(relx=0.15, rely=0.50, anchor="nw")

    window.mainloop()


if __name__ == "__main__":
    main()
