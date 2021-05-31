import csv
files = "play_2.csv"
with open("fixed.csv", mode="w") as updata:
    up_dater = csv.writer(updata, delimiter=",")
    with open(files) as data:
        content = csv.reader(data)
        for cards in content:
            if cards[1][-1] == ".":
                cards[1] = cards[1][::-1].replace(".", "", 1)
                cards[1] = cards[1][::-1]
                cards[2] = cards[2][::-1].replace(".", "", 1)
                cards[2] = cards[2][::-1]
            if cards[0].find("____") == -1 and cards[0].find("____") == -1:
                # print(cards[0])
                cards[0] = cards[0]  +" " + cards[1] + ", " + cards[2] + "."
                print(cards[0])

            if cards[2].find(".") != -1:
                cards[2]= cards[2].replace(".", "")
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
            if cards[0].find("____") != -1:
                cards[0] = cards[0].replace("____", cards[1],1)
                cards[0] = cards[0].replace("____", cards[2])


            if cards[4] != "win":
                laplace_score = (int(cards[4]) + 1) / (int(cards[3]) + 4)
            else:
                laplace_score = "laplace Score  "
                cards[0] = "Combined"
                cards[3] = "Played"
                cards[4] = "Win"

            up_dater.writerow([cards[0], cards[3], cards[4], str(laplace_score)])