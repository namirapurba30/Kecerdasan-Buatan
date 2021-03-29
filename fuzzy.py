#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_excel (r'C:\Users\Asus\Mahasiswa.xlsx') #read data
income = df['Penghasilan'].tolist() #make the income data into list
outcome = df['Pengeluaran'].tolist() #make the outcome data into list


# In[3]:


def bottomIncome(x):#membership function for income with bottom categorize
    bottom = 0 #initial value of the variable
    if (x <= 6): #determind the value of x 
        bottom = 1 # if condition fulfilled,define the variable as 1
    elif (x > 6 and x <= 10):#determind the value of x
        bottom = (10-x)/4 #if condition fulfilled,calculate the value
    else:
        bottom = 0 #there is no condition fulfilled define variable as 0
    return bottom #return the variable

def middleIncome(x):#membership function for income with middle categorize
    middle = 0 #initial value of the variable
    if (x<= 8 or x >=15): # check the if condition whether it fulfilled or not
        middle = 0 # if condition fulfilled,define the variable as 0
    elif (x > 8 and x<=13):# check the if condition whether it fulfilled or not
        middle = (x-8)/(5) #if condition fulfilled,calculate the value
    elif (x>13 and x<15):#check the if condition whether it fulfilled or not
        middle = (15-x)/(2)#if condition fulfilled,calculate the value
    return middle #return the value

def upperIncome(x):#membership function for income with upper categorize
    upper = 0  #initial value of the variable
    if (x < 13):#check the if condition whether it fulfilled or not
        upper = 0 # if condition fulfilled,define the variable as 0
    elif (x>=17):#check the if condition whether it fulfilled or not
        upper = 1 # if condition fulfilled,define the variable as 1
    elif (x>=13 and x <= 19):#check the if condition whether it fulfilled or not
        upper = (19-x)/(6)#if condition fulfilled,calculate the value
    return upper  #return the value

 


# In[4]:


def bottomOutcome(x):#membership function for income with bottom categorize
    bottom = 0 
    if (x <= 2):#check the if condition whether it fulfilled or not
        bottom = 1 # if condition fulfilled,define the variable as 1
    elif (x > 2 and x <= 5):#check the if condition whether it fulfilled or not
        bottom = (5-x)/3 #if condition fulfilled,calculate the value
    else:
        bottom = 0 #define the variable as 0
    return bottom #return the value

def middleOutcome(x):#membership function for income with middle categorize
    middle = 0
    if (x > 6 and x < 8):#check the if condition whether it fulfilled or not
        middle = 1 #if condition fulfilled,define the variable as 1
    elif (x<=5 or x >= 10):#check the if condition whether it fulfilled or not
        middle = 0 # if condition fulfilled,define the variable as 0
    elif (x > 5 and x < 6):#check the if condition whether it fulfilled or not
        middle = (x-5)/(1)  # if condition fulfilled,calculate the variable
    elif (x > 8 and x < 10):#check the if condition whether it fulfilled or not
        middle = (10-x)/(2)# if condition fulfilled,calculate the variable
    return middle #return the value

def upperOutcome(x):#membership function for income with upper categorize
    upper = 0
    if (x>=10):#check the if condition whether it fulfilled or not
        upper = 1#if condition fulfilled,define the variable as 1
    elif (x < 7):#check the if condition whether it fulfilled or not
        upper = 0#if condition fulfilled,define the variable as 0
    elif (x>=7 and x < 10):#check the if condition whether it fulfilled or not
        upper = (7-x)/(3) #if condition fulfilled,calculate the value
    return upper #return the value


# In[5]:


def fuzzIncome(income):#function to input the result into array
    inarray = []
    for i in range(100): #looping in the range of 100 datas
        x = income[i] 
        upper = upperIncome(x)
        middle = middleIncome(x)
        bottom = bottomIncome(x)
        inarray.append([upper,middle,bottom]) #input it into array
    return inarray #return the value


# In[6]:


def fuzzOutcome(outcome):#function to input the result into array
    outarray = []
    for i in range(100):#looping in the range of 100 datas
        x = outcome[i]
        upper = upperOutcome(x)
        middle = middleOutcome(x)
        bottom = bottomOutcome(x)
        outarray.append([upper,middle,bottom])#input it into array
    return outarray #return the value


# In[7]:


def inference(infin,infout): #inference function
    res1 = []
    for i in range(100):#looping in 100 ranges
        rej = max(min(infin[i][0],infout[i][0]),min(infin[i][0],infout[i][1]),min(infin[i][1],infout[i][0])) #find the inference value
        cons = max(min(infin[i][0],infout[i][2]),min(infin[i][1],infout[i][1]),min(infin[i][2],infout[i][0]))#find the inference valu
        acc = max(min(infin[i][1],infout[i][2]),min(infin[i][2],infout[i][1]),min(infin[i][2],infout[i][2]))#find the inference valu
        res1.append([rej,cons,acc]) #input it into array
    return res1 #return the value


# In[8]:


def sugeno(sug): #sugeno defuzzification method
    final = []
    for i in range(100): #looping in 100 range
            res = ((100*sug[i][0])+(70*sug[i][1])+(50*sug[i][2])/(sug[i][0]+sug[i][1]+sug[i][2])) #calculate the value using sugeno formula
            final.append([i+1,res])#input it into array
    return final #return the value


# In[9]:


def sort(param):  #sort function
    sortres = sorted(param,reverse = True,key = lambda x: x[1]) #sort the value
    return sortres # return the value

def output(sortres):
    finalout = []
    for i in range(20): #looping in 20 ranges
        finalout.append(sortres[i]) #print the value
    return finalout
    


# In[10]:


inc = fuzzIncome(income) 
outc = fuzzOutcome(outcome)
infresult = inference(inc,outc)
sugresult = sugeno(infresult)
sorting = sort(sugresult)
finalresult = output(sorting)


df = pd.DataFrame({'id':finalresult})
writer = pd.ExcelWriter('Bantuan.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[11]:


print("ID", "||" ,"Values")
print("=================")
print(*sugresult, sep="\n")


# In[12]:


sugeno=[[50,50],[70,70],[100,100]]
plt.plot(sugeno[0],[1,0],color="red")
plt.plot(sugeno[1],[1,0],color="yellow")
plt.plot(sugeno[2],[1,0],color="blue")
plt.suptitle("Sugeno")
plt.show()


# In[13]:


print("Chosen id:")
print("========")
print(*finalresult,sep = "\n") 

