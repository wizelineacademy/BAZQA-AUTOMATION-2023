from behave import Then
from behave import
from screens.Descripcion_Producto import DescripcionProducto
from Utils.dictionaries.home_screen_text import HOME_TEXTS


@When('Tap boton añadir a carrito')
def step_impl(context):
    desc_producto = DescripcionProducto(context)
    desc_producto.tap_element(*desc_producto.btn_ADDCarrito)


@Then('Tap boton carrito')
def step_impl(context):
    btn_car = DescripcionProducto(context)
    btn_car.tap_element(*btn_car.btn_carrito)


@Then('Validar detalle carrito')
def step_impl(context):
    detalle_car = DescripcionProducto(context)
    detalle_car.assert_text(*detalle_car.etiqueta_producto, text=HOME_TEXTS.get('lbl_producto_carrito'))
    detalle_car.assert_text(*detalle_car.etiqueta_precio, text=HOME_TEXTS.get('$9.99'))
