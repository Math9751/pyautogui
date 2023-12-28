import pyautogui

pyautogui.PAUSE = 2

# abrir a ferramenta
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter", interval=12)

# preencher o login
pyautogui.click(x=310, y=225)
pyautogui.write("matheus")

# preencher a senha 
pyautogui.click(x=310, y=265)
pyautogui.write("abc123")

# clicar em fazr login
pyautogui.click(x=310, y=350)
pyautogui.keyDown("ctrl")
pyautogui.click(x=310, y=350)
pyautogui.keyUp("ctrl")