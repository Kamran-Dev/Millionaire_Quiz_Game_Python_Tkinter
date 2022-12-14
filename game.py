from tkinter import *
import random
from tkinter.ttk import Progressbar
import pygame
import time

pygame.mixer.init()


def win_window():
    winner_window = Tk()
    winner_window.overrideredirect(True)
    background_color = "#790ea1"

    width = 560
    height = 360

    screen_width = winner_window.winfo_screenwidth()  # width of the screen
    screen_height = winner_window.winfo_screenheight()  # height of the screen

    about_center_x = (screen_width / 2) - (width / 2)  # find the location of app on the x coordinate
    about_center_y = (screen_height / 2) - (height / 2)  # find the location of app on the y coordinate
    winner_window.geometry("{}x{}+{}+{}".format(width, height, int(about_center_x), int(about_center_y)))
    winner_window.mainloop()

#pygame.mixer.music.load("files/start_music.mp3")
#pygame.mixer.music.play(0)

global amount_win
amount_win = 0

def game_over_function():
    import game_over
    game_over.game_over_command()


# Returns 15 random numbers generated from 3 different list
def fifteenNumberGenerator(listA, listB, listC):
    return_list = []
    while len(return_list) < 5:
        x = random.choice(listA)
        if x not in return_list:
            return_list.append(x)
    while len(return_list) < 10:
        y = random.choice(listB)
        if y not in return_list:
            return_list.append(y)
    while len(return_list) < 15:
        z = random.choice(listC)
        if z not in return_list:
            return_list.append(z)
    return return_list

# <<<<<<< ALL QUESTIONS >>>>>>>
# 1-2-3-4-5 Easy questions - 40 questions
# Totally 40 + 30 + 31 = 101 questions

