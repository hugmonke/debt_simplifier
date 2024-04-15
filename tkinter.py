import tkinter as tk
import algorithm as al 


 
if __name__ == "__main__": 
    # Lista przechowująca wpisy [dłużnik, wierzyciel, kwota]
    entries = []
    def submit():
        debtor = debtor_entry.get()
        creditor = creditor_entry.get()
        amount = amount_entry.get()

        # Dodawanie wpisu do listy
        entries.append([debtor, creditor, amount])
        # Wyczyszczenie pola tekstowego
        output_text.delete(1.0, tk.END)
        last_entry = entries[-1]
        # Wyświetlenie listy wpisów w polu tekstowym 
        input_text.insert(tk.END, f"Dłużnik: {last_entry[0]}, Wierzyciel: {last_entry[1]}, Kwota: {last_entry[2]} zł\n")
        # Tutaj można dodać logikę zapisywania danych lub wykonywania innych operacji na wprowadzonych danych
        # print("Dłużnik:", debtor)
        # print("Wierzyciel:", creditor)
        # print("Kwota:", amount)
        
        
        # Wyczyszczenie pól po zatwierdzeniu
        debtor_entry.delete(0, tk.END)
        creditor_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        
    
    calculator = al.Calculator(entries)
    def calculate():

        if len(entries) == 1:
            output_text.insert(tk.END, f"{entries[0][0]} ---> {entries[0][1]}, {entries[0][2]} PLN\n")
        else:
            results = calculator.return_result()
            print(results)
            for res in results:
                output_text.insert(tk.END, f"{res[0]} ---> {res[1]}, {res[2]} PLN\n")
        
    



# Tworzenie okna głównego
root = tk.Tk()
root.title("Wprowadź dane")

# Ramka do umieszczenia elementów interfejsu
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Etykiety i pola tekstowe dla danych
debtor_label = tk.Label(frame, text="Dłużnik:")
debtor_label.grid(row=0, column=0, sticky="w")
debtor_entry = tk.Entry(frame)
debtor_entry.grid(row=0, column=1)

creditor_label = tk.Label(frame, text="Wierzyciel:")
creditor_label.grid(row=1, column=0, sticky="w")
creditor_entry = tk.Entry(frame)
creditor_entry.grid(row=1, column=1)

amount_label = tk.Label(frame, text="Kwota:")
amount_label.grid(row=2, column=0, sticky="w")
amount_entry = tk.Entry(frame)
amount_entry.grid(row=2, column=1)

# Przycisk do zatwierdzania
submit_button = tk.Button(frame, text="Dodaj", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

calculate_button = tk.Button(frame, text="Oblicz", command=calculate)
calculate_button.grid(row=3, column=2, pady=10)
# Ramki do wyświetlania listy wpisów
display_frame = tk.Frame(root)
display_frame.pack(padx=20, pady=10)

# Zmienna do wyświetlania listy wpisów
display_text = tk.StringVar()
display_text.set("Lista wpisów:")
display_label = tk.Label(display_frame, textvariable="display_text")
display_label.pack()

# Pole tekstowe dla wejscia
output_label = tk.Label(root, text="Wejście")
output_label.pack()
input_text = tk.Text(root, height=10, width=60)
input_text.pack(padx=20, pady=10)

# Pole tekstowe dla wyników
output_label = tk.Label(root, text="Wyniki")
output_label.pack()
output_text = tk.Text(root, height=10, width=60)
output_text.pack(padx=20, pady=20)
# Uruchomienie pętli głównej programu

root.mainloop()