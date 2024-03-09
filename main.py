import flet as ft
import random


def main(page: ft.Page):
    page.title = "PwGen"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 650
    page.window_height = 550
    page.window_resizable = True
    page.update()

    # remember to add max lines propriety here later
    passwordfiled = ft.TextField(label="Password to be generated:", password=True, can_reveal_password=True, read_only=True)

    uppercases = ft.Checkbox(label="Include Uppercases", value=True)
    nums = ft.Checkbox(label="Include Numbers", value=True)
    specialcharacters = ft.Checkbox(label="Include Special Characters", value=True)

    def slider_change(e):
        valuetext.value = f"Password length is: {round(e.control.value)}"
        page.update()

    valuetext = ft.Text()
    lenghttext = ft.Text("Select the password length")
    passwordlenght = ft.Slider(min=8, max=120, divisions=120, label="{value}", adaptive=True, round=0, on_change=slider_change)

    def generating_password(self):
        chars = "abcdefghijklmnopqrstuvwxyz"
        upper = chars.upper()
        numbers = "0123456789"
        special_chars = "!@#$%&*_?|"
        allchars = chars + upper + numbers + special_chars
        if uppercases.value is True and nums.value is True and specialcharacters.value is True:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(allchars)
        elif uppercases.value is True and nums.value is False and specialcharacters.value is False:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(upper)
        elif uppercases.value is True and nums.value is True and specialcharacters.value is False:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(upper + numbers)
        elif uppercases.value is True and nums.value is False and specialcharacters.value is True:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(upper + special_chars)
        elif uppercases.value is False and nums.value is True and specialcharacters.value is False:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(numbers)
        elif uppercases.value is False and nums.value is False and specialcharacters.value is True:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(special_chars)
        elif uppercases.value is False and nums.value is True and specialcharacters.value is True:
            password = ""
            for i in range(int(passwordlenght.value)):
                password += random.choice(numbers + special_chars)

        passwordfiled.value = password
        page.update()

    generatebutton = ft.FilledButton(text="Generate Password", on_click=generating_password)

    page.add(passwordfiled, uppercases, nums, specialcharacters, lenghttext, passwordlenght, generatebutton, valuetext)


ft.app(target=main)
