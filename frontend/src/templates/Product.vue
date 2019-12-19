<template>
    <div class="product">
        <div class="pic">
            <img src="../assets/no-img.png" alt="">
        </div>
        <div class="title" v-text="product.title"></div>
        <div class="manufacturer" v-text="product.manufacturer"></div>
        <div class="price" v-text="product.price + ' руб.'"></div>
        <div class="action">
            <div class="btn">Где есть</div>
            <div class="btn">В корзину</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Product",
        props: {
            product: {
                type: Object
            }
        }
    }
</script>

<style scoped>
    .product {
        text-align: center;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 10px 30px;
        /*background: #5a8028;*/
        /*padding: 15px;*/
        /*margin: 15px;*/
        /*width: calc(100% / 2 - 30px);*/
    }

    .title {
        font-size: 14px;
        grid-row: 1;
        grid-column: 2 / 4;
    }

    .manufacturer {
        font-style: italic;
        grid-row: 3;
        grid-column: 1 / 2;
    }

    .pic {
        grid-row: 1;
        grid-column: 1 / 2;
    }

    .price {
        grid-row: 2;
        grid-column: 1 / 1;
    }

    .action {
        grid-row: 4;
        grid-column: 2 / 4;
    }

    .btn {

    }
</style>