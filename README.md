<p align="center"> <img src="/readme/B1NAR10S.svg" alt="Equipe B1NAR10S"/></p>
<br>
<p align="center">
  <samp>
    <a href="#o-projeto">Projeto</a> ▪️
    <a href="#proposta">Proposta</a> ▪️
    <a href="#tecnologias">Tecnologias</a> ▪️
    <a href="#metodologia">Metodologia</a> ▪️
    <a href="#cronograma-das-sprints">Cronograma das Sprints</a> ▪️
    <a href="#product-backlog">Product Backlog</a> ▪️
    <a href="#sprints-backlog">Sprints Backlog</a> ▪️
    <a href="#equipe">Equipe</a>
  </samp>
</p>

<br>

<h1 align="center"><samp>O PROJETO</samp></h1>

![Equipe B1NAR10S](/readme/Objetivo.png)

<br>
<h1 align="center"><samp>PROPOSTA</samp></h1>

Desenvolver um sistema web para automatizar o processo de catalogar vagas de diversas profissões, principalmente na área de TI.

### 📖 Requisitos
+ - [x] Página Home
+ - [x] Página de vagas
+ - [x] Página Cursos
+ - [ ] Página Institucional
+ - [ ] Página para cada vaga

### 🔖 Requisitos funcionais
+ - [x] Raspagem das vagas
+ - [x] Raspagem dos cursos

<br>
<h1 align="center"><samp>TECNOLOGIAS</samp></h1>

![Equipe B1NAR10S](/readme/Tecnologias.png)

<table align="center">
  <tr>
    <th><b>Front-end</b></th>
    <th><b>Back-end</b></th>
    <th><b>Ferramentas</b></th>
  </tr>
  <tr>
    <td>HTML</td>
    <td>JavaScript</td>
    <td>Visual Studio Code</td>
  </tr>
  <tr>
    <td>CSS</td>
    <td>Python</td>
    <td>Figma</td>
  </tr>
  <tr>
    <td>Bootstrap</td>
    <td></td>
    <td>Git</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Github</td>
  </tr>
</table>

<br>
<h1 align="center"><samp>CRONOGRAMA DAS SPRINTS</samp></h1>

![Equipe B1NAR10S](/readme/Cronograma.png)

<br>
<h1 align="center"><samp>PRODUCT BACKLOG</samp></h1>

![Equipe B1NAR10S](/readme/ProductBacklog.png)

<br>
<h1 align="center"><samp>SPRINTS BACKLOG</samp></h1>

![Equipe B1NAR10S](/readme/SprintBacklog.png)

<h3>Detalhes das sprints</h3>
<details>
  <summary>Sprint 1</summary>
  
  <h1 align="center">Sprint 1</h1>
  <h3 align="center">Demonstração de usabilidade</h3>
  
  <h4>Página Home</h4>
  <img src="/readme/home.gif" width="100%" />
  <a href="https://youtu.be/tYYEdszhfYs">Youtube (Qualidade melhor)</a>
  <br>
  <p></p>

  <h4>Página Home > Link 'vagas' da barra de navegação</h4>
  <img src="/readme/vagas-link.gif" width="100%" />
  <a href="https://youtu.be/Ap9goqxyAiI">Youtube (Qualidade melhor)</a>
  <br>
  <p></p>

  <h4>Página Home > Botão 'conferir vagas'</h4>
  <img src="/readme/vagas-botao.gif" width="100%" />
  <a href="https://youtu.be/3PkO0mMF3cU">Youtube (Qualidade melhor)</a>
  <br>
  <p></p>

  <h4>Página Cursos e Certificações</h4>
  <img src="/readme/cursos-link.gif" width="100%" />
  <a href="https://youtu.be/L_Cu1CS14Fo">Youtube (Qualidade melhor)</a>
  <br>
  <p></p>

  <h4>Captação de dados (Raspagem)</h4>
  <img src="/readme/raspagem.gif" width="100%" />
  <a href="https://youtu.be/vKMSfNvmp7g">Youtube (Qualidade melhor)</a>
  <br>
  <p></p>
</details>

<br>
<h1 align="center"><samp>EQUIPE</samp></h1>

<table align="center">
  <tr>
    <th><b>Nome</b></th>
    <th><b>Função</b></th>
    <th><b>Github</b></th>
  </tr>
  <tr>
    <td>Gustavo Marques</td>
    <td>Product Owner</td>
    <td><a href="https://github.com/gusta7597">Github</a></td>
  </tr>
  <tr>
    <td>Camila Redondo</td>
    <td>Scrum Master</td>
    <td><a href="https://github.com/CamilaRedondo">Github</a></td>
  </tr>
  <tr>
    <td>Micael Leal</td>
    <td>Desenvolvedor</td>
    <td><a href="https://github.com/micael-leal">Github</a></td>
  </tr>
  <tr>
    <td>João Henrique</td>
    <td>Desenvolvedor</td>
    <td><a href="https://github.com/JoaoHenrique7">Github</a></td>
  </tr>
  <tr>
    <td>Simone Kanzawa</td>
    <td>Desenvolvedor</td>
    <td><a href="https://github.com/Simonehk">Github</a></td>
  </tr>
  <tr>
    <td>Henrique Neto</td>
    <td>Desenvolvedor</td>
    <td><a href="https://github.com/henriqFerreira">Github</a></td>
  </tr>
</table>

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
