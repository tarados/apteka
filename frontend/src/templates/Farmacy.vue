<template>
    <div class="row content-box">
        <b-table striped hover :items="payload.pharmacyes"></b-table>
    </div>
</template>

<script>
    import * as axios from "axios";

    export default {
        data() {
            return {
                payload: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app/farmacy'
                }
            }
        },
        computed: {},
        methods: {
            async getPayload() {
                const response = await axios.get(this.url.index);
                this.payload = response.data;
            }
        },
        mounted() {
            this.getPayload();
        }
    }
</script>

<style scoped>

</style>