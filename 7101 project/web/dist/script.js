"use strict";
const items = [
    { id: 1, name: "Teemo" },
    { id: 2, name: "Mordekaiser" },
    { id: 3, name: "Sylas" },
];
function searchItems(searchTerm) {
    return items.filter((item) => item.name.toLowerCase().includes(searchTerm.toLowerCase()));
}
console.log(searchItems("a"));
//# sourceMappingURL=script.js.map