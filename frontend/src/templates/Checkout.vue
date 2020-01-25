<template>
    <div class="wrapper">
        <div class="checkOut" v-for="(product, index) in productList" :key="index">
            <div class="checkOutContent">
                <div class="title" v-text="product.title"></div>
                <div class="manufacturer" v-text="product.manufacturer"></div>
                <div class="price" v-text="product.price"></div>
                <div class="quantity" v-text="product.quantity"></div>
                <div class="valueProduct" v-text="product.valueProduct"></div>
            </div>
        </div>
        <div class="totalPrice" v-text="totalPrice"></div>
        <Farmacy/>
    </div>
</template>

<script>
    import * as basket from '../basket'
    import Farmacy from './Farmacy'
    export default {
        name: "Checkout",
        components: {
            Farmacy
        },
        data() {
            return {
                productList: [],
                totalPrice: 0
            }
        },
        methods: {
            loadBasketContent() {
                this.productList = basket.getItems();
                this.totalPrice = basket.getItemsCheck();
            }
        },
        mounted() {
            this.loadBasketContent();
        }
    }
</script>

<style scoped>

</style>