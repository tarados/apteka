<template>
    <div class="container-fluid">
        <b-nav-form class="form-inline">
            <b-form-input v-model="query" size="lg" class="my-lg-2" placeholder="Search"></b-form-input>
        </b-nav-form>
        <div class="row content-box">
            <b-table striped hover :items="payload"></b-table>
        </div>
    </div>
</template>

<script>
    import * as axios from "axios";

    export default {
        data() {
            return {
                query: "",
                payload: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app'
                }
            }
        },
        computed: {},
        methods: {
            async getPayload() {
                const response = await axios.get(this.url.index);
                this.payload = response.data;
            },
            async getPayloadParam(query) {
                const response = await axios.get(this.url.index, {
                    params: {
                        query: query
                    }
                });
                this.payload = response.data.payload;
                this.count = response.data.valueOf().payload.length;
            }
        },
        mounted() {
            // this.getPayload();
        },
        watch: {
            query: function (seach) {
                if (this.timerId) {
                    clearTimeout(this.timerId);
                }
                this.timerId = setTimeout(() => {
                    this.getPayloadParam(seach);
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