import flet as ft


def main(page: ft.Page):
    field_first_name = ft.Ref[ft.TextField]()
    field_last_name = ft.Ref[ft.TextField]()

    def handleVisibility(e):
        print("Toggle visibility button clicked: ", e)
        field_first_name.current.visible = not field_first_name.current.visible
        field_last_name.current.visible = not field_last_name.current.visible
        page.update()

    def handleReset(e):
        print("Reset button clicked: ", e)
        field_first_name.current.label = "First name"
        field_last_name.current.label = "Last name"
        field_first_name.current.value = ""
        field_last_name.current.value = ""
        field_first_name.current.disabled = False
        field_last_name.current.disabled = False
        page.update()

    def handleSend(e):
        print("Send button clicked: ", e)
        field_first_name.current.value = "Form sent!"
        field_last_name.current.value = "Form sent!"
        field_first_name.current.disabled = True
        field_last_name.current.disabled = True
        page.update()

    class CustomButton(ft.ElevatedButton):
        def __init__(self, text, icon, on_click):
            super().__init__()
            self.bgcolor = ft.colors.PURPLE_300
            self.color = ft.colors.GREY_200
            self.text = text
            self.icon = icon
            self.on_click = on_click

    button_send = CustomButton("Send", ft.icons.SEND, handleSend)
    button_reset = CustomButton("Reset", ft.icons.RESTORE, handleReset)
    button_toggle_visibility = CustomButton("Toggle Visibility", ft.icons.VISIBILITY, handleVisibility)

    buttons = [ button_send, button_reset, button_toggle_visibility ]

    page.add(
        ft.TextField(ref=field_first_name, label="First name"),
        ft.TextField(ref=field_last_name, label="Last name"),
        ft.Container(content = ft.Row(controls=buttons)) # pyright: ignore reportArgumentType
    )

ft.app(main)
