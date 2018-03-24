import os
import json

gp = {"1":{"nombre": "Australia","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Australia/_jcr_content/circuitMap.img.png/1458295808922.png" ,"long":"58"},
"2":{"nombre": "Malasia","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Malaysia/_jcr_content/circuitMap.img.png/1475050117806.png", "long":"56"},
"3":{"nombre": "China","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/China/_jcr_content/circuitMap.img.png/1460623306406.png",  "long":"56"},
"4":{"nombre": "Bahrein","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Bahrain/_jcr_content/circuitMap.img.png/1459333291738.png" ,  "long":"57"},
"5":{"nombre": "España", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Spain/_jcr_content/circuitMap.img.png/1462284701312.png" , "long":"66"},
"6":{"nombre": "Monaco", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Monaco/_jcr_content/circuitMap.img.png/1464250239871.png", "long":"78"},
"7":{"nombre": "Canadá", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Canada/_jcr_content/circuitMap.img.png/1465384883597.png", "long":"70"},
"8":{"nombre": "Austria", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2018/Austria/_jcr_content/circuitMap.img.png/1496396643536.png", "long":"71"},
"9":{"nombre": "Gran Bretaña","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Great_Britain/_jcr_content/circuitMap.img.png/1467972674844.png",  "long":"52"},
"10":{"nombre": "Hungría", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2018/Hungary/_jcr_content/circuitMap.img.png/1468859161502.png", "long":"69"},
"11":{"nombre": "Bélgica", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Belgium/_jcr_content/circuitMap.img.png/1472117728959.png", "long":"43"},
"12":{"nombre": "Italia", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Italy/_jcr_content/circuitMap.img.png/1472813738069.png", "long":"53"},
"13":{"nombre": "Singapur", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Singapore/_jcr_content/circuitMap.img.png/1442316898012.png", "long":"61"},
"14":{"nombre": "Japón", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Japan/_jcr_content/circuitMap.img.png/1442577419217.png", "long":"53"},
"15":{"nombre": "Rusia","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Russia/_jcr_content/circuitMap.img.png/1443697558344.png", "long":"53"},
"16":{"nombre": "Estados Unidos", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/United_States/_jcr_content/circuitMap.img.png/1444839471121.png",  "long":"56"},
"17":{"nombre": "México","image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Mexico/_jcr_content/circuitMap.img.png/1446548160528.png" , "long":"71"},
"18":{"nombre": "Brasil", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Brazil/_jcr_content/circuitMap.img.png/1446807467732.png", "long":"71"},
"19":{"nombre": "Abu Dhabi", "image": "https://www.formula1.com/content/fom-website/en/championship/races/2017/Abu_Dhabi/_jcr_content/circuitMap.img.png/1448472871112.png", "long":"55"}
}

def inicio_bot():
	os.mkdir("DB")

	with open('./DB/comps.json', 'w') as outfile:
		data = {"comps": []}
		json.dump(data, outfile)

	with open('./DB/gp.json', 'w') as outfile:
		json.dump(gp, outfile)

	print "Carpeta y archivo de inicio creados"

inicio_bot()