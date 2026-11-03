import flet as ft

def main(page: ft.Page):
    page.title = "Passport Pro"
    page.padding = 15
    page.theme_mode = ft.ThemeMode.LIGHT
    status = ft.Text("Passport Photo Maker V1 - Ready", size=18)
    img = ft.Image(width=300, height=350, fit=ft.ImageFit.CONTAIN, border_radius=15, bgcolor=ft.Colors.GREY_200)
    
    def picked(e):
        if e.files:
            img.src = e.files[0].path
            status.value = "Photo loaded! Ready to make passport"
            page.update()
    
    picker = ft.FilePicker(on_result=picked)
    page.overlay.append(picker)

    page.add(
        ft.Text("Passport Pro & CV", size=28, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton("Pick Photo", icon=ft.Icons.IMAGE, on_click=lambda _: picker.pick_files()),
        img,
        status,
        ft.Text("V1 built today - Next: White BG + Save", color=ft.Colors.GREY)
    )

ft.app(target=main)
