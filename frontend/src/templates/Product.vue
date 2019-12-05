<template>
    <div class="container-fluid">
        <div class="content-box" v-for="(product, index) in productload" v-bind:key="index">
            <h2 v-text="product.product"></h2>
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
                    return;
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
    .container-fluid {
        display: flex;
    }

    .content-box {
        border: 1px solid grey;
        border-radius: 3px;
    }
</style>