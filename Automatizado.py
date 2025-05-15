from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time 

# INFORMAÇÕES DE LOGIN
usuario = 'meu_usuario' # exemplo de login
senha = 'minha_senha'  # exemplo de login

# Abre o navegador Chrome
navegador = webdriver.Chrome() # Abre o Chrome
navegador.get("https://www.instagram.com") # Entra no Instagram

# Espera a pagina carregar
time.sleep(5) # Tempo pro navegador ficar aberto

# Faz o login automatico
campo_usuario = navegador.find_element(By.NAME, "username") # Armazena o campo de usuario na variavel (campo_usuario)
campo_senha = navegador.find_element(By.NAME, "password")  # Armazena o campo de senha na variavel (campo_senha)

campo_usuario.send_keys(usuario) # preeche o campo com as informaçoes amazenadas na variavel (usuario)
campo_senha.send_keys(senha)  # preeche o campo com as informaçoes amazenadas na variavel (senha)
campo_senha.send_keys(Keys.RETURN) # Retorna o login ou informaçoes invalidas

time.sleep(7) # Tempo pro navegador ficar aberto

# Fechar os Pop-ups que aparecem após o login 
try:
    botao_agora_nao = navegador.find_element(By.XPATH, "//button[contains(text(), 'Agora não')]") # Armazena na variavel (botao_agora_nao) o botao "Agora não"
    botao_agora_nao.click() # Cria um evento de clique
    time.sleep(3) # Tempo pro navegador ficar aberto
except:
    pass


# busca pelo perfil do CR7
campo_busca = navegador.find_element(By.XPATH, "//input[@placeholder='Pesquisar']") # Armazena na variavel (campo_busca) o campo pesquisar do instagram
campo_busca.send_keys("cristiano")
time.sleep(3) # Tempo pro navegador ficar aberto
campo_busca.send_keys(Keys.RETURN)
time.sleep(1) # Tempo pro navegador ficar aberto
campo_busca.send_keys(Keys.RETURN)

#espera a pagina do perfil carregar 
time.sleep(5) # Tempo pro navegador ficar aberto

#Tentar seguir o perfil 
try:
    botao_seguir = navegador.find_element(By.XPATH, "//button[text()='Seguir]") # Armazena na variavel (botao_seguir) o botao de seguir do instagram
    botao_seguir.click() # Cria um evento de clique
    print("Perfil do cristiano seguido com sucesso!") # Retorna menssagem de sucesso
except:
    print("Não foi possivel seguir o perfil. Talvez você ja segue!")


# Mantem o navegador aberto por 2 minutos
print("Mantendo o navegador aberto!")
time.sleep(120) # Tempo pro navegador ficar aberto
navegador.quit # Fecha o navegador