<template>
    <div class="product">
        <div class="pic">
<!--            <img src="../assets/no-img.png" alt="">-->
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
        background: grey;
        padding: 15px;
        margin: 15px;
        width: 100%;
    }

    .title {
        font-size: 14px;
    }

    .manufacturer {
        font-style: italic;
    }

    .pic {

    }

    .price {

    }

    .action {

    }

    .btn {

    }
</style>