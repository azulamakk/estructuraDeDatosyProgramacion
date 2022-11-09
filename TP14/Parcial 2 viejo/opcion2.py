import csv
from ventas import *
from opcion9y10 import *

def cargarVentaManual():
    while True:
        try:
            invoiceID = input('Ingrese Invoice ID')
            while isinstance(invoiceID, str) == False:
                invoiceID = input('Tipo de dato incorrecto. Ingrese Invoice ID')
            
            branch = input('Ingrese branch')
            while isinstance(branch, str) == False:
                branch = input('Tipo de dato incorrecto. Ingrese branch')
            
            city = input('Ingrese ciudad')
            while isinstance(city, str) == False:
                city = input('Tipo de dato incorrecto. Ingrese ciudad')
            
            customerType = input('Ingrese tipo de cliente')
            while isinstance(customerType, str) == False:
                customerType = input('Tipo de dato incorrecto. Ingrese tipo de cliente')
            
            gender = input('Ingrese tipo de cliente')
            while isinstance(gender, str) == False and gender != 'Female' and gender != 'Male':
                gender = input('Tipo de dato incorrecto. Ingrese genero')
            
            productLine = input('Ingrese linea de producto')
            while isinstance(productLine, str) == False:
                productLine = input('Tipo de dato incorrecto. Ingrese linea de producto')
            
            unitPrice = float(input('Ingrese precio unitario'))
            while isinstance(unitPrice, float) == False:
                unitPrice = input('Tipo de dato incorrecto. Ingrese precio unitario')       

            quantity = int(input('Ingrese cantidad'))
            while isinstance(quantity, int) == False:
                quantity = input('Tipo de dato incorrecto. Ingrese cantidad') 

            payment = input('Ingrese tipo de pago')
            while isinstance(payment, str) == False:
                payment = input('Tipo de dato incorrecto. Ingrese tipo de pago')

            total = int(quantity) * float(unitPrice)
            tax5 = total * 0.05

            date = IngresoSoloFecha()

            time = IngresoSoloHora() 

            grossMarginPercentage = float(input('Ingrese margen burto de ganancia'))
            while isinstance(grossMarginPercentage, float) == False:
                grossMarginPercentage = input('Tipo de dato incorrecto. Ingrese margen bruto de ganancia')   
            
            grossIncome = float(input('Ingrese ingreso bruto'))
            while isinstance(grossIncome, float) == False:
                grossIncome = input('Tipo de dato incorrecto. Ingrese ingreso bruto')               

            rating = float(input('Ingrese calificacion'))
            while isinstance(rating, float) == False:
                rating = input('Tipo de dato incorrecto. Ingrese calificacion')       
            break
        except:
            print('Hubo un error de carga, lo vas a hacer nuevamente\n')

    cargaManual=Ventas(invoiceID, branch, city, customerType, gender, productLine, unitPrice, quantity, tax5, 
    total, date, time, payment, grossMarginPercentage, grossIncome, rating)
    
    field_names = ['Invoice ID','Branch','City','Customer type','Gender',
    'Product line', 'Unit price','Quantity','Tax 5%', 'Total','Date',
    'Time','Payment','gross margin percentage', 'gross income','Rating']
    
    dict = {'Invoice ID':invoiceID,
    'Branch':branch,'City':city,'Customer type':customerType,'Gender':gender,
    'Product line':productLine, 'Unit price':unitPrice,'Quantity':quantity,'Tax 5%':tax5, 'Total':total,
    'Date':date,'Payment':payment,'gross margin percentage':grossMarginPercentage, 'gross income':grossIncome,'Rating':rating}
    
    with open('/Users/azulmakk/Desktop/Estructura de Datos/TP14/Parcial 2 viejo/supermarket_sales - Sheet1.csv', 'a') as csvFile:
        dict_object = csv.DictWriter(csvFile, fieldnames=field_names) 
        dict_object.writerow(dict)
    
    return cargaManual

