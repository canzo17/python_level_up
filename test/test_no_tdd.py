## tiene una estado ciclico donde se repiten los pasos y se corre las 
#pruebas hasta que deje fallar haciendo las correcciones correspondientes
#en cada ciclo de correccion #
# prueba roja estado donde las pruebas siguen fallando
# #refactori - es la etapa donde se optimiza el codigo que 
#ya este funcionando 
def sumar(n1,n2):
        return n1 + n2 

def test_sumar_dos_numeros():
    num1 = 3 
    num2 = 5
    resultado = sumar(num1,num2)

    assert resultado == 8
#probando cambios 
