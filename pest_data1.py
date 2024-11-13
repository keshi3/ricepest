from sklearn.tree import DecisionTreeClassifier
import numpy as np

feature_mapping = {
    'pest_type': {'Rice Bug': 0, 'Stem Borer': 1, 'Green Leafhopper': 2, 'Leaf Folder': 3, 'Mole Cricket': 4},
    'season': {'sunny': 0, 'rainy': 1},
    'pest_density': {'Maritak': 0, 'Marakal': 1, 'Sobra Karakal': 2, 'Ali na Abilang': 3},
    'eradication_technique': {'Physical+Mechanical 1': 0, 'Cultural 1': 1, 'Biological 1': 2,  'Chemical 1': 3,
                                 'Physical+Mechanical 2': 4,  'Cultural 2': 5,  'Biological 2': 6, 'Chemical 2': 7,
                                  'Physical+Mechanical 3': 8,  'Cultural 3': 9, 'Chemical 3': 10,  'Physical+Mechanical 4': 11,
                                   'Cultural 4': 12,  'Chemical 4': 13,  'Physical+Mechanical 5': 14,  'Cultural 5': 15,  'Biological 5': 16,
                                    'Chemical 5': 17,  'None': 18}
}
data = [ 
['Rice Bug', 'sunny', 'Maritak', 'Physical+Mechanical 1'],      
['Rice Bug', 'rainy', 'Maritak', 'Cultural 1'],
['Rice Bug', 'sunny', 'Marakal', 'Biological 1'],
['Rice Bug', 'rainy', 'Marakal', 'Cultural 1'],
['Rice Bug', 'sunny', 'Sobra Karakal', 'Chemical 1'],
['Rice Bug', 'rainy', 'Sobra Karakal', 'Chemical 1'],
['Rice Bug', 'rainy', 'Ali na Abilang', 'None'],
['Rice Bug', 'sunny', 'Ali na Abilang', 'None'],
['Stem Borer', 'sunny', 'Maritak', 'Physical+Mechanical 2'],
['Stem Borer', 'rainy', 'Maritak', 'Cultural 2'],
['Stem Borer', 'sunny', 'Marakal', 'Biological 2'],
['Stem Borer', 'rainy', 'Marakal', 'Cultural 2'],
['Stem Borer', 'sunny', 'Sobra Karakal', 'Chemical 2'],
['Stem Borer', 'rainy', 'Sobra Karakal', 'Chemical 2'],
['Stem Borer', 'rainy', 'Ali na Abilang', 'None'],
['Stem Borer', 'sunny', 'Ali na Abilang', 'None'],
['Green Leafhopper', 'sunny', 'Maritak', 'Cultural 3'],  
['Green Leafhopper', 'rainy', 'Maritak', 'Cultural 3'],
['Green Leafhopper', 'sunny', 'Marakal', 'Physical+Mechanical 3'],      
['Green Leafhopper', 'rainy', 'Marakal', 'Cultural 3'],
['Green Leafhopper', 'sunny', 'Sobra Karakal', 'Chemical 3'],
['Green Leafhopper', 'rainy', 'Sobra Karakal', 'Chemical 3'],
['Green Leafhopper', 'sunny', 'Ali na Abilang', 'None'],
['Green Leafhopper', 'rainy', 'Ali na Abilang', 'None'],
['Leaf Folder', 'sunny', 'Maritak', 'Cultural 4'],
['Leaf Folder', 'rainy', 'Maritak', 'Cultural 4'],
['Leaf Folder', 'sunny', 'Marakal', 'Cultural 4'],   
['Leaf Folder', 'rainy', 'Marakal', 'Physical+Mechanical 4'],
['Leaf Folder', 'sunny', 'Sobra Karakal', 'Chemical 4'],
['Leaf Folder', 'rainy', 'Sobra Karakal', 'Chemical 4'],
['Leaf Folder', 'sunny', 'Ali na Abilang', 'None'],
['Leaf Folder', 'rainy', 'Ali na Abilang', 'None'],
['Mole Cricket', 'sunny', 'Maritak', 'Biological 5'],
['Mole Cricket', 'rainy', 'Maritak', 'Cultural 5'],
['Mole Cricket', 'sunny', 'Marakal', 'Physical+Mechanical 5'],      
['Mole Cricket', 'rainy', 'Marakal', 'Cultural 5'],
['Mole Cricket', 'sunny', 'Sobra Karakal', 'Chemical 5'],
['Mole Cricket', 'rainy', 'Sobra Karakal', 'Chemical 5'],
['Mole Cricket', 'sunny', 'Ali na Abilang', 'None'],
['Mole Cricket', 'rainy', 'Ali na Abilang', 'None']
]

