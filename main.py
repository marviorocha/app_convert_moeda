from kivy.app import App
from kivy.lang import Builder
import requests
GUI = Builder.load_file("screen.kv")

class MeuApplicativo(App):
    def build(self):
      return GUI
    def on_start(self):

        self.root.ids["item1"].text = f"{self.pegar_cotacao('USD')}"
        self.root.ids["item2"].text = f"{self.pegar_cotacao('CAD')}"
        self.root.ids["item3"].text = f"{self.pegar_cotacao('EUR')}"
        self.root.ids["item4"].text = f"{self.pegar_cotacao('JPY')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao_name = dic_requisicao[f"{moeda}BRL"]['name']
        cotacao_price = dic_requisicao[f"{moeda}BRL"]['bid']
        cotacao = f"{cotacao_name} - {cotacao_price}"

        return cotacao

MeuApplicativo().run()