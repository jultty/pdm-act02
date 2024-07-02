import flet as ft

def main(page: ft.Page):
    field_task_name = ft.Ref[ft.TextField]()
    tasks_container = ft.Ref[ft.Container]()
    tasks = []

    def handleVisibility(e):
        print("Toggle visibility button clicked: ", e)
        field_task_name.current.visible = not field_task_name.current.visible
        field_task_name.current.disabled = not field_task_name.current.visible
        tasks_container.current.visible = not tasks_container.current.visible
        if field_task_name.current.visible:
            field_task_name.current.focus()
        page.update()

    def handleClear(e):
        print("Clear button clicked: ", e)
        tasks.clear()
        field_task_name.current.label = "Task name"
        field_task_name.current.value = ""
        field_task_name.current.disabled = False
        field_task_name.current.focus()
        page.update()

    def handleAdd(e):
        print("Add button clicked: ", e)
        tasks.append(
            ft.Container(content = ft.Row(controls=[
                ft.Checkbox(),
                ft.Text(field_task_name.current.value)
            ])
        ))
        field_task_name.current.value = ""
        field_task_name.current.focus()
        page.update()

    class CustomButton(ft.ElevatedButton):
        def __init__(self, text, icon, on_click):
            super().__init__()
            self.bgcolor = ft.colors.GREEN_500
            self.color = ft.colors.WHITE
            self.text = text
            self.icon = icon
            self.on_click = on_click

    button_send = CustomButton("Add", ft.icons.ADD, handleAdd)
    button_clear = CustomButton("Clear", ft.icons.CLEAR, handleClear)
    button_toggle_visibility = CustomButton("Toggle Visibility", ft.icons.VISIBILITY, handleVisibility)

    buttons = [ button_send, button_clear, button_toggle_visibility ]

    page.add(
        ft.Container(ref=tasks_container, content = ft.Column(controls=tasks)),
        ft.TextField(
            ref=field_task_name, label="Task name", autofocus=True,
            on_submit=handleAdd),
        ft.Container(content = ft.Row(controls=buttons)) # pyright: ignore reportArgumentType
    )

ft.app(main)
