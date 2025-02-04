import pandas as pd
import json
from cherrypicker import CherryPicker


json_string= '{"title":"Varuimport och varuexport. Volymindex 2015=100 efter produktgrupp SPIN 2015, tabellinnehåll och år","variables":[{"code":"SPIN2015","text":"produktgrupp SPIN 2015","values":["Tot","01-03","05-08","05-06","07.1","07.2+08","10-32","10-12","13-15","16","16.1","17.11","17.12+17.2","18","19","20","21","22","23","24","24.1-24.3+24.51-.52","24.4+24.53-24.54","25","26-28","26.1-26.4","26.5-26.8+27","28","29-30","29.101","29.102","29.2-29.3","30","31-32","35+37+38+58+59+71 mm"],"valueTexts":["Total varuhandel","Produkter från jord- och skogsbruk och fiske","Råolja, kol, metallmalmer, mineraler och naturgas","Råolja, kol och naturgas","Järnmalm","Övriga metallmalmer, produkter från utvinning mineral","Tillverkningsindustrivaror","Livsmedel, drycker och tobaksvaror","Textilvaror, kläder, lädervaror","Trä och varor av trä och kork (utom möbler); varor av halm, rotting o.d.","Trä, sågat och hyvlat","Massa","Papper, papp och pappersvaror","Grafiska tjänster och tjänster avseende reproduktion av inspelningar","Stenkolsprodukter och raffinerade petroleumprodukter","Kemikalier och kemiska produkter","Farmaceutiska basprodukter och läkemedel","Gummi- och plastvaror","Andra icke-metalliska mineraliska produkter","Metaller","Järn och stål, ferrolegeringar, järn- och stålprodukter","Övriga metaller","Metallvaror, utom maskiner och apparater","Datorer, elektronikvaror, optik, elapparatur och övriga maskiner","Elektroniska komponenter, kretskort, datorer, kringutrustning och hemelektronik","Mätinstrument, ur, optik- o fotovaror och elapparatur","Övriga maskiner","Lastbilar, andra tunga motorfordon och andra transportmedel","Personbilar och andra lätta motorfordon","Lastbilar och andra tunga motorfordon","Karosserier, släpvagnar, motorfordonsdelar och tillbehör","Andra transportmedel","Möbler och andra tillverkade varor","Övriga varor"]},{"code":"ContentsCode","text":"tabellinnehåll","values":["0000029W","0000029V"],"valueTexts":["Varuimportvolym, index","Varuexportvolym, index"]},{"code":"Tid","text":"år","values":["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"],"valueTexts":["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"],"time":true}]}'
dataf= json.loads(json_string)

data_variables = dataf['variables']
# from_dict(json_string["variables"])
picker = CherryPicker(dataf)
flat = picker['variables'].flatten().get()
df = pd.DataFrame(flat)
print(df)

# for i in data_variables:
#     print(i)

# df = pd.DataFrame.from_dict(data_variables)
# piv = pd.pivot_table(pd, values='år', index=["Tid"])

# def replace_nulls(dataf):
#     if isinstance(dataf, dict):
#         return {key: replace_nulls(value) for key, value in dataf.items()}
#     elif isinstance(dataf, list):
#         return [replace_nulls(item) for item in dataf]
#     else:
#         # Replace None (null) and False with a default value
#         if dataf is None:
#             return ""  # Replace None (null) with empty string or another value
#         elif dataf is False:
#             return "N/A"  
#         else: 
#             return dataf
        

# dataf = replace_nulls(dataf)

# # Print the modified dataset
# print(json.dumps(dataf, indent=4))
# print(df.get('title'))
# print(type(df))
# print(piv)


