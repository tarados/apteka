export function getItems() {
    let items = localStorage.getItem('basket');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = [];
    }
    return items
}

export function getItemsCheck() {
    let items = localStorage.getItem('check');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = '';
    }
    return items
}

export function addItem(item) {
    const items = getItems();
    items.push(item);
    setItems(items);
}

export function addItemCheck(item) {
    item = JSON.stringify(item);
    localStorage.setItem('check', item);
}

export function incrementItem(index) {
    const items = getItems();
    items[index].quantity++;
    items[index].valueProduct = items[index].price * items[index].quantity;
    setItems(items);
}

export function decrementItem(index) {
    const items = getItems();
    items[index].quantity--;
    items[index].valueProduct = items[index].price * items[index].quantity;
    setItems(items);
}

export function deleteItem(index) {
    const items = getItems();
    items.splice(index, 1);
    setItems(items);
}

export function clearLocalStorage() {
    localStorage.clear();
}

function setItems(items) {
    items = JSON.stringify(items);
    localStorage.setItem('basket', items);
}

