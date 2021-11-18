
import json

#start with a list of employees
#the list contains: employee info(number), empl. name
#   empl, hourly wage(decimal), some rows have extra
#   information that no one can remember the purpose
#   The true values and random decimal numbers

Employee_info = [1121, "Jackie Grainger",22.22,
                 1122,"Jignesh Thrakkar", 25.25,
                 1127, "Dion Green", 28.75, True,
                 24.32, 1132, "Jacob Gerber",
                 "Sarah Sanderson", 23.45, 1137, True,
                 "Brandon Heck", 1138, 25.84, True,
                 1152, "David Toma", 22.65,
                 23.75, 1157, "Charles King", False,
                 "Jackie Grainger", 1121,22.22,False,
                 22.65, 1152, "David Toma"]

#list filter
EmployeeFilt = []
for i in range(len(Employee_info)):
    if Employee_info[i] not in EmployeeFilt and not type(Employee_info[i]) == bool:
        EmployeeFilt.append(Employee_info[i])
#sort the information into a list of dictionary items
#Each dictionary must be in a database-like format

#no duplicate data should make its way into the list
#of dictionary items.

# If list[i] == string, append to name
#if list[i] == int, append to employeeID
#if list[i] == float, append to hourly_rate
Employee_Dict = {"Empl_Num":[],"Empl_Name":[],"Hourly_Wage":[]}
list2 = []
i = 0
FiltLength = int(len(EmployeeFilt))
for k in range (1,int(FiltLength/3)+1):
    #for i in range(k*3,len(EmployeeFilt)):
    while i <=k*3:
        if type(EmployeeFilt[i]) == str:# and value not in Employee_Dict["Empl_Name"]:
            Employee_Dict["Empl_Name"]=EmployeeFilt[i]
            i+=1
            if i ==k*3:
                break
        elif type(EmployeeFilt[i]) ==int:# and value not in Employee_Dict["Empl_Num"]:
            Employee_Dict["Empl_Num"]= EmployeeFilt[i]
            i+=1
            if i ==k*3:
                break
        elif type(EmployeeFilt[i]) ==float:# and value not in Employee_Dict["Hourly_Wage"]:
            Employee_Dict["Hourly_Wage"]= EmployeeFilt[i]
            i+=1
            if i ==k*3:
                break
    Employee_Dict['total_hourly_wage']= round(Employee_Dict["Hourly_Wage"]*1.3,2)
    Employee_Dict_copy = Employee_Dict.copy()
    list2.append(Employee_Dict_copy)
#           print("list of dictionaries: \n",list2)
#for each value in the list, mult hourly wage by 1.3
#add a key to each dictionary item called total_hourly_rate Number 4
#store value just calculated there
i = 0
#           print("\nOne Dictionary: ",Employee_Dict)
#for k in range (1,int(FiltLength/3)):
    #for i in range(k*3,len(EmployeeFilt)):
   # while i <=k*3:
        #print(i)
        #list2[i].append(Employee_Dict['total_hourly_wage'])
        #i+=1
#print(list2)

#iterate through Employee_Dict["Hourly_Wage"]

##for value in Employee_Dict["Hourly_Wage"]:
##    Employee_Dict['total_hourly_wage'].append(round(value*1.3,2))

#Determin if anyone's hourly rate is between 28.15
#and 30.65, if so, add stored dict info
#and call it underpaid_salaries
##Employee_Dict['underpaid_salaries'] = []
##ite=0
##for value in Employee_Dict.items():
##    if value >= 28.15 and value <= 30.65:
##        Employee_Dict['underpaid_salaries'].append(Employee_Dict[value])

underpaid_salaries = []
i = 0
for i in range(len(list2)):
    if list2[i].get("total_hourly_wage") >= 28.15 and list2[i].get("total_hourly_wage") <= 30.65:
        underpaid_salaries.append(list2[i])

company_raises = []
dict_update = {}
i = 0
for i in range(len(list2)):
    raise_holder = list2[i].get("Hourly_Wage")
    dict_update = ()
        
    #company_raises.append(dict_update)
    
    if list2[i].get("Hourly_Wage") >= 22.00 and list2[i].get("Hourly_Wage") <= 23.99:

        company_raises.append({'Empl_Name':list2[i].get("Empl_Name"),'company_raises':raise_holder*1.05})
    elif list2[i].get("Hourly_Wage") >= 24.00 and list2[i].get("Hourly_Wage") <= 25.99:
        
        company_raises.append({'Empl_Name':list2[i].get("Empl_Name"),'company_raises':raise_holder*1.04})
    elif list2[i].get("Hourly_Wage") >= 26.00 and list2[i].get("Hourly_Wage") <= 28.00:
        
        company_raises.append({'Empl_Name':list2[i].get("Empl_Name"),'company_raises':raise_holder*1.03})
    else:
        company_raises.append({'Empl_Name':list2[i].get("Empl_Name"),'company_raises':raise_holder*1.02})

#Calculate a raise if the hourly rate is between 22-24
#apply a 5% raise to the current rate.

##for value in Employee_Dict["Hourly_Wage"]:
##    if value >= 22.0 and value <= 24.0:
##        Employee_Dict['total_hourly_wage'].append(round(value*1.05,2))
###if between 24-26, apply a 4% raise to current        
##    elif value >= 22.0 and value <= 24.0:
##        Employee_Dict['total_hourly_wage'].append(round(value*1.04,2))
###if between 26-28, apply a 3% raise to current        
##    elif value >= 22.0 and value <= 24.0:
##        Employee_Dict['total_hourly_wage'].append(round(value*1.03,2))
###else: 2% raise to current
##    else:
##        Employee_Dict['total_hourly_wage'].append(round(value*1.02,2))
print("UnderPaid_Salaries: ")
json_underPaid = json.dumps(underpaid_salaries, indent = 4)
print(json_underPaid)
print("Company_Raises: ")
json_Company = json.dumps(company_raises, indent = 4)
print(json_Company)
print("EmployeeList: ")
json_EmplInfo = json.dumps(list2, indent = 4)
print(json_EmplInfo)
#add new list called company_raises the name of the
#employee and the raise you calculated for each person
#info will be stored as a dictionary in dblike format

#print out data in all 3 lists generated
