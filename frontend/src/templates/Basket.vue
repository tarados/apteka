<template>
    <div class="container">
        <div class="wrapper">
            <div id="header">
                <div class="contentHeader">
                    <div class="titleBasket">
                        <i>Корзина ({{count}})</i>
                    </div>
                    <div content="totalPrice" v-text="getTotalPrice"></div>
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
                <div class="quantity">
                    <b-button variant="outline" @click="minusQuantity(index)">
                        <custom-icon name="minus-square" class="custom-icon"/>
                    </b-button>
                    <div class="productQuantity" v-text="product.quantity"></div>
                    <b-button variant="outline" @click="plusQuantity(index)">
                        <custom-icon name="plus-square" class="custom-icon"/>
                    </b-button>
                </div>
                <div class="total">{{product.valueProduct}} руб.</div>
                <b-button-close class="deleteOrder" @click="deleteOrder(index)">
                    <custom-icon name="x" class="custom-icon"/>
                </b-button-close>
            </div>
            <div id="footer">
                <b-button variant="outline-primary" @click="toHome">
                    <custom-icon name="chevron-left" class="custom-icon"/>
                    Продолжить покупки
                </b-button>
                <b-button variant="success" @click="toCheckout">Оформить заказ</b-button>
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
                productList: [],
                count: Number,
            }
        },
        computed: {
            getTotalPrice: function() {
                let valueTotal = [];
                this.productList.forEach(function (item) {
                    valueTotal.push(item.valueProduct);
                });
                let totalPrice = eval(valueTotal.join('+'));
                return totalPrice
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
               basket.addItemCheck(this.getTotalPrice);
            },
            loadBasket() {
                this.productList = basket.getItems();
                this.count = this.productList.length;
            },
            deleteOrder(index) {
                basket.deleteItem(index);
                this.loadBasket();
            },
            minusQuantity(index) {
                this.productList[index].quantity--;
                this.productList[index].valueProduct = this.productList[index].price * this.productList[index].quantity;
                basket.decrementItem(index);
            },
            plusQuantity(index) {
                this.productList[index].quantity++;
                this.productList[index].valueProduct = this.productList[index].price * this.productList[index].quantity;
                basket.incrementItem(index);
            }
        },
        mounted() {
            this.loadBasket();
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
        margin-bottom: 5px;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center
    }

    .contentBasket {
        width: 100%;
        margin: 5px 0;
        border: 1px solid grey;
        border-radius: 5px;
        display: grid;
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

    .custom-icon {
        width: 24px;
    }

</style>