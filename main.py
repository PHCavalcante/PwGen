import flet as ft
import random

def main(page: ft.Page):
    page.title = "PwGen"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    # remember to add max lines propriety here later
    passwordfiled = ft.TextField(label="Password to be generated:", password=True, can_reveal_password=True, read_only=True)

    uppercases = ft.Checkbox(label="Include Uppercases?", value=True)
    nums = ft.Checkbox(label="Include Numbers?", value=True)
    specialcharacters = ft.Checkbox(label="Include Special Characters?", value=True)

    def slider_change(e):
        valuetext.value = f"Password lenght is: {int(e.control.value)}"
        page.update()

    valuetext = ft.Text()
    lenghttext = ft.Text("Select the password lenght")
    passwordlenght = ft.Slider(min=8, max=120, divisions=120, label="{value}", adaptive=True, on_change=slider_change)
    def generating_password(lenght):
        chars = "abcdefghijklmnopqrstuvwxyz"
        upper = chars.upper()
        numbers = "0123456789"
        special_chars = "!@#$%&*_?|"
        allchars = chars + upper + numbers + special_chars

        if uppercases.value == True and nums.value == True and specialcharacters.value == True:
            password = ""
            for i in range(lenght):
                password += random.choice(allchars)

        print(password)
        passwordfiled.value = password
        print(passwordfiled.value)

    generatebutton = ft.FilledButton(text="Generate Password", on_click=generating_password(20))

    page.add(passwordfiled, uppercases, nums, specialcharacters, lenghttext, passwordlenght, generatebutton, valuetext)


ft.app(target=main)
