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
            state.basketProducts[index].quantity++;
            state.basketProducts[index].valueProduct = state.basketProducts[index].price * state.basketProducts[index].quantity;

        },
        decrement(state, index) {
            state.products[index].quantity--;
            state.basketProducts[index].valueProduct = state.basketProducts[index].price * state.basketProducts[index].quantity;

        },
        delProduct(state, index) {
            state.basketProducts.splice(index, 1);
        }
    },
    state: {
        basketProducts: []
    },
    getters: {
        allProducts(state) {
            return state.basketProducts;
        }
    }
}
