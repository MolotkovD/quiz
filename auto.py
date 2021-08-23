import json, pprint

app_run = True
with open('data.json', 'r', encoding='utf8') as file:
    bd = json.load(file)
    len_bd = len(bd['game_data'])
    pprint.pprint(bd)
    file.close()
#text, var1/var2/var3 , true/true_int
while app_run == True:
    text = input('text or stop (str)--> ')
    if text != "stop":
        
        var1 = '1. ' + input('var1 (str)--> ')
        var2 = '2. ' + input('var2 (str)--> ')
        var3 = '3. ' + input('var3 (str)--> ')
        true = input('true (str)--> ')
        true_int = int(input('true_int (int)--> '))
        str_len_bd = str(len_bd+1)
        bd["game_data"][str_len_bd] = {"text": text,
                                    "var1": var1,
                                    "var2": var2,
                                    "var3": var3,
                                    "true": true,
                                    "true_int": true_int}
    else:
        with open('data.json', 'w', encoding='utf8')as f:
            json.dump(bd, f, indent=4, ensure_ascii=False)
            f.close()
        pprint.pprint(bd)
        app_run = False

