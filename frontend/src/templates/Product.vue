<template>
    <div class="product">
        <div class="pic">
            <img src="../assets/no-img.png" alt="">
        </div>
        <div class="title" v-text="product.title"></div>
        <div class="price" v-text="product.price + ' руб.'"></div>
        <div class="manufacturer" v-text="product.manufacturer"></div>
        <b-button variant="success" class="action">
            <custom-icon name="shopping-cart" class="custom-icon"/>
            <span>Купить</span>
        </b-button>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'

    export default {
        name: "Product",
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon
        },
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
    }

    .title {
        font-size: 14px;
        grid-row: 1;
        grid-column: 2 / 4;
    }

    .manufacturer {
        font-style: italic;
        grid-row: 2;
        grid-column: 2 / 4;
    }

    .pic {
        grid-row: 1 / 5;
        grid-column: 1 / 2;
        border: 1px solid grey;
    }

    .price {
        grid-row: 3;
        grid-column: 2 / 4;
        font-weight: bold;
    }

    .action {
        grid-column: 2 / 4;
        margin-top: 10px;
        /*display: flex;*/
        /*flex-wrap: wrap;*/
        /*justify-content: flex-end;*/
        /*align-items: flex-end;*/

    }

    .btn {
        margin: 0 5px;
        width: 100%;
    }

    .custom-icon {
        width: 24px;
    }

    span {
        font-style: italic;
        font-size: 14px;
        margin-left: 10px;
    }

    p {
        margin: 0;
    }
</style>