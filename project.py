import flet as ft

def main(page: ft.Page):
    page.title="Financial Budget Tracker"
    title = ft.Text(value="Your Budget Tracker")

    moneySpent = ft.TextField(label="Input Money Spent")
    expenseCats = ft.Dropdown(label="Expense Category", options=
                              [ft.dropdown.Option("Food"), ft.dropdown.Option("Health/Medicine"), ft.dropdown.Option("Trips"), ft.dropdown("Wishlist"), ft.dropdown.Option("House Bills")])
    def addTransaction(e):
        pass
    def calcBalance(e):
        pass
    def deleteTransaction(e):
        pass

ft.app(target=main)