questionList_A = ["0. Azərbaycan dilində hansı durğu işarəsi var?",
                  "1. İnsanın qanını qaraltmaq üçün kefinə nə doğrayırlar?",
                  "2. „Qayınana“ filmində Cənnət xala gəlinini hansı məişət əşyasına bənzətmişdir?",
                  "3. Yerli klubda çıxış edən xarici idmançılara nə deyirlər?",
                  "4. 'Mehmandar' adlı peşə sahibinin vəzifəsi nədir?",
                  "5. Çox savadlı insana nə deyirlər?",
                  "6. Nəsli kəsilmək üzrə olan heyvan və bitkilər haqqında kitab necə adlanır?",
                  "7. Aşağıdakı uzunluq vahidlərindən hansı daha kiçikdir?",
                  "8. Hansı metro stansiyası „Nizami“ və „İnşaatçılar“ stansiyalarının arasında yerləşir?",
                  "9. Qız evində elçilərə nəyin verilməsi razılıq əlaməti sayılır?",
                  "10. Pizza hansı xalqın mətbəxinə aiddir?",
                  "11. Məşhur nağılda hansı personaj yoxdur?",
                  "12. Orta əsrlərdə Azərbaycanda haranı 'Dar üş-Şəfa' adlandırırdılar?",
                  "13. Həddən artıq acıdil və kobud adama nə deyirlər?",
                  "14. 'İmzalamaq' sözünün sinonimi nədir?",
                  "15. Həftənin hansı günü çeşmə başında Aşıq Ələsgərin gözü bir alagöz xanıma düşür?",
                  "16. Hansı heyvanın adı Malay dilindən tərcümədə „Meşə adamı“ mənasını verir?",
                  "17. Tüfəngin hansı hissəsi həm də kabab adıdır?",
                  "18. Hansı heyvan növü mövcuddur?",
                  "19. Tennis meydançası necə adlanır?",
                  "20. Mollah Pənah Vaqifin türbəsi hansı şəhərdə yerləşir?",
                  "21. Azərbaycan dilinin orfoqrafiya lüğətində hansı söz daha əvvəl gəlir?",
                  "22. Hündür binaları necə adlandırırlar?",
                  "23. Restoranda müştərilərə nə tətbiq edirlər?",
                  "24. Atalar sözünə görə, ot nəyi üstə bitər?",
                  "25. Azərbaycan xalq mahnısı „Gəlmişəm otağına, oyadam səni“ sözləri kimə ünvanlanıb?",
                  "26. 221 santimetr boyu olan Ardivas Sabonis hansı idman növündə şöhrət qazanıb?",
                  "27. Şuşadakı “Xan qızı” bulağı kimin adı ilə bağlıdır?",
                  "28. Astronomlar öz peşələrində hansı cihazdan istifadə edirlər?",
                  "29. İnternetdə kobud və ya təxribatçı mesajlar yazanları necə adlandırırlar?",
                  "30. Atalar sözünə görə özgəsinə quyu qazanın aqibəti necə olur?",
                  "31. Yeni mənzil almaq istəyənlər nədən istifadə edə bilərlər?",
                  "32. Abşeron yarımadasında əsən isti cənub küləyinin adı nədir?",
                  "33. Yanıltmaca görə, hansı peşə sahibi bir bərədə öz həmkarını bər-bər bəyirdir?",
                  "34. Qədim yemək növü olan qaysavanı nədən bişirirlər?",
                  "35. Fikrini açıq, səlis və gözəl şəkildə ifadə edə bilən adama nə deyirlər?",
                  "36. Atalar sözünə görə, hansı bazar dostluğu pozar?",
                  "37. Azərbaycanda atanın bacısına nə deyirlər?",
                  "38. 'Formula 1' sürücülərini necə adlandırırlar?",
                  "39. Tamaşa zamanı aktyorlara rolların sözlərini yavaşcadan söyləyən teatr işçisi kimdir?",

                  "40. Hansı tarixi şəxsiyyət yaddaşlarda saqqalsız qalıb?",
                  "41. David Ben Qurion adına hava limanı hansı ölkədə yerləşir?",
                  "42. Hansı geyim növünün adı ingilis dilində tərcümədə „tərləmək“ mənasını verir.",
                  "43. Aşağıdakılardan hansı Şuşa qalasının əsas qapılarına aid deyil",
                  "44. Əfsanəvi isveçrəli qəhrəman Vilhelm Tell kimin başına qoyulmuş almanı oxla vurur?",
                  "45. Heyvanlar aləmini təsvir edən rəssam necə adlanır?",
                  "46. Hansı qədim kələzlər uça bilirdi?",
                  "47. Moldavanlar „Mertsişor“ bayramını hansı ayda qeyd edirlər?",
                  "48. “Molla Nəsrəddin” satiric jurnalının ilk nömrəsi harada nəşr olunmuşdur?",
                  "49. İçərişəhərdə yerləşən Sınıqqala məscidinin digər adı nədir?",
                  "50. Payızgülünü başqa cür necə adlandırırlar?",
                  "51. “Şərikli Çörək” filmində Fazil Salayevin yaratdığı Məhəmməd obrazı hansı peşənin sahibi idi?",
                  "52. Göstərilən geyim ölçülərindən ən kiçiyi hansıdır?",
                  "53. Vinni-Puh haqqında hekayədə bayquş uzunqulağa ad günündə nə hədiyyə etmişdir?",
                  "54. Fırçaotu bitkisinin digər adı nədir?",
                  "55. Sadalanan şəhərlərdən hansı daha cənubda yerləşir?",
                  "56. Satirik Stanislav Yeji Letsin fikrincə, nida işarəsi qocalıqda nəyə bənzəyir?",
                  "57. Azərbaycanlı idmançı İlham Zəkiyev hansı idman növü üzrə dəfələrlə dünya və Avropa çempionu olub?",
                  "58. Hansı ölkənin bayrağı formasına görə digərlərindən fərqlənir.",
                  "59. Əvvəlki adı “Avrora” olan metro stansiyasının indiki adı nədir?",
                  "60. Rəssam Pablo Pikassonun 1901-1904-cü illəri əhatə edən yaradıcılıq dövrü necə adlanır?",
                  "61. Hansı ayın adı qədim Roma imperatoru Qay Yuli Sezarın adı ilə bağlıdır?",
                  "62. “Karib Dənizinin Quldurları” filmində kapitan Cekin ləqəbi nə idi?",
                  "63. NATO abreviaturunda “N” hərfi hansı mənanı verir?",
                  "64. Hansı memarlıq abidəsi içəri şəhərdə yerləşir?",
                  "65. “Mən düşünürəm, deməli mövcudam.” İfadəsi hansı filosofa məxsusdur?",
                  "66. Astrid Lindqrenin qəhramanı Karlson harada yaşayırdı?",
                  "67. Əlkimyaçılar hansı elementi “canlı gümüş” adlandırırdılar?",
                  "68. Latte-art üzrə mütəxəssis nəyin üzərində naxışlar çəkir?",
                  "69. Hansı ölkənin gerbində 7 qollu şamdan təsvir olunub?",

                  # Hard questions - 31
                  "70. Deymos hansı planetin peykidir?",
                  "71. Basillər adlanan bakteriyalar hansı formada olurlar?",
                  "72. ABŞ prezidenti Qrover Klivlend evlənənə qədər Birinci Ledi adını kim daşıyırdı?",
                  "73. Azərbaycanın görkəmli şairi və musiqişünas alimi Mir Möhsün Nəvvabın evi Şuşanın hansı məhəlləsindədir?",
                  "74. Amerika basketbolçusu Devid Robinsonun ləqəbi nə idi?",
                  "75. Azərbaycan opera müğənnisi və aktyoru Hüseynqulu Sarabski səhnə fəaliyyətinə hansı rolla başlamışdır?",
                  "76. Dünya okeanında qurudan ən uzaq olan yer necə adlanır?",
                  "77. 24 Noyabr 1959-cu il tarixində hansı rayona böyük meteorit düşüb?",
                  "78. Səməd Vurğun kimi “əli qılınclı şair” adlandırırdı?",
                  "79. İslandiya parlamenti necə adlanır?",
                  "80. Daniel Defonun ədəbi qəhrəmanı Robinzon Kruzo düşdüyü adada neçə il qalıb?",
                  "81. Bunlardan hansı temperament tipi deyil?",
                  "82. Konstantinopolu hansı türk sultanı fəth edib?",
                  "83. Qədim İran Atəşpərəstləri Günəşin və Odun vəkili olan mələyi necə adlandırırdılar?",
                  "84. Əfsanəyə görə məşhur “Kohinu” almazına bu adı kim verib?",
                  "85. Kəşfiyyat üçün nəzərdə tutulmuş iti sürətli kiçik xidmət gəmisi necə adlanır?",
                  "86. İngiltərə kralı İ Eduard hansı ləqəbi daşıyırdı?",
                  "87. Yapon dilindən tərcümədə “Aykido” nə deməkdir?",
                  "88. Bir tərəfi şirin digər tərəfi şor sulu olan göl hansıdır?",
                  "89. Robin Qudun ən yaxın dostunun adı nə olub?",
                  "90. Azərbaycan dili hansı dillər ailəsinə aid edilir?",
                  "91. Napoleonun birinci arvadının adı nə idi?",
                  "92. Dəməşq poladının sirrini hansı alim açıb?",
                  "93. Rəvayətə görə bu peyğəmbər quşların və heyvanların dilini bilirdi?",
                  "94. A.S. Puşkini dueldə öldürən Dantes hansı ölkədən mühacirət etmişdir?",
                  "95. Bu gəmilərdən hansı Xristofor Kolumbun Amerika sahillərinə çatmış ekspedisiyasının tərkibinə daxil deyil?",
                  "96. Bədənə şəkil döydürmək sənəti Yaponiyada necə adlanır?",
                  "97. Olimpiya Oyunlarının medalını alan ilk azərbaycanlı idmançı kimdir?",
                  "98. 1840-cı ildə buraxılmış ilk poçt markasında kimin portreti təsvir olunub?",
                  "99. Abbasqulu ağa Bakıxanov “Kəşfül-Qəraib” əsərində haranın kəşfini qələmə alıb?",
                  "100. Roma İmperatoru Konstantinin atası Flavi Valeri Konstantinin ləqəbi nə idi?"]

