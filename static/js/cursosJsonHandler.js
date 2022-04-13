const content = document.getElementById("section-2");

fetch("../static/json/cursos.json")
    .then(resposta => {
        return resposta.json();
    })
    .then(jsondata => {
        cursos = jsondata.filter(i => {
            var titulo = i.titulo;
            var descricao = i.descricao;

            content.innerHTML += `
                <!-- Cada class="row" é uma linha na lista de cursos -->
                <div class="row">
                    <div class="curso">
                        <img src="../static/images/SVG-Certificados.svg" alt="Placeholder da imagem dos cursos">
                        <!-- Cada class="col" é uma coluna na row em que está contida -->
                        <div class="col curso-content">
                            <h3 class="titulo">${titulo}</h3>
                            <p class="descricao">${descricao}</p>
                        </div>
                    </div>
                </div>
            `;
        });

    });