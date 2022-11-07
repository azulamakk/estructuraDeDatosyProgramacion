import csv
from ventas import *
from punto9y10 import *

def cargarVentaManual():
    
    invoiceID = input('Ingrese Invoice ID')
    branch = input('Ingrese branch')
    city = input('Ingrese ciudad')
    customerType = input('Ingrese tipo de cliente')
    gender = str(input('Ingrese genero'))
    productLine = input('Ingrese linea del producto')
    unitPrice = float(input('Ingrese precio unitario'))
    quantity= int(input('Ingrese cantidad'))
    total = quantity * unitPrice
    tax5 = total * 0.05
    date = IngresoFechayHora()
    time = input('Ingrese hora')
    payment = input('Ingrese pago')
    grossMarginPercentage = input('Ingrese porcentaje de margen grueso')
    grossIncome = input('Ingrese ingreso bruto')
    rating = input('Ingrese rating')
    
    cargaManual=Ventas(invoiceID, branch, city, customerType, gender, productLine, unitPrice, quantity, 
    tax5, total, date, time, payment, grossMarginPercentage, grossIncome, rating)
    
    field_names = ['Invoice ID','Branch','City','Customer type','Gender',
    'Product line', 'Unit price','Quantity','Tax 5%', 'Total','Date',
    'Time','Payment','gross margin percentage', 'gross income','Rating']
    
    dict = {'Invoice ID':invoiceID,
    'Branch':branch,'City':city,'Customer type':customerType,'Gender':gender,
    'Product line':productLine, 'Unit price':unitPrice,'Quantity':quantity,'Tax 5%':tax5, 'Total':total,
    'Date':date,'Time':time,'Payment':payment,'gross margin percentage':grossMarginPercentage, 'gross income':grossIncome,'Rating':rating}
    
    with open('/Users/azulmakk/Desktop/Estructura de Datos/TP14/Parcial 2 viejo/supermarket_sales - Sheet1.csv', 'a') as csvFile:
        dict_object = csv.DictWriter(csvFile, fieldnames=field_names) 
        dict_object.writerow(dict)
    
    return cargaManual