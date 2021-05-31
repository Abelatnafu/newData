import csv
filenames="./1.csv", "./2.csv", "./3.csv", "./4.csv"
starter = 0
for files in filenames:
    with open("fixed.csv",  'a', newline='') as updata:
        up_dater = csv.writer(updata, delimiter= ",")
        with open(files) as data:
            content = csv.reader(data)
            for cards in content:

                if cards[0].find("<i>") != -1:
                    cards[0] = cards[0].replace('<i>', '')
                    cards[0] = cards[0].replace('</i>', ' ')
                    # print(cards[0])
                if cards[0].find("<br>") != -1:
                    cards[0] = cards[0].replace('<br>', ' ')
                    # print(cards[0])
                if cards[1].find("&reg") != -1 or cards[0].find("&reg") != -1:
                    cards[0] = cards[0].replace('&reg', '')
                    cards[1] = cards[1].replace('&reg', '')
                if cards[0].find("____.") != -1:
                    cards[0] = cards[0].replace("____.", cards[1])
                    cards[0] = cards[0].replace("____.", cards[1])
                elif cards[0].find("____") != -1:
                    cards[0] = cards[0].replace("____", cards[1])
                    # print(cards[0])
                else:
                    cards[0] = cards[0] + " " + cards[1]
                if cards[3] != "win":
                    laplace_score = (int(cards[3]) + 1)/(int(cards[2])+4)      #(win+1)/(played + 4)
                else:
                    laplace_score = "laplace Score  "
                if cards[0] != "" and cards[1] != "":
                    # print(cards[0])
                    up_dater.writerow([cards[0],cards[2], cards[3],str(laplace_score)])


