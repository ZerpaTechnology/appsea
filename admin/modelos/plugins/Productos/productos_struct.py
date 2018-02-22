db=DB()
#============================================
#TABLA de opciones
db("Opciones").campo("Nombre",db.str)
db("Opciones").campo("Valores",db.list)
db("Opciones").insertar("Becas",["Empresarial","Política","Preparaduria","Trabajo"])
#=============================================
db("Plantillas").campo("Nombre",db.str)
db("Plantillas").campo("Contenido",db.list)
db("Plantillas").campo("args",db.dict)
db("Plantillas").campo("Fecha",db.str)
db("Plantillas").campo("Status",db.list)
#============================================
db("Productos").campo("Nombre",db.str)
db("Productos").campo("Contenido",db.list)
db("Productos").campo("args",db.dict)
db("Productos").campo("Fecha",db.str)
db("Productos").campo("Status",db.list)

#--------------------------------------------
db("Plantillas").insertar("Productos",[
	[{"Nombre":"titulo","name":"titulo","value":"zapatos nike"}],
	[
	{"Vista previa":"SelecImage","value":0,"name":"familia","opciones":"archivos"},
	{"Familia":"text","value":"Moda de hombre","name":"familia"},# Moda hombre, Moda Mujeres, Moda niños
	{"Categorias":"Dict","value":{},"name":"categoria"},# Ropa | Color #{'Ropa':'pantalones','Color':'azul'}
	
	
	]
	],
	{"Plantilla":0},
	zu.DateTime(),
	[]
	)

db("Productos").insertar("zapatos nike",[
	[{"Nombre":"text-titulo","name":"titulo","value":""}],
	[
	{"Vista previa":"SelecImage","value":0,"name":"familia","opciones":"archivos"},
	{"Familia":"text","value":"Moda de hombre","name":"familia"},# Moda hombre, Moda Mujeres, Moda niños
	{"Categorias":"Dict","value":{},"name":"categoria"},# Ropa | Color #{'Ropa':'pantalones','Color':'azul'}
	]
	],
	{"Producto":0},
	zu.DateTime(),
	[]
	)