X = [[feature_mapping['pest_type'][d[0]], feature_mapping['season'][d[1]], feature_mapping['pest_density'][d[2]]] for d in data]
y = [feature_mapping['eradication_technique'][d[3]] for d in data]

clf = DecisionTreeClassifier()
clf.fit(X, y)

eradication_descriptions = {
    'Physical+Mechanical 1': "Hulihin ang rice bugs gamit ang lambat tuwing umaga o hapon. Epektibo ito kung kakaunti lang ang rice bugs, pero nangangailangan ito ng tiyaga.",
    
    'Cultural 1': (
        "Tanggalin ang mga damo sa loob at paligid ng bukid para hindi dumami ang rice bugs kapag bakante ang mga taniman.<br><br>"
        "Pantayin ang lupa at maglagay ng pantay-pantay na pataba at tubig para sabay-sabay tumubo ang palay.<br><br>"
        "Sabay-sabay na magtanism sa mga bukid sa baryo para mabawasan ang rice bugs."
    ),
    
    'Biological 1': "Hayaan ang mga natural na kalaban ng rice bugs tulad ng wasps, grasshoppers, at gagamba na kumakain ng rice bugs at ng kanilang mga itlog. Iwasan ang sobrang paggamit ng insecticide para hindi mamatay ang mga ito.",
    
    'Chemical 1': (
        "Kumonsulta muna sa crop protection expert bago gumamit ng pesticide para sa tamang payo at babala.<br><br>"
        "Simulan ang pag-inspeksyon ng bukid bago mamulaklak ang palay at ituloy araw-araw hanggang tumigas ang butil.<br><br>"
        "Bilangin ang rice bugs tuwing umaga o hapon sa 20 halaman habang naglalakad sa bukid.<br><br>"
        "Karaniwang lumilipad ang mga adult, kaya mas madalas mabibilang ay mga juvenile. Kung may higit 10 rice bugs sa 20 halaman, maaaring kailangan ng direktang aksyon.<br><br>"
        "Pumili ng insecticide batay sa kagamitan, presyo, karanasan, at kung may presensya ng isda sa lugar. Timbangin ang benepisyo at panganib sa kalusugan at kalikasan bago gamitin."
    ),
    
    'Physical+Mechanical 2': (
        "Sa seedbed at paglipat-tanim, pitasin at sirain ang mga itlog ng peste sa halaman.<br><br>"
        "Paminsan-minsang taasan ang antas ng tubig sa irigasyon upang malubog ang mga itlog sa ibabang bahagi ng halaman.<br><br>"
        "Bago maglipat-tanim, putulin ang tuktok ng dahon para mabawasan ang itlog na naililipat mula seedbed papunta sa bukid."
    ),
    
    'Cultural 2': (
        "Gumamit ng mga matitibay na uri ng palay na hindi madaling dapuan ng peste.<br><br>"
        "Siguraduhing tama ang timing ng pagtatanim at gawin itong sabay-sabay sa buong baryo.<br><br>"
        "Anihin ang pinakamababang bahagi ng halaman upang alisin ang mga larvae sa mga tangkay.<br><br>"
        "Alisin ang mga natirang tangkay at kusang tumutubo na palay, saka araruhin at bahaing mabuti ang bukid."
    ),
    
    'Biological 2': "Hayaan ang mga natural na kalaban ng mga peste: may mga insekto tulad ng wasps, langgam, lady beetle, damselfly, dragonfly, gagamba, at iba pa na tumutulong sa pagkontrol ng peste. Bacteria, fungi, at nematodes ay nakakaapekto rin sa mga larvae ng peste.",
    
    'Chemical 2': "Hatiin ang paglagay ng nitrogen fertilizer at sundin ang tamang dami at tamang oras ng aplikasyon.",
    
    'Physical+Mechanical 3': "Maglagay ng nitrogen ayon sa pangangailangan gamit ang Leaf Color Chart para maiwasan ang pagdami ng leafhopper.",
    
    'Cultural 3': (
        "Gumamit ng mga matitibay na uri ng palay laban sa GLH at tungro; kumonsulta sa lokal na opisina ng agrikultura.<br><br>"
        "Magtanim ng palay nang dalawang beses sa isang taon at sabay-sabay sa ibang bukid para mabawasan ang leafhopper.<br><br>"
        "Gumamit ng lumang punla (3 linggo pataas) para mabawasan ang panganib ng sakit.<br><br>"
        "Magtanim nang maaga, lalo na sa tag-init, para maiwasan ang sakit na dulot ng mga insekto.<br><br>"
        "Iwasan ang pagtatanim sa panahon ng mataas na aktibidad ng GLH. Gumamit ng light traps para malaman ang dami ng GLH."
    ),
    
    'Chemical 3': "Mag-spray ng insecticide nang dalawang beses, 15 at 30 araw pagkatapos maglipat-tanim. Mag-spray ng tulad ng Fenitrothion.",
    
    'Physical+Mechanical 4': (
        "Pag-spray ng pesticides: Hindi inirerekomenda ang paggamit ng pesticides sa maagang yugto ng crop.<br><br>"
        "Maraming magsasaka sa Asya ang walang tamang safety equipment at kaalaman para sa ligtas na paggamit ng pesticides. Mas mainam na kumonsulta sa crop protection specialist para sa tamang payo."
    ),
    
    'Cultural 4': (
        "Gumamit ng matitibay na uri ng palay; kumonsulta sa lokal na opisina ng agrikultura para sa updated na listahan.<br><br>"
        "Magtanim ng ibang crop pagkatapos ng palay o magpahinga ng lupa.<br><br>"
        "Iwasan ang ratooning (pagtatanim mula sa natirang ugat).<br><br>"
        "Magbaha at araruhin ang bukid pagkatapos anihin kung posible.<br><br>"
        "Alisin ang mga damo sa loob at gilid ng bukid.<br><br>"
        "Bawasan ang dami ng tanim.<br><br>"
        "Gumamit ng tamang dami ng pataba."
    ),
    
    'Chemical 4': "Mag-spray ng insecticides tulad ng flubendiamide, chlorantraniliprole, alpha-cypermethrin, abamectin 2%, cartap hydrochloride, at profenofos.",
    
    'Physical+Mechanical 5': "Panatilihing may nakatayong tubig sa bukirin.",
    
    'Cultural 5': (
        "Gumamit ng matitibay na uri ng palay (modernong uri na may mahahabang hibla) na mas matibay sa pinsala. Kumonsulta sa lokal na opisina ng agrikultura para sa updated na listahan.<br><br>"
        "Bahain ang mga bukirin nang 3-4 na araw at pantayin ang lupa para sa mas mabuting kontrol ng tubig.<br><br>"
        "Iwasan ang raised nursery para mabawasan ang pinsala sa mga punla.<br><br>"
        "Sa paghahanda ng lupa, kolektahin ang mga nymph at adult na mole crickets."
    ),
    
    'Biological 5': "Hayaan ang mga natural na kalaban tulad ng sphecid wasp, carabid beetle, nematodes, at fungus; nagkakainan din ang mga mole cricket dahil sa kanilang cannibalistic na ugali.",
    
    'Chemical 5': "Gumamit ng pain para sa mga insekto: haluin ang basang rice bran at insecticide at ilagay ito sa tabi ng mga bunton ng palay o mas tuyong bahagi ng bukirin.",
    
    'None': "Walang kailangang gawin dahil anumang paraan ay makakadagdag lamang sa gastos."
}

