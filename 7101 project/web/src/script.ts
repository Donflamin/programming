// rune trees
class runeTrees {
  private divElement: HTMLDivElement;
  private ulElements: HTMLUListElement[];

  constructor() {
    this.divElement = document.createElement("div");
    this.ulElements = [];

    for (let i = 0; i < 4; i++) {
      const ulElement = document.createElement("ul");
      const liElement = document.createElement("li");
      liElement.textContent = "Item ${i +1}";
      ulElement.appendChild(liElement);
      this.ulElements.push(ulElement);
    }

    this.ulElements.forEach((ul) => {
      this.divElement.appendChild(ul);
    });
  }

  appendTo(parent: HTMLElement) {
    parent.appendChild(this.divElement);
  }
}

const divWithMultipleUl = new runeTrees();
divWithMultipleUl.appendTo(document.body);

interface itemInt {
  id: number;
  name: string;
}

const items: itemInt[] = [
  { id: 1, name: "Teemo" },
  { id: 2, name: "Mordekaiser" },
  { id: 3, name: "Sylas" },
];

function searchItems(searchTerm: string): itemInt[] {
  return items.filter((item) =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase()),
  );
}

// function createMenu(containerId: string, runeTreeOne, runeTreeTwo, menuItems: []): void {

// catch error
//  const container = document.getElementById(containerId)
//  if (!container) {
//    console.error("Container with ID '${containerId}' not found.");
//    return;  }

//  if runeTreeOne == precision {

//  }

//  const menu = document.createElement('ul')

// find div with id ...
// add menu items
// }
// addMenu("my-item");

console.log(searchItems("a"));
