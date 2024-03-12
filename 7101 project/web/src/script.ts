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

function displaySearchResults();

console.log(searchItems("a"));
