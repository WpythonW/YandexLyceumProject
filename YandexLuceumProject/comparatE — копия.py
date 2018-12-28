import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtWidgets import QLCDNumber, QInputDialog, QLCDNumber
from PyQt5.QtGui import QIcon
from fuzzywuzzy import fuzz
import time


def forma(pretexts, signs, extra, text1, text2): 
    corrected1 = text1[:]
    corrected2 = text2[:]

    corrected1 = corrected1.lower()
    corrected2 = corrected2.lower()

    for i in signs:
        corrected1 = corrected1.replace(i, ' ')
    corrected1 = corrected1.split() 
    
    for i in pretexts:
        value = corrected1.count(i)
        for j in range(value):
            corrected1.remove(i)       
            
    for i in extra:
        value = corrected1.count(i)
        for j in range(value):
            corrected1.remove(i)    
    
    for i in signs:
        corrected2 = corrected2.replace(i, ' ')
    corrected2 = corrected2.split() 
    
    for i in pretexts:
        value = corrected2.count(i)
        for j in range(value - 1):
            corrected2.remove(i)
            
    for i in extra:
        value = corrected2.count(i)
        for j in range(value - 1):
            corrected2.remove(i) 
            
    return corrected1, corrected2


def style_read():
    sci = open('научный.txt')
    pub = open('публицистический.txt')
    deal = open('официально-деловой.txt')
    ex = open('лишние_сочетания.txt')

    scientic = ''
    public = ''
    office = ''
    extra = ''

    for i in pub:
        public = public + i

    for i in sci:
        scientic = scientic + i

    for i in deal:
        office = office + i
  
    for i in ex:
        extra = extra + i

    public = public.split('\n')
    scientic = scientic.split('\n')
    office = office.split('\n')
    extra = extra.split('\n')
    
    return public, scientic, office, extra


def read_PreSigns():
    pre = open('pretexts.txt')
    sig = open('signs.txt')

    pr = ''
    si = ''

    for i in pre:
        pr = pr + i
    for i in sig:
        si = si + i

    pretexts = pr.split(',')
    signs = si.split('s')

    return pretexts, signs


def style_initial(corrected1, corrected2, public, scientic, office, extra):            #Зависит от inp() -> forma(pretexts, signs)
    p1 = 0
    s1 = 0
    o1 = 0

    p2 = 0
    s2 = 0
    o2 = 0

    for i in corrected1:
        if i in public:
            p1 = p1 + 1

    for i in corrected1:
        if i in scientic:
            s1 = s1 + 1

    for i in corrected1:
        if i in office:
            o1 = o1 + 1

    for i in corrected2:
        if i in public:
            p2 = p2 + 1

    for i in corrected2:
        if i in scientic:
            s2 = s2 + 1

    for i in corrected2:
        if i in office:
            o2 = o2 + 1
            
    list1 = [p1, s1, o1]
    list2 = [p2, s2, o2]
    
    maxim1 = max(list1)
    maxim2 = max(list2)   

    flagP1 = False
    flagS1 = False
    flagO1 = False
    
    flagP2 = False
    flagS2 = False
    flagO2 = False    

    if maxim1 == p1:
        flagP1 = True
    elif maxim1 == s1:
        flagS1 = True
    elif maxim1 == o1:
        flagO1 = True
        
    if maxim2 == p2:
        flagP2 = True
    elif maxim2 == s2:
        flagS2 = True
    elif maxim2 == o2:
        flagO2 = True    
    
    return flagP1, flagS1, flagO1, flagP2, flagS2, flagO2
    

def style_form(realP1, realS1, realO1, realP2, realS2, realO2, corrected1, corrected2):      
    corrected1 = '\n'.join(corrected1)
    corrected2 = '\n'.join(corrected2)
    #Если флаг p1 то запись в публицистический...
    if realS1:
        with open('научный.txt', 'a') as file:
            file.write(corrected1 + '\n')  
        
    elif realP1:
        with open('публицистический.txt', 'a') as file:
            file.write(corrected1 + '\n')  
            
    elif realO1:
        with open('официально-деловой.txt', 'a') as file:
            file.write(corrected1 + '\n')  
    
    if realS2:
        with open('научный.txt', 'a') as file:
            file.write(corrected2 + '\n')  
        
    elif realP2:
        with open('публицистический.txt', 'a') as file:
            file.write(corrected2 + '\n')  
        
    elif realO2:
        with open('официально-деловой.txt', 'a') as file:
            file.write(corrected2 + '\n')  
    
    
