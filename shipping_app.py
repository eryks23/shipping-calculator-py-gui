import tkinter as tk
from tkinter import messagebox

class ShippingApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shipping Calculator")
        self.root.geometry("450x550")
        self.root.configure(bg="#2d3436")

        self.cost = 0.0
        self.package_type = ""

        self.container = tk.Frame(self.root, bg="#2d3436")
        self.container.pack(fill="both", pady=20)

        self.card1 = tk.Frame(self.container, bg="#636e72")
        self.card2 = tk.Frame(self.container, bg="#636e72")
        
        self.build_card_1()
        self.build_card_2()

        self.show_card(self.card1)

    def build_card_1(self):
        tk.Label(self.card1, text="Shipping Data", font=("Arial", 16, "bold"), bg="#636e72", fg="white").pack(pady=15)

        tk.Label(self.card1, text="Weight (kg): ", bg="#636e72", fg="white").pack(pady=5)
        self.weight = tk.Entry(self.card1, width=15)
        self.weight.pack(pady=5)

        tk.Label(self.card1, text="Price per kg: ", bg="#636e72", fg="white").pack(pady=5)
        self.price = tk.Entry(self.card1, width=15)
        self.price.pack(pady=5)

        tk.Label(self.card1, text="Distance (km): ", bg="#636e72", fg="white").pack(pady=5)
        self.distance = tk.Entry(self.card1, width=15)
        self.distance.pack(pady=5)

        self.result_cost = tk.Label(self.card1, text="Cost: --- USD", bg="#636e72", fg="white", font=("Arial", 11))
        self.result_cost.pack(pady=5)

        self.result_type = tk.Label(self.card1, text="Package type: ---", bg="#636e72", fg="white", font=("Arial", 11))
        self.result_type.pack(pady=5)
        
        self.summary = tk.Label(self.card1, text="", bg="#636e72", fg="#fdcb6e", font=("Arial", 12, "bold"))
        self.summary.pack(pady=10)

        tk.Button(self.card1, text="Calculate", bg="#0984e3", fg="white", width=12, command=self.calculate_cost).pack(pady=5)
        tk.Button(self.card1, text="Rate", bg="#6c5ce7", fg="white", width=12, command=self.rate_package).pack(pady=5)
        tk.Button(self.card1, text="Summary", bg="#00b894", fg="white", width=12, command=self.show_summary).pack(pady=5)
        tk.Button(self.card1, text="Details", bg="#fdcb6e", fg="white", width=12, command=self.go_to_details).pack(pady=5)

    def build_card_2(self):
        tk.Label(self.card2, text="Shipping Details", font=("Arial", 16, "bold"), bg="#636e72", fg="white").pack(pady=20)
            
        self.result_cost_2 = tk.Label(self.card2, text="Shipping cost: --- USD", bg="#636e72", fg="white", font=("Arial", 12))
        self.result_cost_2.pack(pady=10)
        
        self.result_weight_2 = tk.Label(self.card2, text="Package weight: --- kg", bg="#636e72", fg="white", font=("Arial", 12))
        self.result_weight_2.pack(pady=10)
        
        self.result_average_2 = tk.Label(self.card2, text="Avg cost per km: --- USD/km", bg="#636e72", fg="white", font=("Arial", 12))
        self.result_average_2.pack(pady=10)

        tk.Button(self.card2, text="Back", bg="#d63031", fg="white", width=15, command=lambda: self.show_card(self.card1)).pack(pady=20)
        tk.Button(self.card2, text="Reset", bg="#e17055", fg="white", width=15, command=self.reset_data).pack(pady=10)

    def show_card(self, card):

        self.card1.pack_forget()
        self.card2.pack_forget()

        card.pack(fill="both", expand=True)

    def get_data(self):

        try:
            weight = float(self.weight.get().replace(",", "."))
            price = float(self.price.get().replace(",","."))
            distance = float(self.distance.get().replace(",","."))
            return weight, price, distance
            
        except ValueError:
            messagebox.showerror("Error", "Enter valid numerical values!")
            return None, None, None
            
    def calculate_cost(self):

        weight, price, distance = self.get_data()

        if weight is not None and price is not None and distance is not None:

            self.cost = weight * price * (distance / 100)
            self.result_cost.config(text=f"Cost: {self.cost:.2f} USD")

    def rate_package(self):

        weight, price, distance = self.get_data()

        if weight is None:
            return

        if weight < 1:
            self.package_type = "Light package"

        elif 1 <= weight <= 5:
            self.package_type = "Medium package"

        else:
            self.package_type = "Heavy package"

        self.result_type.config(text=f"Package type: {self.package_type}")

    def show_summary(self):

        if self.cost == 0.00 or not self.package_type:
            messagebox.showinfo("Information", "First click 'Calculate' and 'Rate'!")
            return
        
        self.summary.config(text=f"Summary:\n{self.cost:.2f} USD | {self.package_type}")
    
    def go_to_details(self):

        weight, price, distance = self.get_data()

        if weight is None:
            return
        
        self.calculate_cost()

        if distance > 0:
            avg_cost = self.cost / distance
        else:
            avg_cost = 0.00

        self.result_cost_2.config(text=f"Shipping cost: {self.cost:.2f} USD")
        self.result_weight_2.config(text=f"Package weight: {weight:.2f} kg")
        self.result_average_2.config(text=f"Avg cost per km: {avg_cost:.2f} USD/km")

        self.show_card(self.card2)

    def reset_data(self):
        
        self.weight.delete(0, tk.END)
        self.price.delete(0, tk.END)
        self.distance.delete(0, tk.END)

        self.cost = 0.0
        self.package_type = ""

        self.result_cost.config(text="Cost: --- USD")
        self.result_type.config(text="Package type: ---")
        self.summary.config(text="")

        self.show_card(self.card1)

if __name__ == "__main__":
    app = ShippingApp()
    app.root.mainloop()