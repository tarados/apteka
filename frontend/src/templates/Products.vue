<template>
    <div class="wrapper">
        <div class="products">
            <div v-for="product in products" :key="product.title">
                <Product
                        :product="product"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import * as axios from "axios";
    import Product from "./Product";

    export default {
        components: {
            // eslint-disable-next-line vue/no-unused-components
            Product
        },
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
    .wrapper {
        max-width: 1280px;
        padding: 0 15px;
        margin: 0 auto;
        border: 1px solid yellow;
    }
    .products {
        margin: 0 -15px;
        display: flex;
        flex-wrap: wrap;
        /*background: #f00;*/
    }
</style>