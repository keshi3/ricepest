from sklearn.tree import DecisionTreeClassifier
import numpy as np

feature_mapping = {
    'pest_type': {'Rice Bug': 0, 'Stem Borer': 1, 'Green Leafhopper': 2, 'Leaf Folder': 3},
    'season': {'sunny': 0, 'rainy': 1},
    'pest_density': {'Maritak': 0, 'Marakal': 1, 'Sobra Karakal': 2, 'Ali na Abilang': 3},
    'eradication_technique': {'Physical + Mechanical 1': 0, 'Cultural 1': 1, 'Biological 1': 2,  'Chemical 1': 3,
                                 'Physical + Mechanical 2': 4,  'Cultural 2': 5,  'Biological 2': 6, 'Chemical 2': 7,
                                  'Physical + Mechanical 3': 8,  'Cultural 3': 9, 'Chemical 3': 10,  'Physical + Mechanical 4': 11,
                                   'Cultural 4': 12,  'Chemical 4': 13,  'None': 14}
}
data = [ 
['Rice Bug', 'sunny', 'Maritak', 'Physical + Mechanical 1'],      
['Rice Bug', 'rainy', 'Maritak', 'Cultural 1'],
['Rice Bug', 'sunny', 'Marakal', 'Biological 1'],
['Rice Bug', 'rainy', 'Marakal', 'Cultural 1'],
['Rice Bug', 'sunny', 'Sobra Karakal', 'Chemical 1'],
['Rice Bug', 'rainy', 'Sobra Karakal', 'Chemical 1'],
['Rice Bug', 'rainy', 'Ali na Abilang', 'None'],
['Rice Bug', 'sunny', 'Ali na Abilang', 'None'],
['Stem Borer', 'sunny', 'Maritak', 'Physical + Mechanical 2'],
['Stem Borer', 'rainy', 'Maritak', 'Cultural 2'],
['Stem Borer', 'sunny', 'Marakal', 'Biological 2'],
['Stem Borer', 'rainy', 'Marakal', 'Cultural 2'],
['Stem Borer', 'sunny', 'Sobra Karakal', 'Chemical 2'],
['Stem Borer', 'rainy', 'Sobra Karakal', 'Chemical 2'],
['Stem Borer', 'rainy', 'Ali na Abilang', 'None'],
['Stem Borer', 'sunny', 'Ali na Abilang', 'None'],
['Green Leafhopper', 'sunny', 'Maritak', 'Cultural 3'],  
['Green Leafhopper', 'rainy', 'Maritak', 'Cultural 3'],
['Green Leafhopper', 'sunny', 'Marakal', 'Physical + Mechanical 3'],      
['Green Leafhopper', 'rainy', 'Marakal', 'Cultural 3'],
['Green Leafhopper', 'sunny', 'Sobra Karakal', 'Chemical 3'],
['Green Leafhopper', 'rainy', 'Sobra Karakal', 'Chemical 3'],
['Green Leafhopper', 'sunny', 'Ali na Abilang', 'None'],
['Green Leafhopper', 'rainy', 'Ali na Abilang', 'None'],
['Leaf Folder', 'sunny', 'Maritak', 'Cultural 4'],
['Leaf Folder', 'rainy', 'Maritak', 'Cultural 4'],
['Leaf Folder', 'sunny', 'Marakal', 'Cultural 4'],   
['Leaf Folder', 'rainy', 'Marakal', 'Physical + Mechanical 4'],
['Leaf Folder', 'sunny', 'Sobra Karakal', 'Chemical 4'],
['Leaf Folder', 'rainy', 'Sobra Karakal', 'Chemical 4'],
['Leaf Folder', 'sunny', 'Ali na Abilang', 'None'],
['Leaf Folder', 'rainy', 'Ali na Abilang', 'None'],
]

X = [[feature_mapping['pest_type'][d[0]], feature_mapping['season'][d[1]], feature_mapping['pest_density'][d[2]]] for d in data]
y = [feature_mapping['eradication_technique'][d[3]] for d in data]

