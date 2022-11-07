import csv
import datetime

def parseDate(date, time):
    try:    
        dateParts = date.split("/")
        if len(dateParts) < 3:
            return None

        [month, day, year] = dateParts
        timeParts = time.split(":")
        if len(timeParts) < 2:
            return None

        [hour, minute] = timeParts

        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    except:
        return None

listaVentas=[]
class Ventas:
    def __init__(self, invoiceID, branch, city, customerType, gender, productLine, unitPrice, quantity, tax5, total, date, time, payment, grossMarginPercentage, grossIncome, rating):
        self.invoiceID = invoiceID
        self.branch = branch
        self.city = city 
        self.customerType = customerType 
        self.gender = gender 
        self.productLine = productLine
        self.unitPrice = unitPrice
        self.quantity= quantity
        self.tax5 = tax5
        self.total = total 
        self.date = parseDate(date, time)
        self.payment = payment 
        self.grossMarginPercentage = grossMarginPercentage
        self.grossIncome = grossIncome
        self.rating = rating
    def __str__(self):
        return str((self.invoiceID, self.branch, self.city, self.customerType, self.gender, self.productLine, self.unitPrice, self.quantity, self.tax5, self.total, self.date, self.payment, self.grossMarginPercentage, self.grossIncome, self.rating))


with open('/Users/azulmakk/Desktop/Estructura de Datos/TP14/Parcial 2 viejo/supermarket_sales - Sheet1.csv') as csvFile:
    reader=csv.DictReader(csvFile)
    for linea in reader:
        linea = Ventas(linea['Invoice ID'], linea['Branch'], linea['City'], linea['Customer type'], linea['Gender'], linea['Product line'],
            linea['Unit price'], linea['Quantity'], linea['Tax 5%'], linea['Total'], linea['Date'], linea['Time'], linea['Payment'], 
            linea['gross margin percentage'],  linea['gross income'], linea['Rating'])

        listaVentas.append(linea)

listaSucursales=[]
for venta in listaVentas:
    if venta.branch not in listaSucursales:
        listaSucursales.append(venta.branch)
tuplaSucursales=tuple(listaSucursales)

listaCiudades = []
for venta in listaVentas:
    if venta.city not in listaCiudades:
        listaCiudades.append(venta.city)
tuplaCiudades=tuple(listaCiudades)


parseDate("asd/12/12", "ho:21")