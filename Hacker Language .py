class HackerLanguage:

    def write(self,text):
        new_text_list = []
        new_text_list_fix = []
        for i in text :
            if i != ' ':
                if i.isalpha():
                    new_text_list.append(bin(ord(i)))
                else:
                    new_text_list.append(i)
            elif i == ' ':
                new_text_list.append('1000000')

        for i in new_text_list:
            if '0b' in i :
               new_text_list_fix.append(i.replace('0b', ''))
            else:
                new_text_list_fix.append(i)
        print ''.join(new_text_list_fix)





    def delete(self,n):
        print 

    def send(self):
        pass

    def read(self,texty):
        pass

aa = HackerLanguage()
aa.write('i love you 12%$')




