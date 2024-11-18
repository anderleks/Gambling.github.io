from pyscript import when, display, document

@When("click", "#my_button")
def on_click(event):
    result = document.querySelector("#my_input").value
    display(f"Your input:{result}", target="output")