import tkinter as tk
from tkinter import messagebox


class WoodStoreApp:
    """
    This class represents the main application window for the Wood Store.
    It provides buttons to navigate to the 'Sell Wood' and 'View Orders' functionalities.
    """

    def __init__(self, master):
        """
        Initialize the WoodStoreApp object.

        Parameters:
            master (tk.Tk): The root window of the application.
        """
        self.master = master
        master.title("Wood Store")
        master.geometry("400x300")

        # Button to navigate to 'Sell Wood' functionality
        self.sell_button = tk.Button(master, text="Sell Wood", command=self.sell_wood, width=15, height=2)
        self.sell_button.place(relx=0.5, rely=0.4, anchor="center")

        # Button to navigate to 'View Orders' functionality
        self.view_button = tk.Button(master, text="View Orders", command=self.view_orders, width=15, height=2)
        self.view_button.place(relx=0.5, rely=0.6, anchor="center")

        self.orders = []  # List to store orders

    def sell_wood(self):
        """
        Open a new window for selling wood.
        """
        sell_window = tk.Toplevel(self.master)
        SellWood(sell_window, self.orders)

    def view_orders(self):
        """
        Open a new window to view orders.
        """
        orders_window = tk.Toplevel(self.master)
        orders_window.title("View Orders")
        screen_width = orders_window.winfo_screenwidth()
        screen_height = orders_window.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        orders_window.geometry(f"{window_width}x{window_height}")
        ViewOrders(orders_window, self.orders, window_width, window_height)


class SellWood:
    """
    This class represents the functionality for selling wood.
    It allows the user to input wood density, length, and width to calculate the price.
    """

    def __init__(self, master, orders):
        """
        Initialize the SellWood object.

        Parameters:
            master (tk.Toplevel): The parent window.
            orders (list): List of orders to store the sold wood details.
        """
        self.master = master
        self.orders = orders
        master.title("Sell Wood")

        # Labels and entry fields for inputting wood details
        self.density_label = tk.Label(master, text="Wood Density (kg/m^3):")
        self.density_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.density_entry = tk.Entry(master)
        self.density_entry.grid(row=0, column=1, padx=10, pady=5)

        self.length_label = tk.Label(master, text="Length (m):")
        self.length_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=1, column=1, padx=10, pady=5)

        self.width_label = tk.Label(master, text="Width (m):")
        self.width_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.width_entry = tk.Entry(master)
        self.width_entry.grid(row=2, column=1, padx=10, pady=5)

        # Button to sell wood and calculate price
        self.sell_button = tk.Button(master, text="Sell", command=self.sell, width=15, height=2)
        self.sell_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def sell(self):
        """
        Calculate the price of wood based on user input and add the order to the list.
        """
        density_str = self.density_entry.get()
        length_str = self.length_entry.get()
        width_str = self.width_entry.get()
        if density_str and length_str and width_str:
            try:
                density = float(density_str)
                length = float(length_str)
                width = float(width_str)
                volume = length * width  # Calculate volume based on length and width
                price = density * volume * 10  # Example pricing formula
                order = {"Density": density, "Length": length, "Width": width, "Price": price}
                self.orders.append(order)  # Add the order to the list of orders
                messagebox.showinfo("Success", f"The price of wood is ${price:.2f}.")
                self.master.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        else:
            messagebox.showerror("Error", "Please enter all dimensions and density.")


