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
                    <!-- Cada class="col" é uma coluna na row em que está contida -->
                    <div class="col card-curso">
                        <img src="../static/images/SVG-Certificados.svg" alt="Placeholder da imagem dos cursos">
                        <p class="titulo">${titulo}</p>
                        <p class="subtitulo">${descricao}</p>
                    </div>
                </div>
            `;
        });

    });