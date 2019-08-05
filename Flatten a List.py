def flat_list(listy):
    if len(listy) > 0 :
        listy2 = str(listy).replace('[','').replace(']','').replace(' ','')

        if len(listy2) > 0:
            listush = listy2.split(',')
        else:
            listush = listy2.split()


        for i in listush:
            if len(i) is 0 :
                listush.remove(i)

        nums_to_list = False
        for i in str(listush):
            if i.isdigit():
                nums_to_list = True

        new_lisisi = []
        if len(listush) > 0 and nums_to_list:
            for i in listush:
                new_lisisi.append(int(i))
            return new_lisisi
        else:
            return listush
    else:
        return listy
    


flat_list([-1,[1,[-2,[3],[[5],[10,-11],[1,100,[-1000,[5000]]],[20,-10,[[[]]]]]]]])




