import Vue from 'vue'
import * as basket from '/home/sergey/projects/apteka/frontend/src/basket.js'

export default {
    actions: {
        getProduct(ctx, item) {
            // eslint-disable-next-line no-undef
            ctx.commit('addProduct', item);
        },
        deleteProduct(ctx, index) {
            // eslint-disable-next-line no-undef
            ctx.commit('delProduct', index);
        },
        incrementProduct(ctx, index) {
            // eslint-disable-next-line no-undef
            ctx.commit('increment', index);
        },
        decrementProduct(ctx, index) {
            // eslint-disable-next-line no-undef
            ctx.commit('decrement', index);
        }
    },
    mutations: {
        addProduct(state, product) {
            state.basketProducts.push(product);
        },
        increment(state, index) {
            const item = state.basketProducts[index];
            item.quantity++;
            item.valueProduct = item.price * item.quantity;
            Vue.set(state.basketProducts, index, item);
            basket.incrementItem(index);
        },
        decrement(state, index) {
            const item = state.basketProducts[index];
            item.quantity--;
            item.valueProduct = item.price * item.quantity;
            Vue.set(state.basketProducts, index, item);
            basket.decrementItem(index);

        },
        delProduct(state, index) {
            state.basketProducts.splice(index, 1);
            basket.deleteItem(index);
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
        }
    }
}
