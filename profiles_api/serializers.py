from rest_framework import serializers

"""
    Los serializadores sirven para:
    1. Convertir entradas de datos en objetos de django
    2. Generar validaciones ej: tipo especifico de entrada
    Vamos a crear una clase que se va a basar en la clase 
    serializer del rest_framework
"""

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    # Especificamos las entradas que queremos recibir en el serializer
    """
    Genera un campo nombre que debe ser de tipo caracter,
    siempre que envie una peticion de tipo post o 
    patch espere una entrada con la variable 
    """
    name = serializers.CharField(max_length=10)