clf = DecisionTreeClassifier()
clf.fit(X, y)
eradication_descriptions = {
    'Physical + Mechanical 1': (
        "Description: Hulihin ang rice bugs gamit ang lambat tuwing umaga o hapon. Epektibo ito kung kakaunti lang ang rice bugs, pero nangangailangan ito ng tiyaga."
        "Materials Needed: Lambat o net."
        "Precautions: Siguraduhing walang butas ang lambat upang hindi makatakas ang rice bugs."
    ),
    
    'Cultural 1': (
        "Description: Tanggalin ang mga damo sa loob at paligid ng bukid para hindi dumami ang rice bugs kapag bakante ang mga taniman."
        "Pantayin ang lupa at maglagay ng pantay-pantay na pataba at tubig para sabay-sabay tumubo ang palay."
        "Sabay-sabay na magtanim sa mga bukid sa baryo para mabawasan ang rice bugs."
        "Materials Needed: Mga kagamitan sa paglinis ng damo, Pataba."
        "Precautions: Siguraduhing ang mga damo ay ligtas na tinatanggal upang maiwasan ang pagdami ng peste."
    ),
    
    'Biological 1': (
        "Description: Hayaan ang mga natural na kalaban ng rice bugs tulad ng wasps, grasshoppers, at gagamba na kumakain ng rice bugs at ng kanilang mga itlog. Iwasan ang sobrang paggamit ng insecticide para hindi mamatay ang mga ito."
        "Materials Needed: Walang partikular na kagamitan."
        "Precautions: Iwasan ang pag-spray ng insecticides sa lugar kung saan naroroon ang mga natural predators."
    ),
    
    'Chemical 1': (
        "Description: Kumonsulta muna sa crop protection expert bago gumamit ng pesticide para sa tamang payo at babala."
        "Simulan ang pag-inspeksyon ng bukid bago mamulaklak ang palay at ituloy araw-araw hanggang tumigas ang butil."
        "Bilangin ang rice bugs tuwing umaga o hapon sa 20 halaman habang naglalakad sa bukid."
        "Karaniwang lumilipad ang mga adult, kaya mas madalas mabibilang ay mga juvenile. Kung may higit 10 rice bugs sa 20 halaman, maaaring kailangan ng direktang aksyon."
        "Pumili ng insecticide batay sa kagamitan, presyo, karanasan, at kung may presensya ng isda sa lugar. Timbangin ang benepisyo at panganib sa kalusugan at kalikasan bago gamitin."
        "Materials Needed: Insecticide, Konsultasyon sa crop protection expert."
        "Precautions: Siguraduhin ang kaligtasan ng kapaligiran at kalusugan bago mag-spray ng insecticides."
    ),
    
    'Physical + Mechanical 2': (
        "Description: Sa seedbed at paglipat-tanim, pitasin at sirain ang mga itlog ng peste sa halaman."
        "Paminsan-minsang taasan ang antas ng tubig sa irigasyon upang malubog ang mga itlog sa ibabang bahagi ng halaman."
        "Bago maglipat-tanim, putulin ang tuktok ng dahon para mabawasan ang itlog na naililipat mula seedbed papunta sa bukid.<"
        "Materials Needed: Mga kagamitan sa pag-pitas ng itlog, Irigasyon system."
        "Precautions: Siguraduhing maayos ang pagkakatubo ng mga halaman matapos ang proseso."
    ),
    
    'Cultural 2': (
        "Description: Gumamit ng mga matitibay na uri ng palay na hindi madaling dapuan ng peste."
        "Siguraduhing tama ang timing ng pagtatanim at gawin itong sabay-sabay sa buong baryo."
        "Anihin ang pinakamababang bahagi ng halaman upang alisin ang mga larvae sa mga tangkay."
        "Alisin ang mga natirang tangkay at kusang tumutubo na palay, saka araruhin at bahaing mabuti ang bukid.<br><br>"
        "Materials Needed: Matitibay na uri ng binhi ng palay."
        "Precautions: Siguraduhing pantay-pantay ang pataba at tubig sa buong bukid."
    ),
    
    'Biological 2': (
        "Description: Hayaan ang mga natural na kalaban ng mga peste: may mga insekto tulad ng wasps, langgam, lady beetle, damselfly, dragonfly, gagamba, at iba pa na tumutulong sa pagkontrol ng peste. Bacteria, fungi, at nematodes ay nakakaapekto rin sa mga larvae ng peste."
        "Materials Needed: Walang partikular na kagamitan."
        "Precautions: Huwag gumamit ng malalakas na pesticides na maaaring makapinsala sa mga natural predators."
    ),
    
    'Chemical 2': (
        "Description: Hatiin ang paglagay ng nitrogen fertilizer at sundin ang tamang dami at tamang oras ng aplikasyon."
        "Materials Needed: Nitrogen fertilizer."
        "Precautions: Iwasan ang labis na paglalagay ng fertilizer upang hindi makasira sa lupa at tubig."
    ),
    
    'Physical + Mechanical 3': (
        "Description: Maglagay ng nitrogen ayon sa pangangailangan gamit ang Leaf Color Chart para maiwasan ang pagdami ng leafhopper."
        "Materials Needed: Leaf Color Chart, Nitrogen fertilizer."
        "Precautions: Siguraduhing tama ang pagkakalagay ng nitrogen upang maiwasan ang pag-atake ng mga leafhoppers."
    ),
    
    'Cultural 3': (
        "Description: Gumamit ng mga matitibay na uri ng palay laban sa GLH at tungro; kumonsulta sa lokal na opisina ng agrikultura."
        "Magtanim ng palay nang dalawang beses sa isang taon at sabay-sabay sa ibang bukid para mabawasan ang leafhopper."
        "Gumamit ng lumang punla (3 linggo pataas) para mabawasan ang panganib ng sakit."
        "Magtanim nang maaga, lalo na sa tag-init, para maiwasan ang sakit na dulot ng mga insekto."
        "Iwasan ang pagtatanim sa panahon ng mataas na aktibidad ng GLH. Gumamit ng light traps para malaman ang dami ng GLH."
        "Materials Needed: Matitibay na uri ng binhi laban sa GLH."
        "Precautions: Iwasan ang pagtatanim sa panahon ng mataas na aktibidad ng GLH."
    ),
    
    'Chemical 3': (
        "Description: Mag-spray ng insecticide nang dalawang beses, 15 at 30 araw pagkatapos maglipat-tanim. Mag-spray ng tulad ng Fenitrothion."
        "Materials Needed: Insecticide (Fenitrothion)."
        "Precautions: Siguraduhing tamang gamit at proteksiyon para sa ligtas na pag-spray."
    ),
    
    'Physical + Mechanical 4': (
        "Description: Pag-spray ng pesticides: Hindi inirerekomenda ang paggamit ng pesticides sa maagang yugto ng crop."
        "Maraming magsasaka sa Asya ang walang tamang safety equipment at kaalaman para sa ligtas na paggamit ng pesticides. Mas mainam na kumonsulta sa crop protection specialist para sa tamang payo."
        "Materials Needed: Pesticides, Konsultasyon sa crop protection expert."
        "Precautions: Siguraduhing may tamang safety equipment ang magsasaka."
    ),
    
    'Cultural 4': (
        "Description: Gumamit ng matitibay na uri ng palay; kumonsulta sa lokal na opisina ng agrikultura para sa updated na listahan."
        "Magtanim ng ibang crop pagkatapos ng palay o magpahinga ng lupa."
        "Iwasan ang ratooning (pagtatanim mula sa natirang ugat)."
        "Magbaha at araruhin ang bukid pagkatapos anihin kung posible."
        "Alisin ang mga damo sa loob at gilid ng bukid."
        "Bawasan ang dami ng tanim."
        "Gumamit ng tamang dami ng pataba."
        "Materials Needed: Matibay na uri ng palay, Konsultasyon para sa crop rotation."
        "Precautions: Iwasan ang ratooning upang hindi maipasa ang peste sa susunod na tanim."
    ),
    
    'Chemical 4': (
        "Description: Mag-spray ng insecticides tulad ng flubendiamide, chlorantraniliprole, alpha-cypermethrin, abamectin 2%, cartap hydrochloride, at profenofos."
        "Materials Needed: Insecticides (flubendiamide, chlorantraniliprole, etc.)."
        "Precautions: Iwasan ang over-spray at tiyaking ligtas sa kalusugan ang paggamit ng mga insecticides."
    ),

    'None': "Walang kailangang gawin dahil anumang paraan ay makakadagdag lamang sa gastos."
}