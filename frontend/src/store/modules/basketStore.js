import Vue from 'vue'
import * as basket from '../../basket.js'

export default {
    actions: {},
    mutations: {
        addProduct(state, product) {
            state.basketProducts.push(product);
            basket.setItems(state.basketProducts);
        },
        increment(state, index) {
            changeQuantity(state, index, 1);
            basket.setItems(state.basketProducts);
        },
        decrement(state, index) {
            changeQuantity(state, index, -1);
            basket.setItems(state.basketProducts);

        },
        delProduct(state, index) {
            state.basketProducts.splice(index, 1);
            basket.setItems(state.basketProducts);
        },
        clearStore(state) {
            state.basketProducts.splice(0, state.basketProducts.length);
            basket.clearLocalStorage();
        },
        addProductsFromBasket(state) {
            state.basketProducts = basket.getItems();
        }
    },
    state: {
        basketProducts: [],
        totalPrice: 0
    },
    getters: {
        allProducts(state) {
            return state.basketProducts;
        },
        getTotalPrice(state) {
            let valueTotal = [];
            state.basketProducts.forEach(function (item) {
                valueTotal.push(item.valueProduct);
            });
            let totalPrice = eval(valueTotal.join('+'));
            state.totalPrice = parseFloat(totalPrice).toFixed(1);
            return state.totalPrice;
        },
        orderProductList(state) {
            let orderList = [];

            state.basketProducts.forEach(function (item) {
                let order = {
                    'price': item.price,
                    'productId': item.productId,
                    'quantity': item.quantity
                };
                orderList.push(order);
            });
            return orderList;
        }
    }
}

function changeQuantity(array, index, number) {
    const item = array.basketProducts[index];
    item.quantity = item.quantity + number;
    item.valueProduct = parseFloat((item.price * item.quantity).toFixed(1));
    Vue.set(array.basketProducts, index, item);
}