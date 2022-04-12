<p align="center"> <img src="/readme/B1NAR10S.svg" alt="Equipe B1NAR10S"/></p>

<br>

<p align="center">
  <samp>
    <a href="#o-projeto">Projeto</a> ▪️
    <a href="#proposta">Proposta</a> ▪️
    <a href="#tecnologias">Tecnologias</a> ▪️
    <a href="#metodologia">Metodologia</a> ▪️
    <a href="#product-backlog">Product Backlog</a> ▪️
    <a href="#sprints">Sprints</a> ▪️
    <a href="#equipe">Equipe</a>
  </samp>
</p>

<br>

<h1 align="center"><samp>O PROJETO</samp></h1>

![Equipe B1NAR10S](/readme/Objetivo.png)

<h1 align="center"><samp>PROPOSTA</samp></h1>

Desenvolver um sistema web para automatizar o processo de catalogar vagas de diversas profissões, principalmente na área de TI.

> Requisitos
>
> + - [x] Página Home
> + - [x] Página de vagas
> + - [x] Página Cursos
> + - [ ] Página Institucional
> + - [ ] Página para cada vaga

<br>
<h1 align="center"><samp>TECNOLOGIAS</samp></h1>

![Equipe B1NAR10S](/readme/Tecnologias.png)

| **FRONT-END** | **BACK-END** | **FERRAMENTAS** |
| :-------: | :------: | :---------: |
| HTML | JavaScript | Visual Studio Code |
| CSS | Python | Figma |
| Bootstrap | | Git |
| | | Github |

<br>
<h1 align="center">PRODUCT BACKLOG</h1>

![](/readme/ProductBacklog.png)

<details>
  <summary>Detalhes técnicos</summary>
  
  ### Organização e padronização do código
  
  Para fins de melhoria de eficiência e praticidade na realização do projeto, deverão, todos os participantes, seguirem os seguintes padrões:
  
  #### HTML
  Template mínima no HTML, contendo a barra de navegação e rodapé.

~~~html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="../static/css/template.css">
    <title>Cursos e Certificações</title>
</head>
<body>
    <!-- Barra de navegação -->
    <nav>
        <div class="container">
            <ul class="navbar-list">
            <li id="navbar-logo"><a href="">LOGO</a></li>
            <li id="navbar-bar"><span></span></li>
            <li class="link"><a href="">Início</a></li>
            <li class="link"><a href="">Vagas</a></li>
            <li class="link"><a href="">Cursos e Certificações</a></li>
            </ul>
        </div>
    </nav>
    <!-- Conteúdo da página deve ser inserido dentro dessa DIV -->
    <div class="container">
        
    </div>
    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <ul class="footer-list">
                <li id="footer-logo"><a href="">LOGO</a></li>
                <li id="footer-bar"><span></span></li>
                <li class="link"><a href="">All Rights Reserved</a></li> <!-- B1NAR10S Todos os Direitos Reservados -->
            </ul>
        </div>
    </footer>
</body>
</html>
~~~
  
### CSS

Estilização mínima no CSS. Contém os estilos necessários para funcionamento correto da template do HTML.

~~~css
@import url('https://fonts.googleapis.com/css2?family=Capriola&display=swap');

:root {
    --darker-blue: #00296B;
    --dark-blue: #003F88;
    --blue: #00509D;
    --dark-yellow: #FDC500;
    --yellow: #FFD500; 
}

* {
    margin: 0; padding: 0;
    box-sizing: border-box;
    font-family: 'Capriola', sans-serif
}

/* Container que alinhará todo o conteúdo da página na mesma orientação */
    .container {
        width: 90%; height: 100%;
        margin: 0 auto;
    }

/* Barra de navegação */
    nav {
        width: 100%; height: 70px;
    }

    .navbar-list {
        height: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        list-style: none;
    }
        .navbar-list li a {
            text-decoration: none;
            color: var(--dark-blue);
        }

    #navbar-logo {
        font-size: 2em;
    }

    #navbar-bar {
        width: 50%; height: 2px;
        background-color: var(--darker-blue);
    }

/* Footer */
    .footer{
        width: 100%; height: 70px;
        bottom: 0;
        position: fixed;
        text-align: center;
    }

    .footer-list {
        height: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        list-style: none;
    }
        .footer-list li a {
            text-decoration: none;
            color: var(--dark-blue);
        }

    #footer-logo {
        font-size: 2em;
    }

    #footer-bar {
        width: 70%; height: 2px;
        background-color: var(--darker-blue);
    }
~~~

</details>
