import Vue from 'vue'
import * as basket from '../../basket.js'

export default {
    actions: {},
    mutations: {
        addProduct(state, product) {
            state.basketProducts.push(product);
        },
        increment(state, index) {
            changeQuantity(state, index, 1);
            basket.incrementItem(index);
        },
        decrement(state, index) {
            changeQuantity(state, index, -1);
            basket.decrementItem(index);

        },
        delProduct(state, index) {
            state.basketProducts.splice(index, 1);
            basket.deleteItem(index);
        },
        addTotalPriceToCheck(state) {
            basket.addItemCheck(state.totalPrice);
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