def style_correct(public, scientic, office, extra):    
    mix = public + scientic + office
    
    for i in mix:
        if mix.count(i)>1:
            try:
                u = public.count(i)
                for i in range(u - 1):
                    public.remove(i)
            except Exception:
                u = 0
            try:
                u = scientic.count(i)
                for i in range(u - 1):
                    scientic.remove(i)
            except Exception:
                u = 0
            try:
                u = office.count(i)
                for i in range(u - 1):
                    office.remove(i)
            except Exception:
                u = 0
                
            extra.append(i)
    
    public_test = public[:]
    scientic_test = scientic[:]
    office_test = office[:]
    extra_test = extra[:]
    
    public = []
    scientic = []
    office = []
    extra = []
    
    for i in public_test:
        if i not in public:
            public.append(i)
    
    for i in scientic_test:
        if i not in scientic:
            scientic.append(i)
            
    for i in office_test:
        if i not in office:
            office.append(i)
            
    for i in extra_test:
        if i not in extra:
            extra.append(i)

    public_test = public[:]
    scientic_test = scientic[:]
    office_test = office[:]
    extra_test = extra[:]
    
    public = []
    scientic = []
    office = []
    extra = []

    for i in public_test:
        try:
            i = int(i)
        except Exception:
            public.append(i)
            
    for i in scientic_test:
        try:
            i = int(i)
        except Exception:
            scientic.append(i)
            
    for i in office_test:
        try:
            i = int(i)
        except Exception:
            office.append(i)
            
    for i in extra_test:
        try:
            i = int(i)
        except Exception:
            extra.append(i)
    
    public = '\n'.join(public)
    scientic = '\n'.join(scientic)
    office = '\n'.join(office)
    extra = '\n'.join(extra)
    
    with open('официально-деловой.txt', 'w') as file:
        file.write(office)  
        file.close()
    with open('публицистический.txt', 'w') as file:
        file.write(public)  
        file.close()
    with open('научный.txt', 'w') as file:
        file.write(scientic)  
        file.close()
    with open('лишние_сочетания.txt', 'w') as file:
        file.write(extra)  
        file.close()
    

def ComparadE(corrected1, corrected2, realP1, realS1, realO1, realP2, realS2, realO2):
    corrected1 = ' '.join(corrected1)
    corrected2 = ' '.join(corrected2)
    quality = fuzz.ratio(corrected1, corrected2)
    if corrected1 == corrected2:
        quality = 100
        return quality
    elif (realS1 and realS2) or (realP1 and realP2) or (realO1 and realO2):
        if quality <= 75:
            quality+=23 
            return quality
        else:
            return quality
        



