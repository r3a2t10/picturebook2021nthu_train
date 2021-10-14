import csv

list_head = ['Id','Genre',]
list_1 = ['happiness','love','trust','optimism','sadness','fear','disgust','anger','lost','surprise','touched','peace']
list_2 = ['family','friendship','adventure','enjoy-life','beautiful-scenery','home','holiday','imaginary','nostalgia','loneliness','growth','sick']
list_3 = ['classic','cute','romantic','realistic','expressionnisme','abstract','decoration','grotesque','humor']

# ./all_1.txt ./all_2.txt ./all_3.txt
fp = open('./all_3.txt', "r")
lines = fp.readlines()
fp.close()

# output_1.csv output_2.csv output_3.csv
with open('output_3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(list_head + list_3)
    for i in range(len(lines)):

        list_genre = []
        for j in range(len(list_3)):
            if lines[i][j] == '1':
                list_genre.append(list_3[j])
        
        list_item = []
        list_item.append(i) #Id
        list_item.append(list_genre) #Genre
        
        #List
        for j in range(len(list_3)):
            list_item.append(int(lines[i][j]))

        writer.writerow(list_item)
