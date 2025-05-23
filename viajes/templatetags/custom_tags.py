# Los template tags (etiquetas de plantilla) son una forma de agregar lógica personalizada dentro de las plantillas HTML de Django. 
# Sirven para extender las funcionalidades del sistema de templates cuando los filtros o tags incorporados no alcanzan.
#
# Por ejemplo, si querés mostrar un texto personalizado, formatear un dato de una forma especial, 
# o realizar algún cálculo directamente en el HTML, podés crear tu propio template tag.

from django import template

register = template.Library()

# esto es para controlar el acceso a boton de agregar, tiene que ser un usuario con grupo asignado
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()