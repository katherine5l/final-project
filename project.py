import flet as ft

def main(page: ft.Page):
    page.title="Financial Budget Tracker"
    title = ft.Text(value="Your Budget Tracker")

    totalBalance=ft.Text(value="Current Balance: ")
    typeInput=ft.Dropdown(label="Type of Transaction", options= [ft.dropdown.Option("Income"), ft.dropdown.Option("Expense")])
    transAmount = ft.TextField(label="Amount of Money")
    expenseCats = ft.Dropdown(label="Expense Category", options=
                              [ft.dropdown.Option("Food"), ft.dropdown.Option("Health/Medicine"), ft.dropdown.Option("Trips"), ft.dropdown("Wishlist"), ft.dropdown.Option("House Bills"), ft.dropdown("Rent"), ft.dropdown("Other")])

class PresupuestoApp:
    def_init_(self, page: ft.Page):
    self.page = page
    self.page.title = "Manejador de Presupuestos"
    self.page.window_width = 800
    self.page.window_height = 600
    self.page.horizontal_alignment = "center"
    self.page.vertical_alignment = "start"
    self.main_view()

ft.app(target=main)

