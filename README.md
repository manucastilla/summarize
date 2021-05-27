# Summarize
## Nicolas Stegmann e Manuela Castilla

Para este trabalho foi implementado um summarizador de documento. Para isso fizemos a sumarização de extração. Ou seja a partir de um documento é extraído trechos importantes.
Para a sumarização foi utilizado LSA (*Latent Semantic Analysys*). A partir dele para selecionar que tipo de frase seria selecionada, foi escolhido o método *cross method*.

Tudo está no documento `summarize.py`. Para rodar apenas é necessário nodar o seguinte comando no terminal:
`python summarize.py texto sentencas conceitos`
Onde o `texto` será o texto que deseja fazer o summarize, `sentencas` é o número de setenças que quer resumir e por fim `conceitos` é o número de conceitos que deseja usar.