first_option = ["Barmaq", "Soğan", "Tozsoran", "Qladiator", "Həkimlik", "İntellekt okeanı", "Qırmızı kitab",
                "Santimetr", '"28 May"', "Soyuq Limonad", "İtaliya", "Şəngülüm", "Həbsxana", "Alça səbəti", "Qol güləşdirmək",
                "Çərşənbə", "Oranqutan", "Lülə", "Eybəcər", "Kort", "Ağdam", "Zəngin", "Səmayaran", "Anamnez", "Kökü", "Sarıgiləyə",
                "Futbol", "Xurşidbanu Natəvan", "Mikroskop", "İfritələr", "Ad qazanır", "Filmoteka", "Gilənar",
                "Qəssab", "Alma", "Dildən qələm", "Təzə bazar", "Bibi", "Miçman", "Suflyor"]

first_option_six_to_ten = ["Dmitri Mendeleyev", "İsrail", "Cemper", "Gəncə qapısı", "Sevgilisinin", "Marinist",
                           "Steqozavrlar", "Fevral", "Bakı", "Məhəmməd Məscidi", "Lavanda", "Çilingər", "S", "Şar",
                           "Çobandarağı", "Biləsuvar", "Sual işarəsi", "Güləş", "Nepal", "“Neftçilər”", "Sarı dövr",
                           "Mart", "Sərçə", "Şimali", "Səmərqənd karvansarayı", "Rene Dekart", "Zirzəmi", "Platin",
                           "Salfet", "Çili"]

first_option_eleven_to_fifteen = ["Mars", "Kürəşəkilli", "Anası", "Köçərli", "General", "Sərvər", "Kusto nöqtəsi",
                                  "Kürdəmir", "Aşıq Ələsgər", "Knessen", "26", "Fleqmatik", "I Murad", "Hörmüzd", "Nadir şah",
                                  "Avietka", "'Kürən'", "Çətin yol", "Oneqa", "Balaca Con", "Altay dilləri", "İzabella",
                                  "Mendeleyev", "Musa peyğəmbər", "İtaliyadan", "“Santa-Mariya”", "Oriqami",
                                  "İbrahimpaşa Dadaşov", "Benjamin Franklinin", "Amerikanın", "Xlor"]

first_option += first_option_six_to_ten + first_option_eleven_to_fifteen

second_option = ["Dırnaq", "Pomidor", "Xəkəndaz", "Legioner", "Müəllimlik", "Zəka dənizi", "Sarı kitab", "Desimetr",
                 '"20 Yanvar"', "Acı qəhvə", "Yaponiya", "Məngülüm", "Bazar", "Zəhər tuluğu", "Qol vurmaq", "Bazar",
                 "Koala", "Tikə", "Kaftar", "Rinq", "Laçın", "İmkanlı", "Günəçatan", "Diplom", "Toxumu", "Göygiləyə",
                 "Tennis", "Xədicə Sultan xanım", "Teleskop", "Elflər", "Özü düşür", "Diskoteka", "Giləvar", "Həkim",
                 "Armud", "Dildən xətkeş", "Axşam bazar", "Xala", "Avtoş", "Dublyor"]

second_option_six_to_ten = ["Vinston Çörçil", "Qətər", "Jaket", "İrəvan qapısı", "Anasının", "Animalist",
                            "Allozavrlar", "Mart", "Gəncə", "Həsən məscidi", "Xrizantem", "Dulusçu", "M", "Bal",
                            "Çobantütəyi", "Sabirabad", "Nöqtə", "Cüdo", "Namibiya", "“Koroğlu”", "Qırmızı dövr",
                            "May", "Qaşqaldaq", "Cənubi", "Buxara karvansarayı", "Əflatun", "Eyvan", "Civə",
                            "Çay", "İsrail"]

second_option_eleven_to_fifteen = ["Yupiter", "Spirallşəkilli", "Qızı", "Mamayı", "Marşal", "Kərəm", "Dreyk nöqtəsi",
                                   "Şamaxı", "Aşıq Abbas Tufanqarlı", "Altinq", "27", "Xolerik", "II Səlim", "Şirvin", "Məhəmməd şah",
                                   "Avizo", "'Sülhyaradan'", "Yumşaq yol", "Baykal", "Şirürəkli Riçard", "Hindavropa dilləri",
                                   "Josefina", "Zelinski", "Nuh peyğəmbər", "İngiltərədən", "“Pinta”", "Xanami",
                                   "Rəşid Məmmədbəyov", "Corc Vaşinqtonun", "Afrikanın", "Yod"]
second_option += second_option_six_to_ten + second_option_eleven_to_fifteen

third_option = ["Caynaq", "Sarımsaq", "Vedrə", "Senturion", "Qonaq qarşılamaq", "Ağıl dəryası", "Göy kitab",
                "Millimetr", '„Elmlər Akademiyası“', "İsti kakao", "Norveç", "Şüngülüm", "Hamam", "İstiot torbası", "Qol burmaq",
                "Şənbə", "Pələng", "Tava", "Çirkin", "Tatami", "Fizuli", "Milyonçu", "Göydələn", "Menyu", "Torpağı",
                "Qaragiləyə", "Basketbol", "Fatma xanım Ani", "Periskop", "Trollar", "Susuz qalır", "Hipoteka", "Gilas", "Bərbər",
                "Ananas", "Dildən pərgar", "Bağlı bazar", "Baldız", "Pilot", "Kaskadyor"]

third_option_six_to_ten = ["Fidel Kastro", "Livan", "Pulover", "Şamaxı qapısı", "Atasının", "Batalist",
                           "Pterodaktillər", "Aprel", "Tiflis", "Şah Abbas məscidi", "Pion", "Qalayçı", "L", "Quyruq",
                           "Çobançomağı", "Cəlilabad", "Vergül", "Boks", "Nikaraqua", "“Nəriman Nərimanov”", "Çəhrayı dövr",
                           "Iyun", "Qartal", "Qərbi", "Xanaband karvansarayı", "Fridrix Nitşe", "Dam", "Alüminium",
                           "Masa", "Çin"]

