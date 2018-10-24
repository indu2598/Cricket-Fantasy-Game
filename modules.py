import database
def menufunction(self, action):
    txt= (action.text())
    
    if txt =='New Team':
        self.t2.setText(str(no*no))
    if txt =='Open Team':
        self.t2.setText(str(no*no*no))
    if txt =='Save Team':
        self.t2.setText(str(math.sqrt(no)))
    if txt=='Evaluate Team':
        self.t2.setText(str(math.pow(no,1/3)))
def removelist1(self, item): 
    self.list1.takeItem(self.list1.row(item))
    self.list2.addItem(item.text())

def removelist2(self, item):
    self.list2.takeItem(self.list2.row(item))
    self.list1.addItem(item.text())
    
def checkstate(self):
   
    if self.b1.isChecked()==True:
        data = database.selectBTM()
    else:
    state1='OFF'
    if self.rb2.isChecked()==True:
    state2='ON'
    else:
    state2='OFF'
    self.t1.setText("Button1 is {} Button2 is {}".format(state1,state2)) 
