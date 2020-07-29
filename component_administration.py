# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'component_administration.ui'
#
# Created by: Edgar Sáenz Zubía
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from datetime import datetime
import matplotlib.pyplot as pt
import time

window_width = 1300
window_height = 650
side_menu_width = 176
side_menu_height = 171
C1_width = 170
C_width = 150


class Deudores():  # clase para administrar deudores
    def __init__(self):
        self.nombre = None
        self.deuda = 0
        self.fecha = None

    def crear_deudor(self, nombre, deuda, fecha):
        self.nombre = nombre
        self.deuda = deuda
        self.fecha = fecha

    def restar_deuda(self, abono):
        self.deuda -= abono


class Ui_MainWindow(QtWidgets.QWidget):
    font = None
    count = 0
    ultimo_label_menu = ""
    ultimo_grupo_visible = ""
    lista_compras = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(window_width, window_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon("iconos/Hilos.png")
        self.centralwidget.setWindowIcon(icon)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(182, 14, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)

        # menu==============================================================================================
        INICIOx = 10
        self.grupo_menu = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(0, 0, side_menu_width, window_height, "grupo_menu", self.grupo_menu, "rgb(26,32,40)")
        self.grupo_menu.setVisible(True)
        self.edit_filtrar = QtWidgets.QLineEdit(self.grupo_menu)
        self.crear_lineEdit(10, 5, 161, 35, "Buscar", self.edit_filtrar)

        self.boton_inicio = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_inicio = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(INICIOx, self.acomodar_menu(0), 161, 61, "inicio", self.boton_inicio)
        self.crear_label(0, self.acomodar_menu(0), 10, 61, "", self.label_menu_inicio, color="black")

        self.boton_buscar = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_buscar = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(INICIOx, self.acomodar_menu(1), 161, 61, "Buscar producto", self.boton_buscar)
        self.crear_label(0, self.acomodar_menu(1), 10, 61, "", self.label_menu_buscar, color="black")

        self.boton_inventario = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_inventario = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(10, self.acomodar_menu(2), 161, 61, "Inventario", self.boton_inventario)
        self.crear_label(0, self.acomodar_menu(2), 10, 61, "", self.label_menu_inventario, color="black")

        self.boton_planillas = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_planillas = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(10, self.acomodar_menu(3), 161, 61, "Planillas", self.boton_planillas)
        self.crear_label(0, self.acomodar_menu(3), 10, 61, "", self.label_menu_planillas, color="black")

        self.boton_biografias = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_biografias = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(10, self.acomodar_menu(4), 161, 61, "Biografías", self.boton_biografias)
        self.crear_label(0, self.acomodar_menu(4), 10, 61, "", self.label_menu_biografias, color="black")

        self.boton_deudores = QtWidgets.QPushButton(self.grupo_menu)
        self.label_menu_deudores = QtWidgets.QLabel(self.grupo_menu)
        self.crear_boton_menu(10, self.acomodar_menu(5), 161, 61, "Deudores", self.boton_deudores)
        self.crear_label(0, self.acomodar_menu(5), 10, 61, "", self.label_menu_deudores, color="black")

        self.boton_recargas = QtWidgets.QPushButton(self.grupo_menu)
        self.crear_boton_menu(10, self.acomodar_menu(6), 161, 61, "Recargas", self.boton_recargas)

        self.boton_acerca_de = QtWidgets.QPushButton(self.grupo_menu)
        self.crear_boton_menu(10, self.acomodar_menu(7), 161, 61, "Acerca de", self.boton_acerca_de)

        self.cambiar_color(self.label_menu_inicio)
        self.ultimo_label_menu = self.label_menu_inicio

        # ===============================================================================================================
        self.grupo_buscar_producto = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, "gropuBox",
                            self.grupo_buscar_producto)
        self.grupo_buscar_producto.setVisible(False)

        self.label_titulo_buscar = QtWidgets.QLabel(self.grupo_buscar_producto)
        self.crear_label(5, 5, 300, 40, "Buscar Producto", self.label_titulo_buscar)
        self.label_titulo_buscar.setFont(self.set_font(18))
        self.spinbox_cantidad = QtWidgets.QSpinBox(self.grupo_buscar_producto)
        self.crear_spinbox(30, 470, 141, 31, "# artículos", self.spinbox_cantidad)
        self.spinbox_cantidad.setValue(1)

        self.linea_vertical_2 = QtWidgets.QFrame(self.grupo_buscar_producto)
        self.crear_linea(380, 15, 5, 550, "linea_vertical_2", self.linea_vertical_2)

        self.label_imagen_producto = QtWidgets.QLabel(self.grupo_buscar_producto)
        self.crear_label(0, 50, 321, 281, "", self.label_imagen_producto)

        self.label_producto = QtWidgets.QLabel(self.grupo_buscar_producto)
        self.crear_label(0, 331, 311, 31, "", self.label_producto)
        self.label_precio_unitario = QtWidgets.QLabel(self.grupo_buscar_producto)
        self.crear_label(0, 370, 311, 31, "", self.label_precio_unitario)
        self.edit_buscar_producto = QtWidgets.QLineEdit(self.grupo_buscar_producto)
        self.crear_lineEdit(00, 401, 311, 31, "Buscar producto", self.edit_buscar_producto)
        # 0, 331, 311, 31
        # 0, 401, 311, 31
        # 0, 370, 311, 31
        self.boton_comprar = QtWidgets.QPushButton(self.grupo_buscar_producto)
        self.crear_boton(180, 470, 141, 31, "Comprar", self.boton_comprar)
        self.boton_comprar.clicked.connect(lambda: self.funcion_agrega_a_carrito())
        self.boton_lista_surtir = QtWidgets.QPushButton(self.grupo_buscar_producto)
        self.crear_boton(80, 510, 250, 31, "Agregar a lista a surtir", self.boton_lista_surtir, border_style= "solid")
        self.boton_lista_surtir.clicked.connect(lambda: self.crear_lista_a_surtir())
        self.boton_carrito = QtWidgets.QPushButton(self.grupo_buscar_producto)
        self.crear_boton_redondo(self.grupo_buscar_producto.width() - 50, 5, 30, "", self.boton_carrito,
                                 "boton_carrito")
        self.coloca_icono("Comprar", self.boton_carrito)
        self.label_conteo_carrito = QtWidgets.QLabel(self.grupo_buscar_producto)
        self.crear_label(self.grupo_buscar_producto.width() - 90, 5, 40, 30, "", self.label_conteo_carrito)
        self.label_conteo_carrito.setFont(self.set_font(18))

        MainWindow.setCentralWidget(self.centralwidget)

        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.tabla_busqueda = QtWidgets.QTableWidget(self.grupo_buscar_producto)
        self.crear_tableWidget(15, 2, "tabla_busqueda", 450, 50, 400, 300, self.tabla_busqueda)
        self.tabla_busqueda.setColumnWidth(0, 290)
        self.tabla_busqueda.setColumnWidth(1, 60)
        self.tabla_busqueda.setHorizontalHeaderItem(0, self.define_titulo_columna("Artículo"))
        self.tabla_busqueda.setHorizontalHeaderItem(1, self.define_titulo_columna("Precio"))
        self.tabla_busqueda.cellClicked.connect(lambda: self.funcion_seleccion())
        self.tabla_busqueda.cellDoubleClicked.connect(lambda: self.funcion_agrega_a_carrito())

        self.label_count = QtWidgets.QLabel(self.grupo_buscar_producto)
        self.crear_label(450, 400, 250, 30, "", self.label_count)

        # crea un groupBox:------------------------------------------------------------------
        self.grupo_inventario_0 = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, "gropo_inventario_0",
                            self.grupo_inventario_0)

        self.label_inv = QtWidgets.QLabel(self.grupo_inventario_0)
        self.crear_label(0, 450, 121, 16, "", self.label_inv)
        # -------------------------------------------------------------------------------------
        # crea un groupBox:-------------------------------------------------------------------
        self.grupo_inicio = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, "grupo_inicio",
                            self.grupo_inicio)
        self.grupo_inicio.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_inicio

        self.boton_agrega_inventario = QtWidgets.QPushButton(self.grupo_inicio)
        self.crear_boton_redondo(self.acomodar_botones(0), 100, 250, "", self.boton_agrega_inventario,
                                 "boton_agrega_inventario")
        self.coloca_icono("AgregarEliminar inventario", self.boton_agrega_inventario, QtCore.QSize(100, 100))
        self.boton_agrega_inventario.clicked.connect(lambda: self.funcion_agrega_inventario())

        self.boton_buscar_inventario = QtWidgets.QPushButton(self.grupo_inicio)
        self.crear_boton_redondo(self.acomodar_botones(1), 100, 250, "", self.boton_buscar_inventario,
                                 "boton_buscar_inventario")
        self.boton_buscar_inventario.clicked.connect(lambda: self.buscar_producto())
        self.coloca_icono("Buscar", self.boton_buscar_inventario, QtCore.QSize(100, 100))
        self.boton_lista_compras = QtWidgets.QPushButton(self.grupo_inicio)
        self.crear_boton_redondo(self.acomodar_botones(2), 100, 250, "", self.boton_lista_compras,
                                 "boton_lista_compras")
        self.coloca_icono("Lista de compras", self.boton_lista_compras, QtCore.QSize(100, 100))

        self.boton_finanzas = QtWidgets.QPushButton(self.grupo_inicio)
        self.crear_boton_redondo(self.acomodar_botones(3), 100, 250, "", self.boton_finanzas,
                                 "boton_finanzas")
        self.boton_finanzas.clicked.connect(lambda: self.generar_grafica())
        self.coloca_icono("Finanzas", self.boton_finanzas, QtCore.QSize(100, 100))

        self.grupo_reporte = QtWidgets.QGroupBox(self.grupo_inicio)
        self.crear_groupbox(self.grupo_inicio.width() - 800, 375, 815, 200, "grupo_reporte", self.grupo_reporte,
                            "rgb(127,127,127)")

        self.linea_vertical_5 = QtWidgets.QFrame(self.grupo_reporte)
        self.crear_linea(10, 10, 5, self.grupo_reporte.height() - 20, "linea_vertical_5", self.linea_vertical_5)
        self.establecer_estilo(self.linea_vertical_5, backgrond_color="red")
        self.label_articulos_individuales = QtWidgets.QLabel(self.grupo_reporte)
        self.label_articulos_totales = QtWidgets.QLabel(self.grupo_reporte)
        self.label_articulos_mas_vendido = QtWidgets.QLabel(self.grupo_reporte)
        self.label_venta_dia = QtWidgets.QLabel(self.grupo_reporte)
        self.label_venta_mayor = QtWidgets.QLabel(self.grupo_reporte)
        self.label_numero_de_ventas = QtWidgets.QLabel(self.grupo_reporte)
        self.crear_label(17, 10, 280, 30, "No. artículos individuales vendidos: ", self.label_articulos_individuales)
        self.crear_label(17, 40, 280, 30, "Artículos totales vendidos: ", self.label_articulos_totales)
        self.crear_label(17, 70, 280, 30, "Artículo más vendido: ", self.label_articulos_mas_vendido)
        self.crear_label(17, 100, 280, 30, "Venta del día: ", self.label_venta_dia)
        self.crear_label(17, 130, 280, 30, "Venta mayor en un evento: ", self.label_venta_mayor)
        self.crear_label(17, 160, 280, 30, "Número de ventas: ", self.label_numero_de_ventas)

        self.linea_vertical_6 = QtWidgets.QFrame(self.grupo_reporte)
        self.crear_linea(300, 10, 5, self.grupo_reporte.height() - 20, "linea_vertical_6", self.linea_vertical_6)
        self.establecer_estilo(self.linea_vertical_6, backgrond_color="rgb(180,180,180)", border_style="none")

        self.label_articulos_individuales_num = QtWidgets.QLabel(self.grupo_reporte)
        self.label_articulos_totales_num = QtWidgets.QLabel(self.grupo_reporte)
        self.label_articulos_mas_vendido_num = QtWidgets.QLabel(self.grupo_reporte)
        self.label_venta_dia_num = QtWidgets.QLabel(self.grupo_reporte)
        self.label_venta_mayor_num = QtWidgets.QLabel(self.grupo_reporte)
        self.label_numero_de_ventas_num = QtWidgets.QLabel(self.grupo_reporte)
        self.crear_label(306, 10, 280, 30, "", self.label_articulos_individuales_num)
        self.crear_label(306, 40, 280, 30, "", self.label_articulos_totales_num)
        self.crear_label(306, 70, 280, 30, "", self.label_articulos_mas_vendido_num)
        self.crear_label(306, 100, 280, 30, "", self.label_venta_dia_num)
        self.crear_label(306, 130, 280, 30, "", self.label_venta_mayor_num)
        self.crear_label(306, 160, 280, 30, "", self.label_numero_de_ventas_num)

        self.linea_vertical_7 = QtWidgets.QFrame(self.grupo_reporte)
        self.crear_linea(540, 10, 5, self.grupo_reporte.height() - 20, "linea_vertical_7", self.linea_vertical_7)
        self.establecer_estilo(self.linea_vertical_7, backgrond_color="rgb(180,180,180)", border_style="none")

        self.boton_genera_grafica_1 = QtWidgets.QPushButton(self.grupo_reporte)
        self.boton_genera_grafica_2 = QtWidgets.QPushButton(self.grupo_reporte)
        self.crear_boton(555, 40, 240, 60, "Gráfica/artículo", self.boton_genera_grafica_1, border_style="solid")
        self.crear_boton(555, 110, 240, 60, "Gráfica/Venta por evento", self.boton_genera_grafica_2, border_style="solid")
        self.boton_genera_grafica_2.clicked.connect(
            lambda: self.graficar_pie_chart(self.lista_cantidades, self.lista_ventas))
        self.boton_genera_grafica_1.clicked.connect(
            lambda: self.grafica_de_barras(self.lista_productos_individuales, self.lista_cantidades_productos))

        # ===============================================================================================================
        self.grupo_lista_a_surtir = QtWidgets.QGroupBox(self.grupo_inicio)
        self.crear_groupbox(self.grupo_inicio.width() - 700, 375, 550, self.grupo_inicio.height() - 370,
                            "grupo_lista_a_surtir", self.grupo_lista_a_surtir, "rgb(127,127,127)")
        self.boton_lista_compras.clicked.connect(lambda: self.ver_lista_a_surtir())
        self.tabla_lista_a_surtir = QtWidgets.QTableWidget(self.grupo_lista_a_surtir)
        self.crear_tableWidget(0, 1, "tabla_lista_a_surtir", 10, 10, self.grupo_lista_a_surtir.width() - 200,
                               self.grupo_lista_a_surtir.height() - 20, self.tabla_lista_a_surtir)
        self.tabla_lista_a_surtir.setHorizontalHeaderItem(0, self.define_titulo_columna("Artículos a comprar:"))
        self.boton_elimina_articulo = QtWidgets.QPushButton(self.grupo_lista_a_surtir)
        self.crear_boton(self.grupo_lista_a_surtir.width() - 180, 20, 150, 40, "Eliminar articulo", self.boton_elimina_articulo, border_style= "solid" )
        self.boton_elimina_articulo.clicked.connect(lambda: self.elimina_articulo_a_surtir())

        self.boton_elimina_lista = QtWidgets.QPushButton(self.grupo_lista_a_surtir)
        self.crear_boton(self.grupo_lista_a_surtir.width() - 180, 70, 150, 40, "Eliminar Lista",
                         self.boton_elimina_lista, border_style="solid")
        self.boton_elimina_lista.clicked.connect(lambda: self.elimina_lista_a_surtir())

        # ========================================================================================
        self.grupo_agrega_inventario = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height,
                            "grupo_agrega_inventario",
                            self.grupo_agrega_inventario)
        self.label_agrega_elimina_inventario = QtWidgets.QLabel(self.grupo_agrega_inventario)
        self.crear_label(5, 5, 450, 40, "Agrega/Elimina/Modifica inventario", self.label_agrega_elimina_inventario)
        self.label_agrega_elimina_inventario.setFont(self.set_font(18))
        self.label_seleccion = QtWidgets.QLabel(self.grupo_agrega_inventario)
        self.crear_label(50, 100, 250, 30, "¿Que quieres hacer?", self.label_seleccion)
        self.boton_agrega_seccion = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(50, 150, 250, 60, "Agrega sección", self.boton_agrega_seccion, border_style="solid")
        self.boton_agrega_seccion.clicked.connect(lambda: self.funcion_habilita_seccion())
        self.boton_agrega_producto = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(50, 230, 250, 60, "Agrega producto", self.boton_agrega_producto, border_style="solid")
        self.boton_agrega_producto.clicked.connect(lambda: self.funcion_habilita_seccion())
        self.boton_elimina_seccion = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(50, 310, 250, 60, "Elimina sección", self.boton_elimina_seccion, border_style="solid")
        self.boton_elimina_seccion.clicked.connect(lambda: self.funcion_habilita_seccion())
        self.boton_elimina_producto = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(50, 390, 250, 60, "Elimina producto", self.boton_elimina_producto, border_style="solid")
        self.boton_elimina_producto.clicked.connect(lambda: self.funcion_habilita_seccion())
        self.boton_modifica_producto = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(50, 470, 250, 60, "Modifica producto", self.boton_modifica_producto, border_style="solid")
        self.boton_modifica_producto.clicked.connect(lambda: self.funcion_habilita_seccion())

        self.linea_vertical = QtWidgets.QFrame(self.grupo_agrega_inventario)
        self.crear_linea(310, 100, 5, 480, "linea_vertical", self.linea_vertical)

        self.label_titulo_agrega_inventario = QtWidgets.QLabel(self.grupo_agrega_inventario)
        self.crear_label(360, 160, 250, 30, "", self.label_titulo_agrega_inventario, font_weight="bold")

        self.label_configuracion = QtWidgets.QLabel(self.grupo_agrega_inventario)
        self.crear_label(360, 100, 250, 30, "Configuración", self.label_configuracion)
        self.combobox_secciones = QtWidgets.QComboBox(self.grupo_agrega_inventario)
        self.crear_combobox(360, 200, 250, 30, "secciones", self.combobox_secciones)
        self.combobox_secciones.activated.connect(lambda: self.listar_productos())
        self.combobox_secciones.setVisible(False)

        self.combobox_productos = QtWidgets.QComboBox(self.grupo_agrega_inventario)
        self.crear_combobox(360, 240, 250, 30, "productos", self.combobox_productos)
        self.combobox_productos.currentIndexChanged.connect(lambda: self.coloca_titulo_y_precio())
        self.combobox_productos.setVisible(False)

        self.boton_eliminar = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(510, 290, 100, 30, "Eliminar", self.boton_eliminar, border_style="solid")
        self.boton_eliminar.setVisible(False)
        self.boton_eliminar.clicked.connect(lambda: self.funcion_eliminar())

        self.label_modifica = QtWidgets.QLabel(self.grupo_agrega_inventario)
        self.crear_label(360, 290, 250, 30, "Modificar por:", self.label_modifica)
        self.label_modifica.setVisible(False)
        self.edit_titulo = QtWidgets.QLineEdit(self.grupo_agrega_inventario)
        self.crear_lineEdit(360, 320, 250, 30, "Título", self.edit_titulo)
        self.edit_titulo.textChanged.connect(lambda: self.funcion_modifica_boton())
        self.edit_titulo.setVisible(False)


        self.edit_precio = QtWidgets.QLineEdit(self.grupo_agrega_inventario)
        self.crear_lineEdit(360, 360, 250, 30, "Precio", self.edit_precio)
        self.edit_precio.textChanged.connect(lambda: self.modifica_label())
        self.edit_precio.setVisible(False)

        self.boton_modifica = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(455, 450, 155, 30, "Modifica", self.boton_modifica, border_style="solid")
        self.boton_modifica.clicked.connect(lambda: self.modifica_inventario())
        self.boton_modifica.setVisible(False)

        self.linea_vertical_1 = QtWidgets.QFrame(self.grupo_agrega_inventario)
        self.crear_linea(620, 100, 5, 480, "linea_vertical_1", self.linea_vertical_1)

        self.label_vista_previa = QtWidgets.QLabel(self.grupo_agrega_inventario)
        self.crear_label(680, 100, 250, 30, "Vista Previa", self.label_vista_previa)
        w_previo = 200
        h_previo = 250
        self.grupo_previo = QtWidgets.QGroupBox(self.grupo_agrega_inventario)
        self.crear_groupbox(680, 170, w_previo, h_previo, "grupo_previo", self.grupo_previo)
        self.grupo_previo.setVisible(True)
        self.label_imagen_previa = QtWidgets.QLabel(self.grupo_previo)
        self.crear_label(0, 0, w_previo, h_previo - 60, "", self.label_imagen_previa)

        self.boton_previo = QtWidgets.QPushButton(self.grupo_previo)
        self.crear_boton(0, h_previo - 60, w_previo, 30, "", self.boton_previo)
        self.boton_previo.setVisible(False)

        self.label_descripcion_previo = QtWidgets.QLabel(self.grupo_previo)
        self.crear_label(0, h_previo - 60, w_previo, 30, "", self.label_descripcion_previo)
        self.label_descripcion_previo.setVisible(False)

        self.label_precio_previo = QtWidgets.QLabel(self.grupo_previo)
        self.crear_label(0, h_previo - 30, w_previo, 30, "", self.label_precio_previo)
        self.label_precio_previo.setVisible(False)

        self.boton_generar = QtWidgets.QPushButton(self.grupo_agrega_inventario)
        self.crear_boton(455, 450, 155, 30, "Agregar", self.boton_generar, border_style="solid")
        self.boton_generar.clicked.connect(lambda: self.funcion_generar())
        self.boton_generar.setShortcut("Enter")
        self.boton_generar.setVisible(False)
        self.mensaje_guarda = QtWidgets.QMessageBox(self.centralwidget)
        self.crear_mensaje("Se agregó correctamente", self.mensaje_guarda)

        # ========================================================================================
        # crea un groupBox:======================================================================
        self.grupo_planillas = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, "gropuBox_6", self.grupo_planillas)
        self.label_titulo_planillas = QtWidgets.QLabel(self.grupo_planillas)
        self.crear_label(5, 5, 300, 40, "Planillas", self.label_titulo_planillas)
        self.label_titulo_planillas.setFont(self.set_font(18))
        self.tabla_planillas = QtWidgets.QTableWidget(self.grupo_planillas)
        self.crear_tableWidget(463, 2, "planillas", 10, 100, 550, 500, self.tabla_planillas)
        self.tabla_planillas.setHorizontalHeaderItem(0, self.define_titulo_columna("Número"))
        self.tabla_planillas.setHorizontalHeaderItem(1, self.define_titulo_columna("Título"))
        self.tabla_planillas.setColumnWidth(0, 50)
        self.tabla_planillas.setColumnWidth(1, 200)
        self.linea_vertical_3 = QtWidgets.QFrame(self.grupo_planillas)
        self.crear_linea(575, 15, 5, 600, "linea_vertical_2", self.linea_vertical_3)
        self.edit_buscar_planillas = QtWidgets.QLineEdit(self.grupo_planillas)
        self.crear_lineEdit(600, 80, 300, 30, "Buscar planillas", self.edit_buscar_planillas)

        self.tabla_planillas_filtro = QtWidgets.QTableWidget(self.grupo_planillas)
        self.crear_tableWidget(20, 2, "planillas_filtro", 600, 120, 450, 300, self.tabla_planillas_filtro)
        self.tabla_planillas_filtro.setColumnWidth(0, 80)
        self.tabla_planillas_filtro.setColumnWidth(1, 300)
        self.tabla_planillas_filtro.setHorizontalHeaderItem(0, self.define_titulo_columna("Número"))
        self.tabla_planillas_filtro.setHorizontalHeaderItem(1, self.define_titulo_columna("Título"))

        self.cuenta_label = QtWidgets.QLabel(self.grupo_planillas)
        self.crear_label(605, 40, 300, 30, "", self.cuenta_label)

        # crea un groupBox:-------------------------------------------------------------------
        self.grupo_biografias = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, "grupo_biografias",
                            self.grupo_biografias)

        self.label_titulo_biografia = QtWidgets.QLabel(self.grupo_biografias)
        self.crear_label(5, 5, 300, 40, "Biografías", self.label_titulo_biografia)
        self.label_titulo_biografia.setFont(self.set_font(18))

        self.tabla_biografias = QtWidgets.QTableWidget(self.grupo_biografias)
        self.crear_tableWidget(693, 2, "Biografias", 10, 100, 550, 500, self.tabla_biografias)
        self.tabla_biografias.setColumnWidth(0, 50)
        self.tabla_biografias.setColumnWidth(1, 200)
        self.tabla_biografias.setHorizontalHeaderItem(0, self.define_titulo_columna("Número"))
        self.tabla_biografias.setHorizontalHeaderItem(1, self.define_titulo_columna("Nombre"))
        self.tabla_biografias.resizeColumnsToContents()
        self.leer_archivo(self.tabla_biografias, "biografias")
        self.linea_vertical_4 = QtWidgets.QFrame(self.grupo_biografias)
        self.crear_linea(575, 15, 5, 600, "linea_vertical_2", self.linea_vertical_4)
        self.edit_buscar_biografias = QtWidgets.QLineEdit(self.grupo_biografias)
        self.crear_lineEdit(600, 80, 300, 30, "Buscar biografias", self.edit_buscar_biografias)

        self.tabla_biografias_filtro = QtWidgets.QTableWidget(self.grupo_biografias)
        self.crear_tableWidget(20, 2, "biografias_filtro", 600, 120, 450, 300, self.tabla_biografias_filtro)
        self.tabla_biografias_filtro.setHorizontalHeaderItem(0, self.define_titulo_columna("Número"))
        self.tabla_biografias_filtro.setHorizontalHeaderItem(1, self.define_titulo_columna("Nombre"))
        self.tabla_biografias_filtro.setColumnWidth(0, 80)
        self.tabla_biografias_filtro.setColumnWidth(1, 300)

        self.cuenta_label_1 = QtWidgets.QLabel(self.grupo_biografias)
        self.crear_label(605, 40, 300, 30, "", self.cuenta_label_1)

        # crea un groupBox:-------------------------------------------------------------------
        self.grupo_deudores = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, "grupo_deudores", self.grupo_deudores)
        self.label_titulo_deudores = QtWidgets.QLabel(self.grupo_deudores)
        self.crear_label(5, 5, 300, 40, "Deudores", self.label_titulo_deudores)
        self.label_titulo_deudores.setFont(self.set_font(18))

        self.label_nombre = QtWidgets.QLabel(self.grupo_deudores)
        self.crear_label(10, 150, 90, 30, "Nombre: ", self.label_nombre)
        self.edit_nombre_deudor = QtWidgets.QLineEdit(self.grupo_deudores)
        self.crear_lineEdit(100, 150, 200, 30, "Nombre", self.edit_nombre_deudor)
        self.linea_vertical_8 = QtWidgets.QFrame(self.grupo_deudores)
        self.crear_linea(325, 15, 5, 550, "linea_vertical_8", self.linea_vertical_8)
        self.label_adeudo = QtWidgets.QLabel(self.grupo_deudores)
        self.crear_label(10, 185, 90, 30, "Debe: ", self.label_adeudo)
        self.edit_debe = QtWidgets.QLineEdit(self.grupo_deudores)
        self.crear_lineEdit(100, 185, 200, 30, "Debe", self.edit_debe)
        self.tabla_deudores = QtWidgets.QTableWidget(self.grupo_deudores)
        self.boton_registro_deudores = QtWidgets.QPushButton(self.grupo_deudores)
        self.crear_boton(10, 220, 200, 35, "Registrar deudor", self.boton_registro_deudores, border_style= "solid")
        self.crear_tableWidget(6, 3, "tabla_deudores", 350, 50, 450, 300, self.tabla_deudores)

        self.tabla_deudores.setHorizontalHeaderItem(0, self.define_titulo_columna("Nombre"))
        self.tabla_deudores.setHorizontalHeaderItem(1, self.define_titulo_columna("Debe"))
        self.tabla_deudores.setHorizontalHeaderItem(2, self.define_titulo_columna("Fecha"))
        self.tabla_deudores.setColumnWidth(0,220)
        self.tabla_deudores.setColumnWidth(1, 80)
        self.tabla_deudores.setColumnWidth(2, 100)
        self.label_numero_deudor = QtWidgets.QLabel(self.grupo_deudores)
        self.crear_label(10, 285, C1_width, 30, "Numero de Deudor: ", self.label_numero_deudor)
        self.edit_num_deudor = QtWidgets.QLineEdit(self.grupo_deudores)
        self.crear_lineEdit(170, 285, 50, 30, "", self.edit_num_deudor)
        self.elimina_boton = QtWidgets.QPushButton(self.grupo_deudores)
        self.crear_boton(10, 320, 200, 30, "Elimina deudor", self.elimina_boton,  border_style= "solid")
        self.edit_abonar = QtWidgets.QLineEdit(self.grupo_deudores)
        self.crear_lineEdit(10, 355, 50, 30, "", self.edit_abonar)
        self.abono_boton = QtWidgets.QPushButton(self.grupo_deudores)
        self.crear_boton(70, 355, 100, 30, "Abonar", self.abono_boton, border_style= "solid")
        self.elimina_boton.setVisible(True)
        self.crear_contenido()
        # ===============================================================================================================
        self.grupo_carrito_compras = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(window_width - 500, 0, 500, window_height, "grupo_carrito_compras",
                            self.grupo_carrito_compras, "rgb(124,124,124)")
        self.boton_carrito.clicked.connect(lambda: self.funcion_abrir_carrito())
        self.boton_cerrar_carrito = QtWidgets.QPushButton(self.grupo_carrito_compras)
        self.crear_boton_redondo(0, 0, 30, "", self.boton_cerrar_carrito, "boton_cerrar_carrito", border_style="none")
        self.coloca_icono("cerrar", self.boton_cerrar_carrito)
        self.boton_elimina_producto_carrito = QtWidgets.QPushButton(self.grupo_carrito_compras)
        self.crear_boton(60, 0, 200, 30, "Elimina producto", self.boton_elimina_producto_carrito, border_style="none")
        self.boton_elimina_producto_carrito.clicked.connect(lambda: self.eliminar_producto())
        self.boton_guardar_carrito = QtWidgets.QPushButton(self.grupo_carrito_compras)
        self.crear_boton(260, 0, 200, 30, "Guarda carrito", self.boton_guardar_carrito, border_style="none")
        self.boton_guardar_carrito.clicked.connect(lambda: self.guardar_carrito())

        self.boton_cerrar_carrito.clicked.connect(lambda: self.funcion_cerrar_carrito())
        self.tabla_carrito = QtWidgets.QTableWidget(self.grupo_carrito_compras)
        self.crear_tableWidget(0, 3, "tabla_carrito", 20, 50, self.grupo_carrito_compras.width() - 40, 440,
                               self.tabla_carrito)
        self.tabla_carrito.setHorizontalHeaderItem(0, self.define_titulo_columna("Artículo"))
        self.tabla_carrito.setHorizontalHeaderItem(1, self.define_titulo_columna("Precio"))
        self.tabla_carrito.setHorizontalHeaderItem(2, self.define_titulo_columna("Cantidad"))
        self.label_total = QtWidgets.QLabel(self.grupo_carrito_compras)
        self.crear_label(200, 500, 200, 60, "", self.label_total)
        self.label_total.setFont(self.set_font(18))
        self.boton_comprar_ahora = QtWidgets.QPushButton(self.grupo_carrito_compras)
        self.crear_boton(200, 570, 100, 60, "Pagar", self.boton_comprar_ahora)
        self.boton_comprar_ahora.clicked.connect(lambda: self.funcion_pagar())
        self.label_mensaje = QtWidgets.QLabel(self.grupo_carrito_compras)
        self.crear_label(100, 200, 250, 60, "", self.label_mensaje)
        self.label_mensaje.setFont(self.set_font(18))

        # ===============================================================================================================
        self.grupo_acerca_de = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 450, window_width - side_menu_width - 300, window_height - 450,
                            "grupo_acerca_de", self.grupo_acerca_de, "rgb(65,105,225)")
        self.label_acerca_de = QtWidgets.QLabel(self.grupo_acerca_de)
        self.crear_label(10, 10, window_width - side_menu_width, window_height - 460,
                         "Acerca de\nAdministración de productos\nInventario, Lista de compras, Buscador de planillas, "
                         "Buscador de biografías, Registro de deudores\n2020\nDesarrollado por: Edgar Sáenz Zubía\nEmail: "
                         "edgar.sz189@gmail.com\nVersión: 1.0",
                         self.label_acerca_de, "white", "transparent")
        self.boton_acerca_de.clicked.connect(lambda: self.funcion_acerca_de())
        self.boton_cerrar_acerca_de = QtWidgets.QPushButton(self.grupo_acerca_de)
        self.crear_boton_redondo(794, 0, 30, 'cerrar', self.boton_cerrar_acerca_de, "boton_cerrar", border_style="none")
        self.boton_cerrar_acerca_de.setText("")
        self.boton_cerrar_acerca_de.clicked.connect(lambda: self.funcion_acerca_de())

        self.abrir = QtWidgets.QFileDialog(self.centralwidget)
        # señales:

        self.boton_inicio.clicked.connect(lambda: self.inicio())  # conecta el boton  con la función
        self.boton_buscar.clicked.connect(lambda: self.buscar_producto())  # conecta el boton  con la función
        self.boton_inventario.clicked.connect(lambda: self.inventario_add())  # conecta el boton  con la función
        self.boton_planillas.clicked.connect(lambda: self.planillas_funcion())  # conecta el boton  con la función
        self.boton_biografias.clicked.connect(lambda: self.biografias_funcion())  # conecta el boton  con la función
        self.boton_deudores.clicked.connect(lambda: self.deudores_funcion())  # conecta el boton  con la función

        self.edit_buscar_producto.textChanged.connect(lambda: self.leer_precios())
        self.edit_buscar_planillas.textChanged.connect(lambda: self.buscar_planillas())
        self.edit_buscar_biografias.textChanged.connect(
            lambda: self.buscar_en_archivo("biografias", self.tabla_biografias_filtro, self.edit_buscar_biografias,
                                           self.cuenta_label_1))
        self.boton_recargas.clicked.connect(lambda: self.recargas_funcion())  # conecta el boton  con la funció
        self.boton_registro_deudores.clicked.connect(
            lambda: self.add_deudor("deudor"))  # conecta el boton  con la función
        self.elimina_boton.clicked.connect(
            lambda: self.eliminar_deudor(self.edit_num_deudor.text()))  # conecta el boton  con la función
        self.abono_boton.clicked.connect(
            lambda: self.abonar(self.edit_num_deudor.text()))  # conecta el boton  con la función
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def modifica_inventario(self):
        articulo_a_cambiar = self.combobox_productos.currentText()
        flag = False
        with open("archivos/articulos.csv", "r") as data:
            articulos = data.readlines()
            for ind, i in enumerate(articulos):
                articulo = i.split(",")
                if articulo[0] == articulo_a_cambiar:
                    if self.edit_titulo.text() != "" and self.edit_precio.text() != "":
                        articulos[ind] = self.edit_titulo.text() + "," + self.edit_precio.text() + "\n"
                        flag = True
                        break
        if flag:
            with open("archivos/articulos.csv", "w") as data:
                data.writelines(articulos)
            #self.listar_secciones()
            self.listar_productos()
            self.edit_titulo.clear()
            self.edit_precio.clear()
            self.edit_titulo.setFocus()

    def ver_lista_a_surtir(self):
        if self.grupo_lista_a_surtir.isVisible():
            self.grupo_lista_a_surtir.setVisible(False)
        else:
            self.grupo_lista_a_surtir.setVisible(True)
            self.grupo_reporte.setVisible(False)
            self.actualiza_lista_a_surtir()
    def actualiza_lista_a_surtir(self):
        with open("archivos/lista a surtir.csv", "r") as data:
            articulos = data.readlines()
            size = len(articulos)
            self.tabla_lista_a_surtir.setRowCount(size)
            for i in range(size):
                self.poblar_tabla(i, 0, articulos[i].strip(), self.tabla_lista_a_surtir)
            self.tabla_lista_a_surtir.resizeColumnsToContents()

    def crear_lista_a_surtir(self):
        articulo = self.label_producto.text()
        if self.verifica_existencia(articulo.strip()) == False:
            with open("archivos/lista a surtir.csv", "+a") as data:
                data.writelines(articulo + "\n")
            self.mensaje_notifica_agrego = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("Se agrego correctamente a la lista", self.mensaje_notifica_agrego)
            self.mensaje_notifica_agrego.exec_()
            self.actualiza_lista_a_surtir()
        else:
            self.mensaje_notifica_existencia = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("Ya esta agregado a la lista", self.mensaje_notifica_existencia)
            self.mensaje_notifica_existencia.exec_()

    def elimina_articulo_a_surtir(self):
        flag = False
        r = self.tabla_lista_a_surtir.currentRow()
        if r != -1:
            articulo = self.tabla_lista_a_surtir.item(r, 0).text().strip()
            print(articulo)
            with open("archivos/lista a surtir.csv", "r") as data:
                articulos = data.readlines()
                if articulo + "\n" in articulos:
                    # Lo elimina de la lista:
                    articulos.pop(r)
                    flag = True
            if flag:
                with open("archivos/lista a surtir.csv", "w") as data:
                    # sobreescribe el archivo modificado:
                    data.writelines(articulos)
                self.actualiza_lista_a_surtir()
                rows = self.tabla_lista_a_surtir.rowCount()
                self.tabla_lista_a_surtir.selectRow(rows -1)

    def elimina_lista_a_surtir(self):
        with open("archivos/lista a surtir.csv", "w") as data:
            # sobreescribe el archivo con:
            data.writelines("")
        self.actualiza_lista_a_surtir()

    def verifica_existencia(self, articulo):
        with open("archivos/lista a surtir.csv", "r") as data:
            articulos = data.readlines()
            if articulo + "\n" in articulos:
                data.close()
                return True
            else:
                data.close()
                return False

    def guardar_carrito(self):
        # sender = self.sender()
        archivo = self.abrir.getSaveFileName(self, 'Guardar proyecto', "",
                                             "CSV files (*.csv)")  # obtendra la dirección y el nombre del archivo

        if archivo[0] != "":
            self.direccion_actual = archivo[0]
            self.funcion_guardar_tabla(self.direccion_actual)  # le paso la direccion del archivo
            # if sender.text() == "":
            #     self.edit_label_direccion.setText(archivo[0])

    def funcion_guardar_tabla(self, archivo):
        # recorrer toda la tabla:
        tabla = []
        lista_items = []
        r = self.tabla_carrito.rowCount()
        c = self.tabla_carrito.columnCount()

        for i in range(r):
            for j in range(c):
                lista_items.append(self.leer_item(i, j, self.tabla_carrito))
            tabla.append(lista_items)
            lista_items = []

        # guarda en un archivo CSV:
        with open(archivo, "w") as data:
            for i in range(r):
                for j in range(c):
                    data.writelines(tabla[i][j])
                    if j < c - 1:
                        data.writelines(",")
                    else:
                        data.writelines("\n")

    def eliminar_producto(self):
        indexes = self.tabla_carrito.selectionModel().selectedRows()
        if indexes != []:
            for index in indexes:
                num_fila = index.row()
                self.tabla_carrito.removeRow(num_fila)
                self.lista_compras.pop(num_fila)
                self.funcion_abrir_carrito()
                break

    def establecer_estilo(self, nombre_objeto, backgrond_color="transparent", color="black", font_weight="normal",
                          border_width="0.5px", border_style="none", border_radius=2, border_color="transparent"):
        nombre_objeto.setStyleSheet(f"background-color: {backgrond_color};"
                                    f"color: {color};"
                                    f"font-weight: {font_weight};"
                                    f"border_style {border_style};"
                                    f'border-radius: {border_radius}px;'
                                    f"border-width: {border_width};"
                                    f"border-color: {border_color};"
                                    )

    def grafica_de_barras(self, labels, sizes):
        fig1, ax1 = pt.subplots()
        y_pos = range(len(labels))
        numeros = []
        for i in sizes:
            numeros.append(int(i))
        ax1.barh(y_pos, numeros, align='center')
        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(labels)

        pt.show()

    def graficar_pie_chart(self, sizes, labels):
        # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs', "hey"
        # sizes = [15, 30, 45, 10, 100]
        # explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = pt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        pt.show()

    def generar_grafica(self):
        if self.grupo_reporte.isVisible():
            self.grupo_reporte.setVisible(False)
        else:
            self.grupo_reporte.setVisible(True)
            self.grupo_lista_a_surtir.setVisible(False)
            self.generar_reporte()

    def generar_reporte(self):
        try:
            now = datetime.now()
            dia = str(now.day)
            mes = str(now.month)
            year = str(now.year)
            count = 0

            with open(f"archivos/reporte_{dia + '_' + mes + '_' + '_' + year}.csv", "r") as data:
                productos = data.readlines()
                self.lista_cantidades = []
                self.lista_productos_individuales = []
                self.lista_productos_totales = []
                self.lista_ventas = []

                for i in productos:
                    articulos = i.split(",")
                    if articulos[0] == "Total":
                        count += 1
                        self.lista_cantidades.append(float(articulos[1]))
                        self.lista_ventas.append("Venta " + str(count) + "= " + articulos[1])
                    else:
                        self.lista_productos_totales.append(articulos[0])  # todos los articulos

                        if articulos[0] not in self.lista_productos_individuales:
                            self.lista_productos_individuales.append(articulos[0])  # articulos individuales vendidos

                suma = 0
                maximo = 0
                articulo_mas_vendido = ""
                self.lista_cantidades_productos = []
                for i in self.lista_productos_individuales:
                    for j in productos:
                        articulos = j.split(",")
                        if i == articulos[0]:
                            suma += int(articulos[2])
                    self.lista_cantidades_productos.append(suma)
                    if suma > maximo:
                        maximo = suma
                        suma = 0
                        articulo_mas_vendido = i
                    else:
                        suma = 0


                self.label_articulos_mas_vendido_num.setText(articulo_mas_vendido)
                self.label_articulos_totales_num.setText(str(len(self.lista_productos_totales)))
                self.label_articulos_individuales_num.setText(str(len(self.lista_productos_individuales)))
                self.label_venta_dia_num.setText(str(sum(self.lista_cantidades)))
                self.label_venta_mayor_num.setText(str(max(self.lista_cantidades)))
                self.label_numero_de_ventas_num.setText(str(count))
        except:
            self.grupo_reporte.setVisible(False)
            self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("No hay reportes este día", self.mensaje_notifica)
            self.mensaje_notifica.exec_()


    def leer_item(self, row, column, tabla):
        if tabla.item(row, column) != None:
            return tabla.item(row, column).text().strip()
        else:
            return ""

    def funcion_pagar(self):
        if self.tabla_carrito.rowCount() > 0:
            now = datetime.now()
            dia = str(now.day)
            mes = str(now.month)
            year = str(now.year)
            r = self.tabla_carrito.rowCount()
            c = self.tabla_carrito.columnCount()
            articulos = []
            with open(f"archivos/reporte_{dia + '_' + mes + '_' + '_' + year}.csv", "+a") as data:
                for i in range(r):
                    for j in range(c):
                        articulos.append(self.leer_item(i, j, self.tabla_carrito))
                    data.writelines(articulos[0] + "," + articulos[1] + "," + articulos[2])
                    data.writelines("\n")
                    articulos = []
                data.writelines("Total," + str(sum(self.lista_precios)) + "," + "\n")
                self.lista_compras = []
                self.generar_reporte()
                self.funcion_abrir_carrito()

    def funcion_abrir_carrito(self):
        self.grupo_carrito_compras.setVisible(True)
        size = len(self.lista_compras)
        self.lista_precios = []
        self.tabla_carrito.setRowCount(size)
        if size > 0:
            self.tabla_carrito.setVisible(True)
            self.label_mensaje.setVisible(False)
            for i in range(size):
                articulos = self.lista_compras[i].split(",")
                self.poblar_tabla(i, 0, articulos[0], self.tabla_carrito)
                self.poblar_tabla(i, 1, articulos[1], self.tabla_carrito)
                self.poblar_tabla(i, 2, articulos[2], self.tabla_carrito)
                self.lista_precios.append(float(articulos[1].strip()) * int(articulos[2].strip()))
            self.tabla_carrito.resizeColumnsToContents()

            self.label_total.setText("Total = " + str(sum(self.lista_precios)))
            self.tabla_carrito.selectRow(size - 1)
        else:
            self.label_conteo_carrito.setText("")
            self.label_total.setText("Total = 0")
            self.tabla_carrito.setVisible(False)
            self.label_mensaje.setVisible(True)
            self.label_mensaje.setText("El carrito esta vacio")

    def funcion_cerrar_carrito(self):
        self.grupo_carrito_compras.setVisible(False)

    def funcion_agrega_a_carrito(self):
        if self.spinbox_cantidad.value() != 0 and self.label_producto.text() != "":
            for ind, i in enumerate(self.lista_compras):
                articulos = i.split(",")
                if self.label_producto.text() in articulos[0]:
                    self.lista_compras[ind] = self.label_producto.text() + "," + self.label_precio_unitario.text()[
                                                                                 17:] + "," + str(int(articulos[2]) + 1)
                    self.spinbox_cantidad.setValue(1)
                    self.edit_buscar_producto.setFocus()
                    self.funcion_abrir_carrito()
                    self.tabla_carrito.selectRow(ind)
                    return
            self.lista_compras.append(
                self.label_producto.text() + "," + self.label_precio_unitario.text()[17:] + "," + str(
                    self.spinbox_cantidad.value()))

            if self.label_conteo_carrito.text().isnumeric():
                self.label_conteo_carrito.setText(str(int(self.label_conteo_carrito.text()) + 1))
            else:
                self.label_conteo_carrito.setText("1")
            self.spinbox_cantidad.setValue(1)
            self.edit_buscar_producto.setFocus()
            self.funcion_abrir_carrito()

    def acomodar_botones(self, numero_boton):
        initx = 50
        inity = 100
        diametro = 250
        sepx = 10
        sepy = 10
        return initx + numero_boton * (diametro + sepx)

    def funcion_acerca_de(self):
        if self.grupo_acerca_de.isVisible():
            self.grupo_acerca_de.setVisible(False)
        else:
            self.grupo_acerca_de.setVisible(True)

    def funcion_elimina_seccion(self):
        flag = False
        with open("archivos/articulos.csv", "r") as data:
            productos = data.readlines()
            productos_copia = productos

            for ind, i in enumerate(productos):
                articulos = i.split(",")

                if articulos[0].strip() == self.combobox_secciones.currentText():
                    run = True
                    indice = ind
                    while run:
                        productos_copia.pop(indice)
                        articulos = productos_copia[indice].split(",")
                        if articulos[0].strip() == '|':
                            productos_copia.pop(indice)
                            run = False
                            flag = True
                if flag:
                    break

        if flag:
            with open("archivos/articulos.csv", "w") as data:
                data.writelines(productos_copia)

        flag = False
        with open("archivos/Productos principales.csv", "r") as data:
            productos = data.readlines()
            for ind, i in enumerate(productos):
                if i.strip() == self.combobox_secciones.currentText():
                    productos.pop(ind)
                    flag = True
                    break
        if flag:
            with open("archivos/Productos principales.csv", "w") as data:
                data.writelines(productos)
            self.listar_secciones()
            self.crear_contenido()

    def funcion_eliminar(self):
        if self.label_titulo_agrega_inventario.text() == "Elimina producto":
            flag = False
            with open("archivos/articulos.csv", "r") as data:
                productos = data.readlines()
                for ind, i in enumerate(productos):
                    articulos = i.split(",")
                    if articulos[0].strip() == self.combobox_productos.currentText():
                        productos.pop(ind)
                        flag = True
                        break
            if flag:
                with open("archivos/articulos.csv", "w") as data:
                    data.writelines(productos)
                self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
                self.crear_mensaje(f"Se elimino artículo: {self.combobox_productos.currentText()} ", self.mensaje_notifica)
                self.mensaje_notifica.exec_()
                self.listar_productos()
        elif self.label_titulo_agrega_inventario.text() == "Elimina sección":
            self.funcion_elimina_seccion()

    def funcion_generar(self):

        if self.label_titulo_agrega_inventario.text() == "Agrega sección":
            with open("archivos/Productos principales.csv", "a") as data:
                data.writelines(self.edit_titulo.text())
                data.writelines("\n")
            self.crear_contenido()
            self.mensaje_guarda.exec_()
            self.edit_titulo.clear()
            self.edit_precio.clear()
            self.edit_titulo.setFocus()
        elif self.label_titulo_agrega_inventario.text() == "Agrega producto":
            flag = False
            with open("archivos/articulos.csv", "r") as data:
                productos = data.readlines()
                for ind, i in enumerate(productos):
                    articulo = i.split(",")
                    if articulo[0].strip() == self.combobox_secciones.currentText().strip():
                        flag = True
                        continue
                    if flag:
                        if articulo[0].strip() == "|":
                            productos.insert(ind, self.edit_titulo.text() + "," + self.edit_precio.text() + "\n")
                            break
                    if ind == len(productos) - 1:
                        productos.append(self.combobox_secciones.currentText().strip() + "," + "" + "\n")
                        productos.append(self.edit_titulo.text() + "," + self.edit_precio.text() + "\n")
                        productos.append("|" + "," + "" + "\n")
                        break

            with open("archivos/articulos.csv", "w") as data:
                data.writelines(productos)
                self.mensaje_guarda.exec_()
                self.edit_titulo.clear()
                self.edit_precio.clear()
                self.edit_titulo.setFocus()

    def funcion_modifica_boton(self):
        self.boton_previo.setText(self.edit_titulo.text())
        self.coloca_icono(self.edit_titulo.text(), self.boton_previo)
        self.label_imagen_previa.setPixmap(QtGui.QPixmap(f'imagenes/{self.edit_titulo.text()}' + '.jpg'))
        self.label_descripcion_previo.setText(self.edit_titulo.text())

    def modifica_label(self):
        self.label_precio_previo.setText("Precio Unitario: " + self.edit_precio.text())

    def listar_productos(self):
        self.combobox_productos.clear()
        with open("archivos/articulos.csv", "r") as data:
            productos = data.readlines()
            flag = False
            for i in productos:
                articulos = i.split(",")
                if articulos[0].strip() == self.combobox_secciones.currentText():
                    flag = True
                    continue
                if flag:
                    if articulos[0].strip() == "|":
                        break
                    else:
                        self.combobox_productos.addItem(articulos[0].strip())

    def listar_secciones(self):
        self.combobox_secciones.clear()
        with open("archivos/Productos principales.csv", "r") as data:
            secciones = data.readlines()
            for ind, i in enumerate(secciones):
                secciones[ind] = i.strip()
        self.combobox_secciones.addItems(secciones)

    def funcion_habilita_seccion(self):
        sender = self.sender()
        if sender.text() == "Agrega sección":
            self.label_titulo_agrega_inventario.setText("Agrega sección")
            self.combobox_secciones.setVisible(False)
            self.combobox_productos.setVisible(False)
            self.edit_precio.setVisible(False)
            self.boton_generar.setVisible(True)
            self.boton_modifica.setVisible(False)
            self.boton_previo.setVisible(True)
            self.label_precio_previo.setVisible(False)
            self.label_descripcion_previo.setVisible(False)
            self.edit_titulo.setVisible(True)
            self.label_modifica.setVisible(False)
            self.boton_eliminar.setVisible(False)
            self.edit_titulo.clear()
            self.edit_titulo.setFocus()

        elif sender.text() == "Agrega producto":
            self.label_titulo_agrega_inventario.setText("Agrega producto")
            self.edit_precio.setVisible(True)
            self.combobox_secciones.setVisible(True)
            self.boton_generar.setVisible(True)
            self.combobox_productos.setVisible(False)
            self.edit_titulo.setVisible(True)
            self.boton_modifica.setVisible(False)
            self.boton_previo.setVisible(False)
            self.label_precio_previo.setVisible(True)
            self.label_descripcion_previo.setVisible(True)
            self.boton_eliminar.setVisible(False)
            self.label_modifica.setVisible(False)
            self.edit_titulo.clear()
            self.edit_titulo.setFocus()
            self.listar_secciones()
        elif sender.text() == "Elimina producto":
            self.label_titulo_agrega_inventario.setText("Elimina producto")
            self.boton_generar.setVisible(False)
            self.combobox_secciones.setVisible(True)
            self.combobox_productos.setVisible(True)
            self.boton_eliminar.setVisible(True)
            self.label_modifica.setVisible(False)
            self.combobox_productos.clear()
            self.edit_titulo.setVisible(False)
            self.boton_modifica.setVisible(False)
            self.edit_precio.setVisible(False)
            self.boton_previo.setVisible(False)
            self.label_precio_previo.setVisible(False)
            self.label_descripcion_previo.setVisible(False)
            self.listar_secciones()
            self.listar_productos()
        elif sender.text() == "Elimina sección":
            self.label_titulo_agrega_inventario.setText("Elimina sección")
            self.combobox_secciones.setVisible(True)
            self.combobox_productos.setVisible(False)
            self.boton_generar.setVisible(False)
            self.boton_eliminar.setVisible(True)
            self.edit_titulo.setVisible(False)
            self.boton_modifica.setVisible(False)
            self.edit_precio.setVisible(False)
            self.label_modifica.setVisible(False)
            self.boton_previo.setVisible(False)
            self.label_precio_previo.setVisible(False)
            self.label_descripcion_previo.setVisible(False)
            self.listar_secciones()
        elif sender.text() == "Modifica producto":
            self.label_titulo_agrega_inventario.setText("Modifica producto")
            self.boton_modifica.setVisible(True)
            self.boton_generar.setVisible(False)
            self.combobox_secciones.setVisible(True)
            self.combobox_productos.setVisible(True)
            self.boton_eliminar.setVisible(False)
            self.label_precio_previo.setVisible(True)
            self.label_descripcion_previo.setVisible(True)
            self.combobox_productos.clear()
            self.label_modifica.setVisible(True)
            self.edit_titulo.setVisible(True)
            self.edit_precio.setVisible(True)
            self.boton_previo.setVisible(False)
            self.edit_titulo.setFocus()
            self.listar_secciones()
            self.listar_productos()
            self.edit_titulo.setText(self.combobox_productos.currentText())

    def coloca_titulo_y_precio(self):
        self.edit_titulo.setText(self.combobox_productos.currentText())
        self.edit_titulo.setFocus()

    def acomodar_menu(self, numero_boton):
        S_menu = 0
        H_menu = 61
        INICIOy = 80
        return INICIOy + numero_boton * (H_menu + S_menu)

    def crear_objetos(self, nombre_objeto, localizacion):
        nombre_objeto = QtWidgets.QGroupBox(localizacion)
        nombre_objeto_label = str(nombre_objeto) + "_label"
        nombre_objeto_label = QtWidgets.QLabel(nombre_objeto)
        nombre_objeto_label_1 = str(nombre_objeto) + "_boton"
        nombre_objeto_label_1 = QtWidgets.QLabel(nombre_objeto)
        return nombre_objeto, nombre_objeto_label, nombre_objeto_label_1

    def leer_planillas(self, nombre_tabla):
        with open('archivos/planillas.csv', mode='r', encoding="windows-1252") as Data:  # lee el archivo planillas.cvs
            list1 = Data.readlines()  # crea una lista con los datos en Data
            r = 0
            for i in list1:
                palabras = i.split(",")
                self.poblar_tabla(r, 0, palabras[0].strip(), nombre_tabla)
                self.poblar_tabla(r, 1, palabras[1].strip(), nombre_tabla)
                r += 1
            nombre_tabla.resizeColumnsToContents()

    def leer_archivo(self, nombre_tabla, archivo):
        with open(f'archivos/{archivo}.csv', mode='r', encoding="windows-1252") as Data:  # lee el archivo planillas.cvs
            list1 = Data.readlines()  # crea una lista con los datos en Data
            r = 0
            for i in list1:
                palabras = i.split(",")
                self.poblar_tabla(r, 0, palabras[0].strip(), nombre_tabla)
                self.poblar_tabla(r, 1, palabras[1].strip(), nombre_tabla)
                r += 1
            nombre_tabla.resizeColumnsToContents()

    def buscar_planillas(self):
        texto = self.edit_buscar_planillas.text()
        texto = texto.strip()
        count = 0
        j = 0
        self.tabla_planillas_filtro.clearContents()
        with open("archivos/planillas.csv", mode="r") as Data:
            list = Data.readlines()
            for i in list:
                palabras = i.split(",")
                palabras_i = palabras[1].split(" ")
                size = len(texto)
                if size > 0:
                    if palabras[1][0:size].lower().strip() == texto.lower().strip():
                        self.poblar_tabla(j, 0, palabras[0].strip(), self.tabla_planillas_filtro)
                        self.poblar_tabla(j, 1, palabras[1].strip(), self.tabla_planillas_filtro)
                        j += 1
                        count += 1
                        continue
                    for k in palabras_i:
                        if k[0:size].lower().strip() == texto.lower().strip():
                            self.poblar_tabla(j, 0, palabras[0].strip(), self.tabla_planillas_filtro)
                            self.poblar_tabla(j, 1, palabras[1].strip(), self.tabla_planillas_filtro)
                            j += 1
                            count += 1
                            break
                self.cuenta_label.setText("Cantidad encontrada: " + str(count))

    def buscar_en_archivo(self, archivo, tabla, edit, label):
        texto = edit.text()
        texto = texto.strip()
        count = 0
        j = 0
        tabla.clearContents()
        with open(f"archivos/{archivo}.csv", mode="r") as Data:
            list = Data.readlines()
            for i in list:
                palabras = i.split(",")
                palabras_i = palabras[1].split(" ")
                size = len(texto)
                if size > 0:
                    if palabras[1][0:size].lower().strip() == texto.lower().strip():
                        self.poblar_tabla(j, 0, palabras[0].strip(), tabla)
                        self.poblar_tabla(j, 1, palabras[1].strip(), tabla)
                        j += 1
                        count += 1
                        continue
                    for k in palabras_i:
                        if k[0:size].lower().strip() == texto.lower().strip():
                            self.poblar_tabla(j, 0, palabras[0].strip(), tabla)
                            self.poblar_tabla(j, 1, palabras[1].strip(), tabla)

                            j += 1
                            count += 1
                            break
            label.setText("Cantidad encontrada: " + str(count))

    def cambiar_color(self, boton_menu):
        boton_menu.setStyleSheet("background-color: white")

    def abonar(self, row):
        debe = 0
        if row.isnumeric() and self.edit_abonar.text().isnumeric():
            row = int(row) - 1
            with open('archivos/deudores.csv', 'r') as Data:
                palabras = Data.readlines()  # palabras es una lista de strings
                size = len(palabras)
                if row < size:
                    lista = palabras[row].split(
                        ",")  # lista es una lista  de las palabras ubicadas en row(separadas con una coma)
                    debe = float(lista[1])  # Extrae el valor de la deuda
                    debe = debe - float(self.edit_abonar.text())
                    lista[1] = str(debe)
                    palabras[row] = ",".join(lista)

            if debe <= 0:
                self.eliminar_deudor(str(row + 1))
            else:
                with open('archivos/deudores.csv', 'w') as archivo:
                    archivo.writelines(palabras)
                self.tabla_deudores.clearContents()
                self.leer_deudores(self.tabla_deudores)

    def eliminar_deudor(self, row):
        if row.isnumeric():
            row = int(row) - 1
            with open('archivos/deudores.csv', 'r') as data:
                palabras = data.readlines()
                size = len(palabras)
                if row < size:
                    palabras.pop(row)

            with open('archivos/deudores.csv', 'w') as archivo:
                archivo.writelines(palabras)

            self.tabla_deudores.clearContents()
            self.leer_deudores(self.tabla_deudores)

    def funcion_seleccion(self):
        row = self.tabla_busqueda.currentRow()

        imagen = self.tabla_busqueda.item(row, 0)
        if imagen != None:
            imagen = self.tabla_busqueda.item(row, 0).text().strip()
            self.label_imagen_producto.setPixmap(QtGui.QPixmap(f"imagenes/{imagen}.jpg"))
            self.label_precio_unitario.setText("Precio Unitario: " + self.tabla_busqueda.item(row, 1).text().strip())
            self.label_producto.setText(imagen)

    def leer_precios(self):
        with open("archivos/articulos.csv", "r") as data:
            productos = data.readlines()
            texto = self.edit_buscar_producto.text().lower().strip()
            size = len(texto)
            self.tabla_busqueda.clearContents()
            j = 0
            count = 0
            for i in productos:
                articulos = i.split(",")
                articulos_i = articulos[0].split(" ")

                if size > 0:
                    if articulos[0][:size].lower().strip() == texto and articulos[1] != "\n":

                        self.poblar_tabla(j, 0, articulos[0].strip(), self.tabla_busqueda)
                        self.poblar_tabla(j, 1, articulos[1].strip(), self.tabla_busqueda)
                        j += 1
                        count += 1
                        continue
                    elif articulos[1] != "\n":
                        for k in articulos_i:
                            if k[0:size].lower().strip() == texto.lower().strip():
                                self.poblar_tabla(j, 0, articulos[0].strip(), self.tabla_busqueda)
                                self.poblar_tabla(j, 1, articulos[1].strip(), self.tabla_busqueda)
                                j += 1
                                count += 1
                                break
                self.label_count.setText("Cantidad encontrada: " + str(count))
                imagen = self.tabla_busqueda.item(0, 0)
                if imagen != None:
                    imagen = self.tabla_busqueda.item(0, 0).text().strip()
                    self.label_imagen_producto.setPixmap(QtGui.QPixmap(f"imagenes/{imagen}.jpg"))
                    self.label_precio_unitario.setText(
                        "Precio Unitario: " + self.tabla_busqueda.item(0, 1).text().strip())
                    self.label_producto.setText(imagen)
                    self.tabla_busqueda.selectRow(0)

    def add_deudor(self, objeto):
        if self.edit_nombre_deudor.text() != "" and self.edit_debe.text() != "":
            with open('archivos/deudores.csv', mode='a+') as Data:  # crea archivo deudores.cvs (si no existe)
                objeto = objeto + str(self.count)
                objeto = Deudores()                                 # crea objeto deudor
                fecha = time.strftime("%d/%m/%y")                   # obtiene la fecha del sistema
                objeto.crear_deudor(self.edit_nombre_deudor.text(), self.edit_debe.text(), fecha.strip())
                Data.writelines(objeto.nombre + ",")                # escribe en el archivo
                Data.writelines(objeto.deuda + ",")
                Data.writelines(objeto.fecha + "\n")

            self.leer_deudores(self.tabla_deudores)
            self.count += 1
            self.edit_nombre_deudor.clear()
            self.edit_debe.clear()

    def leer_deudores(self, nombre_tabla):
        with open('archivos/deudores.csv', mode='r') as Data:   # lee el archivo planillas.cvs
            list1 = Data.readlines()                            # crea una lista con los datos en Data
            j = 0
            size = len(list1)
            nombre_tabla.setRowCount(size)
            for i in list1:
                palabras = i.split(",")
                count = len(palabras)                           # cuenta la cantidad de datos
                if count == 3:
                    self.poblar_tabla(j, 0, palabras[0].strip(), nombre_tabla)
                    self.poblar_tabla(j, 1, palabras[1].strip(), nombre_tabla)
                    self.poblar_tabla(j, 2, palabras[2].strip(), nombre_tabla)
                    j += 1


    def define_titulo_columna(self, texto):
        item = QtWidgets.QTableWidgetItem()
        item.setText(texto)
        item.setFont(self.set_font())
        return item

    def crear_checkbox(self, x, y, w, h, texto, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setText(texto)

    def crear_tableWidget(self, row_count, column_count, texto, x, y, w, h, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setVisible(True)
        nombre_objeto.setColumnCount(column_count)  # Establece la cantidad de columnas
        nombre_objeto.setRowCount(row_count)  # Establece la cantidad de filas
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setStyleSheet("QTableWidget"
                                    "{"
                                    "gridline-color: gray;"
                                    "selection-background-color: rgb(205,92,92);"
                                    "selection-color: black;"
                                    f"color: black;"
                                    f"background-color : transparent;"
                                    'border-radius: 50px;'
                                    "border-style: none;"
                                    "border-width: 2px;"
                                    "border-color: black"
                                    "}"
                                    "QHeaderView::section"
                                    "{"
                                    "background-color : transparent;"
                                    "border-radius:14px"
                                    "}"
                                    )

    def poblar_tabla(self, row, coloum, text, nombre_tabla):
        item = QtWidgets.QTableWidgetItem()
        item.setText(text)
        nombre_tabla.setItem(row, coloum, item)

    def crear_textedit(self, x, y, w, h, texto, nombre_objeto):
        nombre_objeto_name = str(nombre_objeto) + "_textEdit"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setPlaceholderText(texto)
        nombre_objeto.setObjectName(nombre_objeto_name)
        nombre_objeto.setStyleSheet("border-style: solid; "
                                    "border-width: 0.5px;"
                                    f"background-color: transparent;"
                                    f"color: black"
                                    )

    def crear_lineEdit(self, x, y, w, h, texto, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setPlaceholderText(texto)
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setStyleSheet("border-style: solid; "
                                    "border-width: 0.5px;"
                                    f"background-color: transparent;"
                                    f"color: black"
                                    )

    def crear_spinbox(self, x, y, w, h, ObjectName, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(ObjectName)
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setStyleSheet("border-style: solid; "
                                    "border-width: 0.5px;"
                                    f"background-color: transparent;"
                                    f"color: black"
                                    )

    def crear_scrollarea(self, x, y, w, h, texto, nombre_objeto):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        nombre_objeto.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        nombre_objeto.setWidgetResizable(True)
        nombre_objeto.setVisible(False)

    def crear_groupbox(self, x, y, w, h, texto, nombre_objeto, color="white"):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setVisible(False)
        nombre_objeto.setStyleSheet(f"background-color: {color}; border-style: solid; border-radius: 15px")

    def crear_label(self, x, y, w, h, texto, nombre_objeto, font_color="black", color="transparent", border_radius=10,
                    border_style="none", font_weight="normal"):
        label = texto + "_label"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setText(texto)
        nombre_objeto.setScaledContents(True)
        nombre_objeto.setObjectName(label)
        nombre_objeto.setStyleSheet("QLabel"
                                    "{"
                                    f"color: {font_color};"
                                    f"background-color : {color};"
                                    f'border-radius: {border_radius}px;'
                                    f"border-style: {border_style};"
                                    f"font-weight: {font_weight};"
                                    "border-width: 2px;"
                                    "border-color: black"
                                    "}"
                                    )

    def coloca_icono(self, nombre, nombre_objeto, size=QSize(25, 25)):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"iconos/{nombre}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nombre_objeto.setIcon(icon)
        nombre_objeto.setIconSize(size)

    def crear_combobox(self, x, y, w, h, texto, nombre_objeto, color="transparent", font_color="black"):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setVisible(True)

        nombre_objeto.setFont(self.set_font(12))  # establece el tipo de fuente
        nombre_objeto.setStyleSheet("QComboBox"
                                    "{"
                                    "gridline-color: gray;"
                                    f"color: {font_color};"
                                    f"background-color : {color};"
                                    'border-radius: 15px;'
                                    "border-style: none;"
                                    "border-width: 0.5px;"
                                    "border-color: black"
                                    "}"
                                    )

    def crear_linea(self, x, y, w, h, texto, nombre_objeto, background_color="black"):
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setObjectName(texto)
        nombre_objeto.setFrameShadow(QtWidgets.QFrame.Plain)
        nombre_objeto.setFrameShape(QtWidgets.QFrame.VLine)
        nombre_objeto.setLineWidth(1)
        nombre_objeto.setStyleSheet("QFrame"
                                    "{"
                                    f"background-color: {background_color};"
                                    "}")

    def crear_mensaje(self, texto, nombre_objeto):
        nombre_objeto.setIcon(QtWidgets.QMessageBox.Information)
        nombre_objeto.setText(texto)
        # self.mensaje_guarda.setInformativeText("This is additional information")
        nombre_objeto.setWindowTitle("Gestor de proyectos")
        # self.mensaje_guarda.setDetailedText("The details are as follows:")
        nombre_objeto.setStandardButtons(QtWidgets.QMessageBox.Ok)
        nombre_objeto.setFont(self.set_font())

    def crear_boton(self, x, y, w, h, texto, nombre_objeto, background_color="transparent", border_style="none"):
        boton_nombre = texto + "_boton"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setAutoFillBackground(False)
        nombre_objeto.setObjectName(boton_nombre)
        nombre_objeto.setText(texto)
        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.coloca_icono(texto, nombre_objeto)
        nombre_objeto.setIconSize(QSize(25, 25))
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setStyleSheet("QPushButton"
                                    "{"
                                    "border-radius: 10px;"
                                    f"background-color: {background_color};"
                                    "color: black;"
                                    f"border-style: {border_style};"
                                    "border-width: 0.5px;"
                                    "border-color: black;"
                                    "text-align: center"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "color: white;"
                                    "background-color : rgb(0,80,200);"
                                    "}"
                                    "QPushButton:pressed"
                                    "{"
                                    "background-color : red;"
                                    "}"
                                    )

        nombre_objeto.setVisible(True)

    def crear_boton_menu(self, x, y, w, h, texto, nombre_objeto):
        boton_nombre = texto + "_boton"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, w, h))
        nombre_objeto.setFont(self.set_font())
        nombre_objeto.setAutoFillBackground(False)
        nombre_objeto.setObjectName(boton_nombre)
        nombre_objeto.setText(texto)
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setStyleSheet("QPushButton"
                                    "{"
                                    "border-radius: 10px;"
                                    f"background-color: rgb(26,32,40);"
                                    "color: white;"
                                    "border-style: none;"
                                    "border-width: 0.5px;"
                                    "border-color: black;"
                                    "text-align: left"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "color: white;"
                                    "background-color : rgb(0,80,200);"

                                    "}")
        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        nombre_objeto.setVisible(True)
        self.coloca_icono(texto, nombre_objeto)
        nombre_objeto.setIconSize(QSize(30, 30))

    def crear_boton_redondo(self, x, y, diametro, texto, nombre_objeto, ObjectName, font_color="black",
                            color="transparent", border_style="solid"):
        boton_nombre = texto + "_boton"
        nombre_objeto.setGeometry(QtCore.QRect(x, y, diametro, diametro))
        nombre_objeto.setFont(self.set_font(12))
        nombre_objeto.setAutoFillBackground(True)
        nombre_objeto.setFlat(False)
        nombre_objeto.setObjectName(ObjectName)
        nombre_objeto.setText(texto)
        nombre_objeto.setMouseTracking(True)
        nombre_objeto.setStyleSheet(
            "QPushButton"
            "{"
            f"color: {font_color};"
            f"background-color : {color};"
            f'border-radius: {diametro / 2}px;'
            f"border-style: {border_style};"
            "border-width: 0.5px;"
            "border-color: black"
            "}"
            "QPushButton::hover"
            "{"
            "background-color : rgb(0,80,200);"
            "color : white;"
            f"border-radius: {diametro / 2}px;"
            "}")
        nombre_objeto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        nombre_objeto.setVisible(True)
        self.coloca_icono(texto, nombre_objeto)

    def crear_subcontenido(self, producto):
        sender = self.sender()
        self.grupo_subproductos_0 = QtWidgets.QGroupBox(self.centralwidget)
        self.crear_groupbox(side_menu_width, 0, window_width - side_menu_width, window_height, 'grupo_subproductos_0',
                            self.grupo_subproductos_0)
        self.label_titulo = QtWidgets.QLabel(self.grupo_subproductos_0)
        self.crear_label(5, 5, 300, 40, producto, self.label_titulo)
        self.label_titulo.setFont(self.set_font(18))
        self.boton_atras = QtWidgets.QPushButton(self.grupo_subproductos_0)
        self.crear_boton_redondo(10, 560, 50, "flecha izquierda", self.boton_atras, "boton_atras")
        self.boton_atras.setText("")
        self.boton_atras.setIconSize(QSize(25, 25))
        self.boton_atras.clicked.connect(lambda: self.inventario_add())
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_subproductos_0.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_subproductos_0
        flag = False
        lista_articulos = []
        lista_precios = []
        with open("archivos/articulos.csv", "r") as data:
            productos_principales = data.readlines()
            for i in productos_principales:
                articulo = i.split(",")
                if articulo[0].strip() == producto:
                    flag = True
                    continue
                if flag:
                    if articulo[0].strip() == "|":
                        break
                    else:
                        lista_articulos.append(articulo[0])
                        lista_precios.append(articulo[1])

            size = len(lista_articulos)
        initx = 0
        inity = 50
        separacion_h = 2
        separacion_v = 2
        w = 200
        h = 250
        count = 0
        c = 0
        r = 0

        for i in range(size):
            if initx + (w + separacion_h) * c + w > window_width - side_menu_width:
                r += 1
                c = 0
            if inity + (h + separacion_v) * r + h > window_height:
                r = 0
                count += 1
                exec(f"self.grupo_subproductos_{count} = QtWidgets.QGroupBox(self.centralwidget)")
                exec(
                    f"self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, 'grupo_subproductos_{count}',self.grupo_subproductos_{count})")

                exec(f"self.boton_siguiente_1_{count} = QtWidgets.QPushButton(self.grupo_subproductos_{count - 1})")
                exec(
                    f"self.crear_boton_redondo(window_width - side_menu_width - 60, window_height - 60, 30, 'flecha derecha', self.boton_siguiente_1_{count}, 'boton_siguiente_1_{count}' )")
                exec(f"self.boton_siguiente_1_{count}.setText('')")
                exec(f"self.conectar_boton_siguiente(self.boton_siguiente_1_{count})")

                exec(f"self.boton_atras_1_{count - 1} = QtWidgets.QPushButton(self.grupo_subproductos_{count})")
                exec(
                    f"self.crear_boton_redondo(window_width - side_menu_width - 95, window_height - 60, 30, 'flecha izquierda', self.boton_atras_1_{count - 1}, 'boton_atras_1_{count - 1}' )")
                exec(f"self.boton_atras_1_{count - 1}.setText('')")
                exec(f"self.conectar_boton_atras(self.boton_atras_1_{count - 1})")

            exec(f"self.grupo_subproducto_{i} = QtWidgets.QGroupBox(self.grupo_subproductos_{count})")
            exec(f"self.label_imagen_subproducto_{i} = QtWidgets.QLabel(self.grupo_subproducto_{i})")
            exec(f"self.label_subproducto_{i} = QtWidgets.QLabel(self.grupo_subproducto_{i})")
            exec(f"self.label_subproducto_{i}_1 = QtWidgets.QLabel(self.grupo_subproducto_{i})")

            exec(
                f"self.crear_groupbox(initx + (w + separacion_h)*c, inity + (h + separacion_v)*r, w, h, 'grupo', self.grupo_subproducto_{i})")
            texto = lista_articulos[i].strip() + '\n' + lista_precios[i].strip()

            exec(f"self.crear_label(0, 0, w, h - 60, '', self.label_imagen_subproducto_{i})")
            exec(f"self.crear_label(0, h-60, w, 30, '{lista_articulos[i].strip()}', self.label_subproducto_{i})")
            exec(
                f"self.crear_label(0, h-30, w, 30, 'Precio unitario: {lista_precios[i].strip()}', self.label_subproducto_{i}_1)")
            exec(f"self.grupo_subproducto_{i}.setVisible(True)")
            exec(
                f"self.label_imagen_subproducto_{i}.setPixmap(QtGui.QPixmap(f'imagenes/{lista_articulos[i].strip()}' + '.jpg'))")
            c += 1

    def crear_contenido(self):
        with open("archivos/Productos principales.csv", "r") as data:
            productos_principales = data.readlines()

            size = len(productos_principales)
        initx = 0
        inity = 10
        separacion_h = 0
        separacion_v = 0
        w = 155
        h = 190
        count = 0
        r = 0
        c = 0

        for i in range(size):

            if initx + (w + separacion_h) * c + w > window_width - side_menu_width:
                r += 1
                c = 0
            if inity + (h + separacion_v) * r + h > window_height:
                r = 0
                count += 1
                exec(f"self.grupo_inventario_{count} = QtWidgets.QGroupBox(self.centralwidget)")
                exec(
                    f"self.crear_groupbox(180, 0, window_width - side_menu_width, window_height, 'grupo_inventario_{count}',self.grupo_inventario_{count})")

                exec(f"self.boton_siguiente_{count} = QtWidgets.QPushButton(self.grupo_inventario_{count - 1})")
                exec(
                    f"self.crear_boton_redondo(window_width - side_menu_width - 60, window_height - 60, 30, 'flecha derecha', self.boton_siguiente_{count} , 'boton_siguiente_{count}')")
                exec(f"self.boton_siguiente_{count}.setText('')")
                exec(f"self.conectar_boton_siguiente(self.boton_siguiente_{count})")

                exec(f"self.boton_atras_{count - 1} = QtWidgets.QPushButton(self.grupo_inventario_{count})")
                exec(
                    f"self.crear_boton_redondo(window_width - side_menu_width - 95, window_height - 60, 30, 'flecha izquierda', self.boton_atras_{count - 1}, 'boton_atras_{count - 1}' )")
                exec(f"self.boton_atras_{count - 1}.setText('')")
                exec(f"self.conectar_boton_atras(self.boton_atras_{count - 1})")

            exec(f"self.grupo_producto_{i} = QtWidgets.QGroupBox(self.grupo_inventario_{count})")
            exec(f"self.boton_producto_{i} = QtWidgets.QPushButton(self.grupo_producto_{i})")
            exec(f"self.label_imagen_producto_{i} = QtWidgets.QLabel(self.grupo_producto_{i})")
            exec(f"self.conectar(self.boton_producto_{i}, '{productos_principales[i].strip()}')")

            exec(
                f"self.crear_groupbox(initx + (w + separacion_h)*c, inity + (h + separacion_v)*r, w, h, 'grupo', self.grupo_producto_{i})")
            exec(f"self.crear_boton(0, h - 31, w, 31, '{productos_principales[i].strip()}', self.boton_producto_{i})")
            exec(f"self.crear_label(0, 0, w, h - 30, '', self.label_imagen_producto_{i})")
            exec(f"self.grupo_producto_{i}.setVisible(True)")
            exec(
                f"self.label_imagen_producto_{i}.setPixmap(QtGui.QPixmap(f'imagenes/{productos_principales[i].strip()}' + '.jpg'))")
            c += 1

    def conectar_boton_atras(self, nombre_objeto):
        nombre_objeto.clicked.connect(lambda: self.funcion_atras())

    def conectar_boton_siguiente(self, nombre_objeto):
        nombre_objeto.clicked.connect(lambda: self.funcion_siguiente())

    def conectar(self, nombre_objeto, producto):
        nombre_objeto.clicked.connect(lambda: self.crear_subcontenido(producto))

    def funcion_siguiente(self):
        sender = self.sender()
        self.ultimo_grupo_visible.setVisible(False)
        if sender.objectName()[:-2] == "boton_siguiente":
            for i in range(10):
                if sender.objectName() == f"boton_siguiente_{i}":
                    exec(f"self.grupo_inventario_{i}.setVisible(True)")
                    exec(f"self.ultimo_grupo_visible = self.grupo_inventario_{i}")
                    break
        elif sender.objectName()[:-2] == "boton_siguiente_1":
            for i in range(10):
                if sender.objectName() == f"boton_siguiente_1_{i}":
                    exec(f"self.grupo_subproductos_{i}.setVisible(True)")
                    exec(f"self.ultimo_grupo_visible = self.grupo_subproductos_{i}")
                    break

    def funcion_atras(self):
        sender = self.sender()
        self.ultimo_grupo_visible.setVisible(False)
        if sender.objectName()[:-2] == "boton_atras":
            for i in range(10):
                if sender.objectName() == f"boton_atras_{i}":
                    exec(f"self.grupo_inventario_{i}.setVisible(True)")
                    exec(f"self.ultimo_grupo_visible = self.grupo_inventario_{i}")
                    break
        elif sender.objectName()[:-2] == "boton_atras_1":
            for i in range(10):
                if sender.objectName() == f"boton_atras_1_{i}":
                    exec(f"self.grupo_subproductos_{i}.setVisible(True)")
                    exec(f"self.ultimo_grupo_visible = self.grupo_subproductos_{i}")
                    break

    def set_font(self, font_size=12):
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(font_size)
        return font

    def separa_lista(self, lista):
        string = ""
        self.string_list = []
        count = len(lista)
        if count != 0:
            for i in (lista):  # Recorre el string
                count -= 1
                if i == ",":  # Si encuentra una coma...
                    self.string_list.append(string)  # coloca el string en la lista
                    string = ""  # Reinicia la variable
                elif count == 0:  # Si encuentra un salto de linea...
                    self.string_list.append(string)
                    return self.string_list  # Devuelve la lista
                else:
                    string = string + i  # concatena la letra

    def funcion_agrega_inventario(self):
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_agrega_inventario.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_agrega_inventario
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_inicio)
        self.ultimo_label_menu = self.label_menu_inicio

    def inicio(self):
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_inicio.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_inicio
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_inicio)
        self.ultimo_label_menu = self.label_menu_inicio

    def regresa_color(self, boton_menu):
        boton_menu.setStyleSheet("background-color: black")

    def inventario_add(self):
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_inventario_0.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_inventario_0
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_inventario)
        self.ultimo_label_menu = self.label_menu_inventario

    def buscar_producto(self):
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_buscar_producto.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_buscar_producto
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_buscar)
        self.ultimo_label_menu = self.label_menu_buscar

    def planillas_funcion(self):
        self.leer_planillas(self.tabla_planillas)
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_planillas.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_planillas
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_planillas)
        self.ultimo_label_menu = self.label_menu_planillas

    def biografias_funcion(self):
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_biografias.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_biografias
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_biografias)
        self.ultimo_label_menu = self.label_menu_biografias

    def deudores_funcion(self):
        self.leer_deudores(self.tabla_deudores)
        self.ultimo_grupo_visible.setVisible(False)
        self.grupo_deudores.setVisible(True)
        self.ultimo_grupo_visible = self.grupo_deudores
        self.regresa_color(self.ultimo_label_menu)
        self.cambiar_color(self.label_menu_deudores)
        self.ultimo_label_menu = self.label_menu_deudores

    def recargas_funcion(self):
        import webbrowser
        webbrowser.open("https://eventamovil.mx/login/", new=2, autoraise=True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setStyleSheet("background-color: white; border-radius: 10px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(_translate("MainWindow", "Administración de productos"))
        MainWindow.setFont(self.set_font())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    boton1 = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
