x=1000
y=0
try:

    if x<2000:
        print(x/y)
    else:
        print(x**y) 
    
except:
    print("Ha ocurrido un ERROR")

# # try:

# #     if x<2000:
# #         print(x/y)
# #     else:
# #         print(x**y) 
    
# # except ZeroDivisionError as e:
# #     print("Ha ocurrido un Error ", e)
# from msilib.schema import Error


# x=10000

# seguir=True
# while seguir==True:
#     try:
#         y=int(input("ingrese un dato diferente de CERO "))  
#         if x<2000:
#             if y !=0:
#                 print(x/y)
#                 seguir=False

#             else:
#                 raise ZeroDivisionError ("Division por cero")
#         else:
#             print("Puedes hacer tus compras")
#             seguir=False

#     except ZeroDivisionError as e:
#         print("El error que ha ocurrido es ", e)
#     except ValueError:
#         print("El dato introducido no corresponde al valor esperado")