third_option_eleven_to_fifteen = ["Saturn", "Çöpşəkilli", "Bacısı", "Seyidli", "Kapitan", "Rəsul", "Kuk nöqtəsi", "Ağdam",
                                  "Aşıq Şəmşir", "Stortinq", "28", "Praqmatik", "Osman", "Azər", "Babur şah", "Avaks",
                                  "'Şir ürəyi'", "Uğurlu yol", "Balxaş", "Sanço-Pansa", "Dravid dilləri", "Mariya-Luiza",
                                  "Butlerov", "Süleyman peyğəmbər", "Fransadan", "“Trinidad”", "Seppuku",
                                  "Xandadaş Mədətov", "Kraliça Viktoriyanın", "Antarktidanın", "Ftor"]
third_option += third_option_six_to_ten + third_option_eleven_to_fifteen

fourth_option = ["Ayaq", "Xiyar", "Süpürgə", "Veteran", "Vergi yığmaq", "Elm səhrası", "Yaşıl kitab", "Kilometr",
                 '„Memar Əcəmi“', "Şirin çay", "Meksika", "Səngülüm", "Xəstəxana", "Duzqabı", "Qol çəkmək", "Cümə",
                 "Canavar", "Antrekot", "Idbar", "Akvadrom", "Şuşa", "Varlı", "Buludaqalxan", "Tərcümeyi-hal",
                 "Yarpağı", "Ağgiləyə", "Hokkey", "Rəziyyə Gəncəvi", "Stetoskop", "Cinlər", "Xeyir tapır", "Kartoteka",
                 "Giləli", "Aşpaz", "Ərik", "Dildən pozan", "Örtülü bazar", "Qayınana", "Kamikadze", "Qrimçi"]

fourth_option_six_to_ten = ["Karl Marks", "İordaniya", "Sviter", "Ağoğlan qapısı", "Oğlunun", "Peyzajçı",
                            "Tiranozavrlar", "May", "Təbriz", "Şeyx İbrahim məscidi", "Süsən", "Qırçı", "XL", "Papaq",
                            "Çobanqələmi", "Salyan", "İki nöqtə", "Karate", "Norveç", "“Qara Qarayev”", "Mavi dövr",
                            "Iyul", "Qağayı", "Şərqi", "Daşkənd karvansarayı", "İmadəddin Nəsimi", "Villa", "Qurğuşun",
                            "Qəhvə köpüyü", "Yaponiya"]

fourth_option_eleven_to_fifteen = ["Venera", "Vergülşəkilli", "Rəfiqəsi", "Saatlı", "Admiral", "Məcnun", "Nemo nöqtəsi",
                                   "Yardımlı", "Aşıq Hüseyn Bozalqanlı", "Folkering", "29", "Melanxolik", "II Mehmet", "Əhriman",
                                   "Kraliça Viktoriya", "Anşlüs", "'Uzunayaq'", "Harmoniya yolu", "Ladoqa", "Balaca Rom",
                                   "Ural dilləri", "Selestina", "Anosov", "Davud peyğəmbər", "Avstriyadan", "“Ninya”",
                                   "İredzumi", "Yuri Konovalov", "Mariya Tüdorun", "Avstraliyanın", "Brom"]
fourth_option += fourth_option_six_to_ten + fourth_option_eleven_to_fifteen

correct_answers = ["Dırnaq", "Soğan", "Süpürgə", "Legioner", "Qonaq qarşılamaq", "Ağıl dəryası", "Vinston Çörçil",
                   "İsrail", "Sviter", "Şamaxı qapısı", "Oğlunun", "Mars", "Qırmızı kitab", "Millimetr",
                   '„Elmlər Akademiyası“', "Çöpşəkilli", "Şirin çay", "İtaliya", "Səngülüm", "Xəstəxana", "Animalist",
                   "Pterodaktillər", "Zəhər tuluğu", "Qol çəkmək", "Çərşənbə", "Oranqutan", "Mart", "Tiflis",
                   "Məhəmməd Məscidi", "Xrizantem", "Lülə", "Kaftar", "Kort", "Şuşa", "İmkanlı", "Qırçı", "S", "Quyruq",
                   "Göydələn", "Menyu", "Kökü", "Qaragiləyə", "Basketbol", "Çobandarağı", "Cəlilabad",  "Xurşidbanu Natəvan", "Teleskop", "Trollar", "Sual işarəsi", "Cüdo", "Nepal", "'Qara Qarayev'",
                   "Mavi dövr", "Özü düşür", "Hipoteka", "Giləvar", "Bərbər", "Ərik", "İyul", "Sərçə", "Şimali",
                   "Buxara karvansarayı", "Rene Dekart", "Bacısı", "Dildən pərgar", "Örtülü bazar", "Bibi", "Pilot",
                   "Suflyor", "Dam", "Civə", "Qəhvə köpüyü", "İsrail", "Mamayı", "Admira", "Rəsul", "Nemo nöqtəsi",
                   "Yardımlı", "Aşıq Hüseyn Bozalqanlı", "Altinq", "28", "Praqmatik", "II Mehmet", "Azər", "Nadir şah",
                   "Avizo", "'Uzunayaq'", "Harmoniya yolu", "Balxaş", "Balaca Con", "Altay dilləri", "Josefina", "Anosov",
                   "Süleyman peyğəmbər", "Fransadan", "'Trinidad'", "İredzumi", "Rəşid Məmmədbəyov", "Kraliça Viktoriyanın",
                   "Amerikanın", "Xlor"]

