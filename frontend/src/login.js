export function setLogin(item) {
    item = JSON.stringify(item);
    localStorage.setItem('login', item);
}

export function getLogin() {
    let items = localStorage.getItem('login');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = {};
    }
    return items
}