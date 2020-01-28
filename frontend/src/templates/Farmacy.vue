<template>
    <div class="row content-box">
        <b-dropdown
                split
                split-variant="outline-info"
                :text="text"
                variant="info"
                class="m-2"
        >
            <b-dropdown-item v-for="(city, index) in cities" :key="index" @click="getCity">{{ city }}</b-dropdown-item>
        </b-dropdown>
    </div>
</template>

<script>
    import * as axios from "axios";
    import groupArray from "group-array";

    export default {
        data() {
            return {
                payloads: [],
                cities: [],
                text: "Выберите город",
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
                this.payloads = response.data.pharmacyes;
                const groupProductList = groupArray(this.payloads, 'city');
                const keys = [];
                for (const key in groupProductList) {
                    keys.push(key);
                }
                this.cities = this.cities.concat(keys).sort();
            },
            getCity() {

            }
        },
        mounted() {
            this.getPayload();
        }
    }
</script>

<style scoped>

</style>