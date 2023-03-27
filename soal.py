import requests as r
import os
import platform
import re
import string
from bs4 import BeautifulSoup as par
clear = lambda: os.system("clear") if platform.system().lower() == "linux" else os.system("cls")
url = "paste link here"

def dfine(ujianx, name):
	global url
	abc = list("ABCDE")
	ujian, abcd = [], []
	cek = par(r.get("http://%s/ujianutama/index.php?content=ujian&ujian=%s" % (url, ujianx), allow_redirects=False).text, "html.parser")
	for knt in cek.find_all("div", {"class": "box"}):
		soal = knt.find("div", {"class": "soal"})
		shs = ""
		if "img" in str(soal):
			shs += "http://%s/ujianutama/" % (url) + soal.find("img")["src"]
			try:
				shs += soal.text + "\n"
			except:
				pass
		else:
			try:
				shs += soal.text + "\n"
			except:
				pass
		try:
			ujian.append(shs)
		except:
			pass

		#-> get pilihan berganda
		for row in knt.find_all("table", {"row pilihan"}):
			ok = row.findAll("div", {"class": "teks"})
			ya = [y.text.strip() for y in ok]
			abcd.append(ya)
	string = "MATA PELAJARAN: %s\nID UJIAN: %s \n\n" % (name, ujianx)
	number = 0
	for uji in ujian:
		number += 1
		if uji == "":
			pass
		else:
			string += str(number)+". "+uji
			try:
				for abcde, jawab in zip(abc, abcd[number-1]):
					string += abcde+". "+jawab+"\n"
			except:
				pass
			string += "\n"
	with open("result/"+name+".txt", "w") as sub:
		sub.write(string)
	print("> Output: " + "result/"+name+".txt\n")

def start():
	print("\n\t+( Get soal Ujian )+\n")
	kelas = input("? Soal kelas berapa?: ")
	while kelas == "" or kelas not in ["X","IX","XI","XII"]:
		print("! contoh: X,IX,XI,XII")
		kelas = input("? Soal kelas berapa?: ")
	jurus = input("? Jurusan apa?: ")
	print("! Harap Bersabar\n")
	for xx in range(1, 2000):
		cek = r.get("http://%s/ujianutama/index.php?content=confirm&id=%s" % (url, xx), allow_redirects=False).text
		chek = "".join(re.findall("Mata\sPelajaran.*?\n.*?list-group-item-text.*?>(.*?)</p>", str(cek)))
		if kelas.lower() in chek.lower().split(" ") or jurus.lower() in chek.lower().split(" "):
			print("! Mapel didapatkan\n  Mapel: %s " % (chek))
			print("! Sedang mentransfer file...")
			dfine(xx, chek)
		else:
			pass
	exit("\n* Program sudah saatnya berhenti. good bye..\n")


if __name__=="__main__":
	clear()
	try:os.mkdir("result")
	except:pass
	start()
