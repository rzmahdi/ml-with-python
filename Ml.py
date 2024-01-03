import sql
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

le = LabelEncoder()
# changing car_names to number  
le.fit([car[0] for car in sql.read()])

car_names = []
years = []
mile_ages = []
y = []

for car in sql.read():
    # Add the name of the changed car
    car_names.append(int(le.transform([car[0]])[0]))
    years.append(int(car[1]))
    mile_ages.append(int(car[2]))
    y.append(int(car[3]))

x = list(zip(car_names, years, mile_ages))

# training
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

print("\t\t***HINT***\nYou Can Find The Car Names in truecar.com\n\t *write -> exit <- in car name for exit*")

status = True
while(status):
    car_name = input("Enter the car name: ")
    if car_name == 'exit':
        status = False
    car_year = input("Enter the year: ")
    mile_age = int(input("Enter the mile age: "))
    
    newData = [[int(le.transform([car_name]).item()), car_year, mile_age]]
    answer = int(clf.predict(newData))
    # show the result
    print(f"\nprice of this car is: ${int(answer)}")
