<template>
    <div class="container-fluid">
        <div class="row content-box">
            <b-table striped hover :items="productload"></b-table>
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
                if (this.$route.params.textseach === undefined)
                    this.getProductload();
                if (this.$route.params.textsaech === this.query)
                    return;
                else
                    this.query = this.$route.params.textseach;
                // eslint-disable-next-line no-console
                console.log(this.query);
                this.getProductloadParam(this.query);
            }
        },
        mounted() {
            this.getProduct()
        },
        updated() {
            this.getProduct()
        }
        // watch: {
        //     query: function (seach) {
        //         if (this.timerId) {
        //             clearTimeout(this.timerId);
        //         }
        //         this.timerId = setTimeout(() => {
        //             // eslint-disable-next-line no-console
        //             console.log('sdfsadf');
        //             this.getProductloadParam(seach);
        //             this.timerId = 0;
        //         }, 1000);
        //     }
        // }
    }
</script>

<style scoped>
    .content-box {
        margin: 20px 0 5px 0;
    }
</style>