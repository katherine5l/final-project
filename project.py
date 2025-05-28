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

def main_view(self, e=None):
    self.page.controls.clear()
    titulo = ft.Text('Menú Principla", size=30, weight="bold")
    btn_nuevo = ft.ElevatedButton ("Agregar nuevo presupuesto"), on_click=self.nuevo_presupuesto_view)
    btn_lista = ft.ElevatedButton ("Listar presupuestos", on_click=self.listar_presupiestos_view)
    self.page.add(titulo, btn_nuevo, btn_lista)
    self.page.update()


ft.app(target=main)