class Graphics(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("ComparadE")
        self.setGeometry(0, 30, 700, 250)
        
        self.qual_out = QLCDNumber(self)
        self.qual_out.move(350, 10)
        self.qual_out.resize(300, 100)
        
        self.style1_print = QLabel(self)
        self.style1_print.resize(300, 30)
        
        self.style2_print = QLabel(self)
        self.style2_print.resize(300, 30)
        
        self.setWindowIcon(QIcon('maxresdefault.jpg'))
        
        self.show()   
        
    def output(self):  
        self.realS1 = False
        self.realP1 = False
        self.realO1 = False
        
        self.realS2 = False
        self.realP2 = False
        self.realO2 = False
        
        if self.flagP1:
            s = QInputDialog.getText(self, 'Quation','Первый текст публицистический. ЭТО ВЕРНО?(y/n):') 
            m = s[0]
            if m == 'n':
                s = QInputDialog.getText(self, 'Quation','Тогда какой?(научный/официальный):')
                prime = s[0]
                if prime == 'научный':                
                    self.realS1 = True
                elif prime == 'официальный':
                    self.realO1 = True
            else:
                self.realP1 = self.flagP1
                
        elif self.flagS1:
            s = QInputDialog.getText(self, 'Quation','Первый текст научный. ЭТО ВЕРНО?(y/n):') 
            m = s[0]
            if m == 'n':
                s = QInputDialog.getText(self, 'Quation','Тогда какой?(публицистический/официальный):')
                prime = s[0]
                if prime == 'публицистический':                
                    self.realP1 = True
                elif prime == 'официальный':
                    self.realO1 = True
            else:
                self.realS1 = self.flagS1
                
        elif self.flagO1:
            s = QInputDialog.getText(self, 'Quation','Первый текст официальный. ЭТО ВЕРНО?(y/n):') 
            m = s[0]
            if m == 'n':
                s = QInputDialog.getText(self, 'Quation','Тогда какой?(публицистический/научный):')
                prime = s[0]
                if prime == 'публицистический':                
                    self.realP1 = True
                elif prime == 'научный':
                    self.realS1 = True
            else:
                self.realO1 = self.flagO1
        
        if self.flagP2:
            s = QInputDialog.getText(self, 'Quation','Второй текст публицистический. ЭТО ВЕРНО?(y/n):') 
            m = s[0]
            if m == 'n':
                s = QInputDialog.getText(self, 'Quation','Тогда какой?(научный/официальный):')
                prime = s[0]
                if prime == 'научный':                
                    self.realS2 = True
                elif prime == 'официальный':
                    self.realO2= True
            else:
                self.realP2 = self.flagP2
                
        elif self.flagS2:
            s = QInputDialog.getText(self, 'Quation','Второй текст научный. ЭТО ВЕРНО?(y/n):') 
            m = s[0]
            if m == 'n':
                s = QInputDialog.getText(self, 'Quation','Тогда какой?(публицистический/официальный):')
                prime = s[0]
                if prime == 'публицистический':                
                    self.realP2 = True
                elif prime == 'официальный':
                    self.realO2 = True
            else:
                self.realS2 = self.flagS2
                
        elif self.flagO2:
            s = QInputDialog.getText(self, 'Quation','Второй текст официальный. ЭТО ВЕРНО?(y/n):') 
            m = s[0]
            if m == 'n':
                s = QInputDialog.getText(self, 'Quation','Тогда какой?(публицистический/научный):')
                prime = s[0]
                if prime == 'публицистический':                
                    self.realP2 = True
                elif prime == 'научный':
                    self.realS2 = True
            else:
                self.realO2 = self.flagO2
                
    def Learn(self):
        if self.realS1:
            self.style1_print.setText("Первый текст научный")
            self.style1_print.move(10, 10)
            
        elif self.realP1:
            self.style1_print.setText("Первый текст публицистический")
            self.style1_print.move(10, 10)
            
        elif self.realO1:
            self.style1_print.setText("Первый текст официальный")
            self.style1_print.move(10, 10)
            
            
        if self.realS2:
            self.style2_print.setText("Второй текст научный")
            self.style2_print.move(10, 60)
            
        elif self.realP1:
            self.style2_print.setText("Второй текст публицистический")
            self.style2_print.move(10, 60)
            
        elif self.realO2:
            self.style2_print.setText("Второй текст официальный")
            self.style2_print.move(10, 60)
        
        if self.quality == 98:
            self.qual_out.display(self.quality + 2)  
        else:
            self.qual_out.display(self.quality)
        
        
    def main(self):  
        answer = QInputDialog.getText(self, 'Just question','Вы хотите просто откорректировать словарь?(да/нет):') 
        a = answer[0]

        if a == "да":
            public, scientic, office, extra = style_read()
            style_correct(public, scientic, office, extra)   
            
        elif a == "нет":
            pretexts, signs = read_PreSigns()
            public, scientic, office, extra = style_read()
            
            t1 = QInputDialog.getText(self, 'Input text1','Введите первый текст:                                                                                                                                                         ') 
            t2 = QInputDialog.getText(self, 'Input text2','Введите второй текст:                                                                                                                                                         ') 
            
            text1 = t1[0]
            text2 = t2[0]
            
            self.corrected1, self.corrected2 = forma(pretexts, signs, extra, text1, text2)
            
            self.flagP1, self.flagS1, self.flagO1, self.flagP2, self.flagS2, self.flagO2 = style_initial(self.corrected1, self.corrected2, public, scientic, office, extra)
            
            self.output()
            
            style_form(self.realP1, self.realS1, self.realO1, self.realP2, self.realS2, self.realO2, self.corrected1, self.corrected2)
            
            public, scientic, office, extra = style_read()
            
            style_correct(public, scientic, office, extra)
            self.quality = ComparadE(self.corrected1, self.corrected2, self.realP1, self.realS1, self.realO1, self.realP2, self.realS2, self.realO2)
            
            self.Learn()  


app = QApplication(sys.argv)
gr = Graphics()
gr.main()
sys.exit(app.exec_())