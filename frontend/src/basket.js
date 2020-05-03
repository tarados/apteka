export function getItems() {
    let items = localStorage.getItem('basket');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = [];
    }
    return items
}

export function clearLocalStorage() {
    localStorage.removeItem("basket");
}

export function setItems(items) {
    items = JSON.stringify(items);
    localStorage.setItem('basket', items);
}

