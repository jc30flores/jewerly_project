document.addEventListener("keyup", e => {
    if (e.target.matches("#buscador")){
        document.querySelectorAll(".articulos").forEach(fruta => {
            fruta.textContent.toLocaleLowerCase().includes(e.target.value)
            ? fruta.classList.remove("filtro")
            : fruta.classList.add("filtro");

        })
    }
})