<template>
    <div class="wrapper">
        <div class="productContent">
            <div class="product" v-for="(product, index) in productload" v-bind:key="index">
                <div class="title" v-text="product.product"></div>
                <div class="pic">
                    <img src="../assets/no-img.png" alt="">
                </div>
                <div class="manufacturer" v-text="product.manufacturer"></div>
                <div class="price" v-text="product.price + ' руб.'"></div>
                <div class="action">
                    <div class="btn">Где есть</div>
                    <div class="btn">В корзину</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import * as axios from "axios";

    export default {
        data() {
            return {
                query: '',
                productload: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app'
                }
            }
        },
        methods: {
            async getProductload() {
                const response = await axios.get(this.url.index, {
                    params: {
                        query: 'empty'
                    }
                });
                this.productload = response.data.productload;
            },
            async getProductloadParam(query) {
                const response = await axios.get(this.url.index, {
                    params: {
                        query: query
                    }
                });
                this.productload = response.data.productload;
                this.count = response.data.valueOf().productload.length;
            },
            getProduct() {
                if (this.$route.params.textseach === undefined) {
                    this.getProductload();
                } else if (this.$route.params.textseach === this.query) {
                    return 'df';
                } else {
                    this.query = this.$route.params.textseach;
                    this.getProductloadParam(this.query);
                }

            }
        },
        mounted() {
            this.getProduct()
        },
        updated() {
            if ((this.query === '') || (this.query === undefined)) {
                this.$route.params.textseach = '';
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        max-width: 1280px;
        padding: 0 15px;
        margin: 0 auto;
        border: 1px solid #ff0;
    }

    .productContent {
        background: #f00;
    }

    .productContent:after {
        content: "";
        display: block;
        clear: both;
    }

    .wrapper .product {
        text-align: center;
        background: #777;
        min-height: 250px;

        float: left;
        margin: 15px;
        width: calc(100% / 4 - 30px);
    }

    .title {
        font-size: 20px;
    }

    .manufacturer {
        font-style: italic;
    }

    .price {
        text-align: right;
    }

    .action {

    }

    .btn {

    }
</style>