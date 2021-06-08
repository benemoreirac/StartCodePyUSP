import ordenador
import pytest

class TestaOrdendaor:
    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = ContaTempos()
        return c.lista_quase_ordenado(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len9(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenado(l_aleat)
