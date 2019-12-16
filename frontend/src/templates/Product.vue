<template>
    <b-container>
        <b-row class="productContent" align-h="center">
            <b-col class="product" cols="4" v-for="(product, index) in products" v-bind:key="index">
                <div class="pic">
                    <img src="../assets/no-img.png" alt="">
                </div>
                <div class="title" v-text="product.product"></div>
                <div class="manufacturer" v-text="product.manufacturer"></div>
                <div class="price" v-text="product.price + ' руб.'"></div>
                <div class="action">
                    <div class="btn">Где есть</div>
                    <div class="btn">В корзину</div>
                </div>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import * as axios from "axios";

    export default {
        data() {
            return {
                query: '',
                products: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app'
                }
            }
        },
        methods: {
            async loadProducts(query) {
                if (!query || !query.length) {
                    query = 'empty'
                }
                const response = await axios.get(this.url.index, {
                    params: {
                        query: query
                    }
                });
                this.products = response.data.products;
                this.count = this.products.length;
            },
            checkQueryAndLoadProducts() {
                if (this.$route.params.textseach !== this.query) {
                    this.query = this.$route.params.textseach;
                    this.loadProducts(this.query);
                }
            }
        },
        mounted() {
            this.checkQueryAndLoadProducts();
        },
        updated() {
            if ((this.query === '') || (this.query === undefined)) {
                this.$route.params.textseach = '';
            }
        },
        watch: {
            // eslint-disable-next-line no-unused-vars
            $route(to, from) {
                this.checkQueryAndLoadProducts()
            }
        }
    }
</script>

<style scoped>
    .productContent {
        background: #6DDCBD;
    }

    .product {
        background: grey;
        padding: 15px;
        margin: 15px;
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