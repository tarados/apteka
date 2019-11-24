<template>
    <div class="container-fluid">
        <b-nav-form class="form-inline">
            <b-form-input v-model="query" size="lg" class="my-lg-2" placeholder="Search"></b-form-input>
        </b-nav-form>
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
                query: "",
                productload: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app'
                }
            }
        },
        computed: {},
        methods: {
            async getProductload() {
                const response = await axios.get(this.url.index);
                this.productload = response.data;
            },
            async getProductloadParam(query) {
                const response = await axios.get(this.url.index, {
                    params: {
                        query: query
                    }
                });
                this.productload = response.data.productload;
                this.count = response.data.valueOf().productload.length;
            }
        },
        mounted() {
            // this.getProductload();
        },
        watch: {
            query: function (seach) {
                if (this.timerId) {
                    clearTimeout(this.timerId);
                }
                this.timerId = setTimeout(() => {
                    this.getProductloadParam(seach);
                    this.timerId = 0;
                }, 1000);
            }
        }
    }
</script>

<style scoped>
    .content-box {
        margin: 20px 0 5px 0;
    }

    .my-lg-2 {
        margin: 0 auto;
    }

    .form-inline {
        margin-top: 10px;
    }

</style>