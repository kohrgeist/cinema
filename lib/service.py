from repository import SessaoRepository

class SessaoService:
    def __init__(self):
        self.repo = SessaoRepository()

    def listar_catalogo(self):
        dados = self.repo.buscar_todas()
        return [
            {"id": d[0], "filme": d[1], "data_hora": d[2], "vagas": d[3]}
            for d in dados
        ]
        
    def comprar_ingresso(self, sessao_id):
        return self.repo.deduzir_ingresso(sessao_id)