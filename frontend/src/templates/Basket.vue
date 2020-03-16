<template>
    <div class="container">
        <div id="header">
            <div class="titleBasket">
                <i>Заказано наименований - {{getCount}}</i>
            </div>
            <div class="totalPrice">
                <i>Всего к оплате: <span>{{getTotalPrice}} руб.</span></i>
            </div>
        </div>
        <div class="wrapper">
            <div class="contentBasket" v-for="(product, index) in allProducts" :key="index">
                <div class="photo">
                    <img :src="product.photo" :alt="product.title">
                </div>
                <div class="product">
                    <div class="title" v-text="product.title"></div>
                    <div class="manufacturer" v-text="product.manufacturer"></div>
                    <div class="price" v-text="product.price + ' руб.'"></div>
                </div>
                <div class="quantity">
                    <b-button variant="outline" @click="minusQuantity(index)">
                        <custom-icon name="minus-square" class="custom-icon"/>
                    </b-button>
                    <div class="productQuantity" v-text="product.quantity"></div>
                    <b-button variant="outline" @click="plusQuantity(index)">
                        <custom-icon name="plus-square" class="custom-icon"/>
                    </b-button>
                </div>
                <div class="total">{{product.valueProduct.toFixed(1)}} руб.</div>
                <b-button-close class="deleteOrder" @click="deleteOrder(index)">
                    <custom-icon name="x" class="custom-icon"/>
                </b-button-close>
            </div>
            <div id="footer">
                <b-button
                        variant="outline-primary"
                        @click="toHome"
                        class="basket"
                >
                    <custom-icon name="chevron-left" class="custom-icon"/>
                    Продолжить покупки
                </b-button>
                <b-button
                        variant="success"
                        @click="toCheckout"
                        class="basket"
                >
                    Оформить заказ
                </b-button>
            </div>
        </div>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import {mapGetters, mapState} from 'vuex'

    export default {
        name: "Basket",
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon
        },
        computed: {
            ...mapGetters(["allProducts"]),
            ...mapGetters(["getTotalPrice"]),
            ...mapState(["basketProducts"]),
            getCount() {
                const count = this.allProducts.length ? this.allProducts.length : 0;
                return count;
            }
        },
        methods: {
            toHome() {
                this.$router.go(-1);
            },
            toCheckout() {
                // eslint-disable-next-line no-unused-vars
                this.$router.push('/basket/checkout').catch(err => {
                });
                this.$store.dispatch('totalPriceToCheck');
            },
            deleteOrder(index) {
                this.$store.dispatch('deleteProduct', index);
            },
            minusQuantity(index) {
                this.$store.dispatch('decrementProduct', index);
            },
            plusQuantity(index) {
                this.$store.dispatch('incrementProduct', index);
            }
        }
    }
</script>

<style scoped>
    .container {
        border: 1px solid grey;
    }

    .wrapper {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }

    #header {
        width: 100%;
        height: 3em;
        border: 1px solid grey;
        padding: 0 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    span {
        font-style: normal;
        font-size: calc(0.95em + 0.3vw);
        font-weight: 600;
    }

    .contentBasket {
        width: 100%;
        margin: 5px 0;
        border: 1px solid grey;
        border-radius: 5px;
        display: grid;
        font-size: calc(0.65em + 0.3vw);
        grid-template-columns: 0.7fr 3fr 1fr 0.5fr 0.3fr;
    }

    .photo {
        grid-column: 1 / 1;
    }

    img {
        max-height: 6em;
        padding: 1px;
    }

    .product {
        grid-column: 2 / 2;
        display: flex;
        flex-wrap: wrap;
    }

    .title, .manufacturer, .price {
        flex-grow: 0.5;
        width: 100%;
        text-align: center;
        font-size: calc(0.65em + 0.3vw);
    }

    .titleBasket, .totalPrice {
        font-size: calc(0.65em + 0.3vw);
    }

    .quantity, .total {
        place-self: center;
    }

    .quantity {
        grid-column: 3 / 3;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        width: 70%;
    }

    .productQuantity {
        align-self: center;
    }

    .total {
        grid-column: 4 / 4;
    }

    .deleteOrder {
        grid-column: 5 / 5;
        place-self: self-start;
        margin-left: auto;
    }

    #footer {
        margin: 40px 0 20px 0;
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .basket {
        font-size: calc(0.65em + 0.3vw);
    }

    .custom-icon {
        width: 24px;
    }

</style>