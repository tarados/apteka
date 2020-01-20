<template>
    <div class="container">
        <div class="wrapper">
            <div id="header">
                <div class="title">
                    <i>Basket</i>
                </div>
            </div>
            <div class="contentBasket" v-for="(product, index) in productList" :key="index">
                <div class="photo">
                    <img :src="product.photo" :alt="product.title">
                </div>
                <div class="product">
                    <div class="title" v-text="product.title"></div>
                    <div class="manufacturer" v-text="product.manufacturer"></div>
                    <div class="price" v-text="product.price + ' руб.'"></div>
                </div>
                <div class="quantity">quantity</div>
                <div class="total">total</div>
                <b-button-close class="deleteOrder" @click="deleteOrder(index)">
                    <custom-icon name="x" class="custom-icon"/>
                </b-button-close>
            </div>
            <div id="footer">
                <b-button variant="success" @click="toHome">Button</b-button>
                <b-button variant="success" @click="toHome">Button</b-button>
            </div>
        </div>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import * as basket from '../basket'

    export default {
        name: "Basket",
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon
        },
        data() {
            return {
                productList: []
            }
        },
        methods: {
            toHome() {
                this.$router.go(-1);
            },
            loadBasket() {
                this.productList = basket.getItems();
            },
            deleteOrder(index) {
                basket.deleteItem(index);
                this.loadBasket();
            }
        },
        mounted() {
            this.loadBasket();
        }
    }
</script>

<style scoped>
    .container {
        border: 1px solid red;
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
        margin-bottom: 5px;
        background-color: gold;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center
    }

    .contentBasket {
        width: 100%;
        margin: 5px 0;
        background-color: #6DDCBD;
        display: grid;
        grid-template-columns: 0.7fr 3fr 1fr 0.5fr 0.3fr;
    }

    .photo {
        grid-column: 1 / 1;
    }

    img {
        max-height: 6em;
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
    }

    .manufacturer {

    }

    .price {

    }

    .quantity, .total {
        place-self: center;
    }

    .quantity {
        grid-column: 3 / 3;
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
        margin: 10px auto;
    }

    .custom-icon {
        width: 24px;
    }

</style>