def run_game():
    global gameWindow

    gameWindow = Tk()
    gameWindow.title("Milyonçu")
    mainColor = "#000b55"
    questionColor = "#002669"
    optionsColor = "#003088"
    orangeColor = "#cd6802"
    gameWindow.config(bg=mainColor)




    firstList = list(range(0, 40, 1))
    secondList = list(range(40, 69, 1))
    thirdList = list(range(69, 100, 1))
    print(firstList)
    print(secondList)
    print(thirdList)

    displayedList = fifteenNumberGenerator(firstList, secondList, thirdList)
    print(displayedList)
    width = 1009
    height = 680
    screenWidth = gameWindow.winfo_screenwidth()  # width of the screen
    screenHeight = gameWindow.winfo_screenheight()  # height of the screen
    center_x = (screenWidth / 2) - (width / 2)  # find the location of app on the x coordinate
    center_y = (screenHeight / 2) - (height / 2)  # find the location of app on the y coordinate
    gameWindow.geometry("{}x{}+{}+{}".format(width, height, int(center_x), 3))

    mainColor = "#000b55"

    # <<<<<<< MAIN FRAME FOR THE CENTER >>>>>>>
    mainFrame = Frame(gameWindow, bg=mainColor)
    mainFrame.pack()

    # <<<<<<< LEFT FRAME >>>>>>>
    leftFrame = Frame(mainFrame,
                      bg=mainColor)
    leftFrame.grid(row=0, column=0)

    # <<<<<<< TOP FRAME >>>>>>>
    topFrame = Frame(leftFrame, bg=mainColor)
    topFrame.grid(row=0, column=0, pady=0)

    # <<<<<<< 50-50 Button >>>>>>>
    photo50 = PhotoImage(file="files/50-50.png")

    halfButton = Button(topFrame,
                        image=photo50,
                        bg=mainColor,
                        bd=0,
                        activebackground=mainColor,
                        width=180,
                        height=80)
    halfButton.grid(row=0, column=0)

    # <<<<<<< Audience Pole Button >>>>>>>
    photoAudience = PhotoImage(file="files/audiencePole.png")
    photoAudienceX = PhotoImage(file="files/audiencePoleX.png")
    audienceButton = Button(topFrame,
                            image=photoAudience,
                            bg=mainColor,
                            bd=0,
                            activebackground=mainColor,
                            width=180,
                            height=80)
    audienceButton.grid(row=0, column=1)

    # <<<<<<< Phone a friend Button >>>>>>>
    photoPhone = PhotoImage(file="files/phoneAFriend.png")
    photoPhoneX = PhotoImage(file="files/phoneAFriendX.png")
    phoneButton = Button(topFrame,
                         image=photoPhone,
                         bg=mainColor,
                         bd=0,
                         activebackground=mainColor,
                         width=180,
                         height=80)
    phoneButton.grid(row=0, column=2)

    # <<<<<<< Logo on the Center Label >>>>>>>
    centreFrame = Frame(leftFrame, bg=mainColor)
    centreFrame.grid(row=1, column=0)

    centerPhoto = PhotoImage(file="files/main_logo.png")
    logoLabel = Label(centreFrame, image=centerPhoto, height=360, width=370, bg=mainColor)
    logoLabel.grid(row=0, column=0)

    # <<<<<<< Bottom Frame >>>>>>>
    bottomFrame = Frame(mainFrame, bg=mainColor)
    bottomFrame.grid(row=1, column=0, columnspan=2)

    # <<<<<<< Right Frame >>>>>>>
    rightFrame = Frame(mainFrame, bg=mainColor)
    rightFrame.grid(row=0, column=1)

    # # <<<<<<< AMOUNT IMAGE LABEL >>>>>>>
    amountPhoto = PhotoImage(file="files/001.png")
    amountPhoto1 = PhotoImage(file="files/001.png")
    amountPhoto2 = PhotoImage(file="files/002.png")
    amountPhoto3 = PhotoImage(file="files/003.png")
    amountPhoto4 = PhotoImage(file="files/004.png")
    amountPhoto5 = PhotoImage(file="files/005.png")
    amountPhoto6 = PhotoImage(file="files/006.png")
    amountPhoto7 = PhotoImage(file="files/007.png")
    amountPhoto8 = PhotoImage(file="files/008.png")
    amountPhoto9 = PhotoImage(file="files/009.png")
    amountPhoto10 = PhotoImage(file="files/010.png")
    amountPhoto11 = PhotoImage(file="files/011.png")
    amountPhoto12 = PhotoImage(file="files/012.png")
    amountPhoto13 = PhotoImage(file="files/013.png")
    amountPhoto14 = PhotoImage(file="files/014.png")
    amountPhoto15 = PhotoImage(file="files/015.png")
    amountPhotoList = [amountPhoto1, amountPhoto2, amountPhoto3, amountPhoto4, amountPhoto5, amountPhoto6, amountPhoto7,
                       amountPhoto8, amountPhoto9, amountPhoto10, amountPhoto11, amountPhoto12, amountPhoto13,
                       amountPhoto14,
                       amountPhoto15]
    amountLabel = Label(rightFrame, image=amountPhoto, height=440)
    amountLabel.grid(row=0, column=0)

    # <<<<<<< QUESTIONS LAY LABEL >>>>>>>
    questionLay = PhotoImage(file="files/lay1.png")
    questionLayA = PhotoImage(file="files/lay1_A.png")
    questionLayB = PhotoImage(file="files/lay1_B.png")
    questionLayC = PhotoImage(file="files/lay1_C.png")
    questionLayD = PhotoImage(file="files/lay1_D.png")
    questionLabel = Label(bottomFrame, image=questionLay, bg=mainColor, anchor="center")
    questionLabel.grid(row=0, column=0)

    global i
    i = 0

    # <<<<<<< QUESTION TEXT AREA >>>>>>>
    questionsArea = Text(bottomFrame,
                         font=("arial", 18, "bold"),
                         width=60,
                         height=2,
                         wrap="word",
                         bg=questionColor,
                         fg="white",
                         bd=0)
    questionsArea.place(x=110, y=15)

    questionsArea.insert(END, questionList_A[displayedList[i]])
    questionsArea.config(state=DISABLED)

    # <<<<<<< FIRST OPTION >>>>>>>
    option_button_A = Button(bottomFrame,
                           text=first_option[displayedList[i]],
                           font=("arial", 17, "bold"),
                           bg=optionsColor,
                           fg="white",
                           bd=0,
                           activebackground=optionsColor,
                           activeforeground="white")
    option_button_A.place(x=130, y=116)

    def option_button_A_enter(e):

        questionLabel.config(image=questionLayA)
        option_button_A.config(bg=orangeColor, fg="BLACK", activeforeground="BLACK", activebackground=orangeColor)

    def option_button_A_leave(e):
        questionLabel.config(image=questionLay)
        option_button_A.config(bg=optionsColor, fg="WHITE", activeforeground="WHITE", activebackground=optionsColor)

    option_button_A.bind("<Enter>", option_button_A_enter)
    option_button_A.bind("<Leave>", option_button_A_leave)


    # <<<<<<< SECOND OPTION >>>>>>>
    option_button_B = Button(bottomFrame,
                           text=second_option[displayedList[i]],
                           font=("arial", 17, "bold"),
                           bg=optionsColor,
                           fg="white",
                           bd=0,
                           activebackground=optionsColor,
                           activeforeground="white")
    option_button_B.place(x=570, y=116)


    def option_button_B_enter(e):

        questionLabel.config(image=questionLayB)
        option_button_B.config(bg=orangeColor, fg="BLACK", activeforeground="BLACK", activebackground=orangeColor)

    def option_button_B_leave(e):
        questionLabel.config(image=questionLay)
        option_button_B.config(bg=optionsColor, fg="WHITE", activeforeground="WHITE", activebackground=optionsColor)

    option_button_B.bind("<Enter>", option_button_B_enter)
    option_button_B.bind("<Leave>", option_button_B_leave)

    # <<<<<<< THIRD OPTION >>>>>>>
    option_button_C = Button(bottomFrame,
                           text=third_option[displayedList[i]],
                           font=("arial", 17, "bold"),
                           bg=optionsColor,
                           fg="white",
                           bd=0,
                           activebackground=optionsColor,
                           activeforeground="white")
    option_button_C.place(x=132, y=180)


    def option_button_C_enter(e):

        questionLabel.config(image=questionLayC)
        option_button_C.config(bg=orangeColor, fg="BLACK", activeforeground="BLACK", activebackground=orangeColor)

    def option_button_C_leave(e):
        questionLabel.config(image=questionLay)
        option_button_C.config(bg=optionsColor, fg="WHITE", activeforeground="WHITE", activebackground=optionsColor)

    option_button_C.bind("<Enter>", option_button_C_enter)
    option_button_C.bind("<Leave>", option_button_C_leave)



    # <<<<<<< FOURTH OPTION >>>>>>>
    option_button_D = Button(bottomFrame,
                           text=fourth_option[displayedList[i]],
                           font=("arial", 17, "bold"),
                           bg=optionsColor,
                           fg="white",
                           bd=0,
                           activebackground=optionsColor,
                           activeforeground="white")
    option_button_D.place(x=572, y=180)


    def option_button_D_enter(e):

        questionLabel.config(image=questionLayD)
        option_button_D.config(bg=orangeColor, fg="BLACK", activeforeground="BLACK", activebackground=orangeColor)

    def option_button_D_leave(e):
        questionLabel.config(image=questionLay)
        option_button_D.config(bg=optionsColor, fg="WHITE", activeforeground="WHITE", activebackground=optionsColor)

    option_button_D.bind("<Enter>", option_button_D_enter)
    option_button_D.bind("<Leave>", option_button_D_leave)


    # <<<<<<< COMMANDS CHECK ANSWER >>>>>>>
    def show_first_opt():
        option_button_A.config(text=first_option[displayedList[i]])
    def show_second_opt():
        option_button_B.config(text=second_option[displayedList[i]])
    def show_third_opt():
        option_button_C.config(text=third_option[displayedList[i]])
    def show_forth_opt():
        option_button_D.config(text=fourth_option[displayedList[i]])

    list_of_function = [show_first_opt, show_second_opt, show_third_opt, show_forth_opt]

    def run_this():
        #time.sleep(1)
        for func in list_of_function:
            time.sleep(0.5)
            func()
            gameWindow.update_idletasks()


    def select_command(event):
        b = event.widget
        value = b["text"]
        global i

        if value in correct_answers:  # it starts with [0]
            pygame.mixer.music.load("files/correct-2-46134.mp3")
            pygame.mixer.music.play(0)
            i += 1

            questionsArea.config(state=NORMAL)  # make question editable for next question
            questionsArea.delete(1.0, END)  # delete current question
            questionsArea.insert(END, questionList_A[displayedList[i]])  # write new question
            # update amount label with amount photo
            amountLabel.config(image=amountPhotoList[i])
            print(i)
            option_button_A.config(text="")
            option_button_B.config(text="")
            option_button_C.config(text="")
            option_button_D.config(text="")
            time.sleep(1)
            gameWindow.update()
            # CHANGE ALL OPTIONS
            run_this()

            # Questions from 0 to 4. First 5 questions
            global amount_win
            if i == 1:
                amount_win = 100
                print(amount_win)

            elif i == 2:
                amount_win = 200
                print(amount_win)
            elif i == 3:
                amount_win = 300
                print(amount_win)
            elif i == 4:
                amount_win = 500
                print(amount_win)
            elif i == 5:
                amount_win = 1000
                print(amount_win)
            elif i == 6:
                amount_win = 2000
                print(amount_win)
            elif i == 7:
                amount_win = 4000
                print(amount_win)
            elif i == 8:
                amount_win = 8000
                print(amount_win)
            elif i == 9:
                amount_win = 16000
                print(amount_win)
            elif i == 10:
                amount_win = 32000
                print(amount_win)
            elif i == 11:
                amount_win = 64000
                print(amount_win)
            elif i == 12:
                amount_win = 125000
                print(amount_win)
            elif i == 13:
                amount_win = 250000
                print(amount_win)
            elif i == 14:
                amount_win = 500000
                print(amount_win)
            elif i == 15:
                amount_win = 1000000
                print(amount_win)
                win_window()

        if value not in correct_answers:

            print("Wrong answer!")
            option_button_A.bind("<Button-1>", NONE)
            option_button_B.bind("<Button-1>", NONE)
            option_button_C.bind("<Button-1>", NONE)
            option_button_D.bind("<Button-1>", NONE)
            pygame.mixer.music.load("files/negative_beeps-6008.mp3")
            pygame.mixer.music.play(0)
            game_over_function()

    # <<<<<<< COMMANDS FOR OPTION BUTTONS >>>>>>>
    option_button_A.bind("<Button-1>", select_command)
    option_button_B.bind("<Button-1>", select_command)
    option_button_C.bind("<Button-1>", select_command)
    option_button_D.bind("<Button-1>", select_command)

    # <<<<<<< Call a friend button >>>>>>>
    def callFriend():
        pygame.mixer.music.load("files/Zings1.mp3")
        pygame.mixer.music.play(0)
        bg_color = "#24094e"
        #bg_color = "#500868"
        #bg_color = "#670a8e"
        #bg_color = "#400057"
        call_friend_window = Toplevel()
        call_friend_window.overrideredirect(True)
        call_friend_window.config(bg=bg_color,
                                  borderwidth=2,
                                  relief=RAISED)
        window_width = 300
        window_height = 225
        screen_width = call_friend_window.winfo_screenwidth()  # width of the screen
        screen_height = call_friend_window.winfo_screenheight()  # height of the screen

        center_x = (screen_width / 2) - (window_width / 2)  # find the location of app on the x coordinate
        center_y = (screen_height / 2) - (window_height / 2)  # find the location of app on the y coordinate
        call_friend_window.geometry("{}x{}+{}+{}".format(window_width, window_height, int(center_x), int(center_y)))

        #pygame.mixer.music.load("files/calling.mp3")
        #pygame.mixer.music.play(0)

        option1 = option_button_A.cget('text')
        option2 = option_button_B.cget('text')
        option3 = option_button_C.cget('text')
        option4 = option_button_D.cget('text')

        if option1 in correct_answers:
            answer = option1
        if option2 in correct_answers:
            answer = option2
        if option3 in correct_answers:
            answer = option3
        if option4 in correct_answers:
            answer = option4

        possible_answers = ["Səhf eləmirəmsə, cavab:",
                            "Düşünürəm ki, cavab:",
                            "Mənə elə gəlir ki, cavab:",
                            "Əmin deyiləm. Yəqin ki, cavab:",
                            "Ola bilsin ki, cavab:",
                            "Əminəm, cavab:",
                            "Mənə inana bilərsən, cavab:",
                            "Maraqlı sualdır, məncə cavab:",
                            "Böyük ehtimal ki, cavab:",
                            "Qəti qərarımdır, cavab:"]
        ans = random.choice(possible_answers)
        answer_frame = Frame(call_friend_window, bg=bg_color)
        answer_frame.place(relx=0.5, rely=0.48, anchor=CENTER)

        #about_label = Label(call_friend_window, font=("arial", 14), text=ans, foreground="BLUE")
        #about_label.grid(row=0, column=0, pady=5, padx=5)

        phone_image = PhotoImage(file="files/phone.png")
        phone_image_label = Label(answer_frame,
                                  image=phone_image,
                                  borderwidth=0)
        phone_image_label.image = phone_image
        phone_image_label.grid(row=0, column=0)

        about_label = Label(answer_frame,
                            font=("arial", 14, "bold"),
                            text=ans,
                            bg=bg_color,
                            fg="WHITE",
                            pady=5,
                            padx=5)
        about_label.grid(row=1, column=0)
        #phoneButton.config(image=photoPhoneX, state=DISABLED)

        correct_answer_label = Label(answer_frame,
                                     font=("Desired_font", 15, "bold"),
                                     text=answer,
                                     bg=bg_color,
                                     fg="#f2bc30",
                                     padx=5,
                                     pady=5)
        correct_answer_label.grid(row=2, column=0)

        # EXIT BUTTON FOR CALL A FRIEND WINDOW
        tshk_hover_image = PhotoImage(file="files/button9.png")
        def exit_command():
            pygame.mixer.music.load("files/click_04.wav")
            pygame.mixer.music.play(0)
            call_friend_window.destroy()

        #exit_button = Button(call_friend_window, text="Təşəkkürlər", font=("arial", 15, "bold"), command=exit_command)
        #exit_button.grid(row=1, column=0)

        tshk_button_image = PhotoImage(file="files/button8.png")
        exit_button = Button(answer_frame,
                             image=tshk_button_image,
                             bg=bg_color,
                             bd=0,
                             borderwidth=0,
                             activebackground=bg_color,
                             command=exit_command)
        exit_button.image = tshk_button_image
        exit_button.grid(row=3, column=0)


        def start_button_hover(e):

            exit_button.config(image=tshk_hover_image)

        def start_button_leave(e):
            exit_button.config(image=tshk_button_image)

        exit_button.bind("<Enter>", start_button_hover)
        exit_button.bind("<Leave>", start_button_leave)

    phoneButton.config(command=callFriend)

    half50x = PhotoImage(file='files/50-50-X.png')


    # <<<<<<< 50 - 50 Button >>>>>>>
    def halfQuestion():
        pygame.mixer.music.load("files/Zings1.mp3")
        pygame.mixer.music.play(0)
        incorrect_answers = []
        option1 = option_button_A.cget('text')
        option2 = option_button_B.cget('text')
        option3 = option_button_C.cget('text')
        option4 = option_button_D.cget('text')

        if option1 not in correct_answers:
            incorrect_answers.append(option_button_A)
        if option2 not in correct_answers:
            incorrect_answers.append(option_button_B)
        if option3 not in correct_answers:
            incorrect_answers.append(option_button_C)
        if option4 not in correct_answers:
            incorrect_answers.append(option_button_D)

        incorrect_answers[0].config(text='')
        incorrect_answers[2].config(text='')
        halfButton.config(image=half50x, state=DISABLED)

    halfButton.config(command=halfQuestion)


    # <<<<<<< AUDIANCE COMMAND >>>>>>>

    def audience_command():
        pygame.mixer.music.load("files/Zings1.mp3")
        pygame.mixer.music.play(0)

        audience_window = Toplevel()
        audience_window.overrideredirect(True)
        window_width = 200
        window_height = 300
        screen_width = audience_window.winfo_screenwidth()  # width of the screen
        screen_height = audience_window.winfo_screenheight()  # height of the screen
        bg_color = "#24094e"
        center_x = (screen_width / 2) - (window_width / 2)  # find the location of app on the x coordinate
        center_y = (screen_height / 2) - (window_height / 2)  # find the location of app on the y coordinate
        audience_window.geometry("{}x{}+{}+{}".format(window_width, window_height, int(center_x), int(center_y)-30))
        audience_window.config(#bg="#003088",
                               #bg="#3f005a",
                               bg=bg_color,
                               borderwidth=2,
                               relief=RAISED)

        percentageA = list(range(1, 26, 1))
        percentageB = list(range(26, 51, 1))
        percentageC = list(range(51, 76, 1))
        percentageD = list(range(76, 100, 1))
        list_of_percentage = [random.choice(percentageA), random.choice(percentageB), random.choice(percentageC),
                              random.choice(percentageD)]
        print(list_of_percentage)

        progbarA = Progressbar(audience_window, orient=VERTICAL, length=120)
        progbarB = Progressbar(audience_window, orient=VERTICAL, length=120)
        progbarC = Progressbar(audience_window, orient=VERTICAL, length=120)
        progbarD = Progressbar(audience_window, orient=VERTICAL, length=120)

        progbarLabelA = Label(audience_window, text="A", font=("arial", 18, "bold"), bg=bg_color, fg="WHITE")
        progbarLabelB = Label(audience_window, text="B", font=("arial", 18, "bold"), bg=bg_color, fg="WHITE")
        progbarLabelC = Label(audience_window, text="C", font=("arial", 18, "bold"), bg=bg_color, fg="WHITE")
        progbarLabelD = Label(audience_window, text="D", font=("arial", 18, "bold"), bg=bg_color, fg="WHITE")

        percentageLabelA = Label(audience_window, font=("arial", 11, "bold"), bg=bg_color, fg="WHITE")
        percentageLabelB = Label(audience_window, font=("arial", 11, "bold"), bg=bg_color, fg="WHITE")
        percentageLabelC = Label(audience_window, font=("arial", 11, "bold"), bg=bg_color, fg="WHITE")
        percentageLabelD = Label(audience_window, font=("arial", 11, "bold"), bg=bg_color, fg="WHITE")

        option1 = option_button_A.cget('text')
        option2 = option_button_B.cget('text')
        option3 = option_button_C.cget('text')
        option4 = option_button_D.cget('text')

        if option1 in correct_answers:
            progbarA.config(value=list_of_percentage[3])
            progbarB.config(value=list_of_percentage[1])
            progbarC.config(value=list_of_percentage[2])
            progbarD.config(value=list_of_percentage[0])

            percentageLabelA.config(text="{}%".format(list_of_percentage[3]))
            percentageLabelB.config(text="{}%".format(list_of_percentage[1]))
            percentageLabelC.config(text="{}%".format(list_of_percentage[2]))
            percentageLabelD.config(text="{}%".format(list_of_percentage[0]))

        if option2 in correct_answers:
            progbarA.config(value=list_of_percentage[0])
            progbarB.config(value=list_of_percentage[3])
            progbarC.config(value=list_of_percentage[1])
            progbarD.config(value=list_of_percentage[2])

            percentageLabelA.config(text="{}%".format(list_of_percentage[0]))
            percentageLabelB.config(text="{}%".format(list_of_percentage[3]))
            percentageLabelC.config(text="{}%".format(list_of_percentage[1]))
            percentageLabelD.config(text="{}%".format(list_of_percentage[2]))

        if option3 in correct_answers:
            progbarA.config(value=list_of_percentage[1])
            progbarB.config(value=list_of_percentage[0])
            progbarC.config(value=list_of_percentage[3])
            progbarD.config(value=list_of_percentage[2])

            percentageLabelA.config(text="{}%".format(list_of_percentage[1]))
            percentageLabelB.config(text="{}%".format(list_of_percentage[0]))
            percentageLabelC.config(text="{}%".format(list_of_percentage[3]))
            percentageLabelD.config(text="{}%".format(list_of_percentage[2]))

        if option4 in correct_answers:
            progbarA.config(value=list_of_percentage[2])
            progbarB.config(value=list_of_percentage[1])
            progbarC.config(value=list_of_percentage[0])
            progbarD.config(value=list_of_percentage[3])

            percentageLabelA.config(text="{}%".format(list_of_percentage[2]))
            percentageLabelB.config(text="{}%".format(list_of_percentage[1]))
            percentageLabelC.config(text="{}%".format(list_of_percentage[0]))
            percentageLabelD.config(text="{}%".format(list_of_percentage[3]))

        percentageLabelA.place(x=20, y=20)
        percentageLabelB.place(x=60, y=20)
        percentageLabelC.place(x=100, y=20)
        percentageLabelD.place(x=140, y=20)

        progbarA.place(x=25, y=60)
        progbarB.place(x=65, y=60)
        progbarC.place(x=105, y=60)
        progbarD.place(x=145, y=60)

        progbarLabelA.place(x=25, y=190)
        progbarLabelB.place(x=65, y=190)
        progbarLabelC.place(x=105, y=190)
        progbarLabelD.place(x=145, y=190)

        # BUTTON
        aexbi = PhotoImage(file="files/sagol1.png")
        exit_hover_image = PhotoImage(file="files/sagol2.png")

        def exit_command():
            pygame.mixer.music.load("files/click_04.wav")
            pygame.mixer.music.play(0)
            audience_window.destroy()

        exit_button = Button(audience_window,
                             command=exit_command,
                             image=aexbi,
                             borderwidth=0,
                             bg="#24094e",
                             activebackground="#24094e")
        exit_button.image = aexbi
        exit_button.place(x=22, y=240)

        def start_button_hover(e):
            exit_button.config(image=exit_hover_image)

        def start_button_leave(e):
            exit_button.config(image=aexbi)

        exit_button.bind("<Enter>", start_button_hover)
        exit_button.bind("<Leave>", start_button_leave)
        audienceButton.config(state=DISABLED, image=photoAudienceX)



    audienceButton.config(command=audience_command)


    gameWindow.mainloop()


def closeit():
    print("close it")
    gameWindow.destroy()
