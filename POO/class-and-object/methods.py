class Celular:
    # method __init__ -> Metodo especial -> Sirve para hacer referencia al constructor.
    # self -> Para hacer referencia a la misma clase o así mismo.
    # (self) -> No se pasa como parametro, pero es obligatorio en los methods para
    # que python interprete a que clase se hace referencia.
    def __init__(self, mark, model, camera):
        self.mark = mark
        self.model = model
        self.camera = camera
    # method -> son metodos que nos sirven para realizar acciones y hacen referencia a
    # a una func de una clase.
    def call(self):
        print(f"{self.mark}: calling...")
    
    def finish_call(self):
        print(f"{self.mark}: I finish the call.")


cel1 = Celular("Samsung", "S23", "48MP")

cel1.call()
cel1.finish_call()