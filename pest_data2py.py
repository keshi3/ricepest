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
        "Hulihin ang rice bugs gamit ang lambat tuwing umaga o hapon. Epektibo ito kung kakaunti lang ang rice bugs, pero nangangailangan ito ng tiyaga.<br>"
        "<strong>Materials Needed:</strong> Lambat o net.<br>"
        "<strong>Precautions:</strong> Siguraduhing walang butas ang lambat upang hindi makatakas ang rice bugs."
    ),
    
    'Cultural 1': (
        "Tanggalin ang mga damo sa loob at paligid ng bukid para hindi dumami ang rice bugs kapag bakante ang mga taniman.<br>"
        "Pantayin ang lupa at maglagay ng pantay-pantay na pataba at tubig para sabay-sabay tumubo ang palay.<br>"
        "Sabay-sabay na magtanim sa mga bukid sa baryo para mabawasan ang rice bugs.<br>"
        "<strong>Materials Needed:</strong> Mga kagamitan sa paglinis ng damo, Pataba.<br>"
        "<strong>Precautions:</strong> Siguraduhing ang mga damo ay ligtas na tinatanggal upang maiwasan ang pagdami ng peste."
    ),
    
    'Biological 1': (
        "Hayaan ang mga natural na kalaban ng rice bugs tulad ng wasps, grasshoppers, at gagamba na kumakain ng rice bugs at ng kanilang mga itlog. Iwasan ang sobrang paggamit ng insecticide para hindi mamatay ang mga ito.<br>"
        "<strong>Materials Needed:</strong> Walang partikular na kagamitan.<br>"
        "<strong>Precautions:</strong> Iwasan ang pag-spray ng insecticides sa lugar kung saan naroroon ang mga natural predators."
    ),
    
    'Chemical 1': (
        "Kumonsulta muna sa crop protection expert bago gumamit ng pesticide para sa tamang payo at babala.<br>"
        "Simulan ang pag-inspeksyon ng bukid bago mamulaklak ang palay at ituloy araw-araw hanggang tumigas ang butil.<br>"
        "Bilangin ang rice bugs tuwing umaga o hapon sa 20 halaman habang naglalakad sa bukid.<br>"
        "Karaniwang lumilipad ang mga adult, kaya mas madalas mabibilang ay mga juvenile. Kung may higit 10 rice bugs sa 20 halaman, maaaring kailangan ng direktang aksyon.<br>"
        "Pumili ng insecticide batay sa kagamitan, presyo, karanasan, at kung may presensya ng isda sa lugar. Timbangin ang benepisyo at panganib sa kalusugan at kalikasan bago gamitin.<br>"
        "<strong>Materials Needed:</strong> Insecticide, Konsultasyon sa crop protection expert.<br>"
        "<strong>Precautions</strong> Siguraduhin ang kaligtasan ng kapaligiran at kalusugan bago mag-spray ng insecticides."
    ),
    
    'Physical + Mechanical 2': (
        "Sa seedbed at paglipat-tanim, pitasin at sirain ang mga itlog ng peste sa halaman.<br>"
        "Paminsan-minsang taasan ang antas ng tubig sa irigasyon upang malubog ang mga itlog sa ibabang bahagi ng halaman.<br>"
        "Bago maglipat-tanim, putulin ang tuktok ng dahon para mabawasan ang itlog na naililipat mula seedbed papunta sa bukid.<br>"
        "<strong>Materials Needed:</strong> Mga kagamitan sa pag-pitas ng itlog, Irigasyon system.<br>"
        "<strong>Precautions:</strong> Siguraduhing maayos ang pagkakatubo ng mga halaman matapos ang proseso."
    ),
    
    'Cultural 2': (
        "Gumamit ng mga matitibay na uri ng palay na hindi madaling dapuan ng peste.<br>"
        "Siguraduhing tama ang timing ng pagtatanim at gawin itong sabay-sabay sa buong baryo.<br>"
        "Anihin ang pinakamababang bahagi ng halaman upang alisin ang mga larvae sa mga tangkay.<br>"
        "Alisin ang mga natirang tangkay at kusang tumutubo na palay, saka araruhin at bahaing mabuti ang bukid.<br>"
        "<strong>Materials Needed:</strong> Matitibay na uri ng binhi ng palay.<br>"
        "<strong>Precautions:</strong> Siguraduhing pantay-pantay ang pataba at tubig sa buong bukid."
    ),
    
    'Biological 2': (
        "Hayaan ang mga natural na kalaban ng mga peste: may mga insekto tulad ng wasps, langgam, lady beetle, damselfly, dragonfly, gagamba, at iba pa na tumutulong sa pagkontrol ng peste. Bacteria, fungi, at nematodes ay nakakaapekto rin sa mga larvae ng peste.<br>"
        "<strong>Materials Needed:</strong> Walang partikular na kagamitan.<br>"
        "<strong>Precautions:</strong> Huwag gumamit ng malalakas na pesticides na maaaring makapinsala sa mga natural predators.<br>"
    ),
    
    'Chemical 2': (
        "Hatiin ang paglagay ng nitrogen fertilizer at sundin ang tamang dami at tamang oras ng aplikasyon.<br>"
        "<strong>Materials Needed:</strong> Nitrogen fertilizer.<br>"
        "<strong>Precautions:</strong> Iwasan ang labis na paglalagay ng fertilizer upang hindi makasira sa lupa at tubig.<br>"
    ),
    
    'Physical + Mechanical 3': (
        "Maglagay ng nitrogen ayon sa pangangailangan gamit ang Leaf Color Chart para maiwasan ang pagdami ng leafhopper.<br>"
        "<strong>Materials Needed:</strong> Leaf Color Chart, Nitrogen fertilizer.<br>"
        "<strong>Precautions:</strong> Siguraduhing tama ang pagkakalagay ng nitrogen upang maiwasan ang pag-atake ng mga leafhoppers."
    ),
    
    'Cultural 3': (
        "Gumamit ng mga matitibay na uri ng palay laban sa GLH at tungro; kumonsulta sa lokal na opisina ng agrikultura.<br>"
        "Magtanim ng palay nang dalawang beses sa isang taon at sabay-sabay sa ibang bukid para mabawasan ang leafhopper.<br>"
        "Gumamit ng lumang punla (3 linggo pataas) para mabawasan ang panganib ng sakit.<br>"
        "Magtanim nang maaga, lalo na sa tag-init, para maiwasan ang sakit na dulot ng mga insekto.<br>"
        "Iwasan ang pagtatanim sa panahon ng mataas na aktibidad ng GLH. Gumamit ng light traps para malaman ang dami ng GLH.<br>"
        "<strong>Materials Needed:</strong> Matitibay na uri ng binhi laban sa GLH.<br>"
        "<strong>Precautions:</strong> Iwasan ang pagtatanim sa panahon ng mataas na aktibidad ng GLH."
    ),
    
    'Chemical 3': (
        "Mag-spray ng insecticide nang dalawang beses, 15 at 30 araw pagkatapos maglipat-tanim. Mag-spray ng tulad ng Fenitrothion.<br>"
        "<strong>Materials Needed:</strong> Insecticide (Fenitrothion).<br>"
        "<strong>Precautions:</strong> Siguraduhing tamang gamit at proteksiyon para sa ligtas na pag-spray."
    ),
    
    'Physical + Mechanical 4': (
        "Pag-spray ng pesticides: Hindi inirerekomenda ang paggamit ng pesticides sa maagang yugto ng crop.<br>"
        "Maraming magsasaka sa Asya ang walang tamang safety equipment at kaalaman para sa ligtas na paggamit ng pesticides. Mas mainam na kumonsulta sa crop protection specialist para sa tamang payo.<br>"
        "<strong>Materials Needed:</strong> Pesticides, Konsultasyon sa crop protection expert.<br>"
        "<strong>Precautions:</strong> Siguraduhing may tamang safety equipment ang magsasaka."
    ),
    
    'Cultural 4': (
        "Gumamit ng matitibay na uri ng palay; kumonsulta sa lokal na opisina ng agrikultura para sa updated na listahan.<br>"
        "Magtanim ng ibang crop pagkatapos ng palay o magpahinga ng lupa.<br>"
        "Iwasan ang ratooning (pagtatanim mula sa natirang ugat).<br>"
        "Magbaha at araruhin ang bukid pagkatapos anihin kung posible.<br>"
        "Alisin ang mga damo sa loob at gilid ng bukid.<br>"
        "Bawasan ang dami ng tanim.<br>"
        "Gumamit ng tamang dami ng pataba.<br>"
        "<strong>Materials Needed:</strong> Matibay na uri ng palay, Konsultasyon para sa crop rotation.<br>"
        "<strong>Precautions:</strong> Iwasan ang ratooning upang hindi maipasa ang peste sa susunod na tanim.<br>"
    ),
    
    'Chemical 4': (
        "Mag-spray ng insecticides tulad ng flubendiamide, chlorantraniliprole, alpha-cypermethrin, abamectin 2%, cartap hydrochloride, at profenofos.<br>"
        "<strong>Materials Needed:</strong> Insecticides (flubendiamide, chlorantraniliprole, etc.).<br>"
        "<strong>Precautions:</strong> Iwasan ang over-spray at tiyaking ligtas sa kalusugan ang paggamit ng mga insecticides.<br>"
    ),

    'None': "Walang kailangang gawin dahil anumang paraan ay makakadagdag lamang sa gastos."
}