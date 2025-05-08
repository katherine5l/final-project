import flet as ft

def main(page: ft.Page):
    page.title="Financial Budget Tracker"
    title = ft.Text(value="Your Budget Tracker")

    moneySpent = ft.TextField(label="Input Money Spent")
    expenseCats = ft.Dropdown(label="Expense Category", options=
                              [ft.dropdown.Option("Food"), ft.dropdown.Option("Health/Medicine"), ft.dropdown.Option("Trips"), ft.dropdown("Wishlist"), ft.dropdown.Option("House Bills")])

    
    def addTransaction(e):
        try:
            amount = float(money_input.vslue_
            category_dropdown.value
            if not category;
                status.value = "Please select a category."
        else:
            transictions.append({"amount"; amount, "category"; category})
            rseult.value = "Transactin added"
            money_input.value = ""
            category_dropdown.value = None
        except ValueError:
            result.value = "Enter a alid number"
        page.update()
                           
    def calcBalance(e):
        pass
    def deleteTransaction(e):
        pass

ft.app(target=main)

