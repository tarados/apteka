export function save(item) {
    item = JSON.stringify(item);
    localStorage.setItem('login', item);
}

export function load() {
    let items = localStorage.getItem('login');
    if (items) {
        items = JSON.parse(items);
    } else {
        items = {};
    }
    return items
}