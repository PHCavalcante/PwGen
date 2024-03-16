import flet as ft
import random


def main(page: ft.Page) -> None:
    page.title = "PwGen"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 650
    page.window_height = 550
    page.window_resizable = True
    page.bgcolor = ft.colors.GREY_900
    page.theme = ft.Theme(color_scheme_seed=ft.colors.WHITE70)
    page.update()


    passwordfield = ft.TextField(label="Password to be generated:", password=True, can_reveal_password=True, read_only=True)
    pass_cont = ft.Container(
        content=passwordfield,
        alignment=ft.alignment.center,
        # border=ft.border.all(1, ft.colors.WHITE70),
        # border_radius=ft.border_radius.all(10.0),
        # bgcolor=ft.colors.YELLOW
    )

    uppercases = ft.Checkbox(label="Include Uppercases", value=True)
    upper_cont = ft.Container(
        content=uppercases,
        alignment=ft.alignment.center
    )

    nums = ft.Checkbox(label="Include Numbers", value=True)
    nums_cont = ft.Container(
        content=nums,
        alignment=ft.alignment.center
    )

    specialcharacters = ft.Checkbox(label="Include Special Characters", value=True)
    special_cont = ft.Container(
        content=specialcharacters,
        alignment=ft.alignment.center
    )
    def slider_change(e):
        valuetext.value = f"Password length is: {round(e.control.value)}"
        page.update()

    valuetext = ft.Text()
    lenghttext = ft.Text("Select the password length")

    passwordlenght = ft.Slider(min=8, max=120, divisions=120, label="{value}", adaptive=True, round=0, on_change=slider_change)
    pass_len_cont = ft.Container(
        content=passwordlenght,
        alignment=ft.alignment.center
    )

    def generating_password(self):
        chars = "abcdefghijklmnopqrstuvwxyz"
        upper = chars.upper()
        numbers = "0123456789"
        special_chars = "!@#$%&*_?|"
        allchars = chars + upper + numbers + special_chars

        def dialog_popup():
            popup = ft.AlertDialog(
                modal=False,
                title=ft.Text("Oops"),
                content=ft.Text("Please select the password lenght!"),
                actions=[ft.TextButton("Ok", on_click=close_popup)],
                actions_alignment=ft.MainAxisAlignment.CENTER
            )
            page.add(popup)
            return popup

        def open_popup(popup):
            page.dialog = popup
            popup.open = True
            page.update()

        def close_popup(popup):
            popup.open = False
            page.update()

        if uppercases.value is True and nums.value is True and specialcharacters.value is True:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(allchars)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is True and nums.value is False and specialcharacters.value is False:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(upper)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is True and nums.value is True and specialcharacters.value is False:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(upper + numbers)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is True and nums.value is False and specialcharacters.value is True:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(upper + special_chars)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is False and nums.value is True and specialcharacters.value is False:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(numbers)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is False and nums.value is False and specialcharacters.value is True:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(special_chars)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is False and nums.value is True and specialcharacters.value is True:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(numbers + special_chars)
            except:
                open_popup(dialog_popup())
        elif uppercases.value is False and nums.value is False and specialcharacters.value is False:
            password = ""
            try:
                for i in range(int(passwordlenght.value)):
                    password += random.choice(chars)
            except:
                open_popup(dialog_popup())

        passwordfield.value = password
        page.update()

    generatebutton = ft.FilledButton(text="Generate Password", on_click=generating_password)
    gen_cont = ft.Container(
        content=generatebutton,
        alignment=ft.alignment.center
    )

    page.add(pass_cont, upper_cont, nums_cont, special_cont, lenghttext, pass_len_cont, gen_cont, valuetext)


ft.app(target=main)
