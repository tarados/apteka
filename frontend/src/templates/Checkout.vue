<template>
    <div class="container">
        <div class="header">
            <b-button variant="outline-primary" @click="toBasket">
                <custom-icon name="chevron-left" class="custom-icon"/>
                Вернуться в корзину
            </b-button>
            <div class="title"> Оформление заказа</div>
        </div>

        <div>
            <b-table striped hover :items="productList" :fields="fields"></b-table>
        </div>
        <hr>
        <div class="totalPrice">
            <div>
                <i>Всего к оплате:</i>
            </div>
            <div class="price" v-text="totalPrice + ' руб.'"></div>
        </div>
        <hr>
        <Farmacy/>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import Farmacy from "./Farmacy";
    import * as basket from '../basket'

    export default {
        name: "Checkout",
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon,
            Farmacy
        },
        data() {
            return {
                productList: [],
                fields: {
                    title: "Наименование",
                    manufacturer: 'Производитель',
                    price: 'Цена',
                    quantity: 'Количество',
                    valueProductFixed: 'Сумма'
                },
                totalPrice: 0,
            }
        },
        methods: {
            loadBasketContent() {
                this.productList = basket.getItems();
                this.productList.forEach(function (item) {
                    item.valueProductFixed = item.valueProduct.toFixed(1);
                });
                this.totalPrice = basket.getItemsCheck();
            },
            toBasket() {
                this.$router.go(-1);
            }
        },
        mounted() {
            this.loadBasketContent();
        }
    }
</script>

<style scoped>
    .header {
        padding: 10px;
        margin-bottom: 10px;
        display: flex;
        flex-wrap: wrap;
    }

    .header .title {
        width: 70%;
        text-align: center;
        align-self: center;
    }

    .totalPrice {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .price {
        font-size: 22px;
        font-weight: 500;
        font-style: italic;
    }

    .custom-icon {
        width: 24px;
    }
</style>