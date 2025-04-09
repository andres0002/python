class Celular:
    # attributes static.
    # mark = "Samsung"
    # model = "S23"
    # camera = "48MP"
    
    # __init__ -> Es la palabra clave para referirce al constructor de la clase y
    # es el method que se ejecuta una ves se instancia la clase.
    # self -> Para hacer referencia a la misma clase o así mismo.
    # (self) -> No se pasa como parametro, pero es obligatorio en los methods para
    # que python interprete a que clase se hace referencia.
    # (mark, model, camera) -> Parametros a pasar a la calse o attributes de instancia.
    def __init__(self, mark, model, camera):
        # attributes dinamics.
        self.mark = mark
        self.model = model
        self.camera = camera

cel1 = Celular("Samsung", "S23", "48MP")
cel2 = Celular("Apple", "Iphone 15 Pro", "35MP")

print(f"Mark: {cel1.mark}, model: {cel1.model}, camera: {cel1.camera}.")
print(f"Mark: {cel2.mark}, model: {cel2.model}, camera: {cel2.camera}.")