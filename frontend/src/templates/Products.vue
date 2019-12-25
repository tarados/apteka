<template>
    <div class="container">
        <div>
            <h3 v-if="query">
                Результаты поиска по запросу "{{ query }}"
            </h3>
            <h3 v-else>Первые пять позиций прайса</h3>
        </div>
        <Sorting :count="count" @sortingProductPrice="sortingProductPrice"/>
        <div class="products">
            <div class="item" v-for="product in products" :key="product.title">
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
    import Sorting from "./Sorting";

    export default {
        components: {
            // eslint-disable-next-line vue/no-unused-components
            Product,
            Sorting
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
            },
            sortingProductPrice(text) {
                let sortByPrice = function (d1, d2) {
                    if (text === 'min'){
                        return (d1.price > d2.price) ? 1 : -1;
                    } else if (text === 'max') {
                        return (d1.price < d2.price) ? 1 : -1;
                    }
                };
                this.products.sort(sortByPrice);
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
            $route() {
                this.checkQueryAndLoadProducts()
            }
        }
    }

</script>

<style scoped>
    .products {
        display: flex;
        flex-wrap: wrap;
        margin: 0 auto;
        padding: 0;
    }

    .item {
        border: 1px solid #EDEDED;
        padding: 15px;
        margin: 5px;
        width: calc(100% / 2 - 10px);
    }

    @media screen and (max-width: 992px) {
        .item {
            width: calc(100% / 1 - 10px);
        }
    }

    h3 {
        font-size: 1.5rem;
        font-weight: 300;
        margin: 10px;
    }

</style>