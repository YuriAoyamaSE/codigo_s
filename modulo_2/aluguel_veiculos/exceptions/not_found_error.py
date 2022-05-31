from src.exceptions.base_aluguel_error import BaseAluguelError


class NotFoundError(BaseAluguelError):
    
    def __init__(self, *args: object) -> None:
        self.mensagem = args[0]
        super().__init__(*args)
