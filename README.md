<h2>Equipe Perseus</h2>

<table>
<tr><th>Nome</th><th>RA</th></tr>
<tr><th>Victor Codonho</th><th>1700715</th></tr>
<tr><th>Emerson Carbonaro</th><th>1700190</th></tr>
<tr><th>Gabriela Conde</th><th>1700654</th></tr>
<tr><th>Victor Souza</th><th>1700768</th></tr>
<tr><th>Gabriel Leal</th><th>17006602</th></tr>
</table>

<h3>Regras Gerais</h3>

* Olhar o Trello pelo menos uma vez ao dia.
* Reunião do Projeto todas as terças (tente não faltar).
* Dificuldade em alguma coisa, avise o quanto antes para não virar bola de neve.

<h2>Padronização Arquivos</h2>

<h3>Static</h3>

* static/css/arquivo.css
* static/css/imgs/arquivo.jpg
* static/imgs/arquivo.jpg
* static/js/arquivo.js

<h3>Templates</h3>

* templates/arquivo.html


<h2>Padronização Front-end (HTML, CSS, JS)</h2>

<h3>Regras</h3>

* Usar display Grid ou Flex.
* Padronização C# exemplo: conteudoFilho, conteudoPai, menuHorizontal.
* Comentar o código, para todos entenderem.
* Proibido o uso de CSS dentro do HTML.
* Ultilize somente id para casos especiais.
* Proibido usar ```<center></center> | <strong></strong>```.

<h3>Estrutura HTML</h3>

```
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="utf-8" />
  <title>Nome da Pagina | Faculdade Perseus</title>
  <link rel="stylesheet" type="text/css" href="css/style.css" />
  <link rel="stylesheet" type="text/css" href="css/nomeArquivo.css" />
  <script type="text/javascript" src="js/script.js"></script>
</head>
<body>

  <header>
  </header>
  
  <section class="sobrePai"> <!-- nome da classe tem que ter o nome do conteudo e em seguida a hierarquia -->
    <article class="sobreFilho">
    </article>
  </section>
  
  <section class="conteudoHierarquia">
    <article class="conteudoHierarquia">
      <div class="item1">
      </div>
      <div class="item2">
      </div>
    </article>
  </section>
  
  <footer>
  </footer>

</body>
</html>
```

> Ultilize sempre o section para a estrutura e o article para o conteudo dentro da estrutura.

<h3>Fonts</h3>

Titulo 'Questrial'<br/>
Texto 'Arimo'<br/>
Install fonts ``` @import url('https://fonts.googleapis.com/css?family=Arimo:700|Questrial'); ```

<h2>Padronização Back-end (Python Django)</h2>

<h3>Regras</h3>

* Usar codigo padrão underscore exemplo: nome_classe, classe_metodo.
* Comente seu codigo.
