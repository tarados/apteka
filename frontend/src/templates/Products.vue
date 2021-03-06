<template>
    <div class="container">
        <div>
            <h3 v-if="query">
                Результаты поиска по запросу "{{ query }}"
            </h3>
        </div>
        <Sorting
                :count="count"
                @sortingProductPrice="sortingProductPrice"
                @filterProduct="filterProduct"
        />
        <Filtration
                @filteredItem="filteredManufacturer"
                v-if="filter"
                :filterable-list="products"
                filterable-field="manufacturer"
        />
        <div v-else></div>
        <div class="products">
            <div class="item" v-for="product in productsFiltered" :key="product.title">
                <Product
                        :product="product"
                />
            </div>
        </div>
    </div>

</template>

<script>
    import * as send from '../send';
    import Product from "./Product";
    import Sorting from "./Sorting";
    import Filtration from "./Filter";

    export default {
        components: {
            Product,
            Filtration,
            Sorting
        },
        data() {
            return {
                query: '',
                filter: null,
                manufacturerFilter: null,
                products: [],
                count: 0
            }
        },
        computed: {
            productsFiltered() {
                if (this.manufacturerFilter && this.manufacturerFilter.length) {
                    const filter = this.manufacturerFilter.join('|');
                    const filteredList = this.products.filter(item => item.text.match(filter));
                    this.count = filteredList.length;
                    return filteredList
                }
                this.count = this.products.length;
                return this.products;
            }
        },
        methods: {
            async loadProducts(query) {
                if (!query || !query.length) {
                    query = ''
                }
                const response = await send.get('products', {
                        query: query
                    });
                this.products = response.products;
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
                    if (text === 'min') {
                        return (d1.price > d2.price) ? 1 : -1;
                    } else if (text === 'max') {
                        return (d1.price < d2.price) ? 1 : -1;
                    }
                };
                this.products.sort(sortByPrice);
            },
            filterProduct(text) {
                if (text === true) {
                    this.filter = text;
                } else {
                    this.filter = null;
                    this.manufacturerFilter = null;
                }
            },
            filteredManufacturer(manufacturerList) {
               this.manufacturerFilter = manufacturerList;
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

    h3 {
        font-size: calc(1em + 1vw);
        font-weight: 300;
        margin: 10px;
    }

    @media screen and (max-width: 992px) {
        .item {
            width: calc(100% / 1 - 10px);
        }
    }


</style>