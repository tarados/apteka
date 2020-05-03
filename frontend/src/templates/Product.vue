<template>
    <div class="product">
        <div class="pic">
            <img id="myImg" src="../assets/no-img.png" alt="">
        </div>
        <div class="title" v-text="product.title"></div>
        <div class="manufacturer" v-text="product.manufacturer"></div>
        <div class="price" v-text="product.price + ' руб.'"></div>
        <b-button variant="success" class="action" @click="toBasket">
            <custom-icon name="shopping-cart" class="custom-icon"/>
            <span>Купить</span>
        </b-button>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import * as basket from '../basket'

    export default {
        name: "Product",
        components: {
            customIcon
        },
        props: {
            product: {
                type: Object
            }
        },
        methods: {
            toBasket() {
                this.$router.push('/basket');
                this.product.photo = document.getElementById("myImg").src;
                this.product.quantity = 1;
                this.product.valueProduct = parseFloat((this.product.quantity * this.product.price).toFixed(1));
                this.$store.commit('addProduct', this.product);
            }
        }
    }
</script>

<style scoped>
    .product {
        text-align: center;
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-gap: 5px 5px;
    }

    .title {
        font-size: calc(0.8em + 0.3vw);
        grid-column: 2 / 4;
    }

    .manufacturer {
        font-size: calc(0.65em + 0.3vw);
        font-style: italic;
        grid-column: 2 / 4;
    }

    .pic {
        grid-row: 1 / 5;
        border: 1px solid grey;
    }

    .pic img {
        max-width: 100%;
    }

    .price {
        grid-column: 2 / 4;
        font-weight: bold;
    }

    .action {
        grid-column: 2 / 4;
        margin-top: 10px;
        align-self: end;
    }

    .custom-icon {
        width: 24px;
    }

    span {
        font-style: italic;
        font-size: 14px;
        margin-left: 10px;
    }
</style>