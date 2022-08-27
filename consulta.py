import requests
import json
import re
import os
os.system("cls")
url = "https://tmsa-transmiapp-shvpc.uc.r.appspot.com/lectura_tarjeta"
print("Herramienta para ver cuanto saldo tiene en la tarjeta TuLLave sin NFC")
print("\nHerramienta desarrollada por https://instagram.com/nicolas.5301")
print("GitHub https://github.com/nicolashacku")
numero = str(input("\nDigite El Numero De La Tarjeta: "))
os.system("cls")
payload = {
    "numero_tarjeta":f"{numero}",
    "consultar":"true"
    }
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url,headers=headers,json=payload)
words = str(json.loads(response.text)).split()
x=0
for i in words:
    if x == 1:
        numeroTarjeta = i
        numeroTarjeta = re.sub("\'|\,", "", numeroTarjeta)
    elif x == 3:
        saldoTarjeta = i
        saldoTarjeta = re.sub("\'|,","",saldoTarjeta)
    x=x+1
print(f"[!] Numero De La Tarjeta: {numeroTarjeta}")
print(f"\n[!] Saldo De La Tarjeta: {saldoTarjeta}")
print("\n[!] Recuerde que el saldo mostrado es de hace 24h")