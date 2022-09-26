from email import message
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from calcula_media import media_aritmetica, media_ponderada


class Media(BoxLayout):
    aritmetica = ObjectProperty(None)
    ponderada = ObjectProperty(None)

    def calcular_media(self):
        nota1 = int(self.ids.nota1.text)
        nota2 = int(self.ids.nota2.text)

        if self.aritmetica.active:
            resultado = self.media_aritmetica(nota1, nota2)
        if self.ponderada.active:
            resultado = self.media_ponderada(nota1, nota2)

        if (resultado >= 60):
            mensagem = 'Aprovado'
        elif (resultado < 30):
            mensagem = 'Reprovado'
        else:
            mensagem = 'Recuperação'

        resultado_completo = f'Sua média: {resultado} - {mensagem}'

        self.ids.lbResultado.text = str(resultado_completo)

    def media_aritmetica(self, prova1, prova2) -> int:
        return int((prova1 + prova2) / 2)

    def media_ponderada(self, prova1, prova2) -> int:
        return int((prova1 * 2 + prova2 * 4) / 6)


class Main(App):
    def build(self):
        return Media()


if __name__ == '__main__':
    Main().run()
