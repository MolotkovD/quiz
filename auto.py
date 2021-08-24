import json, pprint, time

app_run = True
try:
    with open('data.json', 'r', encoding='utf8') as file:
        bd = json.load(file)
        
        pprint.pprint(bd)
        time.sleep(3)
        file.close()
    with open('version.txt', 'r', encoding='utf8') as ver:
        version = ver.read()
        ver.close()
    #text, var1/var2/var3 , true/true_int
    while app_run == True:
        len_bd = len(bd['game_data'])
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
            pprint.pprint(bd["game_data"][str_len_bd])
        else:
            print(f"version now: {version} ",end='')
            new_version = input("new_version or pass_: ")
            if new_version != "pass_":
                with open('version.txt', 'w', encoding='utf8') as ver_up:
                    ver_up.write(new_version)
                    ver_up.close()
                bd["version"] = new_version  

            with open('data.json', 'w', encoding='utf8')as f:
                json.dump(bd, f, indent=4, ensure_ascii=False)
                f.close()
            pprint.pprint(bd)
            time.sleep(3)
            app_run = False
except FileNotFoundError:
    print('{Error} File not found')
    print("файл data.json не найдено")
    time.sleep(5)