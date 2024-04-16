const bars = document.getElementById("bars");
const barraLateral = document.querySelector(".sidebar");

let listElements = document.querySelectorAll('.list-button');
const submenus = document.querySelectorAll(".list-show");

// Este para cerrar y abrir el sidebar
bars.addEventListener("click", () => {
    barraLateral.classList.toggle("mini-sidebar");
});

//Este es para mostrar y cerrar los submenus
listElements.forEach(listElement => {
    listElement.addEventListener("click", () => {
        // Cerrar todos los menús abiertos
        listElements.forEach(element => {
            if (element !== listElement) {
                element.classList.remove("flecha");
                element.nextElementSibling.style.height = "0px";
            }
        });

        // Toggle del menú actual
        listElement.classList.toggle("flecha");

        let height = 0;
        let menu = listElement.nextElementSibling;
        if (menu.clientHeight === 0) {
            height = menu.scrollHeight;
        }

        menu.style.height = height + "px";
    });
});

// if (barraLateral === "mini-sidebar") {
//     listElements.forEach(listElement => {
//         listElement.addEventListener("click", () =>{
//             submenus.classList.toggle("mostrar");
//         });
//     });
// }