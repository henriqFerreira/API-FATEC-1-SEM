<p align="center">
  <img src="/readme/B1NAR10S.svg" alt="Equipe B1NAR10S"/>
</p>

# API-FATEC

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
    <link rel="stylesheet" href="template.css">
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
    <footer>
        <div class="container">
            <ul class="footer-list">
                <li id="footer-logo"><a href="">LOGO</a></li>
                <li id="footer-bar"><span></span></li>
                <li class="link"><a href="">All Rights Reserved</a></li>
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
        width: 60%; height: 2px;
        background-color: var(--darker-blue);
    }

/* Footer */
    footer {
        width: 100%; height: 70px;
        position: relative;
        bottom: 0;
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
        width: 80%; height: 2px;
        background-color: var(--darker-blue);
    }
~~~

</details>
