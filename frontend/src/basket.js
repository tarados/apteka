export function getItems() {
    let items = localStorage.getItem('basket');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = [];
    }
    return items
}

export function addItem(item) {
    const items = getItems();
    items.push(item);
    setItems(items);
}

export function deleteItem(index) {
    const items = getItems();
    items.splice(index, 1);
    setItems(items);
}

function setItems(items) {
    items = JSON.stringify(items);
    localStorage.setItem('basket', items);
}