class ViewOrders:
    """
    This class represents the functionality for viewing orders.
    It displays a list of orders and provides options to edit, cancel, and delete orders.
    """

    def __init__(self, master, orders, window_width, window_height):
        """
        Initialize the ViewOrders object.

        Parameters:
            master (tk.Toplevel): The parent window.
            orders (list): List of orders to display.
            window_width (int): Width of the window.
            window_height (int): Height of the window.
        """
        self.master = master
        self.orders = orders
        master.title("View Orders")
        self.window_width = window_width
        self.window_height = window_height

        # Label to display orders
        self.orders_label = tk.Label(master, text="Today's Orders:")
        self.orders_label.pack(padx=10, pady=5)

        # Listbox to display orders
        self.orders_listbox = tk.Listbox(master, width=int(window_width * 0.6), height=int(window_height * 0.6))
        self.orders_listbox.pack(padx=10, pady=5)
        # Display orders in the listbox
        for order in self.orders:
            self.orders_listbox.insert(tk.END,
                                       f"Density: {order['Density']}, Length: {order['Length']}, Width: {order['Width']}, Price: ${order['Price']:.2f}")

        # Buttons for editing, canceling, and deleting orders
        self.edit_button = tk.Button(master, text="Edit Order", command=self.edit_order, width=15, height=2)
        self.edit_button.pack(padx=10, pady=5)

        self.cancel_button = tk.Button(master, text="Cancel Order", command=self.cancel_order, width=15, height=2)
        self.cancel_button.pack(padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete Order", command=self.delete_order, width=15, height=2)
        self.delete_button.pack(padx=10, pady=5)

        # Entry fields for editing order details
        self.edit_density_label = tk.Label(master, text="Wood Density (kg/m^3):")
        self.edit_density_label.pack(padx=10, pady=5)

        self.edit_density_entry = tk.Entry(master)
        self.edit_density_entry.pack(padx=10, pady=5)

        self.edit_length_label = tk.Label(master, text="Length (m):")
        self.edit_length_label.pack(padx=10, pady=5)

        self.edit_length_entry = tk.Entry(master)
        self.edit_length_entry.pack(padx=10, pady=5)

        self.edit_width_label = tk.Label(master, text="Width (m):")
        self.edit_width_label.pack(padx=10, pady=5)

        self.edit_width_entry = tk.Entry(master)
        self.edit_width_entry.pack(padx=10, pady=5)

        # Button to save changes
        self.save_button = tk.Button(master, text="Save Changes", command=self.save_changes, width=15, height=2)
        self.save_button.pack(padx=10, pady=5)

    def edit_order(self):
        """
        Edit the selected order by populating the entry fields with its details.
        """
        selected_index = self.orders_listbox.curselection()
        if selected_index:
            selected_order = self.orders[selected_index[0]]
            # Clear entry fields
            self.edit_density_entry.delete(0, tk.END)
            self.edit_length_entry.delete(0, tk.END)
            self.edit_width_entry.delete(0, tk.END)
            # Populate entry fields with selected order details
            self.edit_density_entry.insert(0, selected_order["Density"])
            self.edit_length_entry.insert(0, selected_order["Length"])
            self.edit_width_entry.insert(0, selected_order["Width"])
        else:
            messagebox.showerror("Error", "Please select an order to edit.")

    def cancel_order(self):
        """
        Display a message indicating that the Cancel Order button was clicked.
        """
        messagebox.showinfo("Cancel Order", "You clicked the Cancel Order button!")

    def delete_order(self):
        """
        Delete the selected order from the list.
        """
        selected_index = self.orders_listbox.curselection()
        if selected_index:
            self.orders_listbox.delete(selected_index[0])
            del self.orders[selected_index[0]]
            messagebox.showinfo("Delete Order", "Order deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select an order to delete.")

    def save_changes(self):
        """
        Save the changes made to the selected order's details.
        """
        selected_index = self.orders_listbox.curselection()
        if selected_index:
            selected_order = self.orders[selected_index[0]]
            # Update selected order with new details
            selected_order["Density"] = float(self.edit_density_entry.get())
            selected_order["Length"] = float(self.edit_length_entry.get())
            selected_order["Width"] = float(self.edit_width_entry.get())
            # Display a message to indicate changes are saved
            messagebox.showinfo("Success", "Changes saved successfully.")
        else:
            messagebox.showerror("Error", "Please select an order to edit.")


def main():
    """
    Main function to create the root window and start the application.
    """
    root = tk.Tk()
    app = WoodStoreApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
